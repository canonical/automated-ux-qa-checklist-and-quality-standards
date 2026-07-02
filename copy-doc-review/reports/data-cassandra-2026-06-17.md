# UX content audit report – copy doc

**Document:** _data_cassandra.md (canonical.com/data/cassandra)
**Date:** 17 June 2026
**Note:** Review based on the pasted markdown only. External links, assets, and source claims were not independently verified.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 15 | 4 | 8 | 2 | 3 | 3 |

**Total issues:** 14 (four critical, eight needs work, two minor) · **Needs review:** three · **N/A sections:** Forms & Inputs, Error & Feedback States, interactive states in Completeness

---

## Issues by page section

### Metadata

#### 🟡 Needs work
- **[Character limits]** – The page description is 166 characters, which exceeds the 160-character limit.
  - *Found:* "Get enterprise-grade Apache Cassandra support from Canonical. Enjoy security, automation, and SLA-backed expertise for your clusters across private and public clouds." | *Recommendation:* Trim the description to 160 characters or fewer.
- **[Navigation]** – The navigation field mixes final navigation guidance with template instructions, which makes the handoff harder to follow.
  - *Found:* "Indicate how a user navigates to the page... Please select the primary navigation for the page. Bubble navigation *All Canonical > Data > Cassandra.*" | *Recommendation:* Leave only the final path and any required implementation notes.

### Hero

#### 🔴 Critical
- **[CTAs]** – The primary CTA has no destination, so design and development cannot implement it confidently.
  - *Found:* `[Contact us]` | *Recommendation:* Add the exact URL or page reference for this CTA.

#### 🔵 Minor
- **[Accessibility]** – The logo image does not include alt text.
  - *Found:* `![][image1]` with a separate logo link note | *Recommendation:* Add concise alt text, such as "Apache Cassandra logo".

### Logo cloud

#### 🟡 Needs work
- **[Completeness]** – The section still contains a production instruction instead of finished copy or a clear implementation note.
  - *Found:* `[Use the standard logos for: OpenStack Microcloud VMware AWS GCP Azure]` | *Recommendation:* Replace this with finalized content or move the implementation note outside the visible-copy section.

#### 🔵 Minor
- **[Accessibility]** – The cloud-provider logos do not have alt text guidance.
  - *Found:* Logo list only, with no alt-text notes | *Recommendation:* Confirm whether the component supplies standard logo alt text. If not, add it in the doc.

### Data spotlight

#### 🔴 Critical
- **[CTAs]** – The CTA destination is missing here as well.
  - *Found:* `[Contact us]` | *Recommendation:* Add the exact destination so this card can be implemented.

#### 🟡 Needs work
- **[Character limits]** – Several spotlight items exceed the component limits.
  - *Found:* `1 million+ users` (value over 10), `Served by our stack` description at 101 characters, `To scale your operations` label at 24 characters, `~ 30 minutes` (value over 10), and the final description at 110 characters | *Recommendation:* Shorten the over-limit values, labels, and descriptions to fit the data spotlight component.

### Equal height row

#### 🟡 Needs work
- **[Accessibility]** – The image files are hosted on Google Drive instead of the asset manager.
  - *Found:* Four image links pointing to `drive.google.com` | *Recommendation:* Move these files to the Canonical asset manager before handoff.
- **[Accessibility]** – The four use-case images have no alt text or guidance on whether they are decorative.
  - *Found:* `[Image 1]`, `[Image 2]`, `[Image 3]`, `[Image 4]` | *Recommendation:* Add alt text for each image, or explicitly mark them decorative if that is the intent.

### Options/pricing

#### 🔴 Critical
- **[CTAs]** – One CTA is present with no destination.
  - *Found:* `[More details]` | *Recommendation:* Add the exact URL or page reference.

#### 🟡 Needs work
- **[CTAs]** – "More details" is too vague to stand alone or make sense out of context.
  - *Found:* `[More details]` | *Recommendation:* Use specific action text, such as "View service options" or "Compare support services".
- **[CTAs]** – "Get in touch" appears as plain text, so it is unclear whether it is body copy or an intended CTA.
  - *Found:* `... [More details] Get in touch` | *Recommendation:* Decide whether this is a CTA. If it is, format it as one and add the destination.

### Resources

#### 🔴 Critical
- **[CTAs]** – The CTA destination is missing.
  - *Found:* `[Tell us more about your needs]` | *Recommendation:* Add the exact destination URL or page reference.

---

## Brand & style compliance

### 🟡 Needs work
- **[A1 – US English]** – Use US spelling.
  - *Found:* "data centre" | *Corrected:* "data center"
- **[A3 – Product names]** – Product capitalization is inconsistent.
  - *Found:* "Microcloud" and "VMWare" | *Corrected:* "MicroCloud" and "VMware"
- **[A10 – Acronyms]** – Spell out acronyms on first mention for this audience.
  - *Found:* "SLA-backed support", "IoT sensor streams" | *Recommendation:* Expand on first use, for example "service-level agreement (SLA)-backed support" and "internet of things (IoT) sensor streams".
- **[A12 – Hyphens]** – Compound adjectives are missing needed hyphens.
  - *Found:* "Mission critical applications" and "multi-data center replication" | *Corrected:* "Mission-critical applications" and "multi-data-center replication"
- **[B7 – Superlatives]** – One claim reads as an unproved superlative.
  - *Found:* "the smallest footprint and attack surface" | *Recommendation:* Replace with a measurable comparison or a more specific benefit.
- **[B3/B10 – Clarity]** – Some copy is dense and jargon-heavy for an executive audience.
  - *Found:* "Whether you are exploring Apache Cassandra or need deep expertise to scale your deployments and meet your SLAs..." | *Recommendation:* Shorten the sentence and reduce terms such as "artifacts," "auto-tuning," and "firefighting support" unless they are explained.

---

## ❓ Needs review

- **[Metadata]** – The audience and funnel stage may not align with the page depth.
  - *Found:* Target audience `Executives`; stage `2. Trial/evaluation` | *Question:* Is this page really aimed at executives evaluating a trial, or should the audience/stage be adjusted?
- **[Navigation]** – Redirect requirements are not stated.
  - *Found:* New path `canonical.com/data/cassandra` with no note about an old location | *Question:* Is this a net-new page, or does an existing Cassandra page need redirects?
- **[Claims]** – Several proof points need source confirmation before publication.
  - *Found:* `15 years of security maintenance`, `1 million+ users`, `9+ automations`, `~ 30 minutes` | *Question:* Are these claims approved and traceable to current source material?

---

## ⬜ Not applicable

- **Forms & Inputs** – N/A: this is a product/service page with no form flow documented.
- **Error & Feedback States** – N/A: this doc does not describe an interactive product flow.
- **Completeness – interactive states** – N/A: hover, focus, error, success, empty, and loading states are outside scope for this page type.

---

## ✅ What looks good

- The metadata includes the core required fields: page title, description, URL, navigation path, keyword, audience, page type, and owner.
- The page title is exactly at the 60-character limit and clearly targets the main offering.
- The hero presents the core value proposition early, with a clear primary and secondary action pattern.
- The page supports multiple stages of the journey with exploration content, proof points, deployment options, use cases, services, and resources.
- Most link text is descriptive and specific, including "Give it a try," "Check our automation," and the named resource links.
- The use-case section is scannable and covers four distinct scenarios, which helps readers self-identify quickly.
- The resources section offers a good mix of community, product, and educational links.
- The trademark line is present, which is useful for Apache Cassandra naming compliance.

---

## 🔲 Manual checks for reviewer

- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify any copy that pulls from external sources is accurate and approved
- [ ] **CTA destinations:** confirm the final URLs for `Contact us`, `More details`, and `Tell us more about your needs`
- [ ] **Assets:** confirm all images and logos will be supplied through the approved asset workflow
