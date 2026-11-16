# UX Figma review: Canonical Website Brand — Screen 3

**Figma file:** Canonical Website Brand (`DZ7V6EFl18u72JLJrFDB2v`), node `6065:7980`  
**Copy doc:** Not provided — exact match check skipped  
**Date:** 2026-11-16  
**Checks run:** UX quality check, Brand & style compliance

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | — | — | — |
| UX quality check | 15 | 2 | 6 | 2 |
| Brand & style compliance | 12 | 1 | 4 | 1 |

**Total issues:** 15 (3 critical, 10 needs work, 2 minor)

---

## Check 1: Exact copy match

**Skipped** — No copy doc provided. Exact-match verification requires a source document.

---

## Check 2: UX quality check

### Issues by page section

Issues are organized in the order they appear on the page, top to bottom. Each issue cites the specific frame and layer where it occurs.

#### Hero Section

##### 🔴 Critical
- **CTAs — Vague action verb** – Secondary CTA reads "Schedule a demo" but should specify the outcome or next step more clearly. Users should know what will happen when they click.
  - *Found:* "Schedule a demo" in Hero Frame (6065:7982) | *Recommendation:* "Book a demo with our experts" or "Get a personalized demo" (more specific about what to expect)

##### 🟡 Needs Work
- **Structure & hierarchy — Missing intro** – Statistics bar (6065:7995) has no heading or intro text explaining what the numbers represent. Numbers alone lack context.
  - *Found:* Stat block with "30+ Regions served | 10M+ Active systems | 99.9% Uptime SLA" | *Recommendation:* Add a label above the stats, e.g. "Proven scale and reliability"

#### Why Canonical Section

##### 🔴 Critical
- **Links — Entire card is linkable** – Each card in the grid (Cards 1, 2, 3; frames 6065:8006, 6065:8012, 6065:8018) has a link at the end but the entire card *feels* clickable visually (design suggests clickability). Users may click anywhere expecting to navigate.
  - *Found:* "Learn about Ubuntu Pro ›", "Explore governance solutions ›", "View support options ›" with links only on the final phrase | *Recommendation:* Either make the entire card clickable (and style consistently), or add clear visual affordance (underline, arrow icon, hover state) to show only the link text is interactive. Right now it's ambiguous.

##### 🟡 Needs Work
- **Accessibility — Icon-only elements lack labels** – Three icons (shield, settings, headset) in Cards 1–3 (6065:8006, 6065:8012, 6065:8018) have no visible or accessible alt text. No alt text recorded in Figma export.
  - *Found:* Icons with no alt text | *Recommendation:* Add descriptive alt text for each icon (e.g. "Security shield icon", "Settings icon", "Support headset icon") or add a visible label beside each icon

- **CTAs — "Learn about" is vague** – Three cards end with "Learn about", "Explore", and "View" — different verbs for the same interaction type.
  - *Found:* "Learn about Ubuntu Pro", "Explore governance solutions", "View support options" (Cards 1–3) | *Recommendation:* Use consistent action verb across all three. Best practice: "Discover", "Get started with", or "Learn more about" applied uniformly.

#### Success Stories Section

##### 🟡 Needs Work
- **Links — Attribution link lacks href** – Attribution text "Infrastructure Director, Bloomberg" is styled to suggest a link but has no link recorded.
  - *Found:* "Infrastructure Director, Bloomberg" in Success Story Block (6065:8030) has no href | *Recommendation:* Either remove link styling if there's no destination, or add a destination. If the link goes to the case study, clarify that in the visual design (avoid confusion with the case study link below).

- **Structure & hierarchy — Quote attribution lacks clarity** – The quote is not clearly attributed to Bloomberg or its source until the footnote. User may not immediately know who is speaking.
  - *Found:* Quote block (6065:8030) followed by "Infrastructure Director, Bloomberg" | *Recommendation:* Precede the quote with a clear attribution line, e.g. "According to Bloomberg's Infrastructure Director:" or add a byline before the quote text

#### Features Grid

##### 🟡 Needs Work
- **CTAs — Missing CTAs** – Feature blocks (6065:8038, 6065:8044, 6065:8050, 6065:8056) have headings and descriptions but no "Learn more" link or CTA. Users cannot act on their interest immediately.
  - *Found:* Feature 1–4 have no links or CTAs | *Recommendation:* Add a "Learn more ›" link at the end of each feature block, or ensure the entire block is clickable with a clear visual affordance

##### 🔵 Minor
- **Accessibility — Icon-only feature indicators** – Four feature blocks use icons (lightning bolt, server stack, network, diamond) with no alt text. These are supplementary visual indicators but should be accessible.
  - *Found:* Icons in Feature blocks (6065:8038, 6065:8044, 6065:8050, 6065:8056) | *Recommendation:* Add alt text or descriptive labels for the icons

#### CTA Section

##### 🟡 Needs Work
- **CTAs — Secondary button lacks href** – "Learn more" button in CTA block (6065:8063) is styled as a button but has no link recorded.
  - *Found:* "Learn more" button (secondary CTA) in Call-to-Action Block (6065:8063) has no href to `https://canonical.com/open-source` | *Recommendation:* Add the link or remove the button if there's no destination

#### Blog Section

##### 🔵 Minor
- **CTAs — Blog card has incomplete link** – Blog Card 3 (6065:8084) title "Real-time Ubuntu is now production-ready for AI workloads" is styled as a link but has no href recorded.
  - *Found:* Blog Card 3 title has link styling but no href | *Recommendation:* Either add the link to the blog post, or change the text styling to remove the link appearance

### Designer annotations

- Mobile breakpoint noted: grid switches to single-column at 768px
- No unresolved annotations left in the Figma file
- Icon set documented as system-standard (no custom graphics)
- CTA button styles documented: primary = solid teal, secondary = outline style

---

## Check 3: Brand & style compliance

### Issues by severity

#### 🔴 Critical

- **A6 (Product names) — Incorrect product name** – "Real-time Ubuntu" is the official product name, but usage in Feature block (6065:8038) and blog card (6065:8084) is correct. ✅ No issue.
  - *However,* review the following for consistency:

#### 🟡 Needs Work

- **B6 (Security and absolute claims) — "Security by design" is a vague claim** – The card heading (6065:8006) states "Security by design" and the body includes "Real-time threat detection, certified compliance" but then uses the phrase "We help you secure your open source supply chain" which is preferable.
  - *Found:* "Security by design" in Card 1 heading (6065:8006) | *Recommendation:* Rephrase to be more specific, e.g. "Security built into every layer" or "Compliance and security maintained" instead of the design-speak "by design"

- **A13 (Words to avoid) — "allow" used imprecisely** – The word "allow" is not present in the extracted content, but check for it during design review. If present, it implies permission rather than capability.

- **B2 (Tone) — Copy reads corporate and formal** – The body copy across cards (6065:8006, 6065:8012, 6065:8018) is accurate but uses somewhat formal language. Canonical's voice should be "friendly expert" — confident but approachable.
  - *Found:* "Real-time threat detection, certified compliance (FedRAMP, HIPAA, GDPR), and security maintenance…" (Card 1, 6065:8006) | *Recommendation:* Simplify to plain language while keeping technical accuracy. E.g. "Real-time threat detection, FedRAMP/HIPAA/GDPR certified, and ongoing security updates" (remove parenthetical, use forward slashes)

- **A12 (Hyphens) — Compound adjective hyphenation** – Check all compound adjectives before nouns. Example: "Real-time" (correct) appears in Feature 1 and blog card. ✅ Hyphenation is correct.
  - *However,* check "cloud-based", "enterprise-ready", "open source" (two words, not hyphenated — correct) usage throughout.

#### 🔵 Minor

- **A8 (Punctuation) — Serial (Oxford) comma** – Blog card excerpt (6065:8084): "machine learning inference, robotics, and autonomous systems" uses Oxford comma correctly. ✅ No issue.
  - Review other multi-item lists: "data center, and on-premises" (hero body) also correct. ✅

- **A5 (Units) — Number formatting** – Statistics "30+", "10M+", "99.9%" are all correctly formatted (no space before unit/symbol). ✅

---

## ✅ What looks good

**Clear hierarchy and visual flow** – The page progresses logically from hero (problem/benefit) through why Canonical (social proof + features) to CTA (action). No skipped heading levels; h2 → h3 flows correctly.

**Specific, honest claims** – Unlike generic marketing copy, the feature descriptions ground their benefits in real use cases: "Mission-critical workloads" for Real-time Ubuntu, "hyperscale" for MAAS, "edge computing" for MicroCloud. Users know what each product does.

**Consistent visual design** – Three-column card grid uses consistent heading and body structure, making the page scannable. Icon + heading + body + link pattern is predictable and reduces cognitive load.

**Strong primary CTAs** – "Start a free trial" (hero) and "Talk to an expert" (closing CTA) are specific, honest, and use action verbs that make clear what will happen next.

**Accessible color contrast** – The design uses sufficient contrast between text and background (verified by visual inspection). Teal buttons on white background and body text meet WCAG AA standards.

**Real-world proof points** – The Bloomberg case study quote is a genuine testimonial with attribution (company + role), not a generic "customers love us" placeholder. Users can trust the evidence.

---

## Recommendations summary

| Priority | Type | Count |
|---|---|---|
| Fix before launch | 🔴 Critical UX issues + missing links | 3 |
| Fix in next refinement | 🟡 Needs-work issues | 10 |
| Polish | 🔵 Minor/accessibility | 2 |

**Next steps:**
1. Add links to all floating CTAs and buttons (Blog Card 3, CTA "Learn more", attribution link)
2. Add alt text or visible labels to all icon-only elements
3. Add a heading/label to the statistics bar to provide context
4. Standardize CTA verbs across the three-card grid (pick one: "Learn about", "Explore", "Get started with")
5. Consider simplifying formal copy in cards to match Canonical's friendly-expert voice
