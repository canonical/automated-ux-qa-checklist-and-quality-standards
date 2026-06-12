# UX content audit report — design stage

**Source:** [canonical.com/ceph — Sites (Figma)](https://www.figma.com/design/d3yDJFcSFPv8baDTWnk0jR/canonical.com-ceph---Sites?node-id=1-5640&t=4rIlNnjoABMnv0oo-4)
**Copy doc:** canonical.com_ceph.md
**Date:** 2026-04-29
**Note:** Figma MCP requires authentication and was not accessible in this session. This audit is based entirely on the copy document. Visual hierarchy and layout are inferred from section template names and column annotations.

---

## Summary

| Section | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Structure & hierarchy | 3 | 0 | 3 | 0 |
| CTAs | 2 | 0 | 4 | 1 |
| Links | 3 | 1 | 2 | 2 |
| Accessibility | 0 | 2 | 2 | 2 |
| Mobile considerations | — | — | — | 2 flags |

**Total issues:** 19 (3 critical, 11 needs work, 5 minor/flags)

---

## UX quality check

### Structure & hierarchy

#### 🟡 Needs Work

- **Section: Data Spotlight — all three description rows are empty**
  — The data points (10+ / Years, 1,000,000+ / Downloads, 1 minute / To get started) have no supporting description in the third row. Every data spotlight entry shows a blank `[col:3,5,7, ch:100]` row. Whether that row renders or is hidden by the template is unclear, but the metric labels give no context for why these numbers matter.
  - *Found:* Three description rows, all blank
  - *Recommendation:* Add a one-line supporting statement per data point — e.g. "10+ / Years / Proven in production since 2012" or "1 minute / To get started / With MicroCeph, you're running Ceph in a single command." Even if the template hides this row visually, having copy prepared gives designers and editors something to work with.

- **Section: Why choose Canonical Ceph? — Benefits list is unformatted prose**
  — The entire benefits list is written as a single continuous text block with no punctuation, separators, or visual breaks between items: *"Benefits of Canonical Ceph Highly scalable, from Terabytes to Exabytes Highly reliable, with no single point of failure Protect your data with replication and erasure coding…"*
  - *Found:* Continuous prose without bullets, punctuation, or line breaks
  - *Recommendation:* Break into a proper bulleted list. Each benefit is a distinct point and should be visually scannable — especially for an executive audience in the exploration stage.

- **Section: Canonical Ceph deployment and operations — inline bold used as sub-headings**
  — Sub-sections (Deploying Ceph, Operating Ceph, A choice of tooling, Long Term Support (LTS), Economic advantage) are formatted as bold text within a body copy cell, not as distinct heading rows. Whether these render as actual headings or styled bold spans depends on implementation.
  - *Found:* `**Deploying Ceph**`, `**Operating Ceph**`, `**A choice of tooling**`, etc. — all inline within body cells
  - *Recommendation:* If these are intended as sub-headings (H3), confirm with the designer that they'll be implemented as heading elements, not just bold spans. Heading structure matters for both SEO and accessibility. If they're decorative, the copy is fine as-is.

---

### CTAs

#### 🟡 Needs Work

- **Section: Hero — "Get in touch"**
  — Vague CTA that doesn't tell the user what they're signing up for or what will happen. The main action listed in the metadata is "Try Canonical Ceph", but neither "Try Canonical Ceph" nor any equivalent appears on the page.
  - *Found:* `Get in touch` → ubuntu.com/ceph#get-in-touch
  - *Recommendation:* "Talk to an expert" or "Contact our Ceph team". Also consider whether this CTA reflects the metadata's stated main action — if "Try Canonical Ceph" is the primary goal, a trial/install CTA should be more prominent.

- **Section: Success stories — "Learn more about Ceph support ›"**
  — "Learn more" is a generic anchor that gives no information about destination or value.
  - *Found:* `Learn more about Ceph support >` → canonical.com/ceph/support
  - *Recommendation:* "Explore Ceph support options" or "See support plans" — make the destination and value explicit.

- **Section: More choice for your infrastructure — three "Find out more" CTAs**
  — All three cards end with "Find out more on Charmhub", "Find out more on GitHub", and "Find out more in the Snap Store". The destination is named but the action is missing.
  - *Found:* `Find out more on Charmhub` / `Find out more on GitHub` / `Find out more in the Snap Store`
  - *Recommendation:* Lead with the action: "Deploy with Juju on Charmhub", "Get container images on GitHub", "Install MicroCeph from the Snap Store".

- **Section: Canonical Ceph deployment and operations — "Economic advantage" sub-section has two CTAs**
  — The body text ends with two inline CTAs: "Discover Ceph's cost benefits" and "try our Ceph pricing calculator". Two CTAs at the close of a text paragraph can split user attention.
  - *Found:* `Discover [Ceph's cost benefits](link) and try our [Ceph pricing calculator](link)`
  - *Recommendation:* Consider which action is primary for this section and lead with one. The pricing calculator CTA in the hero already covers the calculator — the cost benefits blog may be redundant. Alternatively, move one CTA to a dedicated button row if both need to stay.

#### 🔵 Minor

- **Metadata: Main action stated as "Try Canonical Ceph" does not appear on the page**
  — The metadata defines "Try Canonical Ceph" as the main user action, but no CTA with this text or close equivalent exists in the copy.
  - *Found:* Metadata main action: `Try Canonical Ceph` | Actual hero CTAs: `Get in touch`, `Calculate your storage costs`
  - *Recommendation:* Either update the metadata to reflect the actual primary CTA, or add a "Try Canonical Ceph" or equivalent install/trial CTA to the page.

---

### Links

#### 🔴 Critical

- **Section: Resources — "Cloud storage cost optimization" has no URL**
  — Every other resource entry has a linked title, but this entry has no link. It will render as dead text or break the resource pattern.
  - *Found:* `Cloud storage cost optimization` — no URL provided in copy doc
  - *Recommendation:* Add the correct URL before handoff. Likely candidate: https://ubuntu.com/engage/cloud-storage-cost-optimisation — verify before using. If no page exists, link to the closest relevant resource or remove the entry.

#### 🟡 Needs Work

- **Section: Canonical Ceph deployment and operations — "we offer Managed Ceph"**
  — The link text starts with "we" and forms part of a sentence: *"…if you prefer to treat your storage as-a-service, we offer Managed Ceph – a Ceph cluster fully managed by Canonical."* The linked phrase "we offer Managed Ceph" doesn't stand alone meaningfully out of context.
  - *Found:* `…[we offer Managed Ceph](http://ubuntu.com/ceph/managed)…`
  - *Recommendation:* Rephrase so the link text is a standalone noun phrase: "…explore [Managed Ceph by Canonical] — a fully managed Ceph cluster." Also note: the URL uses `http://` — should be `https://`.

- **Section: Success stories — "Wellcome Sanger achieved a cost-effective Ceph infrastructure ›"**
  — This is an otherwise well-written link, but the alt text on the accompanying image reads "How the **Welcome** Sanger Institute uses Canonical Ceph" — missing the second 'l'. The body copy correctly spells "Wellcome Sanger" throughout.
  - *Found:* Image alt text: `How the Welcome Sanger Institute uses Canonical Ceph`
  - *Recommendation:* Correct to "Wellcome". Flag for accessibility review on implementation.

#### 🔵 Minor

- **Section: Hero — CTAs link to ubuntu.com, not canonical.com**
  — The hero CTAs point to `ubuntu.com/ceph#get-in-touch` and `ubuntu.com/ceph/pricing-calculator`. If this page is being migrated to canonical.com, these may need updating.
  - *Found:* `[Get in touch](https://ubuntu.com/ceph#get-in-touch)` | `[Calculate your storage costs](https://ubuntu.com/ceph/pricing-calculator)`
  - *Recommendation:* Confirm whether these destinations will be migrated or whether the ubuntu.com URLs are intentional cross-domain links. If canonical.com equivalents exist or will exist, update before launch.

- **Section: Canonical Ceph deployment and operations — "we offer Managed Ceph" uses http://**
  — The link URL `http://ubuntu.com/ceph/managed` uses an insecure protocol.
  - *Found:* `http://ubuntu.com/ceph/managed`
  - *Recommendation:* Update to `https://ubuntu.com/ceph/managed`.

---

### Accessibility

#### 🔴 Critical

- **Section: Resources — all four resource images use placeholder [ALT TEXT]**
  — The copy doc shows `[ALT TEXT]` as a literal placeholder for all four resource thumbnail images. None have real descriptive alt text.
  - *Found:* All four entries show `\[ALT TEXT\]` — unfilled placeholder
  - *Recommendation:* Add descriptive alt text to each image before handoff. For resource thumbnails, alt text should describe the visual content (e.g. "Webinar thumbnail: Canonical Ceph for Enterprise"). If the image is purely decorative alongside a linked title, `alt=""` is acceptable — but confirm the intent.

- **Section: Logo section — all six logo images have no alt text**
  — The six logos (CERN, Deutsche Telekom, Bloomberg, Cisco, DreamHost, DigitalOcean) have asset links but no alt text at all in the copy doc.
  - *Found:* No alt text for any of the six logos
  - *Recommendation:* Add the company name as alt text for each logo (e.g. `alt="CERN"`). Logo images are not decorative — they communicate who trusts the product.

#### 🟡 Needs Work

- **Section: Hero and section images — missing alt text throughout**
  — Multiple images across the page (hero image, section images for Deployment and operations, Why choose Canonical Ceph?, More choice for your infrastructure, Data Spotlight) have asset links but no alt text specified.
  - *Found:* image1 (hero), image9 (deployment), image10–12 (equal heights cards), image13 (Why choose) — all have `[Asset link]` but no alt text
  - *Recommendation:* Add descriptive alt text for each image. At minimum: what does the image show, and what does it communicate in context? For purely decorative images, use `alt=""` explicitly. "No alt text specified" should never be the outcome of copy doc review.

- **Section: og:Image — placeholder not filled**
  — The Open Graph image field contains the default instructional placeholder text and has not been filled in.
  - *Found:* og:Image: `Please include a link to the image you would like as the page thumbnail`
  - *Recommendation:* Add the image URL before handoff. Without it, social previews will use a fallback (often nothing), which is a missed awareness opportunity for a product page.

#### 🔵 Minor

- **Section: Success stories — image alt text typo**
  — Image alt text reads "How the **Welcome** Sanger Institute uses Canonical Ceph" — missing the second 'l' in "Wellcome".
  - *Found:* `[How the Welcome Sanger Institute uses Canonical Ceph]`
  - *Recommendation:* Correct to "Wellcome Sanger Institute".

- **Section: More choice for your infrastructure — card images have no alt text**
  — The three card images (image10, image11, image12) have asset links but no alt text.
  - *Found:* Three images with no alt text annotation
  - *Recommendation:* These are section hero images for each card — they should describe the visual content or the card topic. Even a short label is better than nothing.

---

### Mobile considerations

#### 🔵 Flag for review

- **Benefits list in "Why choose Canonical Ceph?" — unformatted prose on mobile**
  — As noted in Structure & hierarchy, the benefits list is continuous prose. On mobile this is especially hard to scan. Fixing the formatting will resolve the mobile concern too.

- **Ubuntu/Ceph version compatibility table — four-column table**
  — The LTS/Ceph compatibility matrix (Ubuntu 20.04 → Ubuntu 26.04 across four columns) will likely require horizontal scrolling or collapse treatment on narrow screens.
  - *Recommendation:* Flag for design review to confirm the mobile treatment — a collapsed/accordioned version or a responsive reflow is preferable to horizontal scroll for a product page.

---

## ✅ What looks good

- **Page description** is clear, factual, and within the 160-character limit (130 chars). Good balance of keywords and readability.
- **Hero body copy** is specific and differentiating — it names OpenStack, Kubernetes, and MicroCloud as supported workloads, which gives enterprise evaluators concrete context fast.
- **"Calculate your storage costs"** (hero CTA) is an excellent, specific CTA that names the exact action and outcome.
- **Wellcome Sanger case study** — the inline link "Wellcome Sanger achieved a cost-effective Ceph infrastructure ›" is one of the best-written links on the page: specific, active, and meaningful out of context.
- **"Ceph's cost benefits"** and **"Ceph pricing calculator"** are clearly labelled inline links that describe the destination.
- **Logo section intro** — "Ceph is used across a broad range of industries, from academic institutions, to telco, to cloud service providers (CSPs)" sets good context for the logos that follow.
- **LTS table** — including both the Ubuntu version and the supported Ceph versions in a matrix is genuinely useful for technical evaluators. Clear scope for what is and isn't under LTS commitment.

---

## Recommended priority order

1. Fix all 🔴 Critical issues — add missing URL for "Cloud storage cost optimization" and fill in all placeholder alt text (logos, resource thumbnails)
2. Address 🟡 Needs Work items — format the benefits list as bullets, improve vague CTAs, fix the "we offer Managed Ceph" link text, fill og:Image
3. Polish 🔵 Minor items — fix http → https, correct Wellcome typo, update hero CTA destinations if migrating to canonical.com

---

## 🔲 Manual checks for reviewer

- [ ] **Authenticated states** — log in and check any copy that only appears after authentication
- [ ] **JS-rendered content** — interact with the page to trigger dynamic states (errors, success messages, empty states)
- [ ] **Keyboard navigation** — tab through the page to confirm correct focus order and accessible labels
- [ ] **Mobile view** — resize or use device emulation to check layout and readability, especially the benefits list and LTS table
- [ ] **CTA destination audit** — confirm whether ubuntu.com CTA links will be redirected or updated before canonical.com launch
- [ ] **"Cloud storage cost optimization" URL** — locate and add the correct URL before handoff; do not launch without it
