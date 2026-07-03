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

Outputs a structured markdown report organised by page section order (top to bottom), with issues cited to
specific sections and elements in the document. This lets a reviewer read the report side by side with the page.

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| Copy doc | Yes | Pasted inline or provided as a file path. Exported from Google Docs or similar. |
| Custom UX checklist | Optional | Overrides or supplements the default checklist. User may paste inline or provide a file. |

---

## Step 0 — Confirm inputs

1. Check that the user has provided a copy doc. If not, ask before proceeding.
2. If a custom checklist is provided, use it instead of or alongside the default. If not, fetch the checklist from the designops source of truth: `https://raw.githubusercontent.com/Sophie-32/sites-designops/master/checklists/copy-doc-review.md`. If the fetch fails (network error, 404, etc.), fall back to the local copy at `references/default-checklist.md`.
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
- **Page type** — read the "Page type" metadata field if present (e.g. "Product or service", "Landing page", "App / product UI", "Documentation"). If absent, infer from content. This determines which checklist sections apply (see Step 2).
- Metadata fields (page title, description, navigation placement) and whether they are complete
- Heading levels and whether they are explicitly marked
- CTA text and any noted destinations
- Link text and any noted destinations
- Input field labels and placeholder text
- Any TBD, placeholder, or unresolved markers
- Open comments or revision notes

**Note:** Copy docs exported from Google Docs may have table-based layouts with template markers (e.g. `[col:1, ch:60]`). Extract the meaningful content and ignore template scaffolding.

---

## Step 2 — UX quality check

### First: gate sections by doc type

Not every section applies to every doc. Before checking, decide which sections are **in scope** based on the page type from Step 1:

- **Marketing / product / landing pages** (no interactive flows): section 4 (Forms & Inputs) and the interactive parts of 7 (Completeness — hover/focus/error/success/empty/loading states) are **Not applicable**. Mark them N/A and **do not** flag missing forms as issues — their absence is expected.
- **App / product UI / flow docs**: all sections apply, including Forms. Here a missing form *is* a real gap.

State which sections you are treating as N/A and why, so a reader can see it was a deliberate decision, not an oversight. When genuinely unsure whether a doc has interactive states, mark the relevant checks **needs review** rather than passing or failing them.

### Then: work through each in-scope section

For each checklist item:

1. Check the extracted content to determine a status: **✅ pass / issue / ❓ needs review / ⬜ not applicable**
2. Cite the specific section and text or missing element as evidence
3. For each *issue*, assign severity:
   - 🔴 **Critical** — blocks design from starting (missing required metadata, undefined CTA destination)
   - 🟡 **Needs work** — vague copy, missing best practice, inconsistency
   - 🔵 **Minor** — small wording or pattern improvement

### Evidence requirement

Every issue must be backed by a specific citation from the document. Do not flag something as missing or incorrect without first verifying it against the actual text. For example:

- **Acronyms:** Before flagging an acronym as unexpanded, search the full document for the expanded form. Many copy docs introduce the full term in the body text (e.g. "Software Composition Analysis (SCA)") even if the heading or list only uses the abbreviation. If the expansion exists anywhere before or at the first use of the acronym, the check passes.
- **Character limits:** Count the actual characters rather than estimating.
- **Link destinations:** Confirm a link is genuinely missing or broken — do not assume based on formatting alone.

### Severity overrides

The following should always be treated as **🔵 Minor**, regardless of what the default rules would suggest:

- **Logo alt text** — missing or generic alt text on logos (e.g. company logos in partner sections). These are cosmetic, not functional accessibility gaps.
- **"Learn more" links with an ARIA label** — if a "Learn more" link has an `aria-label` that provides context, the accessibility requirement is technically met. Flag as minor for copy improvement, not as a standard accessibility issue.
4. Use **❓ needs review** for anything you genuinely cannot verify from the text alone (e.g. whether a domain mismatch is intentional, whether an unwritten state exists elsewhere in the flow). Do not force these into a pass or a severity — report them honestly in the Needs review bucket.

### Checklist sections (from designops checklist)

1. Structure & Hierarchy
2. CTAs
3. Links
4. Forms & Inputs
5. Accessibility
6. Navigation
7. Completeness
8. Character Limits
9. Tone & Clarity
10. Comments & Revisions

---

## Step 3 — Write the audit report

Load `references/report-template.md` and use it as the structure for the report. Fill in every section based on findings from Step 2.

**Report ordering:** Organise issues by page section in the order they appear in the document (top to bottom), not by check category. Tag each issue with its check category in brackets (e.g. [CTAs], [Accessibility]) so the category is still visible. This lets a reviewer read the report alongside the copy doc without jumping around.

**Passing checks:** All checks that pass should go at the bottom of the report in the "✅ What looks good" section, not interleaved with issues.

Remove sections that have no findings (e.g. if no forms are present, remove Forms & Inputs entirely rather than leaving it blank).

**The report itself must follow the Canonical copy style guide** (`shared/copy-style-guide-checklist.md`). Key rules for report output:
- Use **en dashes with spaces** ( – ) for sentence breaks, not em dashes (—) or hyphens (-).
- Use US English spelling.
- Spell out single-figure numbers (one–nine); use digits from 10 up.
- No gendered pronouns – use they/them.

---

## Step 4 — Deliver and save the report

1. Output the report inline in chat as markdown.
2. **Automatically save** the report to `reports/` using the filename format `[doc-slug]-[YYYY-MM-DD].md`. Derive the slug from the document title or page URL in the metadata (lowercase, hyphens, no spaces) — e.g. `reports/canonical-ceph-2026-05-01.md`. Do not ask the user for confirmation before saving.
   - **If a file with that name already exists** (e.g. a second review of the same doc on the same day), do **not** overwrite it. Add a run number: `[doc-slug]-[YYYY-MM-DD]-run2.md`, then `-run3.md`, and so on. This keeps every report so runs can be compared.
3. Tell the user the report has been saved and the filename.
4. Offer to dive deeper into any specific section or issue.
5. **Do not** suggest or request a Figma file review. The copy doc stage comes before design — there is no Figma file yet. The Figma review is a separate skill triggered later in the pipeline.

---

## Edge cases

| Situation | How to handle |
|---|---|
| Copy doc is empty or near-empty | Tell the user and ask them to confirm the correct file was provided. |
| Doc has many unresolved TBDs | Flag them all in the Completeness section. Note in the summary that design should not start until they are resolved. |
| No metadata table present | Flag as a critical issue under Structure & Hierarchy. |
| Doc is very long | Process the full document. If sections are clearly marked, process them in order and note any skipped content. |
| No error states defined | Not applicable for this workflow — error and feedback states have been removed from the checklist. |

---

## References

- **Source of truth:** `https://raw.githubusercontent.com/Sophie-32/sites-designops/master/checklists/copy-doc-review.md` — Full default UX content checklist (copy docs), hosted in the [sites-designops](https://github.com/Sophie-32/sites-designops) repo
- `references/default-checklist.md` — Local fallback copy of the checklist (used if GitHub fetch fails)
- `references/report-template.md` — Report structure template
- `reports/` — Saved audit reports, named `[doc-slug]-[YYYY-MM-DD].md`
