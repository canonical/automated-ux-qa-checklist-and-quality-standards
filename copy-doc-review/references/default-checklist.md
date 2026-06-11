# Default UX content checklist: copy docs

UX best practice checks for copy doc reviews. These are independent of any brand or style guide rules.

---

## 1. Structure and hierarchy

- [ ] Heading levels (H1, H2, H3) are clearly indicated in the doc
- [ ] Headings flow logically with no skipped levels
- [ ] All headings are meaningful and descriptive, not vague, generic, or placeholder text
- [ ] Lists and bullet groups have a heading, title, or intro text above them
- [ ] The most important information or action is first in the doc
- [ ] Multi-step flows have clear step labels
- [ ] Metadata table is complete (page title, description, and navigation placement are all filled in)

---

## 2. CTAs

- [ ] CTAs use specific, honest action verbs, not vague phrases like "learn more", "click here", "find out more", "submit"
- [ ] Destructive actions (delete, remove, cancel) are clearly and specifically labelled
- [ ] Primary and secondary CTAs in the same section are not identically labelled
- [ ] CTAs read naturally and make sense out of context (a reader should know what will happen when they click)
- [ ] CTA destinations are noted (where does each CTA link to?)

---

## 3. Links

- [ ] Link text is descriptive and meaningful
- [ ] Entire sentences are not marked as link text, only the relevant phrase
- [ ] Link destinations are specified in the doc (URL or page reference)
- [ ] Links with the same text in the same doc go to the same destination

---

## 4. Forms and inputs

> **Applies to:** docs that include a form or input flow. For marketing/product/landing pages with no form, mark this section **N/A** — do not flag the absence of a form.

- [ ] Every input field has a labelled field name in the copy
- [ ] Placeholder text is noted separately from labels and is not used as the label
- [ ] Required fields are clearly marked
- [ ] Field labels use natural, user-facing language
- [ ] If the page requires a form, a request for it is linked or noted in the doc

---

## 5. Error and feedback states

> **Applies to:** app / product UI / flow docs. For marketing/product/landing pages with no interactive states, mark this section **N/A** — the absence of error/success/loading copy is expected and is not an issue.

- [ ] Every error state in the flow has a defined message with no silent failures
- [ ] Error messages explain what went wrong in plain language
- [ ] Error messages tell the user how to fix the problem
- [ ] Success/confirmation messages confirm the specific action that was completed
- [ ] Empty states have explanatory text and a CTA or next step where appropriate
- [ ] Loading states have descriptive text, not just "loading..."

---

## 6. Accessibility

- [ ] Alt text is provided for any images, graphs, or graphics referenced in the doc, including diagrams
- [ ] Resource files (whitepapers, data sheets) are hosted on asset manager, not Google Drive or other external locations
- [ ] Icon-only elements have a defined accessible label
- [ ] Link text is descriptive with no "click here" or "read more" as standalone link labels
- [ ] Instructions do not rely solely on visual position ("the button on the right"), use labels instead

---

## 7. Navigation

- [ ] Navigation placement is specified: the page's location in the site structure is clearly indicated
- [ ] If the page appears in the mega nav, the nav label and description are included in the doc
- [ ] If the page is being moved, the old location and any required redirects are noted

---

## 8. Completeness

- [ ] All required states are written (default, hover/focus where copy differs, error, success, empty, loading) — *interactive states apply only to app/UI/flow docs; skip for static marketing pages*
- [ ] All variants of a component or flow are documented
- [ ] Microcopy (tooltips, helper text, validation messages) is included where needed
- [ ] Any conditional copy (e.g. "if user is logged in, show X; else show Y") is clearly specified

---

## 9. Character limits

> Reference: `shared/character-limits.md` for the full table of limits by section type.

- [ ] Page title is within 60 characters
- [ ] Page description is within 160 characters
- [ ] Section titles are within the limit for their section type (typically 60–70 characters)
- [ ] Supporting paragraphs are within the limit for their section type (typically 300, up to 900 for extended sections)
- [ ] CTA button text is within 20 characters
- [ ] CTA link/arrow text is within 60 characters
- [ ] Data spotlight values, labels, and descriptions are within their limits (10, 20, 100 characters respectively)
- [ ] Content flagged by the `ch:` markers in the copy doc matches the character limit specified

---

## 10. Tone and clarity

- [ ] Copy is written in plain language appropriate to the audience
- [ ] Sentences are scannable, not overly long or dense
- [ ] Terminology is consistent throughout the doc (same word for the same thing)
- [ ] No internal jargon, acronyms, or shorthand that won't make sense to the user

---

## 11. Comments and revisions

- [ ] All open comments in the doc are resolved or noted
- [ ] All "TBD", "placeholder", or "TK" markers are flagged for resolution before design begins

---

## 12. Manual checks (remind reviewer)

These should be completed by the reviewer:

- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved
