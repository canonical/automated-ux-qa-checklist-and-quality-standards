# UX content audit report

**Source:** EOW Catchup - Sites (2).pdf (Apache Cassandra page — Enterprise support for Apache Cassandra)
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
| UX quality check | 4 | 0 | 6 | 6 |

**Total issues:** 12 (0 critical, 6 needs work, 6 minor)

---

## Check 2: UX quality check

### Structure & hierarchy

#### 🔵 Minor
- **Stats — "Served by our stack":** "Our stack" is internal jargon that doesn't communicate value to an external user. The supporting body copy ("It actively supports our own global Snap Store platform") is better — the subheading should reflect the user benefit, not the internal framing.
  - *Recommendation:* "Proven at global scale" or "Battle-tested in production"

- **Stats — "~30 minutes":** The tilde approximation prefix is informal and inconsistent with "1 million+" and "9+". Consider "Under 30 minutes" for tonal and visual consistency.

---

### CTAs

#### 🟡 Needs Work
- **Hero — "Give it a try":** Vague — does not tell the user what they will be trying or what happens when they click.
  - *Recommendation:* "Try Apache Cassandra for free" or "Start a free trial"

- **Deployment options — Snap — "Try it.":** Extremely minimal and ambiguous — the trailing period makes it read as a statement rather than a CTA, and there is no indication of what is being tried. This is the only CTA for the Snap deployment option.
  - *Recommendation:* "Try the Cassandra snap" or "Install Cassandra on Linux"

- **Support services — "More details":** Vague alongside "Get in touch" — no differentiation of outcome between the two CTAs.
  - *Recommendation:* "See what's included" or "Compare plans"

- **Multiple "Contact us" instances:** "Contact us" appears at least twice (hero, stats section) and may route to different destinations. Same label, potentially different outcomes.
  - *Recommendation:* Apply the community section pattern — "Tell us more about your needs" is already used well there; differentiate others as "Contact sales" or "Talk to our team"

#### 🔵 Minor
- **Stats — "Check our automation ›":** "Check" is informal. *Recommendation:* "Explore automation options"
- **Stats — "Try it yourself ›":** No indication of what to try. *Recommendation:* "Follow the quickstart guide"
- **Deployment options — "Check our software operator":** "Check" is informal. *Recommendation:* "Explore the software operator" or "See what the operator does"
- **Support services — "Get in touch":** Generic alongside other contact CTAs. *Recommendation:* "Request on-demand support"

---

### Copy errors

#### 🟡 Needs Work
- **Geo-distributed applications card:** "...such the ones managing global user or session data." — missing word, should be "such **as** the ones". This is a grammatical error in visible product copy.
  - *Found:* "such the ones" | *Correction:* "such as the ones"

---

### Accessibility

#### 🟡 Needs Work
- **Use case card illustrations:** Four illustrative images appear with no visible alt text. Need descriptive alt text or `alt=""` if purely decorative.
- **Cloud provider logos:** Six logos (OpenStack, MicroCloud, VMware, AWS, Google Cloud, Microsoft Azure) appear as images and need alt text matching each brand name.
- **Cassandra hero icon:** The Cassandra eye/logo icon in the hero area appears as an image and needs appropriate alt text.

---

### Community section

#### 🟡 Needs Work
- **"Connect with the community" — Matrix chat only:** The etcd equivalent page lists both Matrix chat and Discourse forum. If a Cassandra Discourse forum exists, it should be listed here for consistency and discoverability. If there is no Discourse community for Cassandra, this is fine — but worth confirming intentionality.

---

### Mobile considerations

#### 🔵 Flag for review
- **Stats section (3-column):** Three equal-width stat columns with body text will likely stack on mobile — verify stacking order reads logically.
- **Use case cards (4-column grid):** Will need to reflow to 2-column or single-column on mobile.
- **Cloud logos row (6 logos):** Likely to wrap or overflow on small screens — confirm responsive treatment.
- **H2 wrapping:** "Popular Apache Cassandra use cases" is a long heading that wraps at mid-page widths — verify this renders acceptably across breakpoints.

---

### Language consistency

#### 🔵 Minor
- **Cloud logos section body — "data centre":** UK spelling. Should be "data center".

---

### Footer

#### 🔵 Minor
- **"© 2023 Canonical Ltd."** — Copyright year appears outdated. Should be updated to 2026.

---

## ✅ What looks good

- **H1 is specific and benefit-led** — "Enterprise support for Apache Cassandra" is clear, and the hero body copy is stronger than etcd's equivalent, leading with "15 years of security maintenance" as a concrete differentiator.
- **Use case card headings** — "Real-time analytics", "Geo-distributed applications", "Mission critical applications", "Latency-sensitive applications" are all specific and user-relevant.
- **"Tell us more about your needs"** — the community section CTA is the strongest contact label on the page; the pattern should be applied more widely.
- **"Read more" and "Contribute" links** — all use descriptive, specific anchor text.
- **Trademark attribution note** — the Apache Foundation trademark notice above the footer is appropriate and well-placed.

---

## Recommended priority order

1. Fix the copy error — "such the ones" → "such as the ones" (Geo-distributed card) — this is live product copy with a grammatical error
2. Address 🟡 Needs Work items — particularly "Try it." CTA, accessibility gaps, and "Contact us" disambiguation
3. Polish 🔵 Minor items — CTA wording, "data center" spelling, copyright year

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** — open the live page and confirm only the intended sections have changed
- [ ] **Keyboard navigation** — tab through CTAs and confirm all "Contact us" instances have distinguishable accessible names
- [ ] **Discourse community** — confirm whether a Cassandra Discourse forum exists and should be listed in the community section
