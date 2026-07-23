#!/usr/bin/env python3
"""review.py — friendly, self-setting-up launcher for the UX review.

One command, no manual virtualenv juggling. This launcher:

  1. Creates a local .venv (if missing) and installs the Python dependencies
     into it — re-installing only when requirements.txt changes.
  2. Re-runs itself with that venv's interpreter, so the copy-doc fetch
     (google-auth / requests) always works.
  3. Interactively asks for the PR URL and which review(s) to run, then calls
     run_review.py for you.

Platform-agnostic (Linux / macOS / Windows): pure standard library.

Usage:
    python3 review.py                  # interactive: prompts for everything
    python3 review.py <GITHUB_PR_URL>  # skip prompts, run all stages
    python3 review.py <GITHUB_PR_URL> --demo-only --comment

Any extra arguments are passed straight through to run_review.py, so every
flag documented there (--demo-only, --figma-only, --copy-only, --only, --skip,
--comment) works here too.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
VENV_DIR = REPO_ROOT / ".venv"
REQUIREMENTS = REPO_ROOT / "demo-review" / "scripts" / "requirements.txt"
RUN_REVIEW = REPO_ROOT / "run_review.py"
DEPS_MARKER = VENV_DIR / ".deps-installed"

PR_URL_RE = re.compile(r"github\.com/[^/]+/[^/]+/pull/\d+")

STAGE_CHOICES = {
    "1": ("All three stages (default)", []),
    "2": ("Copy doc only", ["--copy-only"]),
    "3": ("Figma only", ["--figma-only"]),
    "4": ("Demo only", ["--demo-only"]),
}


# --------------------------------------------------------------------------- #
# venv bootstrap                                                              #
# --------------------------------------------------------------------------- #
def venv_python(venv_dir: Path) -> Path:
    """Path to the Python interpreter inside a venv, per platform."""
    if os.name == "nt":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def running_inside_venv() -> bool:
    """True if we're already executing from inside the project's venv.

    Compares sys.prefix rather than the interpreter path: a venv's `python`
    is usually a symlink to the base interpreter, so resolving executable
    paths would make the system and venv interpreters look identical.
    """
    try:
        return Path(sys.prefix).resolve() == VENV_DIR.resolve()
    except OSError:
        return False


def deps_up_to_date() -> bool:
    """True if requirements were installed and haven't changed since."""
    if not DEPS_MARKER.exists():
        return False
    if not REQUIREMENTS.exists():
        return True
    return DEPS_MARKER.stat().st_mtime >= REQUIREMENTS.stat().st_mtime


def ensure_venv_and_reexec() -> None:
    """Create the venv, install deps, and re-run this script inside it.

    No-op (returns) once we're already running inside the venv with deps
    installed — that's the branch that continues to the interactive flow.
    """
    if running_inside_venv():
        if not deps_up_to_date():
            install_deps(Path(sys.executable))
        return

    vpy = venv_python(VENV_DIR)
    if not vpy.exists():
        print("Setting up a local environment (.venv)...", flush=True)
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(VENV_DIR)], check=True
            )
        except subprocess.CalledProcessError:
            sys.exit(
                "Error: could not create the virtual environment. Ensure the "
                "'venv' module is available (on Debian/Ubuntu: "
                "sudo apt install python3-venv)."
            )

    if not deps_up_to_date():
        install_deps(vpy)

    # Re-run this launcher with the venv interpreter and the same arguments.
    script = str(Path(__file__).resolve())
    result = subprocess.run([str(vpy), script, *sys.argv[1:]])
    sys.exit(result.returncode)


def install_deps(python_exe: Path) -> None:
    """Install/upgrade the project's Python dependencies into the venv."""
    if not REQUIREMENTS.exists():
        return
    print("Installing dependencies...", flush=True)
    pip = [str(python_exe), "-m", "pip", "install", "--quiet"]
    try:
        subprocess.run(pip + ["--upgrade", "pip"], check=True)
        subprocess.run(pip + ["-r", str(REQUIREMENTS)], check=True)
    except subprocess.CalledProcessError:
        sys.exit("Error: failed to install Python dependencies.")
    DEPS_MARKER.write_text("ok\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# interactive prompts                                                         #
# --------------------------------------------------------------------------- #
def ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        sys.exit(130)


def prompt_pr_url() -> str:
    while True:
        url = ask("GitHub PR URL: ")
        if PR_URL_RE.search(url):
            return url
        print(
            "  That doesn't look like a PR URL "
            "(expected github.com/{owner}/{repo}/pull/{number}). Try again.\n"
        )


def prompt_stage() -> list[str]:
    print("\nWhich review(s) do you want to run?")
    for key, (label, _) in STAGE_CHOICES.items():
        print(f"  {key}) {label}")
    while True:
        choice = ask("Select [1-4] (default 1): ") or "1"
        if choice in STAGE_CHOICES:
            return STAGE_CHOICES[choice][1]
        print("  Please choose 1, 2, 3, or 4.\n")


def prompt_comment() -> bool:
    answer = ask("\nPost the report back to the PR as a comment? [y/N]: ")
    return answer.lower() in ("y", "yes")


# --------------------------------------------------------------------------- #
# main                                                                        #
# --------------------------------------------------------------------------- #
def main() -> int:
    ensure_venv_and_reexec()

    args = sys.argv[1:]

    # If a PR URL was supplied on the command line, run non-interactively and
    # forward every argument to run_review.py unchanged.
    if any(PR_URL_RE.search(a) for a in args):
        cmd = [sys.executable, str(RUN_REVIEW), *args]
        return subprocess.run(cmd).returncode

    # Otherwise, ask nicely.
    print("Automated UX review\n" + "=" * 19)
    pr_url = prompt_pr_url()
    stage_flags = prompt_stage()
    comment = prompt_comment()

    cmd = [sys.executable, str(RUN_REVIEW), pr_url, *stage_flags]
    if comment:
        cmd.append("--comment")

    print()  # blank line before run_review's own output
    return subprocess.run(cmd).returncode


if __name__ == "__main__":
    raise SystemExit(main())
