# UX content audit report — copy doc

**Document:** Canonical CloudRun (test-copy-doc.md)
**Date:** 2026-06-09
**Note:** Test fixture — fake product page for skill benchmarking.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 12 | 3 | 16 | 3 | 1 | 2 |

**Total issues:** 22 (3 critical, 16 needs work, 3 minor) · **Needs review:** 1 · **N/A sections:** Forms & inputs, Error & feedback states — marketing page

---

## UX quality check

### Structure & hierarchy

#### 🔴 Critical
- **Metadata: Page description** — Required metadata field is empty. Page description (160 characters max) has no content. Design and SEO cannot proceed without it.
  - *Found:* `\*Page description (160 characters max)` — blank | *Recommendation:* Write a concise page description before design begins.

#### 🟡 Needs Work
- **"More information" section** — Heading is vague and generic. Does not tell the reader what the section contains.
  - *Found:* "More information" | *Recommendation:* Replace with a descriptive heading, e.g. "How CloudRun works" or "Architecture overview".
- **Heading hierarchy** — Sections use `###` (H3) headings ("Why choose Canonical CloudRun", "Resources and guides", "Customer stories") but no H2 appears anywhere in the doc. Heading levels skip from H1 (hero) directly to H3.
  - *Found:* `### Why choose Canonical CloudRun`, `### Resources and guides`, `### Customer stories` | *Recommendation:* Use H2 for top-level section headings, or add an H2 grouping above.

#### 🔵 Minor
- **"Why choose…" section** — Bullet list ("Fully automated day-2 operations…") starts immediately after the paragraph with no lead-in sentence introducing the list.
  - *Found:* Paragraph ends "…trusted by TBD enterprises worldwide." then jumps to bullets. | *Recommendation:* Add a brief intro, e.g. "Key capabilities include:".

### CTAs

#### 🔴 Critical
- **Hero: "Learn more"** — CTA destination is empty. The link href is `()` with no URL.
  - *Found:* `[Learn more]()` | *Recommendation:* Add the destination URL.

#### 🟡 Needs Work
- **Hero: "Learn more"** — Vague CTA text. "Learn more" does not tell the user what they will learn or where they will go.
  - *Found:* "Learn more" | *Recommendation:* Use a specific action verb, e.g. "Explore CloudRun features" or "Read the docs".
- **CTA Band: "Learn more"** — Duplicate CTA label. Same text as the hero CTA, creating ambiguity on the same page.
  - *Found:* `[Learn more](/cloudrun/docs)` (CTA Band) and `[Learn more]()` (Hero) | *Recommendation:* Differentiate, e.g. "Read the documentation".
- **CTA Band: "Click here to contact us"** — Uses banned "click here" pattern. CTA text should describe the action, not the mechanics.
  - *Found:* "Click here to contact us" | *Recommendation:* "Contact us" or "Talk to an expert".

### Links

#### 🟡 Needs Work
- **"More information" section** — Entire sentence used as link text. The full sentence is wrapped in a single link, making it hard to scan and inaccessible.
  - *Found:* `[Read this document to learn everything about how Canonical CloudRun compares to existing container orchestration platforms and why leading organisations across the globe are choosing it for their mission-critical workloads.]` | *Recommendation:* Link only the key phrase, e.g. "how CloudRun compares to existing platforms".
- **Resources section: "Read more"** — Standalone "Read more" link text is not descriptive. A screen reader user would hear "Read more" with no context.
  - *Found:* `[Read more](https://canonical.com/cloudrun/docs)` | *Recommendation:* "Read the CloudRun documentation" or "Browse CloudRun guides".

### Forms & inputs

#### ⬜ Not applicable
Marketing page ("Product or service") with no form fields, input flows, or validation. Section skipped.

### Error & feedback states

#### ⬜ Not applicable
Marketing page with no interactive or transactional flows. No error, success, empty, or loading states expected. Section skipped.

### Accessibility

#### 🟡 Needs Work
- **"More information" section: image2** — Image reference has no alt text or description in the copy doc.
  - *Found:* `![][image2]` — no alt text, no descriptive bracket text | *Recommendation:* Add alt text describing the image content.
- **Resources section: whitepaper PDF** — Resource file is hosted on Google Drive instead of the Canonical asset manager.
  - *Found:* `[CloudRun architecture whitepaper (PDF)](https://drive.google.com/file/d/1abc123/view?usp=sharing)` | *Recommendation:* Upload to asset manager and update the link.
- **"Read more" / "Click here" link text** — Multiple links use non-descriptive text that is inaccessible for screen reader users. (Overlap with Links and CTAs sections above; noted here for accessibility context.)
  - *Found:* "Read more", "Click here to contact us" | *Recommendation:* Use descriptive link text throughout.

#### 🔵 Minor
- **CTA Band** — Instruction relies on visual position: "click the button on the right". Users who cannot see the layout or are on mobile will not know which button is meant.
  - *Found:* "click the button on the right to access the installation wizard" | *Recommendation:* Reference the button by its label, e.g. "select 'Contact us' to access the installation wizard".

### Navigation

#### 🔴 Critical
- **Metadata: Navigation** — Navigation placement is completely empty. No indication of where this page sits in the site structure, meganav path, or how users reach it.
  - *Found:* `Navigation` row is blank | *Recommendation:* Specify the full navigation path, e.g. "Meganav Canonical > Products > CloudRun".

#### 🟡 Needs Work
- **Meganav label** — If the page will appear in the meganav (likely, given it's a product page), the nav label and description are required but not provided.
  - *Found:* No meganav path or label anywhere in metadata | *Recommendation:* Add meganav path and a short description for the nav item.

### Completeness

#### 🟡 Needs Work
- **"Why choose…" section: TBD placeholder** — Unresolved "TBD" in body copy. Design should not start until this is replaced with a real number.
  - *Found:* "Our platform has been trusted by TBD enterprises worldwide." | *Recommendation:* Replace with the actual number or remove the claim.
- **Customer stories: TK placeholder** — Attribution name is a "TK" placeholder (journalism shorthand for "to come"). Must be filled in.
  - *Found:* "— TK, VP Engineering" | *Recommendation:* Replace with the real person's name and title.
- **Resources section: open author comment** — Unresolved inline comment from the author requesting updated data.
  - *Found:* "[AUTHOR: needs updated stats for Q2 — check with product team]" | *Recommendation:* Resolve before design — get the updated stats or remove the placeholder.

### Tone & clarity

#### 🟡 Needs Work
- **Inconsistent product name** — The product is referred to three different ways across the doc: "CloudRun", "Cloud Run", and "cloud-run". This creates confusion about the official name.
  - *Found:* "Canonical CloudRun" (hero, metadata), "Cloud Run by the numbers" (data spotlight), "cloud-run leverages the CNCF-certified…" (More information section) | *Recommendation:* Pick one canonical form and use it everywhere.
- **Dense jargon / unexpanded acronyms** — The "More information" section uses five acronyms (CNCF, K8s, OCI, CSI, CNI) without expanding any of them. Even for a technical audience, first use should be expanded.
  - *Found:* "cloud-run leverages the CNCF-certified K8s distribution with OCI-compliant container runtimes, integrated CSI drivers, and a CNI plugin architecture…" | *Recommendation:* Expand each acronym on first use.
- **Unsupported superlative claim** — "The world's most reliable" is an unprovable absolute claim that creates brand and potential legal risk.
  - *Found:* "The world's most reliable container management platform" | *Recommendation:* Rewrite with a provable or qualified claim, e.g. "An enterprise-proven container management platform".
- **Conflicting statistics** — The data spotlight claims "50% cost reduction" but the "Why choose" section says "Reduce costs by 40%". These contradict each other.
  - *Found:* "50%" (data spotlight) vs "40%" (Why choose section) | *Recommendation:* Verify the correct figure and use it consistently.

#### 🔵 Minor
- **Hero description** — Single sentence is 50+ words and very dense. Hard to scan.
  - *Found:* "The world's most reliable container management platform, delivering enterprise-grade Kubernetes operations with seamless multi-cloud support and unmatched performance…" (one sentence, ~55 words) | *Recommendation:* Break into 2–3 shorter sentences.

### Comments & revisions

#### 🟡 Needs Work
- **CTA Band: TODO** — Unresolved TODO comment in body copy that must be addressed before design or publishing.
  - *Found:* "TODO: check with legal before publishing pricing claims" | *Recommendation:* Complete the legal review and remove the TODO.
- **Resources section: author comment** — Open inline comment. (Also flagged under Completeness.)
  - *Found:* "[AUTHOR: needs updated stats for Q2 — check with product team]" | *Recommendation:* Resolve and remove.

---

## ❓ Needs review

- **Hero: CTA domain mismatch** — "Get in touch" links to `ubuntu.com/cloudrun#get-in-touch` but this is a `canonical.com/cloudrun` page. May be intentional (shared contact form) or an error.
  - *Found:* `[Get in touch](https://ubuntu.com/cloudrun#get-in-touch)` | *Question:* Is the ubuntu.com domain the correct destination for this CTA, or should it point to canonical.com?

---

## ⬜ Not applicable

- **Forms & inputs** — N/A: marketing product page with no form fields or input flows.
- **Error & feedback states** — N/A: marketing page with no interactive or transactional states.

---

## ✅ What looks good

- **Page title** is concise and within the 60-character limit.
- **Hero structure** follows the standard pattern: title → subtitle → description → CTAs.
- **Data spotlight** uses a clear "by the numbers" format with three concrete data points.
- **Customer stories** section includes a real quote with attribution (pending TK resolution).
- **CTA Band** provides a clear closing section with a direct question and action.
- **Asset links** for hero and customer images use the Canonical asset manager (assets.ubuntu.com).
- **Page owner** and **approval workflow** are specified in metadata.

---

## Recommended priority order

1. Fix all 🔴 Critical issues before design begins
2. Address 🟡 Needs Work items
3. Polish 🔵 Minor items

---

## 🔲 Manual checks for reviewer

- [ ] **Cross-reference with design intent:** confirm the copy matches the structure and intent of any related Figma file (if available)
- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved
