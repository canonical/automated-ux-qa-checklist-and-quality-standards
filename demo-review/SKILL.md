---
name: demo-review
description: >
  Use this skill whenever the user wants to audit a demo or live URL for UX content quality.
  Triggers include: "audit this demo", "review this PR demo", "check UX content on this page",
  "QA this demo", "review the demo page", "check the copy on this URL", or when the user
  pastes a URL or GitHub PR link and asks for a content or UX review.
---

# Demo Review Skill

Performs two checks on a demo or live web page by fetching its content:

1. **UX quality check** — reviews page content against UX best practice checklist
2. **Brand & style compliance** — reviews all copy against the Canonical copy style guide (`shared/copy-style-guide-checklist.md`)

Outputs a structured markdown report organised by page section order (top to bottom), with issues cited to
specific page sections and elements. This lets a reviewer read the report side by side with the page.

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| Demo URL or GitHub PR URL | Yes | A demo URL directly, or a GitHub PR URL to be converted using `scripts/pr-to-demo-url.sh` |
| Custom UX checklist | Optional | Overrides or supplements the default checklist. User may paste inline or provide a file. |

---

## Step 0 — Confirm inputs and resolve URL

1. Check what the user has provided:
   - **Demo URL** (e.g. `https://canonical-com-1444.demos.haus/path`) — use directly.
   - **GitHub PR URL** (e.g. `https://github.com/canonical/canonical.com/pull/1444`) — run `scripts/parse-pr-inputs.sh` to extract all inputs from the PR body. The script returns JSON with demo URL(s), Figma file URL (with node ID if present), and copy doc URL. If the PR body does not contain a `demos.haus` URL, the script falls back to `scripts/pr-to-demo-url.sh` to construct demo URLs from changed template files.
   - If neither is provided, ask before proceeding.
2. If the script returns a Figma URL, use it for design fidelity checks (see Step 2). If it returns a copy doc URL, use it for copy comparison.
3. If the script returns multiple demo URLs (the PR changed multiple pages), ask the user which page(s) to audit, or offer to audit all.
4. If a custom checklist is provided, use it instead of or alongside the default. If not, fetch the checklist from the designops source of truth: `https://raw.githubusercontent.com/Sophie-32/sites-designops/master/checklists/demo-review.md`. If the fetch fails (network error, 404, etc.), fall back to the local copy at `references/default-checklist.md`.
5. Tell the user what will be checked and which inputs were found.

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

### Checklist sections (from designops checklist)

1. Structure & Hierarchy
2. CTAs
3. Links
4. Forms & Inputs
5. Accessibility
6. Navigation
7. Mobile Considerations
8. Manual Checks (include as reminders in report, not as pass/fail)

---

## Step 3 — Brand & style compliance

Load `shared/copy-style-guide-checklist.md` and run it against all extracted text content from the page. This checks the **page copy** against the Canonical copy style guide.

1. Run **Part A (deterministic checks)** — flag every match. These include: US spelling, "open source" formatting, product names, capitalisation, units, dates, numbers, punctuation, apostrophes, acronyms, link/CTA text, hyphens, banned words/phrases, consistency spellings, formatting conventions.
2. Run **Part B (judgment checks)** — apply with examples given. These include: brand voice, tone, sentence length, readability, active voice, security/absolute claims, superlatives, inclusive language, commonly confused words, plain language.

Report findings under a separate **Brand & style compliance** heading in the report. Use the severity scale from the style guide checklist:
- 🔴 **Critical** — legal, compliance, or brand-integrity risk (unprovable claims, wrong product names)
- 🟡 **Needs work** — banned words/phrases, wrong capitalisation, voice/tone misses
- 🔵 **Minor** — punctuation, units, number/date formatting, dash style

**Do not double-count:** If an issue is already flagged by the UX quality check (e.g. non-descriptive link text), report it only once under whichever check is more specific.

---

## Step 4 — Write the audit report

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

## Step 5 — Deliver and save the report

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
| PR URL provided | Run `scripts/pr-to-demo-url.sh` to convert. If the script fails (e.g. `gh` not authenticated, repo not supported), tell the user and ask for the demo URL directly. |
| PR changed non-page files only | The script may return no demo URLs if only CSS, JS, or config files changed. Tell the user and ask for the demo URL manually. |

---

## References

- **Source of truth:** `https://raw.githubusercontent.com/Sophie-32/sites-designops/master/checklists/demo-review.md` — Full default UX content checklist (adapted for live pages), hosted in the [sites-designops](https://github.com/Sophie-32/sites-designops) repo
- `references/default-checklist.md` — Local fallback copy of the checklist (used if GitHub fetch fails)
- `references/report-template.md` — Report structure template
- `scripts/parse-pr-inputs.sh` — Extracts demo URL(s), Figma URL (with node ID), and copy doc URL from a GitHub PR body. Returns JSON.
- `scripts/pr-to-demo-url.sh` — Fallback: converts a GitHub PR URL to demo URL(s) from changed template files
- `reports/` — Saved audit reports, named `[page-slug]-[YYYY-MM-DD].md`
