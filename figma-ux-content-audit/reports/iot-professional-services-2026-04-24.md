# UX content audit report

**Source:** Screenshot — `EOW Catchup - Sites (5).pdf`
**Copy doc:** Not provided — exact match check skipped
**Date:** 2026-04-24
**Checks run:** UX quality check only

> _Audit based on screenshot input. Text extraction uses vision — small or obscured text may have been missed. Layer-level attribution is not available._

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Copy doc check | — | — | — | — |
| UX quality check | 4 | 1 | 4 | 5 |

**Total issues:** 10 (1 critical, 4 needs work, 5 minor)

---

## Check 2: UX quality check

### Structure & hierarchy ✅

Page flows coherently: hero → how it works (Simple choices) → service catalogue (Your services) → feature sections (Embedded Linux / Ubuntu Core / Ubuntu Pro / Support) → closing CTA. Appropriate for a bottom-funnel services page. H1 → H2 hierarchy is consistent.

---

### CTAs

#### 🟡 Needs Work

- **Section: Hero — "Pricing and packages" (secondary CTA)**
  - The label is ambiguous — users can't tell if they'll land on a pricing table, a package comparison, or a quote form.
  - *Recommendation:* `"View device pricing"` or `"Compare packages"` — match the label to the actual destination content.

- **Section: Your services — `"Learn more about our services ›"`**
  - "Learn more" gives no indication of destination. In context of a services section, users expect a services overview or pricing page — the label should reflect this.
  - *Recommendation:* `"View services and pricing"` or `"See full service details"`.

- **Section: A powerful foundation — `"Learn more about Ubuntu Core"`**
  - Second "learn more" pattern on the same page.
  - *Recommendation:* `"Explore Ubuntu Core"` or `"Get started with Ubuntu Core"`.

- **Section: Ready to innovate? — `"Get in touch"`**
  - Generic and context-free. Doesn't indicate who users are contacting or why, weakening the closing CTA.
  - *Recommendation:* `"Talk to our IoT team"` or `"Contact our IoT experts"`.

#### 🔵 Minor

- **Section: Embedded Linux — `"Discover Ubuntu Embedded Services"`**
  - "Discover" is borderline vague but the product name makes it sufficiently descriptive. Consider `"Explore Ubuntu Embedded Services"` for consistency with other CTAs.

- **Section: Mission-critical support — `"Discover Ubuntu Enterprise Support"`**
  - Same pattern as above. `"Explore Ubuntu Enterprise Support plans"` or `"See support options"` would be more action-specific.

---

### Links ✅

- `"Contact us"` — clear ✓
- `"Explore Ubuntu Pro for Devices"` — specific ✓
- Named product links are descriptive throughout — no standalone "click here" or "read more" labels ✓

#### 🔵 Minor

- The `›` chevron on `"Learn more about our services ›"` should be `aria-hidden="true"` or added via CSS `::after` to prevent screen readers announcing it.

---

### Accessibility

#### 🔴 Critical

- **Section: Wind turbine / drone photograph**
  - The photo shows a drone inspecting an industrial wind turbine — a contextually meaningful illustration of IoT in industry. If `alt=""` is set (marking it as decorative), users who cannot see it lose relevant context.
  - *Recommendation:* Confirm intent with the designer. If the image adds meaning, supply: `"A drone inspecting a wind turbine, illustrating IoT monitoring in industrial environments"`. If purely decorative, `alt=""` is correct — but document that decision.

#### 🟡 Needs Work

- **Section: Simple choices — tier illustrations (4 images)**
  - Each of the four tiers has an isometric illustration. These are not confirmed as decorative. If they convey information about the tier's scope or output, they need descriptive `alt` text.
  - *Recommendation:* Confirm with designer whether each illustration is decorative or informational, and supply `alt` values accordingly.

---

### Navigation ✅

Navigation bar shows Features | Customer stories | Services | Docs. "Services" appears highlighted/active, correctly indicating current location. Users can identify where they are in the site.

---

### Mobile considerations

#### 🔵 Flag for review

- **"Simple choices" tiered grid** — four tiles, each with 4–5 bullets, arranged in a 2×2 grid; verify stacking and readability on small screens.
- **"Your services" table layout** — 2-column (service name | description) rows; verify it collapses to a readable single column on mobile.
- **Four 50/50 split sections** (Embedded Linux, A powerful foundation, Up to 15 years, Mission-critical support) — confirm stacking order at small sizes is logical and that the text column always appears before the image column.

---

## ✅ What looks good

- **H1 is strong and specific** — "Power your device with our IoT professional services" names the product, the audience, and the value in one sentence.
- **"Simple choices" sub-headings are action-oriented** — "Pick a board", "Package your apps", "Build your app store", "Manage software updates" put the user as subject, not the product.
- **Bullet copy in each tier is concise and scannable** — 4–5 short bullets per section with no filler phrases.
- **"Your services" one-sentence descriptions are well-calibrated** — SmartStart, Engineering services, System on a chip, and Secure boot entries each say exactly enough for a buyer to self-qualify.
- **"Ready to innovate?" explicitly addresses two buyer types** — startups and enterprises named in a single sentence; well-targeted for a services page closing section.

---

## Recommended priority order

1. **Fix 🔴 Critical** — confirm wind turbine photo alt text intent; supply descriptive alt if informational
2. **Address 🟡 Needs Work** — sharpen hero secondary CTA ("Pricing and packages"), "Learn more about our services", and "Learn more about Ubuntu Core"; update "Get in touch" to be IoT-specific; confirm alt text on the four tier illustrations
3. **Polish 🔵 Minor** — review "Discover" CTA labels for consistency, add `aria-hidden` to chevron in services link

---

## 🔲 Manual checks for reviewer

- [ ] **Wind turbine image** — confirm `alt=""` is intentional or supply descriptive alt text
- [ ] **Simple choices tier images** — confirm each is decorative or informational; supply `alt` values for informational ones
- [ ] **Live page compare** — open `/core/services` and verify only intended sections have changed
- [ ] **Keyboard navigation** — tab through hero CTAs, service links, feature section links, and "Ready to innovate?" CTA to confirm correct focus order
