#!/usr/bin/env bash
#
# pr-to-demo-url.sh — Convert a GitHub PR URL to demo URL(s)
#
# Usage:
#   ./pr-to-demo-url.sh <PR_URL>
#   ./pr-to-demo-url.sh https://github.com/canonical/canonical.com/pull/1444
#
# Output:
#   One demo URL per line for each page changed in the PR.
#
# Pattern:
#   https://{repo-slug}-{pr-number}.demos.haus/{page-path}
#
# Currently supports:
#   - canonical/canonical.com  →  canonical-com-{PR}.demos.haus
#
# To add a new repo, add an entry to the REPO_SLUGS associative array below.

set -euo pipefail

# --- Config: repo name → demo slug prefix ---
declare -A REPO_SLUGS=(
  ["canonical.com"]="canonical-com"
)

# --- Parse PR URL ---
PR_URL="${1:-}"

if [[ -z "$PR_URL" ]]; then
  echo "Usage: $0 <PR_URL>" >&2
  echo "Example: $0 https://github.com/canonical/canonical.com/pull/1444" >&2
  exit 1
fi

# Extract owner, repo, and PR number from URL
if [[ "$PR_URL" =~ github\.com/([^/]+)/([^/]+)/pull/([0-9]+) ]]; then
  OWNER="${BASH_REMATCH[1]}"
  REPO="${BASH_REMATCH[2]}"
  PR_NUMBER="${BASH_REMATCH[3]}"
else
  echo "Error: Could not parse PR URL. Expected format: https://github.com/{owner}/{repo}/pull/{number}" >&2
  exit 1
fi

# Look up the demo slug for this repo
SLUG="${REPO_SLUGS[$REPO]:-}"
if [[ -z "$SLUG" ]]; then
  echo "Error: No demo slug configured for repo '$REPO'." >&2
  echo "Supported repos: ${!REPO_SLUGS[*]}" >&2
  echo "Add an entry to REPO_SLUGS in this script to support it." >&2
  exit 1
fi

DEMO_BASE="https://${SLUG}-${PR_NUMBER}.demos.haus"

# --- Get changed files from the PR ---
if ! command -v gh &>/dev/null; then
  echo "Error: 'gh' CLI is required but not found. Install it: https://cli.github.com" >&2
  exit 1
fi

CHANGED_FILES=$(gh pr view "$PR_NUMBER" \
  --repo "${OWNER}/${REPO}" \
  --json files \
  --jq '.files[].path')

if [[ -z "$CHANGED_FILES" ]]; then
  echo "Error: No changed files found in PR #${PR_NUMBER}." >&2
  exit 1
fi

# --- Filter for template files and build demo URLs ---
# Convention: templates/{path}.html → /{path}
FOUND=0
while IFS= read -r file; do
  if [[ "$file" =~ ^templates/(.+)\.html$ ]]; then
    PAGE_PATH="${BASH_REMATCH[1]}"
    # Skip partials and base templates
    [[ "$PAGE_PATH" == _* ]] && continue
    [[ "$PAGE_PATH" == base* ]] && continue
    echo "${DEMO_BASE}/${PAGE_PATH}"
    FOUND=1
  fi
done <<< "$CHANGED_FILES"

if [[ "$FOUND" -eq 0 ]]; then
  echo "# No page templates found in PR #${PR_NUMBER} changed files." >&2
  echo "# Changed files were:" >&2
  echo "$CHANGED_FILES" | head -20 >&2
  echo "#" >&2
  echo "# You can construct the demo URL manually:" >&2
  echo "# ${DEMO_BASE}/{page-path}" >&2
  # Still output the base URL so the user has something to work with
  echo "${DEMO_BASE}/"
fi
