# UX content audit report – copy doc

**Document:** data_postgresql.md (Data product page – PostgreSQL)
**Date:** July 3, 2026
**Page type:** Product or service
**Target audience:** Executives
**Note:** Navigation field in the metadata table is incomplete – still contains template placeholder text.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 14 | 4 | 8 | 5 | 3 | 2 |

**Total issues:** 17 (four critical, eight needs work, five minor) · **Needs review:** three · **N/A sections:** Forms and inputs – marketing page; Completeness (interactive states) – marketing page

---

## Issues by page section

### Metadata

#### 🔴 Critical
- **[Character limits]** – Page description exceeds the 160-character limit (182 characters).
  - *Found:* "Get enterprise-grade PostgreSQL support from Canonical. Enjoy security maintenance, automated deployment, and upgrades for your PostgreSQL databases across private and public clouds." (182 chars)
  - *Recommendation:* Trim to 160 characters or fewer. For example: "Get enterprise-grade PostgreSQL support from Canonical. Enjoy security maintenance, automated deployment, and upgrades across clouds." (131 chars)

- **[Navigation]** – Navigation placement is not specified. The field still contains the template placeholder text ("Indicate how a user navigates to the page…").
  - *Found:* Template placeholder text instead of an actual navigation path.
  - *Recommendation:* Fill in the bubble navigation path (e.g. "All Canonical > Data > PostgreSQL") or specify the primary navigation for the page before this doc goes to design.

#### 🟡 Needs work
- **[Structure and hierarchy]** – The "Asset manager tag" row in the metadata table is empty. While it is marked "For developers, to be filled in by Sites visual designers," it should be flagged as incomplete.
  - *Found:* Empty cell.
  - *Recommendation:* Confirm whether this should be populated before handoff to design, or note it as a known gap.

---

### Hero

#### 🔴 Critical
- **[Accessibility]** – The hero image has no alt text defined in the copy doc. The image is embedded as `![][image1]` with no alt text annotation.
  - *Found:* `![][image1]` – no alt text provided.
  - *Recommendation:* Add a descriptive alt text for the hero image (e.g. "Diagram showing Canonical's PostgreSQL support services").

#### 🟡 Needs work
- **[CTAs]** – "Contact us" is a generic CTA that does not clearly describe what happens when the user clicks it. While common in the industry, it would benefit from more specificity given the executive audience.
  - *Found:* "Contact us"
  - *Recommendation:* Consider "Get PostgreSQL support" or "Talk to our team" for stronger intent signaling.

- **[Tone and clarity]** – The phrase "automation and artifacts" may be unclear to the target audience (executives). "Artifacts" is technical jargon that could confuse non-technical readers.
  - *Found:* "Canonical's PostgreSQL automation and artifacts provide you with…"
  - *Recommendation:* Consider replacing "artifacts" with a plainer term such as "tools" or "packages."

#### 🔵 Minor
- **[Links]** – The "Supported with Ubuntu Pro logo's link" text uses a possessive apostrophe incorrectly. "Logo's" should be "logos" (plural, no apostrophe).
  - *Found:* "Ubuntu Pro logo's link"
  - *Recommendation:* Change to "Ubuntu Pro logos link" or restructure the annotation.

---

### Logo cloud

#### 🟡 Needs work
- **[Accessibility]** – No alt text is specified for the cloud provider logos (OpenStack, MicroCloud, VMware, AWS, GCP, Azure). The doc only says "Use the standard logos for…" without defining alt text for each.
  - *Found:* "[Use the standard logos for: OpenStack Microcloud VMware AWS GCP Azure]"
  - *Recommendation:* Add alt text for each logo (e.g. "OpenStack logo," "AWS logo"). Note: logo alt text is 🔵 Minor per severity overrides, but the complete absence of any alt text guidance warrants 🟡.

#### 🔵 Minor
- **[Tone and clarity]** – "data centre" uses UK English spelling; the Canonical style guide requires US English.
  - *Found:* "in your private data centre"
  - *Recommendation:* Change to "data center."

- **[Tone and clarity]** – "Microcloud" in the logo list annotation is not capitalized correctly. The official product name is "MicroCloud" (capital M, capital C).
  - *Found:* "Microcloud"
  - *Recommendation:* Change to "MicroCloud."

---

### Data spotlight

#### 🔴 Critical
- **[Character limits]** – Data spotlight values exceed the 10-character limit. "100+ clusters" (13 chars), "10+ automations" (15 chars), and "~ 30 minutes" (12 chars) all exceed the maximum. The value itself (e.g. "100+") should be separate from the label (e.g. "clusters").
  - *Found:* Values and labels are merged in the doc (e.g. "**100+ clusters**").
  - *Recommendation:* Separate the data value from the label clearly. Values: "100+", "10+", "~ 30". Labels: "clusters", "automations", "minutes." The descriptions below should also be separated. Currently, the label and description run together (e.g. "Relying on our services Our stack is tried and tested…"). Add a line break or explicit separation.

#### 🟡 Needs work
- **[Character limits]** – Data spotlight descriptions exceed the 100-character limit. "Relying on our services Our stack is tried and tested in production in numerous sectors ranging from banking to aerospace engineering." is 134 characters; "To scale your operations Includes deployment, scaling, backups, restores, auto-tuning, encryption, monitoring, and upgrades." is 124 characters; "To get started Get up and running quickly in your local lab environment or your live production infrastructure setup." is 117 characters.
  - *Found:* All three descriptions exceed 100 characters.
  - *Recommendation:* Trim each to 100 characters or fewer once the label is separated from the description.

- **[Tone and clarity]** – "numerous" is flagged as a flowery word by the style guide. Use "many" instead.
  - *Found:* "numerous sectors"
  - *Recommendation:* Change to "many sectors."

---

### Tiered list

#### 🟡 Needs work
- **[Tone and clarity]** – "bleeding edge" is informal and potentially confusing for an executive audience. It also carries a slightly negative connotation (implying instability).
  - *Found:* "including for the bleeding edge versions of PostgreSQL"
  - *Recommendation:* Consider "latest" or "newest" versions of PostgreSQL.

---

### Equal height row (use cases)

#### 🟡 Needs work
- **[Accessibility]** – Alt text is missing for all four use case images. The doc references `![][image2]`, `![][image3]`, `![][image4]`, and `![][image5]` without any alt text annotations.
  - *Found:* Four images with no alt text defined.
  - *Recommendation:* Add descriptive alt text for each image (e.g. "Illustration of data warehousing architecture," "Illustration of regulated industry compliance").

- **[Accessibility]** – Three of four image sources link to Google Drive. Per the checklist, resource files should be hosted on asset manager, not Google Drive or other external locations.
  - *Found:* Image source links to `drive.google.com`.
  - *Recommendation:* Move images to the Canonical asset manager.

#### 🔵 Minor
- **[Tone and clarity]** – "a large panel of index types" – "panel" is an unusual word choice here. Consider "range" or "variety."
  - *Found:* "It also supports a large panel of index types"
  - *Recommendation:* Change to "a wide range of index types" or "a variety of index types."

---

### Options/Pricing

#### 🟡 Needs work
- **[Character limits]** – The supporting paragraph is 466 characters, which exceeds the 300-character limit for a basic section supporting paragraph.
  - *Found:* 466-character paragraph.
  - *Recommendation:* Split into two shorter paragraphs or trim the content to fit within the 300-character limit.

---

### Resources

#### 🔵 Minor
- **[Links]** – The "Contribute" section links to the Kafka operator repository (`github.com/canonical/kafka-operator`) rather than the PostgreSQL operator. This appears to be a copy-paste error.
  - *Found:* "[Software operator for PostgreSQL](https://github.com/canonical/kafka-operator)"
  - *Recommendation:* Update the link to the PostgreSQL operator repository (e.g. `https://github.com/canonical/postgresql-operator`).

---

## ❓ Needs review

- **[Metadata]** – The page URL uses `http://` in the metadata table link. Confirm whether this should be `https://`.
  - *Found:* `[canonical.com/data/postgresql](http://canonical.com/data/postgresql)`
  - *Question:* Should this be `https://canonical.com/data/postgresql`?

- **[Hero]** – The "Supported with Ubuntu Pro" badge/logo annotation references a Vanilla Framework GitHub issue (#5699). Confirm whether this component is available or still in development.
  - *Found:* "Supported with Ubuntu Pro logo's link" → links to `github.com/canonical/vanilla-framework/issues/5699`
  - *Question:* Is this component ready for use, or is it a dependency that needs to be resolved before design?

- **[Tiered list]** – The "Software operator" subsection does not explicitly reference Charmed PostgreSQL by name, while the hero video title mentions "Charmed PostgreSQL." Confirm whether the product name should be used consistently.
  - *Found:* "Our software operator helps you automate the operations…"
  - *Question:* Should this reference "Charmed PostgreSQL" for consistency with the hero section?

---

## ⬜ Not applicable

- **Forms and inputs** – N/A: this is a marketing/product page with no interactive form (the "Contact us" CTA links to an anchor, not a form within this doc).
- **Completeness (interactive states)** – N/A: this is a static marketing page with no interactive flows requiring hover/focus/error/success/empty/loading states.

---

## ✅ What looks good

- **Structure and hierarchy** – The doc follows a clear, logical flow from hero through value proposition, deployment options, use cases, pricing, and resources. Heading levels are well structured.
- **Metadata** – Page title (35 chars) and most metadata fields are complete and within limits.
- **Hero** – Hero title is concise (33 chars) and clear. The supporting paragraph (268 chars) is within the 300-character limit and communicates the core value proposition effectively.
- **CTAs** – Most CTAs are specific and action-oriented: "Try the deb," "Try the snap," "Try the container," "Check our software operator," "Check our automation," "Try it yourself" are all descriptive and make sense out of context.
- **Links** – Link destinations are specified throughout the doc. Link text is generally descriptive and meaningful.
- **Tiered list** – Deployment options are clearly organized with distinct subsections, each with a brief description and a CTA. Good parallel structure.
- **Data spotlight** – The three data points ("100+ clusters," "10+ automations," "~ 30 minutes") provide strong social proof and concrete numbers.
- **Options/Pricing** – The two-column layout (subscription-based vs. on-demand) clearly differentiates the service tiers.
- **Trademark notice** – Proper trademark attribution for PostgreSQL is included at the bottom of the doc.
- **Active voice** – The doc predominantly uses active voice throughout, which reads well for the target audience.
- **Tone** – Overall tone is confident and authoritative without being arrogant – aligned with the Canonical brand voice.
- **Consistency** – Terminology is consistent throughout: "PostgreSQL" is always fully spelled out, "Ubuntu Pro" is used correctly, and section headings use sentence case.
- **Serial comma** – Consistently used in lists (e.g. "deployment, scaling, encryption, and upgrades").
