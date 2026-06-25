# UX content audit report

**Figma file:** canonical.com data – Sites (node 4335:3841)
**Copy doc:** Data bubble landing page template .md
**Date:** 2026-06-11
**Checks run:** Both (exact copy match + UX quality check)

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | – | 2 | 1 | 2 |
| UX quality check | 12 | 0 | 5 | 4 |

**Total issues:** 14 (two critical, six needs work, six minor)

---

## Check 1: Exact copy match

### 🔴 Critical – Wording differences

- **Hero section heading**
  - Figma: "Enterprise-grade solutions for your mission critical data"
  - Copy doc: "Enterprise-grade solutions for your open source data platform"
  - The Figma heading has different wording from the approved copy doc. "Mission critical data" vs "open source data platform" changes the page's messaging and SEO keyword targeting.

- **Security section heading**
  - Figma: "Battle tested security, automation and reliability"
  - Copy doc: "Proven security, automation, and reliability"
  - "Battle tested" vs "Proven" – different wording. Also missing Oxford comma after "automation" in Figma.

### 🟡 Needs Work – Extra in Figma

- **Use cases section CTA**
  - Figma: "Choose your use case" (button)
  - Copy doc: "Discuss your use case" (link to #get-in-touch)
  - The Figma has a different CTA entirely. The copy doc specifies "Discuss your use case" linking to the contact form – the Figma shows "Choose your use case" as a button with no defined destination.

### 🔵 Minor – Punctuation / capitalisation / spacing

- **Hero description**
  - Figma: "Data flows better with the right tools. Canonical offers security, compliance, and lifecycle management solutions for the most popular open source databases and big data applications, on any cloud."
  - Copy doc: Same text
  - ✅ Match – confirmed

- **Logo strip heading**
  - Figma: "CANONICAL PRODUCTS ARE TRUSTED BY 19,000+ ENGINEERS AT"
  - Copy doc: "These companies trust Canonical to run their open source data platform"
  - Different wording and framing. The copy doc uses a descriptive sentence; the Figma uses an all-caps trust statement with a different number claim. Flagged as minor because the intent is the same (social proof) but the copy should be aligned.

- **Security section CTA**
  - Figma: Not clearly visible in the design
  - Copy doc: "Get security maintenance with Ubuntu Pro" (linking to ubuntu.com/pro)
  - The copy doc specifies a CTA for this section that does not appear in the Figma. Verify whether it was intentionally removed or missed.

---

## Check 2: UX quality check

### Issues by page section

---

#### Navigation

##### 🟡 Needs Work
- **[Navigation]** – The sub-nav shows "Portfolio / Docs" but an unresolved Figma comment questions whether the "Data" nav item should exist at all. The copy doc specifies "Portfolio | Services | Docs" as the sub-nav – "Services" appears to be missing from the Figma.
  - *Found:* "Portfolio / Docs" sub-nav | *Recommendation:* Confirm nav structure with designer; add "Services" if intended per copy doc

---

#### Hero section

##### 🔵 Minor
- **[CTAs]** – The hero CTA "Get in touch" is generic. On a data portfolio page, a more specific verb would help set expectations – e.g. "Talk to a data expert" or "Contact our data team".
  - *Found:* "Get in touch" | *Recommendation:* Use a more specific CTA that indicates what the user gets

---

#### Product grid (PostgreSQL, MySQL, MongoDB, Valkey, Spark, Kafka, OpenSearch, Etcd, Cassandra)

##### 🔵 Minor
- **[Accessibility]** – Each product tile uses a right-arrow link with just the product name (e.g. "PostgreSQL ›"). The copy doc specifies aria-labels (e.g. "Learn more about PostgreSQL") for each – since the accessibility requirement is met via ARIA labels, this is minor. Confirm aria-labels are implemented in the build.
  - *Found:* "PostgreSQL ›", "MySQL ›", etc. | *Recommendation:* Verify aria-labels are carried through to development (severity override: ARIA label present, minor)

---

#### Security, support and automation across clouds

##### ✅ Pass – no issues. Copy matches doc.

---

#### Multiple packaging formats

##### 🟡 Needs Work
- **[Links]** – The Figma shows only "Learn more about Rocks ›" as a link, but the copy doc specifies separate links for each tab: "Learn more about our containers", "Learn more about snaps", "Learn more about Debs", "Learn more about charms". The Figma appears to show only the Containers tab content – the other tab contents may not be designed yet.
  - *Found:* "Learn more about Rocks ›" only | *Recommendation:* Verify all four tab states are designed with their respective CTAs from the copy doc

---

#### A complete solution for your data use cases

##### 🟡 Needs Work
- **[Structure & hierarchy]** – The four use-case columns (Fully integrated system, Data warehouse, Data lakehouse, Streaming and Real-Time Analytics) have long paragraph descriptions that are dense and hard to scan. The "Streaming and Real-Time Analytics" heading is notably longer than the others.
  - *Found:* Four dense paragraphs under use-case headings | *Recommendation:* Shorten descriptions to two to three lines max; consider bullet points for key features

---

#### Battle tested security, automation and reliability

##### 🟡 Needs Work
- **[Structure & hierarchy]** – The four columns have dense paragraph text that is hard to scan quickly.
  - *Found:* Four paragraph-length descriptions | *Recommendation:* Tighten to two to three lines each; lead with the key benefit

##### 🔵 Minor
- **[Tone & clarity]** – "airgap" in the heading "Multi-cloud and airgap ready" is typically written as "air-gap" or "air gap" in standard usage. The copy doc also uses "airgap" and "airgapped" – both should be updated.
  - *Found:* "airgap" | *Recommendation:* Use "air-gap" / "air-gapped" for consistency with industry standard spelling

---

#### Our services

##### 🔵 Minor
- **[CTAs]** – Two CTAs appear side by side: "Get in touch" and "Discover our services". "Get in touch" repeats the hero CTA. Having the same CTA text appear twice on the page for potentially different destinations can confuse users.
  - *Found:* "Get in touch" (repeated from hero) + "Discover our services" | *Recommendation:* Differentiate – e.g. "Contact our services team" or remove if it goes to the same destination

---

#### Logo strip

##### 🟡 Needs Work
- **[Accessibility]** – The logo strip shows ~20 partner/customer logos. Alt text is not verifiable from the Figma design. Ensure each logo has alt text with the company name in the build. (Severity override: minor per logo alt text rule, but elevated to needs work here because the heading text itself differs from the copy doc – see Check 1.)
  - *Found:* ~20 company logos | *Recommendation:* Align heading with copy doc and ensure logo alt text in build

---

#### Community and support

Matches copy doc structure. The "Read more" heading is present in both the copy doc and Figma – it is the approved copy.

##### ✅ Pass

---

#### Footer

##### ✅ Pass – standard Canonical footer, no issues

---

### Designer annotations

Unresolved comments found on or near this node:

- **Node 4335:3841** – "@mattea not sure if you've talked to Kasia about this but this would be a completely custom section :') the tabbed secti…" – Indicates the tabbed section may require custom development. Confirm scope with dev.
- **Node 4335:3841** – "@mattea is there any way to have the logos on one line, or equally distributed on two lines?" – Layout question, unresolved.
- **Node 4553:4538** – "@mattea qq, why is there a 'Data' nav item?" – Navigation question, unresolved (surfaced above as a needs-work issue).

---

## ✅ What looks good

- **Clear page hierarchy** – the page flows logically from hero → product grid → features → use cases → services → community, with well-structured H1/H2 headings
- **Product grid is scannable** – nine products displayed in a clean grid with logos and arrow links; easy to browse
- **ARIA labels specified** – copy doc includes aria-labels for all product links; good accessibility planning
- **Packaging formats section** – good use of tabs (Containers, Snaps, Debs, Software operators) to organize dense content without overwhelming the user
- **Security section headings** – "Up to 15 years of support", "Hardening and compliance" etc. are specific and benefit-led
- **Services section structure** – clean split between Subscription-based and On-demand with bullet lists; easy to scan
- **Community and support** – well-organized link groups with clear categories (Connect with the community, Contact us, Read more, Other resources)
- **Copy doc is thorough** – destinations are specified for all CTAs and links, page metadata is complete

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** – open the live page and compare; confirm only the intended sections have changed
- [ ] **Keyboard navigation** – for any special or interactive features, manually tab through to confirm correct order
- [ ] **Product grid links** – verify each product link goes to the correct product page and aria-labels are implemented
- [ ] **Tab states** – confirm all four packaging format tabs are designed (Containers, Snaps, Debs, Software operators)
- [ ] **Use cases CTA** – confirm whether "Choose your use case" or "Discuss your use case" is correct, and define the destination
- [ ] **Logo alt text** – verify all logos in the trust strip have appropriate alt text in the build
- [ ] **Hero heading** – resolve which version is correct: "mission critical data" (Figma) vs "open source data platform" (copy doc)
