# Automated UX QA checklist and quality standards

A set of Claude AI skills for reviewing UX content quality at each stage of the Canonical websites design and publishing workflow.

---

## The three-stage review pipeline

| Stage | Skill | Input | When to use |
|---|---|---|---|
| 1. Copy doc | `copy-doc-review` | Google Doc export (`.md`) | When a new page copy doc is ready for UX review, before design begins |
| 2. Figma | `figma-ux-content-audit` | Figma file URL + optional copy doc | When the visual designer has created a Figma draft for UX review |
| 3. Demo | `demo-audit` | Demo URL or GitHub PR URL | When a demo URL is ready for UX sign-off before launch |

Each skill runs independently. Approvals and handoffs between stages are managed in Jira.

---

## Skills

### `copy-doc-review`

Reviews a copy document against UX best practice standards. Checks structure and hierarchy, CTAs, links, forms, error states, accessibility, navigation, completeness, tone, and open comments.

**Input:** A copy doc exported or copied from Google Docs into markdown format.

### `figma-ux-content-audit`

Reviews a Figma file for UX content quality. Can also compare Figma content against a copy doc for exact match checking.

**Input:** A Figma file URL. Optionally, a markdown copy doc for exact match comparison.

### `demo-audit`

Reviews a demo or live page for UX content quality by fetching the page and checking it against the checklist. Accepts a demo URL directly, or a GitHub PR URL which is automatically converted to a demo URL using `scripts/pr-to-demo-url.sh`.

**Input:** A demo URL, or a GitHub PR URL (e.g. `https://github.com/canonical/canonical.com/pull/1444`).

---

## Reports

Each skill saves audit reports to its own `reports/` folder in the format `[slug]-[YYYY-MM-DD].md`.

---

## Checklists

Default checklists are in each skill's `references/` folder. They can be overridden or supplemented with a custom checklist at runtime.

---

## Future considerations

- **Version tracking for reviewed documents.** If a copy doc or Figma file is changed after a review has been completed, there is currently no way to confirm the review was run against the correct version. A future improvement could capture timestamps, document hashes, or Figma version IDs at review time so that any post-review changes are detectable. This would prevent a situation where a review is treated as valid but the source material has since changed.
