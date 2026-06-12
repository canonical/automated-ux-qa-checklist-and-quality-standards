# UX content audit report — design stage

**Source:** [canonical.com/ceph/support — Sites (Figma)](https://www.figma.com/design/d3yDJFcSFPv8baDTWnk0jR/canonical.com-ceph---Sites?node-id=1-10481&t=4rIlNnjoABMnv0oo-4)
**Copy doc:** canonical.com_ceph_support.md
**Date:** 2026-04-29
**Note:** Page returns 404 — this is a pre-launch review of the copy doc. Figma cross-reference noted but not accessible in this session; flag for manual design review.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Structure & hierarchy | 4 | 0 | 1 | 1 |
| CTAs | 3 | 0 | 2 | 4 |
| Links | 2 | 0 | 0 | 1 |
| Accessibility | 2 | 2 | 0 | 0 |
| Navigation | 1 | 0 | 0 | 0 |

**Total issues:** 11 (2 critical, 3 needs work, 6 minor)

---

## UX quality check

### Structure & hierarchy

#### 🟡 Needs Work
- **Tiered List — "Design and delivery"** — Only service in the section with no CTA. Support, Managed services, Firefighting support, and Security and compliance all have follow-on links. Inconsistent pattern leaves users with nowhere to go after reading this service.
  - *Found:* No link row after "Design and delivery" description | *Recommendation:* Add a link — e.g. "Explore design and delivery >" pointing to a relevant page or anchor.

#### 🔵 Minor
- **Data Spotlight heading** — "Enterprise grade Ceph support" is missing a hyphen. "Enterprise-grade" is a compound modifier and should be hyphenated before a noun.
  - *Found:* "Enterprise grade Ceph support" | *Recommendation:* "Enterprise-grade Ceph support"

### CTAs

#### 🟡 Needs Work
- **"Get in touch" (Hero + Equal Heights Row)** — Appears twice on the page. Vague phrasing doesn't set expectations: does it open a form, launch a chat, or send an email? Users can't tell what will happen.
  - *Found:* "Get in touch" (Hero CTA col:1) and "Get in touch" (Equal Heights Row col:5) | *Recommendation:* Be specific — e.g. "Contact our team", "Request a consultation", or "Talk to an expert". If it opens a form, say so.

- **"Discover Canonical Ceph" (Tiered List)** — "Discover" is a weak, passive verb that doesn't tell the user what they're getting or why they'd click.
  - *Found:* "Discover Canonical Ceph" | *Recommendation:* Consider "See all Ceph offerings" or "Explore the full Ceph platform >" to be more specific about destination.

#### 🔵 Minor
- **"Explore support >", "Explore managed services >", "Explore firefighting support >"** — "Explore" is a generic action verb. These CTAs are consistent with each other, which is positive, but "Explore" is weaker than something that describes the action.
  - *Recommendation:* Consider "View support plans >", "View managed services >", "View firefighting support >" — but only if changing all three; consistency here matters more than perfection on any one.

- **"packages" (Fixed price consulting card)** — Inline link text reads only "packages" in isolation. Out of context, the destination is unclear.
  - *Found:* "Get clarity from the beginning with our fixed price [packages](https://assets.ubuntu.com/v1/ef493e88-canonical_ceph_consulting_datasheet_11_09_2025.pdf)" | *Recommendation:* "consulting packages datasheet" or link the whole phrase "fixed price packages" for clarity.

### Links

#### 🔵 Minor
- **"packages" link** — See CTAs section above. Same issue applies as a standalone link.

### Accessibility

#### 🔴 Critical
- **Hero image — alt text placeholder not filled** — The copy doc shows `[ALT TEXT]` as a placeholder. This must be completed before the page goes into development.
  - *Found:* `[ALT TEXT]` for image1 (hero image) | *Recommendation:* Write descriptive alt text. If the image is decorative, mark it as `alt=""`. If it conveys meaning (e.g. a person or scenario), describe what's shown.

- **Equal Heights Row — images with no alt text** — Four product illustration images (image2–image5) have no alt text and no placeholder. This is an accessibility blocker.
  - *Found:* `![][image2]` through `![][image5]` (Fixed price consulting, Support subscription, Firefighting support, Managed Ceph illustrations) with no alt attributes | *Recommendation:* Add alt text for each. If illustrations are decorative, use `alt=""`. If they convey context, describe the visual.

### Navigation

No issues found. Breadcrumb path is defined: Ceph (canonical.com/ceph) > Canonical Ceph support. ✅

---

## ✅ What looks good

- **Body copy is specific and informative** — Each service description in the Tiered List is clearly scoped and avoids generic filler. "Firefighting support offers a bridge between self-management with troubleshooting support, and a managed service" is a strong, honest framing.
- **Data spotlight is well-chosen** — "1 hour", "24/7/365 coverage", and "Up to 15 years" are concrete, enterprise-relevant metrics that build credibility fast.
- **"Access the case study >"** — Good CTA. Specific destination, natural action verb, clear outcome.
- **Service structure is consistent** — Each service in the Tiered List follows the same pattern: name + description + CTA (except Design and delivery — flagged above).
- **Equal Heights Row cards** — Copy for all four cards is distinct, non-repetitive, and speaks clearly to different buyer needs.
- **Inline contextual links** — "guaranteed SLAs", "S3 cost calculator", and "Ubuntu Pro" are all linked in context and the surrounding copy gives enough information to understand what you're clicking.

---

## Recommended priority order

1. 🔴 Write alt text for hero image and all four Equal Heights Row illustrations before handoff to development
2. 🟡 Add a CTA to the "Design and delivery" service to match the other four services
3. 🟡 Replace both "Get in touch" CTAs with more specific, action-oriented text
4. 🔵 Hyphenate "Enterprise-grade" in the Data Spotlight heading
5. 🔵 Review "Explore" CTAs for consistency — change all or none
6. 🔵 Make the "packages" link text more descriptive

---

## 🔲 Manual checks for reviewer

- [ ] **Figma design** — Cross-reference all copy against Figma node [1-10481](https://www.figma.com/design/d3yDJFcSFPv8baDTWnk0jR/canonical.com-ceph---Sites?node-id=1-10481&t=4rIlNnjoABMnv0oo-4). Confirm layout supports the tiered list structure and that "Design and delivery" has space for a CTA if one is added.
- [ ] **"Get in touch" destination** — Confirm whether CTAs open a contact form, modal, or link to a contact page — and update the label to match.
- [ ] **"Design and delivery" page** — Confirm whether a destination page exists for this service before adding a CTA.
- [ ] **Mobile view** — Equal Heights Row (4 cards) and Data Spotlight (3 stats) both need mobile layout review for readability at small sizes.
- [ ] **JS-rendered content** — Any dynamic states (form submission, success/error messages) cannot be checked from copy doc alone.
