#!/usr/bin/env python3
"""run_demo_review.py — Run a UX demo/live-page review locally with the Copilot CLI.

Fetches a demo or live web page and runs the demo-review skill against it:
UX quality check + brand & style compliance. Accepts either a demo URL directly
or a GitHub PR URL (resolved to demo URL(s) via the existing shell scripts).

Uses the Copilot CLI's built-in web fetch — no MCP server required.

Platform-agnostic (Linux / macOS / Windows): pure Python + the Copilot CLI.
PR-URL resolution additionally needs `gh` (GitHub CLI), authenticated.

Usage:
    python3 run_demo_review.py <DEMO_URL | GITHUB_PR_URL>

Examples:
    python3 run_demo_review.py "https://canonical-com-1444.demos.haus/data"
    python3 run_demo_review.py "https://github.com/canonical/canonical.com/pull/1444"

Requirements:
    - copilot (GitHub Copilot CLI), authenticated — https://github.com/github/copilot-cli
    - gh (GitHub CLI), authenticated — only for GitHub PR URLs
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from shutil import which

SCRIPT_DIR = Path(__file__).resolve().parent  # demo-review/scripts/
SKILL_DIR = SCRIPT_DIR.parent  # demo-review/
REPO_ROOT = SKILL_DIR.parent  # repository root

PR_URL_RE = re.compile(r"github\.com/[^/]+/[^/]+/pull/\d+")
HTTP_URL_RE = re.compile(r"^https?://", re.IGNORECASE)


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def resolve_pr(pr_url: str) -> dict:
    """Run parse-pr-inputs.sh and return its JSON output."""
    script = SCRIPT_DIR / "parse-pr-inputs.sh"
    if not script.exists():
        die(f"Missing helper script: {script}")
    if not which("gh"):
        die(
            "'gh' (GitHub CLI) is required to resolve a PR URL but was not found.\n"
            "Install: https://cli.github.com — or pass a demo URL directly."
        )
    proc = subprocess.run(
        ["bash", str(script), pr_url],
        capture_output=True,
        text=True,
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


def choose_demo_urls(demo_urls: list[str]) -> list[str]:
    """If a PR resolved to multiple demo URLs, let the user pick."""
    if len(demo_urls) <= 1:
        return demo_urls
    print("\nThis PR resolved to multiple demo URLs:")
    for i, u in enumerate(demo_urls, 1):
        print(f"  {i}. {u}")
    print("  a. All of them")
    choice = input("Which page(s) to audit? [a] ").strip().lower() or "a"
    if choice == "a":
        return demo_urls
    picked = []
    for part in re.split(r"[,\s]+", choice):
        if part.isdigit() and 1 <= int(part) <= len(demo_urls):
            picked.append(demo_urls[int(part) - 1])
    return picked or demo_urls


def build_prompt(
    demo_urls: list[str], figma_url: str | None, copydoc_url: str | None
) -> str:
    urls_block = "\n".join(f"  - {u}" for u in demo_urls)
    extras = []
    if figma_url:
        extras.append(
            f"- Figma file (from the PR, for design-fidelity context): {figma_url}"
        )
    if copydoc_url:
        extras.append(f"- Copy doc (from the PR): {copydoc_url}")
    extras_block = (
        ("\nAdditional inputs found in the PR:\n" + "\n".join(extras)) if extras else ""
    )

    return f"""Run a UX demo/live-page content review by following the demo-review skill in this repository.

Skill files (read these first):
- Skill instructions: demo-review/SKILL.md
- Default checklist (fallback): demo-review/references/default-checklist.md
- Report template: demo-review/references/report-template.md
- Copy style guide: shared/copy-style-guide-checklist.md

When SKILL.md refers to files by relative path (e.g. references/...), resolve them
under the demo-review/ directory.

Page(s) to audit:
{urls_block}{extras_block}

Instructions:
1. Follow demo-review/SKILL.md end to end.
2. Fetch each page with your web fetch tool and extract the visible text content,
   grouped by section (Step 1). If a page is unreachable or returns near-empty
   content, note that clearly in the report rather than guessing.
3. Run the UX quality check and the brand & style compliance check.
4. Produce the full report using demo-review/references/report-template.md.
5. Save the report to demo-review/reports/ using the naming format [page-slug]-[YYYY-MM-DD].md.
   If auditing multiple pages, save one report per page. Do not ask for confirmation
   before saving.
6. Print the path of each saved report when done."""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a UX demo/live-page review locally via the Copilot CLI.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("url", help="A demo URL, or a GitHub PR URL to resolve")
    args = parser.parse_args()

    if not HTTP_URL_RE.search(args.url):
        die("That doesn't look like a URL (expected http:// or https://).")

    if not which("copilot"):
        die(
            "'copilot' (GitHub Copilot CLI) is required but not found.\n"
            "Install: https://github.com/github/copilot-cli"
        )

    figma_url = copydoc_url = None

    if PR_URL_RE.search(args.url):
        print(f"\nResolving GitHub PR: {args.url}")
        data = resolve_pr(args.url)
        demo_urls = data.get("demo_urls") or []
        figma_url = data.get("figma_url")
        copydoc_url = data.get("copydoc_url")
        if not demo_urls:
            die(
                "No demo URLs found for this PR (it may only change non-page files).\n"
                "Pass the demo URL directly instead."
            )
        demo_urls = choose_demo_urls(demo_urls)
    else:
        demo_urls = [args.url]

    print("\nResolved inputs:")
    for u in demo_urls:
        print(f"  Demo URL: {u}")
    print(f"  Figma:    {figma_url or '(none)'}")
    print(f"  Copy doc: {copydoc_url or '(none)'}\n")

    prompt = build_prompt(demo_urls, figma_url, copydoc_url)

    print("Starting local Copilot demo review... (this may take a few minutes)\n")
    result = subprocess.run(
        [
            "copilot",
            "-p",
            prompt,
            "--add-dir",
            str(REPO_ROOT),
            "--allow-all-tools",
            "--allow-all-urls",
            "--no-ask-user",
        ],
        cwd=str(REPO_ROOT),
    )

    print("\nDone. Check demo-review/reports/ for the saved report(s).")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
