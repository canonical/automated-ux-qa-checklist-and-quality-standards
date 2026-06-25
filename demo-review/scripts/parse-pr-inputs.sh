#!/usr/bin/env bash
#
# parse-pr-inputs.sh — Extract demo URL, Figma URL, and copy doc URL from a GitHub PR
#
# Usage:
#   ./parse-pr-inputs.sh <PR_URL>
#   ./parse-pr-inputs.sh https://github.com/canonical/canonical.com/pull/2511
#
# Output:
#   JSON object with demo_urls, figma_url, figma_node_id, copydoc_url, pr metadata.
#
# Detection is domain-based and position-agnostic — it scans the entire PR body
# regardless of which section the links appear in.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Parse PR URL ---
PR_URL="${1:-}"

if [[ -z "$PR_URL" ]]; then
  echo "Usage: $0 <PR_URL>" >&2
  echo "Example: $0 https://github.com/canonical/canonical.com/pull/2511" >&2
  exit 1
fi

if [[ "$PR_URL" =~ github\.com/([^/]+)/([^/]+)/pull/([0-9]+) ]]; then
  OWNER="${BASH_REMATCH[1]}"
  REPO="${BASH_REMATCH[2]}"
  PR_NUMBER="${BASH_REMATCH[3]}"
else
  echo "Error: Could not parse PR URL. Expected format: https://github.com/{owner}/{repo}/pull/{number}" >&2
  exit 1
fi

if ! command -v gh &>/dev/null; then
  echo "Error: 'gh' CLI is required but not found. Install it: https://cli.github.com" >&2
  exit 1
fi

# --- Fetch PR body ---
PR_BODY=$(gh pr view "$PR_NUMBER" \
  --repo "${OWNER}/${REPO}" \
  --json body \
  --jq '.body')

# --- Extract URLs by domain ---

# Demo URLs: anything matching *.demos.haus/*
DEMO_URLS=$(echo "$PR_BODY" | grep -oP 'https?://[a-zA-Z0-9._-]+\.demos\.haus[^\s\)\]"]*' | sort -u || true)

# Figma URL: figma.com/design/...
FIGMA_URL=$(echo "$PR_BODY" | grep -oP 'https?://[w.]*figma\.com/design/[^\s\)\]"]*' | head -1 || true)

# Copy doc URL: docs.google.com/document/...
COPYDOC_URL=$(echo "$PR_BODY" | grep -oP 'https?://docs\.google\.com/document/[^\s\)\]"]*' | head -1 || true)

# --- Extract Figma node ID if present ---
FIGMA_NODE_ID=""
if [[ -n "$FIGMA_URL" && "$FIGMA_URL" =~ node-id=([0-9]+-[0-9]+) ]]; then
  FIGMA_NODE_ID="${BASH_REMATCH[1]}"
fi

# --- Fall back to constructing demo URLs from changed files if none found in body ---
if [[ -z "$DEMO_URLS" && -f "$SCRIPT_DIR/pr-to-demo-url.sh" ]]; then
  DEMO_URLS=$("$SCRIPT_DIR/pr-to-demo-url.sh" "$PR_URL" 2>/dev/null || true)
fi

# --- Build JSON output ---
# Convert demo URLs (one per line) to a JSON array
DEMO_ARRAY="[]"
if [[ -n "$DEMO_URLS" ]]; then
  DEMO_ARRAY=$(echo "$DEMO_URLS" | python3 -c "
import sys, json
urls = [line.strip() for line in sys.stdin if line.strip() and not line.strip().startswith('#')]
print(json.dumps(urls))
")
fi

python3 -c "
import json

data = {
    'pr_url': '${PR_URL}',
    'pr_number': '${PR_NUMBER}',
    'repo': '${OWNER}/${REPO}',
    'demo_urls': json.loads('${DEMO_ARRAY}'),
    'figma_url': '${FIGMA_URL}' or None,
    'figma_node_id': '${FIGMA_NODE_ID}' or None,
    'copydoc_url': '${COPYDOC_URL}' or None,
}

print(json.dumps(data, indent=2))
"
