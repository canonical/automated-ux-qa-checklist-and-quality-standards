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

## Running it locally

To run the reviews on your own machine – one command from a single PR link – see
**[RUNNING-LOCALLY.md](RUNNING-LOCALLY.md)**. It covers every dependency
(GitHub Copilot CLI, `gh` CLI, Figma MCP login, Google service-account key) and
how to set each one up.

The quickest start is the interactive launcher, which sets up its own
environment and prompts for the PR URL and which review(s) to run:

```bash
python3 review.py
```

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

## GitHub integration

The demo review skill is integrated with GitHub Actions. When someone adds the `Review: UX needed` label to a PR, a workflow automatically:

1. Parses the PR for demo URL, Figma URL, and copy doc URL
2. Posts a `@copilot` comment with all inputs to trigger the demo review
3. The review runs and posts the report as a PR comment

The workflow also supports manual trigger via `workflow_dispatch` with a PR number.

See `.github/workflows/ux-demo-review.yml` for the workflow definition.

---

## Next steps and future work

_This is the running list of planned improvements and deferred ideas. If something comes up as "I should work on this later" or "what should I do next," it goes here._

1. **Refine checklists and report templates.** Iterate on the default checklists and report templates based on real review results to reduce noise and improve signal.
2. **Build a scored test document.** Create a purpose-made copy doc with a known set of deliberately-planted issues and a separate answer key. This lets us score how many issues the skill catches (e.g. 18/20) and measure improvement when we tweak checklists, rather than eyeballing each run.
3. **GCP service account for Google Docs export.** Needed to automatically pull copy doc content via the Google Docs API instead of manual export. Requires a GCP project, service account with Docs read-only scope, and the doc shared with that account.
4. **Linter improvements.** Three partly-scriptable checks not yet implemented: heading levels inside table cells, acronym first-use expansion, sentence length measurement.
5. **Figma audit retry.** The Cassandra page Figma file (`canonical.com-data---Sites`) timed out on first attempt. Can retry now that MCP is confirmed working for smaller queries.
6. **Figma node ID in PR links.** The demo-review skill relies on the `node-id` parameter in Figma URLs to fetch the correct frame. If a developer links to a top-level Figma file without a `node-id`, the skill gets the entire file and cannot reliably match frames to the demo page. Monitor incoming demo PRs to confirm developers are linking to specific frames. If missing node IDs become common, add a fallback that matches by page name or heading text against Figma frame names.
7. **Version tracking for reviewed documents.** If a copy doc or Figma file is changed after a review has been completed, there is currently no way to confirm the review was run against the correct version. A future improvement could capture timestamps, document hashes, or Figma version IDs at review time so that any post-review changes are detectable.
