# UX content audit report – copy doc

**Document:** c.com data services copy doc
**Date:** 2026-06-17
**Note:** Page type is "Product or service" – a marketing page with no interactive flows. Forms, error states, and interactive-only completeness checks are N/A.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | – | 3 | 11 | 3 | 1 | 2 |

**Total issues:** 17 (3 critical, 11 needs work, 3 minor) · **Needs review:** 1 · **N/A sections:** Forms & Inputs, Error & Feedback States – marketing page

---

## UX quality check

### Structure & hierarchy

#### 🟡 Needs Work

- **Metadata: Page URL** – The page URL field is blank. Designers and developers cannot confirm the correct URL for the page, which may lead to incorrect link destinations being used in other docs or specs.
  - *Found:* "\*Current or suggested page URL" field left empty | *Recommendation:* Add the intended URL or a placeholder such as `canonical.com/data/services`.

- **Metadata: Heading levels** – The doc uses template position markers (e.g. `[col:1, ch:60]`) to imply hierarchy, but heading levels (H1, H2, H3) are not explicitly labelled. Designers need to infer intent from context rather than having it stated.
  - *Found:* No H1/H2/H3 labels anywhere in the doc | *Recommendation:* Mark each heading's level explicitly, e.g. add "H1:", "H2:", "H3:" labels to the template marker rows.

- **Metadata: Navigation** – The navigation field contains the template's instructional placeholder text ("Indicate how a user navigates to the page without a direct URL…"). The actual navigation path is not filled in.
  - *Found:* Template instructions present, no navigation path specified | *Recommendation:* Replace with the actual path – e.g. "All Canonical > Products > Data > Services".

---

### CTAs

#### 🔴 Critical

- **Hero / Closing row: "Discover our portfolio >"** – This CTA appears twice (hero and closing row) with no destination noted. Designers cannot link it, and developers cannot implement it.
  - *Found:* `Discover our portfolio >` – no URL or destination | *Recommendation:* Add the target URL, e.g. `canonical.com/data`.

- **Support tab: Phone and ticket support – "Learn more >"** – This CTA has no URL or destination. All other service CTAs have destinations; this one does not.
  - *Found:* `Learn more >` with no link | *Recommendation:* Add the target URL or remove the CTA if the page does not exist yet.

#### 🟡 Needs Work

- **Multiple tables: "Learn more >"** – Four service cards (Ubuntu Pro, Container build service, Firefighting support, Managed services) use "Learn more >" as CTA text. "Learn more" is on the prohibited list – it is vague, does not describe the action, and does not make sense out of context.
  - *Found:* Ubuntu Pro → `ubuntu.com/pro`; Container build service → `ubuntu.com/containers/container-build-service`; Firefighting support → `ubuntu.com/support/firefighting`; Managed services → `ubuntu.com/managed/apps` | *Recommendation:* Replace with action-specific text, e.g. "Explore Ubuntu Pro", "Read about container builds", "Learn about firefighting support", "Explore managed services".

---

### Links

#### ❓ Needs review (moved to Needs review section below)

---

### Accessibility

#### 🟡 Needs Work

- **Equal Heights Row / Logo section: No alt text for images** – Four feature images and at least one logo image are included in the doc with no alt text specified. Without alt text, screen readers and SEO tooling will have nothing to describe the images.
  - *Found:* `![][image1]` through `![][image4]` and `![][image5]` – all without alt text | *Recommendation:* Add descriptive alt text for each image, or confirm with the designer that they are decorative (in which case note `alt=""`).

- **Equal Heights Row: Image assets linked from Google Drive** – The four feature images link to Google Drive (`drive.google.com`). The accessibility checklist requires resource files to be hosted on the asset manager, not external services.
  - *Found:* `[Asset link](https://drive.google.com/file/d/...)` for all four feature images | *Recommendation:* Upload final assets to the Canonical asset manager and update the links.

---

### Navigation

#### 🔴 Critical

- **Metadata: Page URL is blank** – Listed here in addition to Structure & Hierarchy because an undefined URL also blocks correct navigation configuration.
  - *See Structure & hierarchy above.*

#### 🟡 Needs Work

- **Metadata: Navigation path not filled in** – Covered under Structure & Hierarchy.

---

### Completeness

#### 🟡 Needs Work

- **Metadata: og:Image blank** – The og:Image field contains placeholder text ("Please include a link to the image you would like as the page thumbnail") rather than an actual asset. Without this, social sharing and search previews will not have a thumbnail.
  - *Found:* og:Image field = template placeholder | *Recommendation:* Add a link to the approved thumbnail image, or flag as TBD so it is not overlooked.

- **Metadata: Asset manager tag blank** – The asset manager tag field is empty. Designers need this to locate approved assets.
  - *Found:* "Link to asset manager tag (for designers)" – blank | *Recommendation:* Add the relevant tag or mark as TBD.

- **On-demand services tables: Empty rows** – The Training and certifications, Deployment services, Consulting, and Workshops tables all contain multiple blank rows. It is unclear whether these are unused template rows or indicate missing content that is yet to be written.
  - *Found:* Training and certifications – three empty rows; Deployment services – three empty rows; Consulting – four empty rows; Workshops – three empty rows | *Recommendation:* Either fill in the missing content or explicitly remove the empty rows so designers know the list is complete.

- **Logo section: No company names listed** – The "These companies trust Canonical" section contains a single logo image placeholder with no company names. Designers cannot identify which logos to use.
  - *Found:* `![][image5]` – one logo, no names | *Recommendation:* List the company names (and confirm approval to use their logos) so designers know what to include.

---

### Character limits

#### 🟡 Needs Work

- **Metadata: Page description over limit** – The page description is 165 characters against a 160-character limit.
  - *Found:* "Get enterprise-grade services from Canonical. Enjoy security, automation, and SLA-backed expertise for your data and AI solutions across private and public clouds." (165 chars) | *Recommendation:* Trim to 160 characters maximum, e.g. remove "Enjoy" and tighten: "Get enterprise-grade services from Canonical – security, automation, and SLA-backed expertise for your data and AI solutions across private and public clouds."

- **Equal Heights Row: Card descriptions exceed ch:180 limit** – All four card descriptions are significantly over the 180-character limit marked in the doc.
  - *Found:*
    - Full stack experts: ~270 chars (limit 180)
    - Automated infrastructure: ~252 chars (limit 180)
    - Security maintenance: ~265 chars (limit 180)
    - Transparent pricing: ~268 chars (limit 180)
  - *Recommendation:* Shorten each description to 180 characters or fewer.

- **Hero / Closing row: "Discover our portfolio >" over CTA limit** – The CTA text is 24 characters against a ch:20 limit.
  - *Found:* "Discover our portfolio >" (24 chars, limit 20) | *Recommendation:* Shorten, e.g. "Our portfolio >" (15 chars) or "Explore our portfolio" (21 chars – still 1 over, but closer).

#### 🔵 Minor

- **Consulting tab label over limit** – "Consulting and trainings" is 24 characters against a ch:20 limit for tab labels.
  - *Found:* "Consulting and trainings" (24 chars, limit 20) | *Recommendation:* See Tone & clarity note below – correcting the plural also brings the label closer: "Consulting and training" (23 chars, still 3 over). Further shortening to "Consulting & training" (21 chars) or "Consulting" (10 chars) would resolve the limit.

---

### Tone & clarity

#### 🔵 Minor

- **Consulting and trainings tab: Incorrect plural** – "Consulting and trainings" should be "Consulting and training". "Training" is not pluralised in standard English usage.
  - *Found:* "Consulting and trainings" | *Recommendation:* Change to "Consulting and training".

- **Deployment services: Awkward phrasing** – "A handover documentation explaining the deployed stack" uses "a documentation" which is non-standard. Documentation is an uncountable noun.
  - *Found:* "A handover documentation explaining the deployed stack" | *Recommendation:* Change to "Handover documentation explaining the deployed stack" or "A handover document explaining the deployed stack".

---

## ❓ Needs review

- **Support tab: Support portal and knowledge base link to the same URL** – Both "Access to our support portal" and "Access to our knowledge base" link to `https://support-portal.canonical.com/`. This may be a copy error if the knowledge base lives at a different URL.
  - *Found:* Both entries → `support-portal.canonical.com` | *Question:* Are these intentionally the same URL, or does the knowledge base have a dedicated link (e.g. a `/knowledge-base` path)?

---

## ⬜ Not applicable

- **Forms & Inputs** – N/A: marketing / product page with no form or input flow.
- **Error & Feedback States** – N/A: marketing / product page with no interactive states; absence of error and success copy is expected.

---

## ✅ What looks good

- **Clear three-tier service structure** – Organising services into Security maintenance, Support, and Consulting and training, with a clear tabbed layout, makes the offering easy to scan.
- **Most CTAs have destinations** – The majority of CTA links include a URL or named destination, which is good practice.
- **Consistent terminology** – "Data and AI" is used consistently throughout all sections. No conflicting terms for the same concept.
- **Metadata is largely complete** – Page title, description, owner, approvals, target audience, funnel stage, and design support level are all filled in.
- **Service descriptions are specific** – Each service card clearly describes what is included, going beyond vague marketing language.

---

## Recommended priority order

1. Fix all 🔴 Critical issues before design begins – specifically: add the page URL, and confirm destinations for both undefined CTAs.
2. Address 🟡 Needs Work items – particularly character limit overruns on card descriptions and the page description, the navigation path, and accessibility gaps (alt text, asset manager links).
3. Confirm the ❓ Needs review item (duplicate support portal/knowledge base URL) with the page owner.
4. Polish 🔵 Minor items (wording, tab label plural).

---

## 🔲 Manual checks for reviewer

- [ ] **Cross-reference with design intent:** confirm the copy matches the structure and intent of the Figma file linked in the metadata (mock-up and prototype links are provided).
- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path.
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved.
