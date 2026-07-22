#!/usr/bin/env python3
"""fetch_google_doc.py — Export a private Google Doc to markdown.

Platform-agnostic (Linux / macOS / Windows). Authenticates with a local Google
service-account key file, so it runs headless — no browser, no interactive login.

The service account can only read a doc if that doc has been shared with the
service account's email (the "client_email" in the key file, ending in
"...@....iam.gserviceaccount.com").

Credentials — the key file is resolved in this order:
  1. --auth PATH
  2. $GOOGLE_AUTH_JSON
  3. google-auth.json next to this script (demo-review/scripts/)
This file is a secret; it is gitignored so it is never committed to this public repo.

Setup (one-time):
  pip install -r requirements.txt

Usage:
  python3 fetch_google_doc.py <DOC_URL_OR_ID> [--out FILE] [--auth PATH]

Exit codes:
  0 success · 2 setup/auth error · 3 fetch/export error
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
except ImportError as exc:
    sys.exit(
        f"[fetch_google_doc] Missing Google auth library ({exc}).\n"
        "Install it with: pip install -r requirements.txt"
    )

# drive.readonly is enough for the Drive files.export endpoint.
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# The key file lives next to this script and is gitignored (never committed).
DEFAULT_AUTH_FILE = Path(__file__).resolve().parent / "google-auth.json"


def resolve_auth_file(cli_path: str | None) -> Path:
    """Find the service-account key file, or exit with setup guidance."""
    candidate = cli_path or os.environ.get("GOOGLE_AUTH_JSON") or str(DEFAULT_AUTH_FILE)
    path = Path(candidate).expanduser()
    if not path.exists():
        sys.exit(
            f"[fetch_google_doc] Google service-account key not found at {path}.\n"
            "Provide it with --auth PATH, $GOOGLE_AUTH_JSON, or place it at "
            f"{DEFAULT_AUTH_FILE}.\n"
            "In Google Cloud: create a service account, enable the Google Drive API, "
            "download its JSON key, and share the target docs with the service "
            "account's client_email."
        )
    return path


def extract_doc_id(value: str) -> str:
    """Pull the document ID out of a Google Docs URL, or accept a bare ID."""
    match = re.search(r"/document/d/([a-zA-Z0-9_-]+)", value)
    if match:
        return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{20,}", value):
        return value
    sys.exit(f"[fetch_google_doc] Could not find a Google Doc ID in: {value}")


def get_access_token(auth_file: Path) -> str:
    """Mint a short-lived access token from the service-account key."""
    try:
        creds = Credentials.from_service_account_file(str(auth_file), scopes=SCOPES)
    except (ValueError, KeyError) as exc:
        sys.exit(f"[fetch_google_doc] Invalid service-account key {auth_file}: {exc}")
    creds.refresh(Request())
    return creds.token


def export_doc(doc_id: str, token: str) -> str:
    """Export the doc via the Drive API, preferring markdown, then plain text."""
    for mime in ("text/markdown", "text/plain"):
        url = (
            f"https://www.googleapis.com/drive/v3/files/{doc_id}/export?"
            + urllib.parse.urlencode({"mimeType": mime})
        )
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as err:
            # 400 usually means this MIME isn't a valid export format — try the next.
            if err.code == 400 and mime != "text/plain":
                continue
            detail = err.read().decode("utf-8", "replace")[:500]
            if err.code in (401, 403):
                sys.exit(
                    f"[fetch_google_doc] Access denied ({err.code}) for doc {doc_id}. "
                    "Confirm the doc is shared with the service account's client_email "
                    f"and the Drive API is enabled.\n{detail}"
                )
            if err.code == 404:
                sys.exit(f"[fetch_google_doc] Doc {doc_id} not found (404).\n{detail}")
            sys.exit(
                f"[fetch_google_doc] Export failed ({err.code}) for {doc_id}.\n{detail}"
            )
    sys.exit(
        f"[fetch_google_doc] Could not export doc {doc_id} in any supported format."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a Google Doc to markdown.")
    parser.add_argument("doc", help="Google Docs URL or document ID")
    parser.add_argument("--out", help="Write markdown to this file instead of stdout")
    parser.add_argument("--auth", help="Path to the service-account key JSON")
    args = parser.parse_args()

    auth_file = resolve_auth_file(args.auth)
    doc_id = extract_doc_id(args.doc)
    token = get_access_token(auth_file)
    content = export_doc(doc_id, token)

    if args.out:
        out_path = Path(args.out).expanduser()
        out_path.write_text(content, encoding="utf-8")
        print(
            f"[fetch_google_doc] Wrote {len(content)} chars to {out_path}",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
