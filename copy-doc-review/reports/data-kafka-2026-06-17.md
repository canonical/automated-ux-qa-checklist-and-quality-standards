# UX content audit report – copy doc

**Document:** _data_kafka.md (canonical.com/data/kafka)
**Date:** 2026-06-17
**Note:** Page type is "Product or service" – a marketing page with no interactive flows. Forms, error states, and interactive-only completeness checks are N/A.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | – | 2 | 7 | 3 | 1 | 2 |

**Total issues:** 12 (2 critical, 7 needs work, 3 minor) · **Needs review:** 1 · **N/A sections:** Forms & Inputs, Error & Feedback States – marketing page

---

## UX quality check

### CTAs

#### 🔴 Critical

- **Tiered List: Software operator CTA links to the wrong product** – "Check our software operator" links to `charmhub.io/cassandra`, not the Kafka charm. Users clicking this CTA will be sent to the Cassandra operator page.
  - *Found:* `[Check our software operator](https://charmhub.io/cassandra?channel=5/edge)` | *Recommendation:* Update the URL to the correct Kafka charm, e.g. `https://charmhub.io/kafka`.

- **Resources: "Contact us" CTA has no destination** – The "Contact us" link in the Resources section is listed with a label note ("Tell us more about your needs") but no URL. Designers cannot implement this link.
  - *Found:* `Contact us [Tell us more about your needs]` – no URL | *Recommendation:* Add the destination URL, e.g. `canonical.com/data/kafka#get-in-touch`.

---

### Structure & hierarchy

#### 🟡 Needs Work

- **Metadata: Navigation field not filled in** – The navigation field contains the template's instructional placeholder text. The actual navigation path is not provided.
  - *Found:* Template instructions present, no path specified | *Recommendation:* Replace with the actual navigation path, e.g. "All Canonical > Data > Kafka".

---

### Accessibility

#### 🟡 Needs Work

- **Hero: No alt text for either logo image** – The Ubuntu Pro logo (`image1`) and Apache Kafka logo (`image2`) in the hero have no alt text defined. Screen readers will have nothing to describe them.
  - *Found:* `![][image1]` and `![][image2]` with no alt text | *Recommendation:* Add descriptive alt text for each, e.g. `alt="Ubuntu Pro"` and `alt="Apache Kafka"`. If they are purely decorative, note `alt=""`.

- **Equal Height Row: No alt text for use case images** – All four use case images are linked from Google Drive with no alt text specified.
  - *Found:* Four image links (`Image 1` through `Image 4`) with no alt text | *Recommendation:* Add descriptive alt text for each image, or confirm they are decorative.

- **Equal Height Row: Use case images hosted on Google Drive** – All four use case images link to Google Drive, not the Canonical asset manager.
  - *Found:* `[Image 1](https://drive.google.com/...)` through `[Image 4](...)` | *Recommendation:* Upload final assets to the asset manager and update the links.

---

### Character limits

#### 🟡 Needs Work

- **Metadata: Page description over limit** – The page description is 186 characters against a 160-character limit, over by 26.
  - *Found:* "Get enterprise-grade Apache Kafka support from Canonical. Enjoy security, automated deployment, maintenance, and upgrades for your Apache Kafka clusters across private and public clouds." (186 chars) | *Recommendation:* Shorten to 160 characters, e.g. by cutting "Enjoy" and tightening: "Get enterprise-grade Apache Kafka support from Canonical – security, automated deployment, maintenance, and upgrades for your clusters across private and public clouds."

- **Data Spotlight: Multiple character limit overruns** – Four of the nine spotlight fields exceed their limits.
  - *Found:*
    - Value "~ 30 minutes" – 12 chars (limit 10)
    - Label "Relying on our services" – 23 chars (limit 20)
    - Label "To scale your operations" – 24 chars (limit 20)
    - Spotlight 1 description "Our stack is tried and tested in production in numerous sectors ranging from banking to aerospace engineering." – 109 chars (limit 100)
    - Spotlight 3 description "Get up and running quickly whether in your local lab environment or your live production infrastructure setup." – 109 chars (limit 100)
  - *Recommendation:* Trim each field to its limit. For the value, consider "30 min" (6 chars). For the labels, try "Our production users" (20) and "Scale your operations" (21 – still one over; "Scale operations" at 16 works). For the descriptions, cut to 100 characters.

---

### Tone & clarity

#### 🟡 Needs Work

- **Logo Cloud: "VMWare" should be "VMware"** – The body text uses "VMWare" with a capital W, which is incorrect trademark casing.
  - *Found:* "…on top of MAAS and MicroCloud, OpenStack or VMWare." | *Recommendation:* Change to "VMware".

#### 🔵 Minor

- **Logo Cloud: Inconsistent casing for "MicroCloud"** – The logo cloud body text uses "MicroCloud" (correct) but the logo list uses "Microcloud" (lowercase c).
  - *Found:* Logo list: "OpenStack Microcloud VMware AWS GCP Azure" | *Recommendation:* Change to "MicroCloud" to match the correct product name.

- **Hero drafting note: Unnecessary possessive apostrophe** – "Ubuntu Pro logo's link" in the hero note should be "Ubuntu Pro logo link". This is a drafting note, not visible copy, but tidy docs help prevent confusion in handoff.
  - *Found:* "Supported with Ubuntu Pro logo's link" | *Recommendation:* Change to "Ubuntu Pro logo link".

---

## ❓ Needs review

- **Funnel stage vs page content** – The metadata sets the funnel stage as "Trial/evaluation", but the page content is heavily focused on services, subscriptions, and consulting – which is characteristic of a Decision-making stage. The hero CTA is "Contact us", which typically indicates a decision-stage action.
  - *Question:* Should the funnel stage be "3. Decision-making" rather than "2. Trial/evaluation"? Or is the intent to reach users who are still evaluating?

---

## ⬜ Not applicable

- **Forms & Inputs** – N/A: marketing / product page with no form or input flow.
- **Error & Feedback States** – N/A: marketing / product page with no interactive states.

---

## ✅ What looks good

- **Page URL is filled in** – `canonical.com/data/kafka` is clearly specified. ✅
- **Most CTAs have destinations noted** – Hero, Data Spotlight, Tiered List (container), and Resources CTAs all include URLs (aside from the two critical gaps above).
- **CTA language is specific and action-oriented** – "Try the container", "Check our automation", "Try it yourself" all describe what the user is doing. No "learn more" or "click here".
- **Consistent product naming** – "Apache Kafka" is used consistently throughout. No shorthand or conflicting terms.
- **Use cases are detailed and audience-appropriate** – The four use cases go beyond vague claims and describe concrete technical scenarios, well suited to the executive and technical audience.
- **Metadata is largely complete** – Page title, description, URL, owner, approvals, audience, page type, and funnel stage are all filled in.

---

## Recommended priority order

1. Fix all 🔴 Critical issues before design begins – correct the software operator CTA destination (Cassandra → Kafka) and add a URL for the Resources "Contact us" link.
2. Address 🟡 Needs Work items – trim the page description, fix data spotlight character overruns, fill in the navigation path, add alt text, and move image assets to the asset manager.
3. Confirm the ❓ Needs review item (funnel stage) with the page owner.
4. Polish 🔵 Minor items (trademark casing, possessive note).

---

## 🔲 Manual checks for reviewer

- [ ] **Cross-reference with design intent:** confirm the copy matches the structure and intent of the Figma file linked in the metadata.
- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path.
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved.
