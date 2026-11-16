#!/usr/bin/env python3
"""Run a Figma review from a Jira ticket and publish it to a private repo."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

from run_review import FETCH_DOC, REPO_ROOT, figma_server_registered, DEFAULT_FIGMA_MCP_CONFIG

REPORT_REPO = os.environ.get("UX_REVIEW_REPORT_REPO", "")
ISSUE_PATH = re.compile(r"/browse/([A-Za-z][A-Za-z0-9_]*-\d+)/?")
URL_RE = re.compile(r'https://[^\s<>"\']+')


class ReviewError(Exception):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def jira_request(base: str, email: str, token: str, path: str, body=None):
    credentials = base64.b64encode(f"{email}:{token}".encode()).decode()
    headers = {"Authorization": f"Basic {credentials}", "Accept": "application/json"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    request = urllib.request.Request(base + path, data=data, headers=headers)
    try:
        with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise ReviewError(f"Jira request failed (HTTP {error.code}): {path}") from error
    except (urllib.error.URLError, OSError, ValueError) as error:
        raise ReviewError(f"Jira request failed for {path}: {error}") from error


def parse_ticket(url: str, base: str) -> str:
    site = urllib.parse.urlsplit(base)
    ticket = urllib.parse.urlsplit(url)
    match = ISSUE_PATH.fullmatch(ticket.path)
    if (
        site.scheme != "https"
        or not site.hostname
        or site.username
        or site.password
        or site.path not in ("", "/")
        or site.query
        or site.fragment
        or ticket.scheme != "https"
        or ticket.netloc.lower() != site.netloc.lower()
        or not match
    ):
        raise ReviewError("Jira URL must be a /browse/ISSUE-123 link on ATLASSIAN_BASE_URL.")
    return match.group(1).upper()


def jira_credentials() -> tuple[str, str, str]:
    names = ("ATLASSIAN_BASE_URL", "ATLASSIAN_EMAIL", "ATLASSIAN_API_TOKEN")
    values = tuple(os.environ.get(name, "") for name in names)
    if any(values):
        if not all(values):
            raise ReviewError("Set all three ATLASSIAN_BASE_URL, ATLASSIAN_EMAIL and ATLASSIAN_API_TOKEN variables.")
        return values[0].rstrip("/"), values[1], values[2]
    config = Path.home() / ".copilot" / "mcp-config.json"
    try:
        settings = json.loads(config.read_text(encoding="utf-8"))
        env = settings["mcpServers"]["jira"]["env"]
        values = tuple(env[name] for name in names)
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        raise ReviewError(
            "Jira credentials not found. Set ATLASSIAN_BASE_URL, ATLASSIAN_EMAIL "
            "and ATLASSIAN_API_TOKEN, or configure the jira Copilot MCP server."
        ) from error
    if not all(isinstance(value, str) and value for value in values):
        raise ReviewError("The Jira MCP configuration does not contain usable credentials.")
    return values[0].rstrip("/"), values[1], values[2]


def extract_links(data) -> tuple[list[str], list[str]]:
    strings = []

    def walk(value):
        if isinstance(value, str):
            strings.append(value)
        elif isinstance(value, list):
            for item in value:
                walk(item)
        elif isinstance(value, dict):
            for item in value.values():
                walk(item)

    walk(data)
    figma, docs = set(), set()
    for text in strings:
        for match in URL_RE.finditer(text):
            url = match.group().rstrip(".,;:!?)]>}")
            try:
                parts = urllib.parse.urlsplit(url)
                host = (parts.hostname or "").lower()
                port = parts.port
            except ValueError:
                continue
            if parts.username or parts.password or port not in (None, 443):
                continue
            if host in ("figma.com", "www.figma.com") and re.match(
                r"^/(?:design|file)/[A-Za-z0-9]+(?:/|$)", parts.path
            ):
                figma.add(url)
            elif host == "docs.google.com" and re.match(
                r"^/document/d/[A-Za-z0-9_-]+(?:/|$)", parts.path
            ):
                docs.add(url)
    return sorted(figma), sorted(docs)


def choose(label: str, links: list[str]) -> str:
    if not links:
        raise ReviewError(f"No {label} link found in the ticket, comments or remote links.")
    print(f"\n{label} links found:")
    for index, link in enumerate(links, 1):
        print(f"  {index}. {link}")
    if len(links) == 1:
        return links[0]
    while True:
        answer = input(f"Choose the {label} link [1-{len(links)}]: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(links):
            return links[int(answer) - 1]
        print("Enter one of the displayed numbers.")


def get_ticket_links(base: str, email: str, token: str, key: str):
    api = f"/rest/api/3/issue/{key}"
    issue = jira_request(base, email, token, api + "?fields=*all")
    remote = jira_request(base, email, token, api + "/remotelink")
    comments = []
    start = 0
    while True:
        page = jira_request(base, email, token, f"{api}/comment?startAt={start}&maxResults=100")
        batch = page["comments"]
        comments.extend(batch)
        start += len(batch)
        if start >= page["total"]:
            break
        if not batch:
            raise ReviewError("Jira returned an incomplete comment listing.")
    return extract_links([issue.get("fields", {}), remote, comments])


def run_command(command: list[str], *, input_text: str | None = None) -> str:
    try:
        result = subprocess.run(command, input=input_text, text=True, capture_output=True)
    except OSError as error:
        raise ReviewError(f"Could not run {command[0]}: {error}") from error
    if result.returncode:
        raise ReviewError(f"{command[0]} failed: {result.stderr.strip()}")
    return result.stdout


def run_review(
    figma: str, doc_url: str, doc: Path, report: Path, approved: bool,
    model: str | None = None,
) -> None:
    status = "approved" if approved else "not confirmed as approved"
    prompt = f"""Follow figma-review/SKILL.md using its local default checklist,
figma-review/references/report-template.md and shared/copy-style-guide-checklist.md.
Review only the frame identified by this Figma URL: {figma}
Compare it with the Google Doc export at {doc}. The copy doc is {status}.
Mention its approval status in the report. Treat it as the reference for
differences, not as evidence of approval. Do not copy the full document.
Use the Figma MCP server to obtain the design. Run the exact copy match, UX
quality and brand/style checks. If either input is inaccessible or you cannot
complete all three checks, explain the failure and do not write a report.
Otherwise write the complete report to exactly {report}. Match the template's
color-coded severity headings and summary table. Note any limitations.
Do not post, commit, or upload anything."""
    command = [
        "copilot", "-p", prompt, "--add-dir", str(report.parent),
        "--allow-tool=figma", f"--allow-tool=write({report})",
        "--disable-mcp-server", "jira", "--disable-builtin-mcps", "--no-ask-user",
    ]
    if not figma_server_registered():
        command += ["--additional-mcp-config", json.dumps(DEFAULT_FIGMA_MCP_CONFIG)]
    if model:
        command += ["--model", model]
    environment = os.environ.copy()
    for name in ("ATLASSIAN_BASE_URL", "ATLASSIAN_EMAIL", "ATLASSIAN_API_TOKEN"):
        environment.pop(name, None)
    try:
        result = subprocess.run(command, cwd=REPO_ROOT, env=environment)
    except OSError as error:
        raise ReviewError(f"Could not run Copilot: {error}") from error
    if result.returncode:
        raise ReviewError(f"Copilot review failed (exit {result.returncode}).")
    if not report.is_file() or not report.read_text(encoding="utf-8").strip():
        raise ReviewError("Copilot did not produce a report; nothing was published.")
    content = report.read_text(encoding="utf-8")
    for heading in ("exact copy match", "ux quality", "brand & style"):
        if heading not in content.lower():
            raise ReviewError(f"Report is missing the {heading} section; nothing was published.")
    report.write_text(
        f"**Figma:** {figma}\n**Copy doc:** {doc_url}\n"
        f"**Copy doc approval:** {status}\n\n{content}", encoding="utf-8"
    )


def publish(report: Path, key: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", REPORT_REPO):
        raise ReviewError(
            "Set UX_REVIEW_REPORT_REPO to your own private repository (owner/repo)."
        )
    metadata = json.loads(run_command([
        "gh", "repo", "view", REPORT_REPO, "--json", "visibility,defaultBranchRef"
    ]))
    if metadata.get("visibility") != "PRIVATE":
        raise ReviewError("The reports repository is not private; refusing to publish.")
    branch = metadata["defaultBranchRef"]["name"]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    path = f"figma-reviews/{key.lower()}-{stamp}-{uuid.uuid4().hex[:8]}.md"
    payload = json.dumps({
        "message": f"Add Figma review for {key}\n\nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>",
        "content": base64.b64encode(report.read_bytes()).decode(),
        "branch": branch,
    })
    result = json.loads(run_command([
        "gh", "api", "--method", "PUT",
        f"repos/{REPORT_REPO}/contents/{path}", "--input", "-"
    ], input_text=payload))
    sha = result["commit"]["sha"]
    if not re.fullmatch(r"[a-fA-F0-9]{40}", sha):
        raise ReviewError("GitHub returned an invalid commit ID; check the repository.")
    return f"https://github.com/{REPORT_REPO}/blob/{sha}/{path}"


def post_link(base: str, email: str, token: str, key: str, url: str) -> None:
    body = {"body": {"type": "doc", "version": 1, "content": [
        {"type": "paragraph", "content": [
            {"type": "text", "text": "Figma UX review report (private GitHub repository): "},
            {"type": "text", "text": url, "marks": [{"type": "link", "attrs": {"href": url}}]},
            {"type": "text", "text": " — for human review; this is not UX approval."},
        ]}
    ]}}
    jira_request(base, email, token, f"/rest/api/3/issue/{key}/comment", body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jira_url", help="Jira ticket URL, e.g. https://site.atlassian.net/browse/ABC-123")
    parser.add_argument("--model", help="Copilot model override for this review, e.g. auto")
    args = parser.parse_args()
    try:
        if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", REPORT_REPO):
            raise ReviewError(
                "Set UX_REVIEW_REPORT_REPO to your own private repository (owner/repo)."
            )
        base, email, token = jira_credentials()
        key = parse_ticket(args.jira_url, base)
        figmas, docs = get_ticket_links(base, email, token, key)
        figma = choose("Figma", figmas)
        doc_url = choose("Google Doc", docs)
        if not urllib.parse.parse_qs(urllib.parse.urlsplit(figma).query).get("node-id"):
            raise ReviewError("The selected Figma link needs a node-id identifying the review frame.")
        print(f"\nSelected for {key}:\n  Figma: {figma}\n  Copy doc: {doc_url}")
        if input("Run this review and publish its link to Jira? [y/N]: ").strip().lower() not in ("y", "yes"):
            print("Cancelled.")
            return 0
        approved = input("Has the copy doc passed stage 1 review? [y/N]: ").strip().lower() in ("y", "yes")
        with tempfile.TemporaryDirectory(prefix="ux-jira-review-") as directory:
            temp = Path(directory)
            doc, report = temp / "copydoc.md", temp / "report.md"
            run_command([sys.executable, str(FETCH_DOC), doc_url, "--out", str(doc)])
            if not doc.is_file() or not doc.read_text(encoding="utf-8").strip():
                raise ReviewError("Google Doc export is empty; nothing was published.")
            run_review(figma, doc_url, doc, report, approved, args.model)
            url = publish(report, key)
            print(f"\nReport published: {url}", flush=True)
            try:
                post_link(base, email, token, key, url)
            except ReviewError as error:
                raise ReviewError(f"{error}\nReport was published at {url}; add the link to Jira manually.") from error
        print("Report link posted to Jira. Review it before approving.")
        return 0
    except (ReviewError, KeyError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
