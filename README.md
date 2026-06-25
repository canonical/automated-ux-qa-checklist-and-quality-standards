# Automated UX QA checklist and quality standards

A set of Claude AI skills for reviewing UX content quality at each stage of the Canonical websites design and publishing workflow.

---

## The three-stage review pipeline

| Stage | Skill | Input | When to use |
|---|---|---|---|
| 1. Copy doc | `copy-doc-review` | Google Doc export (`.md`) | When a new page copy doc is ready for UX review, before design begins |
| 2. Figma | `figma-review` | Figma file URL + optional copy doc | When the visual designer has created a Figma draft for UX review |
| 3. Demo | `demo-review` | Demo URL or GitHub PR URL | When a demo URL is ready for UX sign-off before launch |

Each skill runs independently. Approvals and handoffs between stages are managed in Jira.

---

## Skills

### `copy-doc-review`

Reviews a copy document against UX best practice standards. Checks structure and hierarchy, CTAs, links, forms, error states, accessibility, navigation, completeness, tone, and open comments.

**Input:** A copy doc exported or copied from Google Docs into markdown format.

### `figma-review`

Reviews a Figma file for UX content quality. Can also compare Figma content against a copy doc for exact match checking.

**Input:** A Figma file URL. Optionally, a markdown copy doc for exact match comparison.

### `demo-review`

Reviews a demo or live page for UX content quality by fetching the page and checking it against the checklist. Accepts a demo URL directly, or a GitHub PR URL which is automatically converted to a demo URL using `scripts/pr-to-demo-url.sh`.

**Input:** A demo URL, or a GitHub PR URL (e.g. `https://github.com/canonical/canonical.com/pull/1444`).

---

## Reports

Each skill saves audit reports to its own `reports/` folder in the format `[slug]-[YYYY-MM-DD].md`.

---

## Git workflow

- **Reports** (`reports/*.md`) — push directly to `main`. These are review outputs and should be collected in the repo without requiring approval.
- **Everything else** (checklists, skill instructions, linter code, templates, README) — get approval before pushing to `main`. These are shared tools that affect how reviews run for everyone.

---

## Checklists

Default checklists are in each skill's `references/` folder. They can be overridden or supplemented with a custom checklist at runtime.

---

## Next steps and future work

_This is the running list of planned improvements and deferred ideas. If something comes up as "I should work on this later" or "what should I do next," it goes here._

1. **Copy doc role in Figma audit.** When a copy doc is provided at the Figma stage, the skill should ask whether it has already been through copy doc review (stage 1). If yes, treat it as the approved source of truth and only flag differences. If no, note that in the report.
2. **GCP service account for Google Docs export.** Needed to automatically pull copy doc content via the Google Docs API instead of manual export. Requires a GCP project, service account with Docs read-only scope, and the doc shared with that account.
3. **Automation pipeline.** Jira automation → GitHub Actions → Google Docs export → linter → Claude API for judgment checks → post report back to Jira. Blocked on GCP access (#2).
4. **Linter improvements.** Three partly-scriptable checks not yet implemented: heading levels inside table cells, acronym first-use expansion, sentence length measurement.
5. **Figma audit retry.** The Cassandra page Figma file (`canonical.com-data---Sites`) timed out on first attempt. Can retry now that MCP is confirmed working for smaller queries.
6. **Figma node ID in PR links.** The demo-review skill relies on the `node-id` parameter in Figma URLs to fetch the correct frame. If a developer links to a top-level Figma file without a `node-id`, the skill gets the entire file and cannot reliably match frames to the demo page. Monitor incoming demo PRs to confirm developers are linking to specific frames. If missing node IDs become common, add a fallback that matches by page name or heading text against Figma frame names.
7. **Version tracking for reviewed documents.** If a copy doc or Figma file is changed after a review has been completed, there is currently no way to confirm the review was run against the correct version. A future improvement could capture timestamps, document hashes, or Figma version IDs at review time so that any post-review changes are detectable.
