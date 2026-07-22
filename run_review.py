#!/usr/bin/env python3
"""run_review.py — One-command UX review from a single GitHub PR link.

A designer provides only the GitHub PR URL. This script:
  1. Parses the PR body to find the copy doc, Figma file, and demo URL(s)
     (via demo-review/scripts/parse-pr-inputs.sh).
  2. Runs whichever review stages apply, each through the GitHub Copilot CLI:
       - Copy doc review   (if a Google Doc copy doc is linked)
       - Figma review      (if a Figma file is linked)
       - Demo review       (if a demo / live URL is linked)
  3. Saves one report per stage in that stage's reports/ folder.

Platform-agnostic (Linux / macOS / Windows): pure Python + the Copilot CLI.

With --comment, the combined report is posted back to the PR as a comment.

Requirements:
  - copilot (GitHub Copilot CLI), authenticated — https://github.com/github/copilot-cli
  - gh (GitHub CLI), authenticated — to read the PR body and post the comment
  - For copy doc fetch: demo-review/scripts/google-auth.json (service account),
    and the target doc shared with that service account.
  - For Figma: a `figma` MCP server available to the CLI. Either register your
    own (remote OAuth, or a local PAT server: `copilot mcp add figma
    --env FIGMA_ACCESS_TOKEN=<token> -- mcp-figma`), or let the runner inject the
    official remote server automatically and authenticate once in the browser:
        copilot
        > Use the figma MCP server to get metadata for <any Figma URL you can open>

Usage:
    python3 run_review.py <GITHUB_PR_URL>
    python3 run_review.py <GITHUB_PR_URL> --only figma,demo
    python3 run_review.py <GITHUB_PR_URL> --skip demo
    python3 run_review.py <GITHUB_PR_URL> --comment      # post combined report to the PR

Examples:
    python3 run_review.py "https://github.com/canonical/canonical.com/pull/1444"
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from shutil import which

REPO_ROOT = Path(__file__).resolve().parent
DEMO_SCRIPTS = REPO_ROOT / "demo-review" / "scripts"
PARSE_PR = DEMO_SCRIPTS / "parse-pr-inputs.sh"
FETCH_DOC = DEMO_SCRIPTS / "fetch_google_doc.py"

PR_URL_RE = re.compile(r"github\.com/[^/]+/[^/]+/pull/\d+")
STAGES = ("copydoc", "figma", "demo")

# Where each stage saves its reports, and a human label for the combined comment.
REPORTS_DIRS = {
    "copydoc": (REPO_ROOT / "copy-doc-review" / "reports", "Copy doc review"),
    "figma": (REPO_ROOT / "figma-review" / "reports", "Figma review"),
    "demo": (REPO_ROOT / "demo-review" / "reports", "Demo review"),
}

# Fallback Figma MCP config, injected only when no `figma` server is already
# registered with the CLI. Keeps the runner portable while respecting an
# existing registration (remote OAuth server, or a local PAT-based server such
# as `mcp-figma`).
DEFAULT_FIGMA_MCP_CONFIG = {
    "mcpServers": {
        "figma": {"type": "http", "url": "https://mcp.figma.com/mcp", "tools": ["*"]}
    }
}


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def info(msg: str) -> None:
    print(msg, flush=True)


def figma_server_registered() -> bool:
    """True if a `figma` MCP server is already configured with the CLI."""
    try:
        proc = subprocess.run(
            ["copilot", "mcp", "get", "figma"],
            capture_output=True,
            text=True,
        )
    except OSError:
        return False
    return proc.returncode == 0


# --------------------------------------------------------------------------- #
# PR parsing                                                                   #
# --------------------------------------------------------------------------- #
def resolve_pr(pr_url: str) -> dict:
    if not PARSE_PR.exists():
        die(f"Missing helper script: {PARSE_PR}")
    if not which("gh"):
        die(
            "'gh' (GitHub CLI) is required to read the PR but was not found.\n"
            "Install: https://cli.github.com"
        )
    proc = subprocess.run(
        ["bash", str(PARSE_PR), pr_url], capture_output=True, text=True
    )
    if proc.returncode != 0:
        die(
            "Failed to parse the PR. gh may not be authenticated, or the repo is "
            f"unsupported.\n{proc.stderr.strip()}"
        )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        die(f"Could not parse JSON from parse-pr-inputs.sh:\n{proc.stdout}")


def fetch_copydoc(copydoc_url: str) -> Path | None:
    """Export the linked Google Doc to a temp markdown file. Returns the path,
    or None if the fetch failed (the copy doc stage is then skipped)."""
    if not FETCH_DOC.exists():
        info(f"  ! {FETCH_DOC} not found — skipping copy doc fetch.")
        return None
    tmp = Path(tempfile.gettempdir()) / "ux-review-copydoc.md"
    proc = subprocess.run(
        [sys.executable, str(FETCH_DOC), copydoc_url, "--out", str(tmp)],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0 or not tmp.exists():
        info(
            "  ! Could not fetch the copy doc (is it shared with the service "
            "account?). Copy doc review will be skipped."
        )
        if proc.stderr.strip():
            info(f"    {proc.stderr.strip().splitlines()[-1]}")
        return None
    return tmp


# --------------------------------------------------------------------------- #
# Report detection                                                             #
# --------------------------------------------------------------------------- #
def snapshot_reports(stage: str) -> dict[Path, float]:
    """Map each existing report file in a stage's reports/ dir to its mtime."""
    reports_dir, _ = REPORTS_DIRS[stage]
    if not reports_dir.exists():
        return {}
    return {p: p.stat().st_mtime for p in reports_dir.glob("*.md")}


def new_reports(stage: str, before: dict[Path, float]) -> list[Path]:
    """Report files created or modified in a stage's dir since the snapshot."""
    reports_dir, _ = REPORTS_DIRS[stage]
    if not reports_dir.exists():
        return []
    out = []
    for p in reports_dir.glob("*.md"):
        if p not in before or p.stat().st_mtime > before[p]:
            out.append(p)
    return sorted(out)


def build_combined_report(pr_url: str, produced: list[tuple[str, list[Path]]]) -> str:
    """Concatenate per-stage reports into one markdown body for a PR comment."""
    parts = [
        "## UX review",
        "",
        "Automated UX QA review generated from this PR. Stages run: "
        + ", ".join(label for label, paths in produced if paths)
        + ".",
        "",
    ]
    for label, paths in produced:
        for path in paths:
            parts.append(
                f"<details>\n<summary><strong>{label} — {path.name}"
                "</strong></summary>\n"
            )
            parts.append(path.read_text(encoding="utf-8").strip())
            parts.append("\n</details>\n")
    parts.append("\n---\n*Generated by the automated UX QA review tool.*")
    return "\n".join(parts)


def post_pr_comment(pr_url: str, body: str) -> int:
    """Post the combined report as a comment on the PR via gh."""
    if not which("gh"):
        info("  ! 'gh' not found — cannot post the PR comment.")
        return 1
    tmp = Path(tempfile.gettempdir()) / "ux-review-pr-comment.md"
    tmp.write_text(body, encoding="utf-8")
    try:
        proc = subprocess.run(
            ["gh", "pr", "comment", pr_url, "--body-file", str(tmp)],
            capture_output=True,
            text=True,
        )
    finally:
        tmp.unlink(missing_ok=True)
    if proc.returncode != 0:
        info(f"  ! Failed to post PR comment:\n    {proc.stderr.strip()}")
        return proc.returncode
    info(f"  Posted combined report to the PR: {proc.stdout.strip()}")
    return 0


# --------------------------------------------------------------------------- #
# Prompt builders                                                              #
# --------------------------------------------------------------------------- #
def prompt_copydoc(copydoc_file: Path) -> str:
    return f"""Run a UX copy doc review by following the copy-doc-review skill in this repository.

Skill files (read these first):
- Skill instructions: copy-doc-review/SKILL.md
- Default checklist (fallback): copy-doc-review/references/default-checklist.md
- Report template: copy-doc-review/references/report-template.md
- Copy style guide: shared/copy-style-guide-checklist.md

Resolve relative paths in SKILL.md under the copy-doc-review/ directory.

Input:
- Copy doc (local markdown, exported from Google Docs): {copydoc_file}

Instructions:
1. Follow copy-doc-review/SKILL.md end to end on that file.
2. Produce the full report using copy-doc-review/references/report-template.md.
3. Save the report to copy-doc-review/reports/ as [page-slug]-[YYYY-MM-DD].md.
   Do not ask for confirmation before saving.
4. Print the path of the saved report when done."""


def prompt_figma(figma_url: str, copydoc_file: Path | None) -> str:
    if copydoc_file:
        copydoc_line = (
            f"Copy doc: read the local markdown file {copydoc_file} as the approved "
            "copy for the exact-match check (Check 1). It has been through copy doc "
            "review (stage 1), so treat it as the source of truth and only flag "
            "differences. Do NOT paste its raw contents into the report."
        )
    else:
        copydoc_line = (
            "Copy doc: Not provided — skip Check 1 (exact match), note "
            "this in the report."
        )
    return f"""Run a UX Figma content review by following the figma-review skill in this repository.

Skill files (read these first):
- Skill instructions: figma-review/SKILL.md
- Default checklist (fallback): figma-review/references/default-checklist.md
- Report template: figma-review/references/report-template.md
- Copy style guide: shared/copy-style-guide-checklist.md

Resolve relative paths in SKILL.md under the figma-review/ directory.

Inputs:
- Figma file: {figma_url}
- {copydoc_line}

Instructions:
1. Follow figma-review/SKILL.md end to end.
2. Extract content from the Figma file using the figma MCP server (Step 1). If the
   figma MCP tools are not available or not authenticated, stop and report that the
   Figma MCP must be connected and authenticated — do not guess at design content.
3. Run the checks the skill specifies.
4. Produce the full report using figma-review/references/report-template.md.
5. Save the report to figma-review/reports/ as [page-slug]-[YYYY-MM-DD].md.
   Do not ask for confirmation before saving.
6. Print the path of the saved report when done."""


def prompt_demo(
    demo_urls: list[str], figma_url: str | None, copydoc_url: str | None
) -> str:
    urls_block = "\n".join(f"  - {u}" for u in demo_urls)
    extras = []
    if figma_url:
        extras.append(f"- Figma file (design-fidelity context): {figma_url}")
    if copydoc_url:
        extras.append(f"- Copy doc URL (context): {copydoc_url}")
    extras_block = (
        ("\nAdditional context from the PR:\n" + "\n".join(extras)) if extras else ""
    )
    return f"""Run a UX demo/live-page content review by following the demo-review skill in this repository.

Skill files (read these first):
- Skill instructions: demo-review/SKILL.md
- Default checklist (fallback): demo-review/references/default-checklist.md
- Report template: demo-review/references/report-template.md
- Copy style guide: shared/copy-style-guide-checklist.md

Resolve relative paths in SKILL.md under the demo-review/ directory.

Page(s) to audit:
{urls_block}{extras_block}

Instructions:
1. Follow demo-review/SKILL.md end to end.
2. Fetch each page with your web fetch tool and extract the visible text content,
   grouped by section (Step 1). If a page is unreachable or near-empty, note that
   in the report rather than guessing.
3. Run the UX quality check and the brand & style compliance check.
4. Produce the full report using demo-review/references/report-template.md.
5. Save one report per page to demo-review/reports/ as [page-slug]-[YYYY-MM-DD].md.
   Do not ask for confirmation before saving.
6. Print the path of each saved report when done."""


# --------------------------------------------------------------------------- #
# Copilot invocation                                                           #
# --------------------------------------------------------------------------- #
def run_copilot(
    prompt: str,
    *,
    figma: bool = False,
    urls: bool = False,
    extra_dirs: list[Path] | None = None,
) -> int:
    cmd = ["copilot", "-p", prompt, "--add-dir", str(REPO_ROOT)]
    for d in extra_dirs or []:
        cmd += ["--add-dir", str(d)]
    if figma and not figma_server_registered():
        cmd += ["--additional-mcp-config", json.dumps(DEFAULT_FIGMA_MCP_CONFIG)]
    cmd += ["--allow-all-tools", "--no-ask-user"]
    if urls:
        cmd += ["--allow-all-urls"]
    return subprocess.run(cmd, cwd=str(REPO_ROOT)).returncode


# --------------------------------------------------------------------------- #
# Main                                                                         #
# --------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(
        description="One-command UX review from a single GitHub PR link.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("pr_url", help="GitHub PR URL")
    parser.add_argument(
        "--only",
        help="Comma-separated stages to run "
        "(copydoc, figma, demo). Default: all applicable.",
    )
    parser.add_argument("--skip", help="Comma-separated stages to skip.")
    parser.add_argument(
        "--comment",
        action="store_true",
        help="Post the combined report as a comment on the PR (via gh).",
    )
    args = parser.parse_args()

    if not PR_URL_RE.search(args.pr_url):
        die(
            "That doesn't look like a GitHub PR URL "
            "(expected github.com/{owner}/{repo}/pull/{number})."
        )

    if not which("copilot"):
        die(
            "'copilot' (GitHub Copilot CLI) is required but not found.\n"
            "Install: https://github.com/github/copilot-cli"
        )

    only = {s.strip() for s in args.only.split(",")} if args.only else set(STAGES)
    skip = {s.strip() for s in args.skip.split(",")} if args.skip else set()
    for s in only | skip:
        if s not in STAGES:
            die(f"Unknown stage '{s}'. Valid stages: {', '.join(STAGES)}")
    wanted = only - skip

    info(f"\nResolving GitHub PR: {args.pr_url}")
    data = resolve_pr(args.pr_url)
    demo_urls = data.get("demo_urls") or []
    figma_url = data.get("figma_url")
    copydoc_url = data.get("copydoc_url")

    info("\nInputs found in the PR:")
    info(f"  Copy doc: {copydoc_url or '(none)'}")
    info(f"  Figma:    {figma_url or '(none)'}")
    info(f"  Demo:     {', '.join(demo_urls) if demo_urls else '(none)'}\n")

    # Fetch the copy doc once; reused by both the copydoc and figma stages.
    copydoc_file: Path | None = None
    if copydoc_url and ("copydoc" in wanted or "figma" in wanted):
        info("Fetching copy doc...")
        copydoc_file = fetch_copydoc(copydoc_url)

    results: list[tuple[str, str]] = []  # (stage, status)
    produced: list[tuple[str, list[Path]]] = []  # (label, report paths) for the comment

    if "copydoc" in wanted:
        if copydoc_file:
            info("\n=== Stage 1: Copy doc review ===\n")
            before = snapshot_reports("copydoc")
            rc = run_copilot(
                prompt_copydoc(copydoc_file), extra_dirs=[copydoc_file.parent]
            )
            results.append(("Copy doc", "ok" if rc == 0 else f"failed (exit {rc})"))
            produced.append(
                (REPORTS_DIRS["copydoc"][1], new_reports("copydoc", before))
            )
        else:
            results.append(("Copy doc", "skipped (no copy doc / fetch failed)"))

    if "figma" in wanted:
        if figma_url:
            info("\n=== Stage 2: Figma review ===\n")
            before = snapshot_reports("figma")
            rc = run_copilot(
                prompt_figma(figma_url, copydoc_file),
                figma=True,
                extra_dirs=[copydoc_file.parent] if copydoc_file else None,
            )
            results.append(("Figma", "ok" if rc == 0 else f"failed (exit {rc})"))
            produced.append((REPORTS_DIRS["figma"][1], new_reports("figma", before)))
        else:
            results.append(("Figma", "skipped (no Figma URL)"))

    if "demo" in wanted:
        if demo_urls:
            info("\n=== Stage 3: Demo review ===\n")
            before = snapshot_reports("demo")
            rc = run_copilot(prompt_demo(demo_urls, figma_url, copydoc_url), urls=True)
            results.append(("Demo", "ok" if rc == 0 else f"failed (exit {rc})"))
            produced.append((REPORTS_DIRS["demo"][1], new_reports("demo", before)))
        else:
            results.append(("Demo", "skipped (no demo URL)"))

    # Clean up the temp copy doc (avoid leaving private content on disk).
    if copydoc_file and copydoc_file.exists():
        try:
            copydoc_file.unlink()
        except OSError:
            pass

    info("\n" + "=" * 48)
    info("Review complete. Summary:")
    for stage, status in results:
        info(f"  {stage:9} {status}")
    info("\nReports saved under each stage's reports/ folder:")
    info("  copy-doc-review/reports/   figma-review/reports/   demo-review/reports/")

    # Post the combined report to the PR, if requested.
    if args.comment:
        report_paths = [p for _, paths in produced for p in paths]
        if report_paths:
            info("\nPosting combined report to the PR...")
            post_pr_comment(args.pr_url, build_combined_report(args.pr_url, produced))
        else:
            info("\nNo reports were produced — nothing to post to the PR.")

    return (
        0
        if all(st.startswith("ok") or st.startswith("skipped") for _, st in results)
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
