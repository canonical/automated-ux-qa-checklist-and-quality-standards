#!/usr/bin/env python3
"""run_figma_review.py — Run a UX Figma review locally with the GitHub Copilot CLI.

Uses the Figma MCP server for design access. If a `figma` MCP server is already
registered with the CLI, that one is used (e.g. the official remote server, or a
local PAT-based server such as `mcp-figma`). Otherwise the script injects the
official remote server (https://mcp.figma.com/mcp) so it works out of the box.

Platform-agnostic (Linux / macOS / Windows): pure Python + the Copilot CLI.

One-time Figma authentication (pick one):
  A. Remote server (default) — OAuth. Run `copilot`, then trigger a Figma tool
     once and approve in the browser (token is cached afterwards):
       copilot
       > Use the figma MCP server to get metadata for <any Figma URL you can open>
  B. Local PAT server — no browser. Install a local Figma MCP and register it
     with a Figma personal access token, e.g.:
       copilot mcp add figma --env FIGMA_ACCESS_TOKEN=<token> -- mcp-figma

Usage:
    python3 run_figma_review.py <FIGMA_URL> [--copydoc FILE.md] [--out FILE]

Examples:
    python3 run_figma_review.py "https://www.figma.com/design/abc/x?node-id=1-23"
    python3 run_figma_review.py "https://www.figma.com/design/abc/x?node-id=1-23" \
        --copydoc /tmp/copydoc.md

Requirements:
    - copilot (GitHub Copilot CLI), authenticated — https://github.com/github/copilot-cli
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from shutil import which

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent  # figma-review/
REPO_ROOT = SKILL_DIR.parent  # repository root

# Fallback Figma MCP config, injected only when no `figma` server is already
# registered with the CLI. This keeps the script portable: a colleague with
# nothing configured gets the official remote server (OAuth), while anyone who
# has already run `copilot mcp add figma ...` (remote OAuth or a local PAT-based
# server) keeps their own registration.
DEFAULT_FIGMA_MCP_CONFIG = {
    "mcpServers": {
        "figma": {"type": "http", "url": "https://mcp.figma.com/mcp", "tools": ["*"]}
    }
}

FIGMA_URL_RE = re.compile(r"figma\.com/(?:file|design)/[a-zA-Z0-9]+")


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


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


def build_prompt(figma_url: str, copydoc_file: Path | None) -> str:
    if copydoc_file:
        copydoc_line = (
            f"Copy doc: read the local markdown file {copydoc_file} as the approved "
            "copy for the exact-match check (Check 1). Do NOT paste its raw contents "
            "into the report or commit it."
        )
    else:
        copydoc_line = "Copy doc: Not provided — skip Check 1 (exact match), note this in the report."

    return f"""Run a UX Figma content review by following the figma-review skill in this repository.

Skill files (read these first):
- Skill instructions: figma-review/SKILL.md
- Default checklist (fallback): figma-review/references/default-checklist.md
- Report template: figma-review/references/report-template.md
- Copy style guide: shared/copy-style-guide-checklist.md

When SKILL.md refers to files by relative path (e.g. references/...), resolve them
under the figma-review/ directory.

Inputs:
- Figma file: {figma_url}
- {copydoc_line}

Instructions:
1. Follow figma-review/SKILL.md end to end.
2. Extract content from the Figma file using the figma MCP server (Step 1). If the
   figma MCP tools are not available or not authenticated, stop and report that the
   Figma MCP must be connected and authenticated — do not guess at design content.
3. Run the checks the skill specifies (exact match only if a copy doc is provided,
   plus the UX quality check and brand & style compliance).
4. Produce the full report using figma-review/references/report-template.md.
5. Save the report to figma-review/reports/ using the naming format [page-slug]-[YYYY-MM-DD].md.
   Do not ask for confirmation before saving.
6. Print the path of the saved report when done."""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a UX Figma review locally via the Copilot CLI + Figma MCP.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("figma_url", help="Figma file URL (ideally with a node-id)")
    parser.add_argument(
        "--copydoc", help="Local markdown copy doc for the exact-match check"
    )
    parser.add_argument(
        "--out", help="(informational) desired report path; the skill names it"
    )
    args = parser.parse_args()

    if not FIGMA_URL_RE.search(args.figma_url):
        die(
            "That doesn't look like a Figma file URL "
            "(expected figma.com/design/<key> or figma.com/file/<key>)."
        )

    if not which("copilot"):
        die(
            "'copilot' (GitHub Copilot CLI) is required but not found.\n"
            "Install: https://github.com/github/copilot-cli"
        )

    copydoc_file = None
    if args.copydoc:
        copydoc_file = Path(args.copydoc).expanduser()
        if not copydoc_file.exists():
            die(f"Copy doc file not found: {copydoc_file}")

    print("\nResolved inputs:")
    print(f"  Figma URL: {args.figma_url}")
    print(f"  Copy doc:  {copydoc_file or '(none)'}\n")

    prompt = build_prompt(args.figma_url, copydoc_file)

    # --add-dir: file access to the repo (skill + reports) and the copy doc, if any.
    add_dir = ["--add-dir", str(REPO_ROOT)]
    if copydoc_file:
        add_dir += ["--add-dir", str(copydoc_file.parent)]

    # Use an already-registered `figma` server if present; otherwise inject the
    # portable remote default.
    mcp_args: list[str] = []
    if figma_server_registered():
        print("Using the figma MCP server already registered with the CLI.\n")
    else:
        print(
            "No figma MCP server registered — using the remote default "
            "(https://mcp.figma.com/mcp).\n"
        )
        mcp_args = ["--additional-mcp-config", json.dumps(DEFAULT_FIGMA_MCP_CONFIG)]

    print("Starting local Copilot Figma review... (this may take a few minutes)\n")
    result = subprocess.run(
        [
            "copilot",
            "-p",
            prompt,
            *mcp_args,
            *add_dir,
            "--allow-all-tools",
            "--no-ask-user",
        ],
        cwd=str(REPO_ROOT),
    )

    print("\nDone. Check figma-review/reports/ for the saved report.")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
