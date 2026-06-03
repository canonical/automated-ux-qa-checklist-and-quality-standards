# UX content audit report

**Source:** EOW Catchup - Sites.pdf (etcd page — Enterprise support for etcd databases)
**Copy doc:** Not provided — exact match check skipped
**Date:** 2026-04-24
**Checks run:** UX quality check only
**Input mode:** Screenshot (PDF export)

> Audit based on screenshot input. Text extraction uses vision — small or obscured text may have been missed. Layer-level attribution is not available.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Copy doc check | — | — | — | — |
| UX quality check | 4 | 0 | 5 | 6 |

**Total issues:** 11 (0 critical, 5 needs work, 6 minor)

---

## Check 2: UX quality check

### Structure & hierarchy

#### 🟡 Needs Work
- **Stats section — Stat 1 subheading:** "Rely on our etcd" is an incomplete sentence that does not communicate a clear value. Unlike the parallel subheadings ("To scale your operations", "To get started"), it has no grammatical structure and reads as a fragment.
  - *Found:* "Rely on our etcd" | *Recommendation:* "Trusted by teams globally" or restructure to match parallel form

#### 🔵 Minor
- **Stats section — "~30 minutes":** The tilde approximation prefix is informal and inconsistent with the precise formatting of "1000+" and "9+". Consider "Under 30 minutes" or "30 minutes" for visual and tonal consistency.

---

### CTAs

#### 🟡 Needs Work
- **Hero — "Give it a try":** Vague — does not tell the user what they will be trying or what happens when they click. Users should be able to predict the destination or action.
  - *Recommendation:* "Try etcd for free" or "Start a free trial"

- **Support services — "More details":** Vague — more details about what, compared to what? The CTA sits next to "Get in touch" with no differentiation of outcome.
  - *Recommendation:* "See what's included" or "Compare plans"

#### 🔵 Minor
- **Stats — "Check our automation ›":** "Check" is informal and vague. Prefer a verb that communicates the action more precisely.
  - *Recommendation:* "Explore automation options" or "See our automations"

- **Stats — "Try it yourself ›":** Vague — no indication of what to try or where the link leads.
  - *Recommendation:* "Try etcd in your lab" or "Follow the quickstart guide"

- **Deployment options — "Explore all features":** Vague; unclear which product's features or what the user will find.
  - *Recommendation:* "Explore operator features" or "See all operator capabilities"

- **Support services — "Get in touch":** Generic. Since "Contact us" also appears elsewhere on the page, two generic contact CTAs create ambiguity about which to use and why.
  - *Recommendation:* "Talk to our team" or "Request on-demand support"

---

### Links

#### 🟡 Needs Work
- **Multiple "Contact us" instances:** "Contact us" appears at least three times on the page (hero, stats section, footer-area community section) and may route to different destinations or forms. Same label, potentially different outcomes — this is confusing for screen reader users and anyone scanning the page.
  - *Recommendation:* Differentiate by context: "Contact sales", "Contact support", "Tell us more about your needs" (already used well in community section — apply this pattern more broadly)

---

### Accessibility

#### 🟡 Needs Work
- **Use case card illustrations:** Four decorative/illustrative images appear in the use case cards with no visible alt text. If these are meaningful (they appear to depict different architecture scenarios), they need descriptive alt text. If purely decorative, they should be marked as such (`alt=""`).

- **Cloud provider logos:** Six partner/cloud logos (OpenStack, MicroCloud, VMware, AWS, Google Cloud, Microsoft Azure) appear as images. These need alt text matching the brand name so screen reader users know which clouds are supported.

---

### Mobile considerations

#### 🔵 Flag for review
- **Stats section (3-column layout):** Three equal-width stat columns with body text beneath each will likely stack on mobile. Verify stacking order and that the full body copy reads logically in a single column.
- **Use case cards (4-column grid):** Four cards side by side will need to reflow to 2-column or single-column on mobile. Card illustrations may be deprioritized or hidden.
- **Cloud logos row (6 logos):** A single row of 6 logos is likely to wrap or overflow on small screens. Confirm responsive treatment.

---

### Language consistency

#### 🔵 Minor
- **Container section — "flavours":** UK spelling. Should be "flavors" for US English consistency.
- **Distributed locking card — "serialise":** UK spelling. Should be "serialize".
- **Cloud logos section body — "data centre":** UK spelling. Should be "data center".

---

### Footer

#### 🔵 Minor
- **Copyright year — "© 2023 Canonical Ltd.":** The copyright year appears to be outdated. Should be updated to 2026 (or "2023–2026" if a range is preferred).

---

## ✅ What looks good

- **H1 is specific and descriptive** — "Enterprise support for etcd databases" clearly communicates what the page offers and who it is for.
- **Deployment options section** — "Install etcd on Linux" and "View GitHub repo" are specific, honest CTAs that set clear expectations.
- **"Read more about" and "Contribute" link groups** — all links use descriptive, specific anchor text (e.g. "How to choose a DBMS", "Database cloud migration", "etcd operator") rather than generic phrases.
- **Community CTA button** — "Tell us more about your needs" is the strongest contact CTA on the page; this pattern should be applied more broadly to replace generic "Contact us" and "Get in touch" labels.
- **Page hierarchy** — sections flow logically from value proposition → proof points → deployment options → use cases → support → community.

---

## Recommended priority order

1. Address 🟡 Needs Work items — particularly the accessibility gaps (logo and illustration alt text) and the multiple "Contact us" link disambiguation
2. Polish 🔵 Minor items — CTA wording, UK spellings, copyright year

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** — open the live page and confirm only the intended sections have changed
- [ ] **Keyboard navigation** — tab through CTAs and links to confirm correct focus order and that all "Contact us" instances have distinguishable accessible names
