# Automated UX QA checklist and quality standards

A set of Claude AI skills for reviewing UX content quality at each stage of the Canonical websites design and publishing workflow.

---

## The three-stage review pipeline

| Stage | Skill | Input | When to use |
|---|---|---|---|
| 1. Copy doc | `copy-doc-review` | Google Doc export (`.md`) | When a new page copy doc is ready for UX review, before design begins |
| 2. Figma | `figma-ux-content-audit` | Figma file URL + optional copy doc | When the visual designer has created a Figma draft for UX review |
| 3. Live page | `url-ux-audit` | Live or demo URL | When a demo URL is ready for UX sign-off before launch |

Each skill runs independently. Approvals and handoffs between stages are managed in Jira.

---

## Skills

### `copy-doc-review`

Reviews a copy document against UX best practice standards. Checks structure and hierarchy, CTAs, links, forms, error states, accessibility, navigation, completeness, tone, and open comments.

**Input:** A copy doc exported or copied from Google Docs into markdown format.

### `figma-ux-content-audit`

Reviews a Figma file for UX content quality. Can also compare Figma content against a copy doc for exact match checking.

**Input:** A Figma file URL. Optionally, a markdown copy doc for exact match comparison.

### `url-ux-audit`

Reviews a live or demo URL for UX content quality by fetching the page and checking it against the checklist.

**Input:** A publicly accessible URL.

---

## Reports

Each skill saves audit reports to its own `reports/` folder in the format `[slug]-[YYYY-MM-DD].md`.

---

## Checklists

Default checklists are in each skill's `references/` folder. They can be overridden or supplemented with a custom checklist at runtime.
