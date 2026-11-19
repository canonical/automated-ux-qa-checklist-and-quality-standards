# UX content audit report – Figma

**Figma file:** canonical.com-data – Sites (node 4553-4538)
**Copy doc:** _data_cassandra (1).md
**Date:** 16 June 2026
**Checks run:** Both (exact copy match + UX quality check)

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review |
|---|---|---|---|---|---|
| Exact copy match | 22 | 2 | 1 | 0 | 1 |
| UX quality check | 14 | 0 | 5 | 4 | 1 |

**Total issues:** 12 (two critical, six needs work, four minor) · **Needs review:** 2

---

## Check 1: Exact copy match

### 🔴 Critical – Wording differences

- **[Hero] Secondary CTA**
  - Figma: "Give it a try"
  - Copy doc: "Try Apache Cassandra"
  - *Impact:* The copy doc CTA is specific and tells the user exactly what they are trying. The Figma version is vague and loses the product name context.

- **[Tiered list – Snap] CTA**
  - Figma: "Try it"
  - Copy doc: "Try the snap"
  - *Impact:* "Try it" is generic. "Try the snap" tells the user what they are getting. The copy doc version is clearer.

### 🟡 Needs work – Extra in Figma

- **[Options/pricing] Strikethrough text**
  - Figma shows "deployments" with strikethrough styling in the sentence "scale your ~~deployments~~ and meet your SLAs"
  - Copy doc: "scale your deployments and meet your SLAs" (no strikethrough)
  - *Impact:* This looks like an in-progress edit that has not been reflected back to the copy doc. The intended replacement word is unclear. This needs to be resolved before development – either update the copy doc with the final wording or remove the strikethrough.

### ❓ Needs review

- **[Logo cloud] "data centre" vs "data center"**
  - Both the Figma and the copy doc use "data centre" (UK spelling). The copy doc review already flagged this as a style issue (US English required). Confirm which version should be implemented – the copy doc needs to be corrected to "data center" and the Figma should follow.

### ✅ Matching content (no issues)

The following content matches exactly between the Figma and the copy doc:

- Hero heading: "Enterprise support for Apache Cassandra"
- Hero body copy
- Hero primary CTA: "Contact us"
- Logo cloud heading and body copy
- Cloud provider logos (OpenStack, MicroCloud, VMware, AWS, Google Cloud, Microsoft Azure)
- Data spotlight heading: "Our offering by the numbers"
- All three data spotlight values, labels, descriptions, and CTAs
- Tiered list heading: "Apache Cassandra deployment options"
- Snap and Software operator descriptions
- Software operator CTA: "Check our software operator"
- All four use case headings and descriptions
- Use cases section heading: "Popular Apache Cassandra use cases"
- Options/pricing heading and body copy (aside from strikethrough)
- Subscription-based and On-demand lists
- Resources section heading, subheadings, and all links
- Trademark notice

---

## Check 2: UX quality check

### Issues by page section

#### Hero

##### 🟡 Needs work
- **[CTAs]** – The secondary CTA "Give it a try" (as rendered in Figma) is vague and does not tell the user what they will try or where they will go. The copy doc version "Try Apache Cassandra" is better but still does not specify the destination (it links to documentation, not a trial).
  - *Found:* "Give it a try" | *Recommendation:* Use the copy doc text "Try Apache Cassandra" or consider "Read the docs" to set accurate expectations, since the link goes to documentation.

#### Logo cloud

##### 🟡 Needs work
- **[Brand & style – A1]** – "data centre" uses UK English. Should be "data center" per Canonical style guide.
  - *Found:* "your private data centre on top of MAAS and MicroCloud, OpenStack, or VMWare" | *Recommendation:* Change to "data center".

- **[Brand & style – A3]** – "VMWare" is incorrectly capitalised. The correct name is "VMware" (lowercase "w").
  - *Found:* "OpenStack, or VMWare" | *Recommendation:* Change to "VMware".

#### Tiered list

##### 🟡 Needs work
- **[CTAs]** – The Snap CTA "Try it" is vague and does not describe what the user is trying.
  - *Found:* "Try it" | *Recommendation:* Use the copy doc text "Try the snap" which is specific and actionable.

#### Equal height row (use cases)

##### 🟡 Needs work
- **[Tone & clarity]** – Grammar error carried from the copy doc: "such the ones" should be "such as the ones" or "such as those".
  - *Found:* "applications distributed across several regions, such the ones managing global user or session data" | *Recommendation:* Change to "such as those managing global user or session data."

##### 🔵 Minor
- **[Accessibility]** – The four use case illustrations do not have visible alt text annotations in the Figma file. These are decorative/informational illustrations and should have descriptive alt text for screen readers.
  - *Recommendation:* Add alt text annotations, e.g. "Illustration of real-time analytics pipeline".

#### Options/pricing

##### 🟡 Needs work
- **[CTAs]** – "More details" is a vague CTA that does not describe what happens when clicked.
  - *Found:* "More details" button | *Recommendation:* Use a specific label such as "See pricing options" or "View service plans".

##### 🔵 Minor
- **[Completeness]** – The strikethrough on "deployments" suggests an unfinished edit. This should be resolved before handoff to development.
  - *Recommendation:* Finalise the wording and update both the copy doc and the Figma file.

#### Resources

##### 🔵 Minor
- **[Links]** – "Read more" is used as a section subheading above a list of resource links. While not link text itself, it is a vague label.
  - *Found:* "READ MORE" as a category heading | *Recommendation:* Consider "Further reading" or "Related resources".

#### General

##### 🔵 Minor
- **[Accessibility]** – The Cassandra logo in the hero section does not have a visible alt text annotation.
  - *Recommendation:* Add alt text, e.g. "Apache Cassandra logo".

### ❓ Needs review

- **[Navigation]** – The bubble navigation shows "Data | Portfolio | Services | Docs". This matches the copy doc but a reviewer should confirm these labels are correct and the navigation structure is current.

---

## ⬜ Not applicable

- **Forms & Inputs** – N/A: this is a marketing/product page with no form or input flow.
- **Error & Feedback States** – N/A: no interactive states on a marketing page.
- **Mobile Considerations** – Not visible in this desktop-only frame. Flag for separate mobile review if applicable.

---

## ✅ What looks good

- **Hero copy** is strong – clear value proposition with specific benefits (hardened artifacts, 15 years of security maintenance, SLA-backed support) and a distinctive voice ("a team that breathes open source").
- **Data spotlight** uses concrete, scannable numbers (1 million+ users, 9+ automations, ~30 minutes) that build credibility effectively.
- **Tiered list** clearly differentiates between the two deployment options (Snap vs Software operator) with distinct descriptions and CTAs.
- **Use cases section** is well structured with four distinct, well-explained scenarios and supporting illustrations.
- **Consistent terminology** – "Apache Cassandra" is used throughout (full name, respecting the trademark).
- **Navigation labels** are reflected correctly in the design ("Data > Portfolio > Services > Docs").
- **Heading hierarchy** flows logically from the page title through section headings.
- **Subscription-based and On-demand** pricing columns are clearly separated with matching structure.
- **Resources section** organises links into clear categories (community, contact, reading, contribute).
- **Trademark notice** is present at the bottom of the page.

---

## Designer annotations

No unresolved designer annotations were visible in the Figma frame. The strikethrough on "deployments" in the pricing section may indicate an in-progress edit – this should be confirmed with the designer.

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** – open the live page, refresh, and confirm only the intended sections have changed
- [ ] **Keyboard navigation** – for any special or interactive features, manually tab through to confirm correct order
- [ ] **Mobile review** – this audit covers the desktop frame only. Confirm a mobile design exists and review separately
- [ ] **Strikethrough resolution** – confirm with the designer whether "deployments" is being replaced and what the final wording should be
- [ ] **Image alt text** – confirm that use case illustrations and the Cassandra logo will have alt text in the build
