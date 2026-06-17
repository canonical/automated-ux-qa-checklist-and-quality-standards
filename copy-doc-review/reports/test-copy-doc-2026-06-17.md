# UX content audit report – copy doc

**Document:** Canonical CloudRun (test-copy-doc.md)
**Date:** 2026-06-17
**Note:** Test fixture – fake product page with deliberately planted issues.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 10 | 3 | 23 | 3 | 1 | 1 |
| Brand & style compliance | 2 | 3 | 9 | 2 | 0 | 0 |

**Total issues:** 43 (6 critical, 32 needs work, 5 minor) · **Needs review:** 1 · **N/A sections:** Forms & inputs – marketing product page with no form flow

---

## Issues by page section

### Metadata

#### 🔴 Critical
- **[Structure & hierarchy]** – The page description field is empty. Design, SEO, and social sharing cannot be finalized without it.
  - *Found:* `*Page description (160 characters max)` – blank | *Recommendation:* Add a page description under 160 characters.
- **[Navigation]** – Navigation placement is blank. The doc does not say where this page sits in the site structure.
  - *Found:* `Navigation` – blank | *Recommendation:* Add the full nav path and any meganav label or description needed.

#### 🟡 Needs Work
- **[Completeness]** – The `og:Image` field still contains template instructions instead of an actual image link.
  - *Found:* "Please include a link to the image you would like as the page thumbnail." | *Recommendation:* Replace the instruction text with the real image URL.

### Hero

#### 🔴 Critical
- **[CTAs]** – The secondary CTA has no destination.
  - *Found:* `[Learn more]()` | *Recommendation:* Add the destination URL before design begins.

#### 🟡 Needs Work
- **[CTAs]** – "Learn more" is vague and does not tell the user what they will get.
  - *Found:* "Learn more" | *Recommendation:* Use specific text such as "Explore CloudRun features" or "Read CloudRun docs".
- **[Character limits]** – The hero supporting paragraph exceeds the 300-character limit by a wide margin.
  - *Found:* Hero paragraph is about 397 characters | *Recommendation:* Cut and simplify the copy to fit the limit.
- **[Tone & clarity]** – The hero paragraph is a single long, dense sentence that is hard to scan.
  - *Found:* "The world's most reliable container management platform, delivering enterprise-grade Kubernetes operations..." | *Recommendation:* Break it into two or three shorter sentences.
- **[Accessibility]** – The hero image has no alt text or note saying it is decorative.
  - *Found:* `![][image1]` with asset link only | *Recommendation:* Add alt text, or note that the image is decorative if that is intentional.

### Data spotlight

#### 🟡 Needs Work
- **[Tone & clarity]** – The cost claim conflicts with a later claim in the "Why choose" section.
  - *Found:* `50%` here vs `Reduce costs by 40%` later | *Recommendation:* Verify the correct figure and use one approved number throughout.

### More information

#### 🟡 Needs Work
- **[Structure & hierarchy]** – "More information" is too vague as a section heading.
  - *Found:* "More information" | *Recommendation:* Replace it with a descriptive heading that explains the content.
- **[Links]** – The full sentence is linked, which makes the link hard to scan and harder to use with assistive technology.
  - *Found:* `[Read this document to learn everything about how Canonical CloudRun compares to existing container orchestration platforms and why leading organisations across the globe are choosing it for their mission-critical workloads.]` | *Recommendation:* Link only the key phrase.
- **[Accessibility]** – The image in this section has no alt text.
  - *Found:* `![][image2]` | *Recommendation:* Add descriptive alt text.
- **[Tone & clarity]** – The paragraph is heavy with unexplained technical shorthand.
  - *Found:* "CNCF-certified K8s distribution with OCI-compliant container runtimes, integrated CSI drivers, and a CNI plugin architecture..." | *Recommendation:* Expand acronyms on first use and simplify where possible.

### Why choose Canonical CloudRun

#### 🟡 Needs Work
- **[Structure & hierarchy]** – The doc uses `###` headings here and in later sections without any preceding H2 structure.
  - *Found:* `### Why choose Canonical CloudRun`, `### Resources and guides`, `### Customer stories` | *Recommendation:* Use H2 for top-level sections, or add the missing H2 level.
- **[Completeness]** – The body copy contains an unresolved `TBD` placeholder.
  - *Found:* "trusted by TBD enterprises worldwide" | *Recommendation:* Replace it with an approved number or remove the claim.
- **[Tone & clarity]** – The bullet list has inconsistent structure.
  - *Found:* Most bullets are noun phrases, but "Reduce costs by 40% compared to self-managed Kubernetes" is a full benefit statement | *Recommendation:* Rewrite the list so items follow the same pattern.

#### 🔵 Minor
- **[Structure & hierarchy]** – The bullet list would scan better with a short lead-in sentence.
  - *Found:* Paragraph ends and the bullets start immediately | *Recommendation:* Add a short intro such as "Key benefits include:".

### Resources and guides

#### 🟡 Needs Work
- **[Links]** – "Read more" is non-descriptive link text.
  - *Found:* `[Read more](https://canonical.com/cloudrun/docs)` | *Recommendation:* Use specific link text such as "Read the CloudRun documentation".
- **[Accessibility]** – The whitepaper is hosted on Google Drive instead of the asset manager.
  - *Found:* `[CloudRun architecture whitepaper (PDF)](https://drive.google.com/file/d/1abc123/view?usp=sharing)` | *Recommendation:* Upload the file to the Canonical asset manager and update the link.
- **[Comments & revisions]** – The section still contains an open author note.
  - *Found:* `[AUTHOR: needs updated stats for Q2 – check with product team]` | *Recommendation:* Resolve the comment and remove it from the doc.

### Customer stories

#### 🟡 Needs Work
- **[Completeness]** – The quote attribution still uses a `TK` placeholder.
  - *Found:* `— TK, VP Engineering` | *Recommendation:* Replace `TK` with the real name and approved title.

#### 🔵 Minor
- **[Accessibility]** – The customer logo image has no alt text. Logo alt text is a minor issue in this workflow.
  - *Found:* `![][image3]` | *Recommendation:* Add brief alt text, or note that the logo is decorative if appropriate.

### CTA band

#### 🟡 Needs Work
- **[Comments & revisions]** – The supporting paragraph is still a TODO, not publishable copy.
  - *Found:* `TODO: check with legal before publishing pricing claims` | *Recommendation:* Resolve the legal question and replace the TODO with final copy.
- **[CTAs]** – The primary CTA repeats the vague label "Learn more" already used in the hero.
  - *Found:* `[Learn more](/cloudrun/docs)` | *Recommendation:* Rename it to something specific, such as "Read the docs".
- **[CTAs]** – The secondary CTA uses the banned "click here" pattern.
  - *Found:* `[Click here to contact us](/cloudrun/contact)` | *Recommendation:* Use "Contact us" or "Talk to an expert".
- **[Character limits]** – The secondary CTA exceeds the 20-character button limit.
  - *Found:* "Click here to contact us" – 24 characters | *Recommendation:* Shorten the label.
- **[Accessibility]** – The instructional line relies on visual position.
  - *Found:* "click the button on the right" | *Recommendation:* Refer to the button by its label instead.
- **[CTAs]** – The instructional sentence promises an installation wizard, but neither CTA label reflects that action.
  - *Found:* "To deploy CloudRun, click the button on the right to access the installation wizard." with CTAs "Learn more" and "Click here to contact us" | *Recommendation:* Align the helper text and CTA labels with the actual destination.

#### 🔵 Minor
- **[Tone & clarity]** – The closing helper sentence is more procedural than persuasive for a marketing page.
  - *Found:* "To deploy CloudRun, click the button on the right to access the installation wizard." | *Recommendation:* Rewrite it around user value rather than mechanics.

---

## Brand & style compliance

### Hero

#### 🔴 Critical
- **[Security and absolute claims]** – The hero uses an unprovable absolute claim.
  - *Found:* "The world's most reliable container management platform" | *Recommendation:* Replace it with a specific, supportable claim.
- **[Superlatives]** – "unmatched performance" is another unsupported superlative.
  - *Found:* "unmatched performance" | *Recommendation:* State the actual performance benefit, metric, or proof.

#### 🟡 Needs Work
- **[US English]** – The copy uses UK spelling.
  - *Found:* "data centres" | *Recommendation:* Change to "data centers".
- **[Consistency spellings]** – The copy uses "on-premises" instead of the preferred style form.
  - *Found:* "on-premises data centres" | *Recommendation:* Change to "on premises data centers".
- **[Sentence length]** – The hero sentence is well above the recommended web-copy range.
  - *Found:* one sentence at about 50-plus words | *Recommendation:* Split it into shorter sentences.

### Data spotlight and body copy

#### 🔴 Critical
- **[Product and service names]** – The product name is inconsistent, which creates brand-integrity risk.
  - *Found:* "Canonical CloudRun", "Canonical Cloud Run", "Cloud Run", and "cloud-run" | *Recommendation:* Choose the approved product name and use it consistently everywhere.

#### 🟡 Needs Work
- **[Words and phrases to avoid]** – The section uses banned jargon.
  - *Found:* "cloud-run leverages" | *Recommendation:* Replace "leverages" with "uses".
- **[US English]** – The doc uses UK spelling more than once.
  - *Found:* "organisations" in the comparison link text and "Organisations choose Canonical Cloud Run..." | *Recommendation:* Change both to "organizations".
- **[Acronyms and abbreviations]** – Several acronyms are not expanded on first use.
  - *Found:* "CNCF", "K8s", "OCI", "CSI", "CNI", and "SLA" | *Recommendation:* Spell each out on first mention.
- **[Superlatives]** – The copy uses unsupported promotional language.
  - *Found:* "leading organisations across the globe" and "leading enterprises" | *Recommendation:* Replace with factual wording unless there is approved proof.
- **[Tone]** – Parts of the copy read as dense, corporate, and over-engineered instead of plain and confident.
  - *Found:* "delivering enterprise-grade Kubernetes operations with seamless multi-cloud support..." and the jargon-heavy architecture paragraph | *Recommendation:* Simplify the language while keeping the technical meaning.
- **[List formatting]** – The bullets are not parallel in structure.
  - *Found:* feature nouns mixed with a benefit claim and a service promise | *Recommendation:* Rewrite the list so every bullet follows the same grammatical pattern.

#### 🔵 Minor
- **[Punctuation]** – The customer quote uses an em dash.
  - *Found:* `"CloudRun helped us..." — TK, VP Engineering` | *Recommendation:* Use the preferred style for sentence breaks and attributions in the final copy system.
- **[Numbers]** – Single-digit numbers should be spelled out in running copy.
  - *Found:* "day-2 operations" | *Recommendation:* Keep as-is only if the product team treats "day-2" as standard industry terminology; otherwise consider "day-two operations".

---

## ❓ Needs review

- **[Hero: CTA destination]** – The primary hero CTA points to `ubuntu.com`, while the page URL in metadata is `canonical.com`. This may be intentional, but the doc does not explain it.
  - *Found:* `[Get in touch](https://ubuntu.com/cloudrun#get-in-touch)` | *Question:* Is the cross-domain destination correct, or should this CTA stay on `canonical.com`?

---

## ⬜ Not applicable

- **Forms & inputs** – N/A: this is a marketing product page with no form fields or input flow in scope.

---

## ✅ What looks good

- The page title is concise and within the 60-character limit.
- The hero title, subtitle, and CTA labels are all within their character limits.
- The data spotlight values and labels fit the pattern limits cleanly.
- The doc clearly states the page type, audience, funnel stage, owner, and primary user action.
- The hero and customer-story images include asset-manager links, which is the right storage pattern for image assets.
- The page has a sensible high-level flow: hero, proof points, supporting detail, resources, customer proof, and closing CTA.
- The whitepaper link correctly signals file type with `(PDF)` in the link text.
- The closing section includes two distinct actions rather than duplicating the same destination.
- The product audience is specific enough to guide design and messaging decisions.
- Several headings are already in sentence case, which matches the style guide.
