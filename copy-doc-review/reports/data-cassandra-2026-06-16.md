# UX content audit report – copy doc

**Document:** Data product page – Apache Cassandra (canonical.com/data/cassandra)
**Date:** 16 June 2026
**Note:** This is a marketing/product page (page type: "Product or service"). Sections for forms, error states, and interactive UI states are not applicable.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 17 | 2 | 7 | 7 | 2 | 3 |

**Total issues:** 16 (two critical, seven needs work, seven minor) · **Needs review:** 2 · **N/A sections:** Forms & Inputs, Error & Feedback States, interactive states in Completeness – marketing page with no interactive flows

---

## Issues by page section

### Metadata

#### 🟡 Needs work
- **[Character limits]** – Page description is 166 characters, exceeding the 160-character limit.
  - *Found:* "Get enterprise-grade Apache Cassandra support from Canonical. Enjoy security, automation, and SLA-backed expertise for your clusters across private and public clouds." (166 chars) | *Recommendation:* Trim by six characters – e.g. "Get enterprise-grade Apache Cassandra support from Canonical. Security, automation, and SLA-backed expertise for your clusters across private and public clouds." (161 chars – remove "Enjoy")

#### 🔵 Minor
- **[Navigation]** – The navigation field contains template instructions mixed with the actual placement. The actual placement ("All Canonical > Data > Cassandra") is present but buried in boilerplate.
  - *Found:* Long template text ending with "Bubble navigation *All Canonical > Data > Cassandra.*" | *Recommendation:* Clean up the field to state only the placement for handoff to design/dev.

---

### Hero

#### 🔴 Critical
- **[CTAs]** – The primary CTA "Contact us" has no destination specified. The metadata says the main action is "Contact us" but no URL or page reference is given.
  - *Found:* `[Contact us]` with no link | *Recommendation:* Add the destination URL (e.g. canonical.com/contact-us or a specific form).

#### 🔵 Minor
- **[Accessibility]** – The Cassandra logo reference has no alt text defined.
  - *Found:* `[Logo link]` and `![][image1]` | *Recommendation:* Add descriptive alt text, e.g. "Apache Cassandra logo".

---

### Logo cloud

#### 🟡 Needs work
- **[Brand & style – A1]** – UK English spelling "data centre" used instead of US English "data center".
  - *Found:* "your private data centre on top of MAAS and MicroCloud" | *Recommendation:* Change to "data center".

- **[Brand & style – A3]** – "VMWare" is incorrectly capitalised. The correct name is "VMware" (lowercase "w").
  - *Found:* "OpenStack, or VMWare" | *Recommendation:* Change to "VMware".

#### 🔵 Minor
- **[Accessibility]** – No alt text specified for the cloud provider logos (OpenStack, MicroCloud, VMware, AWS, GCP, Azure).
  - *Found:* `[Use the standard logos for: OpenStack Microcloud VMware AWS GCP Azure]` | *Recommendation:* Confirm that standard logo alt text is handled by the component; if not, add alt text per logo.

---

### Data spotlight

#### 🟡 Needs work
- **[Character limits]** – Data spotlight value "~ 30 minutes" is 12 characters, exceeding the 10-character limit.
  - *Found:* "~ 30 minutes" | *Recommendation:* Shorten to "~30 min" or "30 min" to fit within the limit.

- **[Tone & clarity]** – The description "Served by our stack" is followed by a second sentence that largely repeats the same point. The connection between "1 million+ users" and the Snap Store is unclear without context.
  - *Found:* "Served by our stack Our stack is tried and tested in production. It actively supports our own global Snap Store platform." | *Recommendation:* Tighten to a single clear statement, e.g. "Our stack powers the global Snap Store, serving over one million users."

#### 🔴 Critical
- **[CTAs]** – "Contact us" CTA in the first data point has no destination specified (same issue as the hero).
  - *Found:* `[Contact us]` | *Recommendation:* Add the destination URL.

---

### Tiered list

#### 🔵 Minor
- **[Brand & style – A3]** – "Microcloud" in the logo cloud section should be "MicroCloud" (capital C). However, in this section the product name does not appear, so no issue here. *(Noted above under Logo cloud.)*

*(No issues specific to this section.)*

---

### Equal height row (use cases)

#### 🟡 Needs work
- **[Accessibility]** – Images are hosted on Google Drive. Resource files should be hosted on the asset manager, not external locations.
  - *Found:* `[Image 1](https://drive.google.com/file/...)`, `[Image 2](https://drive.google.com/file/...)`, etc. | *Recommendation:* Upload images to the Canonical asset manager and update the links.

- **[Accessibility]** – No alt text defined for any of the four use case images.
  - *Found:* `[Image 1]`, `[Image 2]`, `[Image 3]`, `[Image 4]` | *Recommendation:* Add descriptive alt text for each image (e.g. "Illustration of real-time analytics pipeline").

- **[Tone & clarity]** – Grammar error: "such the ones" should be "such as the ones" or "such as those".
  - *Found:* "makes it an excellent choice for applications distributed across several regions, such the ones managing global user or session data." | *Recommendation:* Change to "such as those managing global user or session data."

#### 🔵 Minor
- **[Brand & style – A13]** – "Therefore" is slightly formal for web copy but acceptable. No action required.

---

### Options/pricing

#### 🟡 Needs work
- **[CTAs]** – "More details" is a vague CTA that does not describe what happens when clicked.
  - *Found:* `[More details]` | *Recommendation:* Make it specific, e.g. "See pricing options" or "View service plans".

- **[CTAs]** – "Get in touch" has no destination specified and is not wrapped in a link or button marker.
  - *Found:* `Get in touch` (plain text, no brackets or link) | *Recommendation:* Clarify whether this is a CTA. If so, add a destination URL and mark it as a button or link.

#### 🔵 Minor
- **[Brand & style – A12]** – "subscription-based" is correctly hyphenated as a compound adjective. ✅ (No issue.)
- **[Brand & style – A13]** – "time-consuming and error-prone tasks" – "error-prone" is fine; no issues here.

---

### Resources

#### 🔵 Minor
- **[Links]** – "Read more" is used as a section label above a list of links. While it is not link text itself, it is a vague heading.
  - *Found:* "Read more" as a subheading | *Recommendation:* Consider a more descriptive heading, e.g. "Further reading" or "Related resources".

---

## ❓ Needs review

- **[Metadata]** – The target audience is listed as "Executives" and the funnel stage as "Trial/evaluation". These seem potentially misaligned – executives may be at the decision-making stage rather than trial/evaluation. A reviewer should confirm the intended audience and funnel stage.
  - *Found:* Target audience: "Executives", Stage: "2. Trial/evaluation" | *Question:* Is this the correct funnel stage for an executive audience?

- **[Options/pricing]** – The pricing section mentions "[Ubuntu Pro](https://ubuntu.com/pro)" as part of the subscription services. It is unclear whether this page should detail the relationship between Cassandra support and Ubuntu Pro, or whether a separate page handles that.
  - *Found:* "our subscription-based services – including Ubuntu Pro –" | *Question:* Does the reader need more context about what Ubuntu Pro provides in this context?

---

## ⬜ Not applicable

- **Forms & Inputs** – N/A: this is a marketing/product page with no form or input flow.
- **Error & Feedback States** – N/A: no interactive states on a marketing page.
- **Completeness (interactive states)** – N/A: hover, focus, error, success, empty, and loading states do not apply to a static marketing page.

---

## ✅ What looks good

- **Page title** is exactly 60 characters – right at the limit with a clear, keyword-rich title.
- **Hero copy** is well structured with a clear value proposition, specific benefits (hardened artifacts, 15 years of security maintenance, SLA-backed support), and a differentiated tone ("a team that breathes open source").
- **Hero CTA hierarchy** is clear – primary "Contact us" button and secondary "Try Apache Cassandra" link with a working destination.
- **Data spotlight** uses concrete numbers (1 million+ users, 9+ automations, ~30 minutes) that build credibility and are scannable.
- **Tiered list** clearly differentiates between the Snap and the software operator, giving each a distinct value proposition and CTA.
- **Use cases section** covers four distinct and well-explained scenarios (real-time analytics, geo-distributed, mission-critical, latency-sensitive), supporting the "Exploration" stage of the adoption checklist.
- **Terminology is consistent** – "Apache Cassandra" is used throughout (full name, respecting the trademark).
- **Tone** is confident and expert without being arrogant – fits the Canonical brand voice well.
- **Navigation placement** is specified (All Canonical > Data > Cassandra).
- **Links** are generally descriptive with clear destinations (docs, Charmhub, snapcraft, Matrix chat).
- **Trademark notice** is included at the bottom of the page.
- **Sentence structure** is scannable with good use of short paragraphs and lists.
- **Serial comma** is used correctly throughout.
- **"open source"** is correctly lowercase and two words in all instances.

---

## Brand & style compliance

### 🟡 Needs work
- **[A1 – US English]** – "data centre" should be "data center".
  - *Found:* Logo cloud section: "your private data centre" | *Corrected:* "your private data center"

- **[A3 – Product names]** – "VMWare" should be "VMware".
  - *Found:* Logo cloud section: "OpenStack, or VMWare" | *Corrected:* "OpenStack, or VMware"

- **[A3 – Product names]** – "Microcloud" in the logo cloud instruction should be "MicroCloud".
  - *Found:* `[Use the standard logos for: OpenStack Microcloud VMware AWS GCP Azure]` | *Corrected:* "MicroCloud"

### 🔵 Minor
- **[A8 – Punctuation]** – The pricing section uses an en dash with spaces correctly (" – "). ✅ No issue.
- **[A7 – Numbers]** – Numbers are used appropriately (digits for "15 years", "30 minutes", "9+", "1 million+"). ✅

---

## 🔲 Manual checks for reviewer

- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify that the claim "1 million+ users served by our stack" and "9+ automations" are accurate and approved
- [ ] **Figma reference:** the metadata links to a Figma design – verify it matches the sections in this copy doc
- [ ] **Image assets:** four use case images are on Google Drive – confirm they will be moved to the asset manager before development
