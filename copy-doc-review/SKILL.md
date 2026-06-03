---
name: copy-doc-review
description: >
  Use this skill whenever the user wants to review a copy document for UX content quality.
  Triggers include: "review this copy doc", "check this copy document", "audit the copy",
  "review the brief", "check the content before design", "QA the copy doc", or when the
  user pastes or provides a markdown copy document and asks for a UX review.
---

# Copy Doc Review Skill

Performs a UX content quality check on a copy document by reviewing its content against
a UX best practice checklist.

Outputs a structured markdown report organised by check type, with issues cited to
specific sections and elements in the document.

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| Copy doc | Yes | Pasted inline or provided as a file path. Exported from Google Docs or similar. |
| Custom UX checklist | Optional | Overrides or supplements the default checklist. User may paste inline or provide a file. |

---

## Step 0 — Confirm inputs

1. Check that the user has provided a copy doc. If not, ask before proceeding.
2. If a custom checklist is provided, use it instead of or alongside the default. If not, load `references/default-checklist.md`.
3. Tell the user what will be checked.

---

## Step 1 — Parse and extract content from the copy doc

Read the full copy document and extract all content, grouped by section:

```
Section: [section heading or inferred role — e.g. Metadata, Hero, CTA, Form, Footer]
  - [element role if inferable]: "[text content]"
  - ...
```

Process the full document. Note while extracting:
- Metadata fields (page title, description, navigation placement) and whether they are complete
- Heading levels and whether they are explicitly marked
- CTA text and any noted destinations
- Link text and any noted destinations
- Input field labels and placeholder text
- Error, success, and empty state copy
- Any TBD, placeholder, or unresolved markers
- Open comments or revision notes

**Note:** Copy docs exported from Google Docs may have table-based layouts with template markers (e.g. `[col:1, ch:60]`). Extract the meaningful content and ignore template scaffolding.

---

## Step 2 — UX quality check

Work through each section of the checklist (default or custom). For each item:

1. Check the extracted content to determine: **pass / fail / needs review / not applicable**
2. Cite the specific section and text or missing element as evidence
3. Assign severity:
   - 🔴 **Critical** — blocks design from starting (missing required field, silent error state, undefined CTA destination)
   - 🟡 **Needs work** — vague copy, missing best practice, inconsistency
   - 🔵 **Minor** — small wording or pattern improvement

### Checklist sections (from default-checklist.md)

1. Structure & Hierarchy
2. CTAs
3. Links
4. Forms & Inputs
5. Error & Feedback States
6. Accessibility
7. Navigation
8. Completeness
9. Tone & Clarity
10. Comments & Revisions
11. Manual Checks (include as reminders in report, not as pass/fail)

---

## Step 3 — Write the audit report

Load `references/report-template.md` and use it as the structure for the report. Fill in every section based on findings from Step 2. Remove sections that have no findings (e.g. if no forms are present, remove Forms & Inputs entirely rather than leaving it blank).

---

## Step 4 — Deliver and save the report

1. Output the report inline in chat as markdown.
2. **Automatically save** the report to `reports/` using the filename format `[doc-slug]-[YYYY-MM-DD].md`. Derive the slug from the document title or page URL in the metadata (lowercase, hyphens, no spaces) — e.g. `reports/canonical-ceph-2026-05-01.md`. Do not ask the user for confirmation before saving.
3. Tell the user the report has been saved and the filename.
4. Offer to dive deeper into any specific section or issue.

---

## Edge cases

| Situation | How to handle |
|---|---|
| Copy doc is empty or near-empty | Tell the user and ask them to confirm the correct file was provided. |
| Doc has many unresolved TBDs | Flag them all in the Completeness section. Note in the summary that design should not start until they are resolved. |
| No metadata table present | Flag as a critical issue under Structure & Hierarchy. |
| Doc is very long | Process the full document. If sections are clearly marked, process them in order and note any skipped content. |
| No error states defined | Flag under Error & Feedback States — missing error copy is a critical gap. |

---

## References

- `references/default-checklist.md` — Full default UX content checklist (copy docs)
- `references/report-template.md` — Report structure template
- `reports/` — Saved audit reports, named `[doc-slug]-[YYYY-MM-DD].md`
