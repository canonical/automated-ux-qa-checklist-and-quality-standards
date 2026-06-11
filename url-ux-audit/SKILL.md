---
name: url-ux-audit
description: >
  Use this skill whenever the user wants to audit a live URL for UX content quality.
  Triggers include: "audit this URL", "review this page", "check UX content on this site",
  "post-deployment check", "QA this page", "review the live page", "check the copy on
  this URL", or when the user pastes a URL and asks for a content or UX review.
---

# URL UX Audit Skill

Performs a UX content quality check on a live web page by fetching its content and
reviewing it against a UX best practice checklist.

Outputs a structured markdown report organised by page section order (top to bottom), with issues cited to
specific page sections and elements. This lets a reviewer read the report side by side with the page.

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| URL | Yes | The live page to audit |
| Custom UX checklist | Optional | Overrides or supplements the default checklist. User may paste inline or provide a file. |

---

## Step 0 — Confirm inputs

1. Check that the user has provided a URL. If not, ask before proceeding.
2. If a custom checklist is provided, use it instead of or alongside the default. If not, load `references/default-checklist.md`.
3. Tell the user what will be checked.

---

## Step 1 — Fetch and extract content from the URL

Use `WebFetch` to retrieve the page. Extract all visible text content, grouped by page section using HTML landmarks and structure as a guide:

```
Section: [landmark or inferred role — e.g. Header, Nav, Hero, Main, Form, Footer]
  - [element role if inferable]: "[text content]"
  - ...
```

Process the full page. Note while extracting:
- Input fields and whether they have visible labels (vs placeholder-only)
- Button and link text
- Error or feedback messages if present in the HTML
- Empty or placeholder text nodes (e.g. "Lorem ipsum", "[placeholder]")
- Any alt text on images
- Any visible form validation or hint text

**Limitation note:** `WebFetch` retrieves static HTML. Text rendered purely by JavaScript after page load may not be captured. Note this at the top of the report if the page appears to be a JS-heavy SPA.

---

## Step 2 — UX quality check

Work through each section of the checklist (default or custom). For each item:

1. Check the extracted content to determine: **pass / fail / needs review / not applicable**
2. Cite the specific page section and text or missing element as evidence
3. Assign severity:
   - 🔴 **Critical** — functional or accessibility blocker (missing label, silent error, etc.)
   - 🟡 **Needs work** — vague copy, missing best practice, inconsistency
   - 🔵 **Minor** — small wording or pattern improvement

### Severity overrides

The following should always be treated as **🔵 Minor**, regardless of what the default rules would suggest:

- **Logo alt text** — missing or generic alt text on logos (e.g. company logos in partner sections). These are cosmetic, not functional accessibility gaps.
- **"Learn more" links with an ARIA label** — if a "Learn more" link has an `aria-label` that provides context, the accessibility requirement is technically met. Flag as minor for copy improvement, not as a standard accessibility issue.

### Checklist sections (from default-checklist.md)

1. Structure & Hierarchy
2. CTAs
3. Links
4. Forms & Inputs
5. Error & Feedback States
6. Accessibility
7. Navigation
8. Mobile Considerations
9. Manual Checks (include as reminders in report, not as pass/fail)

---

## Step 3 — Write the audit report

Load `references/report-template.md` and use it as the structure for the report. Fill in every section based on findings from Step 2.

**Report ordering:** Organise issues by page section in the order they appear on the page (top to bottom), not by check category. Tag each issue with its check category in brackets (e.g. [CTAs], [Accessibility]) so the category is still visible. This lets a reviewer read the report alongside the live page without jumping around.

**Passing checks:** All checks that pass should go at the bottom of the report in the "✅ What looks good" section, not interleaved with issues.

Remove sections that have no findings (e.g. if no forms were found, remove Forms & Inputs entirely rather than leaving it blank).

**The report itself must follow the Canonical copy style guide** (`shared/copy-style-guide-checklist.md`). Key rules for report output:
- Use **en dashes with spaces** ( – ) for sentence breaks, not em dashes (—) or hyphens (-).
- Use US English spelling.
- Spell out single-figure numbers (one–nine); use digits from 10 up.
- No gendered pronouns – use they/them.

---

## Step 4 — Deliver and save the report

1. Output the report inline in chat as markdown.
2. **Automatically save** the report to `reports/` using the filename format `[page-slug]-[YYYY-MM-DD].md`. Derive the page slug from the URL path (lowercase, hyphens, no spaces) — e.g. `reports/checkout-2026-04-20.md`. Do not ask the user for confirmation before saving.
3. Tell the user the report has been saved and the filename.
4. Offer to dive deeper into any specific section or issue.

---

## Edge cases

| Situation | How to handle |
|---|---|
| URL is not reachable | Tell the user and ask them to confirm the URL is publicly accessible. |
| Page returns empty or near-empty content | Warn the user — the page may require authentication or be JS-rendered. Note the limitation in the report. |
| Page is behind a login | Note that the audit covers only what is publicly accessible. Flag that authenticated states could not be checked. |
| Very long page | Process all content. If context limits are a concern, prioritise above-the-fold sections and note any sections that were skipped. |

---

## References

- `references/default-checklist.md` — Full default UX content checklist (adapted for live pages)
- `references/report-template.md` — Report structure template
- `reports/` — Saved audit reports, named `[page-slug]-[YYYY-MM-DD].md`
