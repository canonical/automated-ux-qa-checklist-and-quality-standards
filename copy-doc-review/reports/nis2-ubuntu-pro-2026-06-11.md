# UX content audit report – copy doc

**Document:** NIS2 compliance with Ubuntu Pro
**Date:** 2026-06-11
**Note:** Landing page targeting executives. Forms, error states, and interactive copy are N/A.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 14 | 3 | 7 | 3 | 4 | 2 |

**Total issues:** 13 (3 critical, 7 needs work, 3 minor) · **Needs review:** 4 · **N/A sections:** Forms & inputs, Error & feedback states – marketing landing page

---

## UX quality check

### Structure & hierarchy

#### 🟡 Needs Work

- **Throughout** – Heading levels (H1, H2, H3) are not explicitly marked anywhere in the document. The section labels (HERO, TIERED LIST, BASIC TEXT) describe layout slots, not heading hierarchy. Designers cannot infer the correct heading level from this doc alone.
  - *Found:* Section labels only (e.g. HERO, TABBED SECTION, BASIC TEXT) | *Recommendation:* Mark each heading with its intended level – e.g. H1, H2, H3 – directly alongside the text.

- **Mid-page heading** – "Ubuntu Pro supports NIS2 compliance everywhere" is marked with a Markdown `#` (H1), but it appears mid-page after the hero and two other sections. A page should have one H1; this is almost certainly an H2.
  - *Found:* `# Ubuntu Pro supports NIS2 compliance everywhere` | *Recommendation:* Change to H2 and confirm intended level with the visual designer.

### CTAs

#### 🔴 Critical

- **Hero and bottom section** – "Contact us" is used twice in the same doc but links to two different destinations. Same visible label, different behaviour – this will confuse users and is a clear inconsistency.
  - *Found:* Hero → `https://ubuntu.com/security/certifications#get-in-touch`; Bottom section → `https://ubuntu.com/support/contact-us?product=support-overview` | *Recommendation:* Differentiate the labels to reflect the distinct destinations, or confirm that both should resolve to the same URL.

- **Ubuntu Pro section – cloud logos** – "Learn more" CTAs for AWS and Azure have no destination URL. GCP correctly includes a URL (`https://ubuntu.com/gcp`); AWS and Azure do not.
  - *Found:* `Learn more (aria-label: Learn more about Ubuntu on AWS)` – no URL; `Learn more (aria-label: Learn more about Ubuntu on Azure)` – no URL | *Recommendation:* Add destination URLs for AWS and Azure "Learn more" links (e.g. `/aws`, `/azure`).

#### 🟡 Needs Work

- **Ubuntu Pro section – cloud logos** – "Learn more" is vague as visible button text. Aria-labels are provided and partially mitigate this, but visible text should be meaningful on its own – especially for an executive audience who may skim.
  - *Found:* "Learn more" × 3 | *Recommendation:* Use visible text that names the destination, e.g. "Ubuntu Pro on AWS", or restructure so the logo itself carries the link with a proper accessible name.

### Links

#### 🟡 Needs Work

- **Ubuntu Pro section – logo images** – The AWS, Azure, and GCP logos are formatted as links pointing to Google Drive folder URLs. Google Drive is not a user-facing destination. It is unclear whether these are asset handoff references for designers (where the logo files are stored) or intended as clickable links for users. If the logos are user-facing links, proper destination URLs must be specified.
  - *Found:* `[AWS logo](https://drive.google.com/drive/folders/142eE0164AR-u2zpxKvkt0pCnPriNjoJc)` | *Recommendation:* Clarify whether logos should be clickable links for users. If yes, replace Google Drive URLs with the intended live destinations. If no, remove the link syntax and mark as image-only.

### Accessibility

#### 🔵 Minor

- **Ubuntu Pro section – cloud logos** – Alt text for the AWS, Azure, and GCP logo images is not specified in the doc. Even if these are "decorative" logos, a screen reader user should know which cloud platform each refers to.
  - *Found:* `[AWS logo]`, `[Azure logo]`, `[Google Cloud logo]` – no alt text | *Recommendation:* Add explicit alt text for each logo, e.g. `alt="AWS"`, `alt="Microsoft Azure"`, `alt="Google Cloud"`.

### Navigation

#### ✅ Pass

Navigation placement is specified: linked from `https://ubuntu.com/security/security-standards`. No mega nav entry or redirect required.

### Completeness

#### 🔴 Critical

- **Metadata** – "Main action for users to take on the page" is blank. This field informs design prioritisation and CTA hierarchy.
  - *Found:* Field is empty | *Recommendation:* Fill in the primary user action before design begins – e.g. "Contact sales to discuss NIS2 compliance needs" or "Start a free Ubuntu Pro trial".

#### 🟡 Needs Work

- **Blog section** – No copy is defined. The section contains only backend tag IDs (`4633, 4869, 3586, 4632`). There is no section heading for users, no intro text, and no CTA.
  - *Found:* "Latest from our blog | Blogs with tag IDs: 4633 (EU regulations), 4869 (NIS2), 3586 (Ubuntu Pro), 4632 (CRA)" | *Recommendation:* Add a user-facing section heading (e.g. "Learn more about NIS2 compliance") and confirm whether a CTA or intro sentence is needed.

- **Metadata – approvals** – The approvals field shows "Choose", which appears to be an unfilled dropdown. It is unclear who needs to approve this page before it goes into development.
  - *Found:* "Please indicate approvals needed before the page goes into development: Choose" | *Recommendation:* Select the appropriate approver(s) or confirm this field is intentionally left blank.

### Tone & clarity

#### 🟡 Needs Work

- **Tiered list – Monitoring at scale** – "Single pane of glass" is IT industry jargon. The target audience is executives, not infrastructure engineers; this phrase may not land clearly.
  - *Found:* "manage your fleet through a single pane of glass" | *Recommendation:* Replace with plain language, e.g. "manage your entire fleet from one dashboard".

- **Throughout** – Several technically specific terms appear without context for an executive audience: "kernel patching" (Patch management column), "FIPS certified packages" and "FedRAMP compliant" (Lucid case study tab). Executives approving spend need to understand outcomes, not implementation details.
  - *Found:* "kernel patching without downtime"; "FIPS certified packages and became FedRAMP compliant" | *Recommendation:* Either add one-line plain-language explanations alongside technical terms, or replace them with outcome-focused language aligned to executive concerns (risk, cost, compliance outcomes).

#### 🔵 Minor

- **Tiered list – Supply chain security** – "As a one-stop shop" is colloquial and inconsistent with Canonical's direct, technical tone.
  - *Found:* "As a one-stop shop, you can rely on us for software and ongoing maintenance" | *Recommendation:* Rephrase – e.g. "You can rely on Canonical for software supply and ongoing maintenance".

### Comments & revisions

#### ✅ Pass

No open TBD markers or placeholder text found (aside from the "Choose" dropdown noted under Completeness).

---

## ❓ Needs review

- **Ubuntu Pro section – logo links** – The AWS, Azure, and GCP logos are formatted as markdown links pointing to Google Drive folders. If these are asset handoff references for designers only (not intended user-facing links), the copy doc should make that explicit. If logos are clickable, destination URLs are missing for AWS and Azure.
  - *Found:* `[AWS logo](https://drive.google.com/drive/folders/...)` | *Question:* Are the logos intended to be clickable links for users? If yes, what are the destination URLs?

- **Hero – video** – A YouTube video is referenced in the hero, but no accessible label, caption, or transcript note is included in the doc.
  - *Found:* `[Video](https://www.youtube.com/watch?reload=9&v=4DhX_hcLLd0)` | *Question:* Does this video need captions or a transcript? Should the video have a visible title or description alongside it in the UI?

- **Tabbed section – Lucid case study** – The Lucid tab describes FedRAMP compliance, not NIS2. On a page specifically about NIS2, this could confuse visitors or appear off-topic.
  - *Found:* "Ubuntu Pro helps Lucid Software meet FedRAMP compliance for government contracts" | *Question:* Is this intentional cross-regulation positioning? If so, a brief bridging sentence connecting FedRAMP and NIS2 would help justify its presence. If not, a more directly relevant case study should replace it.

- **Navigation** – "Linked from another page" indicates this page will only appear as a contextual link from the security standards page. Confirm whether it will also appear in the mega nav, the security section index, or any other navigational entry point.
  - *Found:* "Navigation: Linked from another page https://ubuntu.com/security/security-standards" | *Question:* Is this the only navigation entry point, or are there additional nav placements to document?

---

## ⬜ Not applicable

- **Forms & inputs** – N/A: marketing landing page with no form or input fields.
- **Error & feedback states** – N/A: marketing landing page with no interactive states.

---

## ✅ What looks good

- **Metadata** – Page title (32 chars), description (55 chars), and URL are all filled in, clearly worded, and within character limits.
- **CTA destinations** – Most CTAs include destination URLs directly in the doc, which is exactly what developers and designers need.
- **CTA differentiation** – Hero and bottom section each have two clearly differentiated CTAs (e.g. "Contact us" + "Get Ubuntu Pro"; "Contact us" + "Access a 30-day free trial"). Primary and secondary are distinct in label and destination (aside from the "Contact us" duplication flagged above).
- **Aria-labels** – "Learn more" buttons for cloud providers all include descriptive aria-labels, showing accessibility was considered.
- **Whitepapers and webinars** – Tab section uses descriptive titles as link text with destination URLs alongside. Easy to implement and accessible.
- **Terminology consistency** – "Ubuntu Pro", "Canonical", and "NIS2" are used consistently throughout. No synonym drift.
- **Navigation placement** – Specified clearly. No ambiguity about where this page lives in the site structure.

---

## Recommended priority order

1. Fix all 🔴 Critical issues before design begins – especially the blank "main action" field and the duplicate "Contact us" destinations
2. Address 🟡 Needs Work items – heading levels and blog section copy in particular will affect design decisions
3. Clarify the four ❓ Needs review points with the author – logo link intent and the Lucid case study relevance are the highest priority among them
4. Polish 🔵 Minor items at any stage

---

## 🔲 Manual checks for reviewer

- [ ] **Cross-reference with design intent:** confirm the copy matches the structure and intent of any related Figma file (if available)
- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved
