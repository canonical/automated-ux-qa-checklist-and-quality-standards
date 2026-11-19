# UX Figma review: Ubuntu Architecture page

**Figma file:** Ubuntu Architecture page (text extract from node 1:4416)  
**Copy doc:** Google Sheets export provided inline  
**Date:** 2026-08-13  
**Checks run:** All

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | 0 | 8 | 5 |
| UX quality check | 0 | 0 | 5 | 2 |
| Brand & style compliance | 0 | 1 | 5 | 1 |

**Total issues:** 27 (one critical, 18 needs work, eight minor)

---

## Check 1: Exact copy match

### 🔴 Critical — Wording differences
- None.

### 🔴 Critical — Missing from Figma
- None.

### 🟡 Needs Work — Extra in Figma
- **[Navigation]** "Canonical Ubuntu" – nav logotype text appears twice and is not present in the copy doc.
- **[Navigation]** "Products" – not present in the copy doc.
- **[Navigation]** "Solutions" – not present in the copy doc.
- **[Navigation]** "Support" – not present in the copy doc.
- **[Navigation]** "Community" – not present in the copy doc.
- **[Navigation]** "Get Ubuntu" – not present in the copy doc.
- **[Navigation]** "All Canonical" – not present in the copy doc.
- **[Navigation]** "Sign in" – not present in the copy doc.

### 🔵 Minor — Punctuation / capitalization / spacing
- **[Hero subtitle]**
  - Figma: "Target any silicon.  Deploy anywhere."
  - Copy doc: "Target any silicon. Deploy anywhere."
- **[Hero CTA]**
  - Figma: "Find out more about our supported architectures ›"
  - Copy doc: "Find out more about our supported architectures >"
- **[Philosophy CTA]**
  - Figma: "Learn more about supported architectures on Ubuntu ›"
  - Copy doc: "Learn more about supported architectures on Ubuntu >"
- **[Certification CTA]**
  - Figma: "Learn about our program ›"
  - Copy doc: "Learn about our program >"
- **[Architecture vs. certification body]**
  - Figma: "...preserve the high-quality user experience."
  - Copy doc: "...preserve the high-quality user experience.."

---

## Check 2: UX quality check

### Issues by page section

#### Hero

##### 🟡 Needs Work
- **[CTAs]** – The primary CTA starts with a vague verb phrase.
  - *Found:* "Find out more about our supported architectures" | *Recommendation:* "Explore supported Ubuntu architectures" or another more specific action-led label.

#### Philosophy section

##### 🟡 Needs Work
- **[Mobile Considerations]** – The opening body copy is dense for small screens, especially with a long paragraph followed by three concept-heavy bullets.
  - *Found:* "The diversification of silicon is driving the next generation of computing..." | *Recommendation:* Consider shorter paragraph breaks or more scannable sub-structure for mobile.

#### Architecture variants section

##### 🟡 Needs Work
- **[Mobile Considerations]** – The section stacks several dense technical paragraphs and a sub-heading before the CTA, which may feel heavy on mobile.
  - *Found:* "Historically, Linux distributions have faced a difficult choice..." | *Recommendation:* Break the copy into shorter chunks and confirm line length and wrapping in mobile designs.

#### Architecture vs. certification section

##### 🟡 Needs Work
- **[Mobile Considerations]** – The certification explanation is long and information-dense for one block.
  - *Found:* "A CPU is just one part of the hardware stack..." | *Recommendation:* Split key ideas into shorter paragraphs or supporting bullets.

##### 🔵 Minor
- **[Accessibility]** – No image alt text is surfaced for the section artwork in the provided Figma text extract.
  - *Found:* No visible alt-text annotation for the server-rack image | *Recommendation:* Add or confirm meaningful alt text in the design spec.

#### Further reading

##### 🟡 Needs Work
- **[Links]** – The contact CTA appears to be broken into multiple linked fragments, which makes the sentence harder to maintain and could create a poor screen-reader experience.
  - *Found:* "If you have anything else we can help with, please {ts2}c{/ts2}{ts2}[ontact us]... [. ]" | *Recommendation:* Make "contact us" one clean link and keep the period outside the link.

##### 🔵 Minor
- **[Accessibility]** – No visible alt text is surfaced for the non-decorative page imagery in the provided extract.
  - *Found:* No alt-text annotations for the hero, philosophy, or architecture-variant images | *Recommendation:* Add or confirm alt text in Figma annotations or implementation notes.

#### Page-level

##### 🟡 Needs Work
- **[Navigation]** – The provided content does not show an active-state cue for the current page, so users may not be able to tell where they are in the site structure.
  - *Found:* Top navigation lists standard items only | *Recommendation:* Confirm there is a visible or accessible current-page indicator in the design.

### Designer annotations

- No designer annotations or comments were included in the provided Figma extract, so this check could not be completed from the available input.

---

## Check 3: Brand & style compliance

### Issues by severity

#### 🔴 Critical
- **[A3]** – Wrong official product name capitalization.
  - *Found:* "Ubuntu server supports all major CPU architectures..." in Further reading | *Correct:* "Ubuntu Server supports all major CPU architectures..."

#### 🟡 Needs Work
- **[A4]** – Technical term capitalization is inconsistent with Canonical style.
  - *Found:* "Ubuntu draws upon advanced X86 vector extensions..." in Architecture variants | *Correct:* "Ubuntu draws upon advanced x86 vector extensions..."
- **[A10]** – Acronym is used before it is spelled out.
  - *Found:* "edge IoT devices" in the hero body and philosophy section | *Correct:* Spell out "internet of things (IoT)" on first mention.
- **[B3]** – Several sections run well beyond the preferred website sentence length, reducing scannability.
  - *Found:* Long sentences in the philosophy, architecture variants, and certification sections | *Correct:* Break long sentences into shorter, clearer statements.
- **[B7]** – A superlative claim appears without support.
  - *Found:* "one of the most popular operating systems for developers" in Further reading | *Correct:* Add evidence or replace with a specific, verifiable benefit.
- **[B10]** – Dense technical jargon may be hard for broader audiences without more framing.
  - *Found:* "architecture variants", "dpkg", "apt", "Launchpad", and "amd64v3" in Architecture variants | *Correct:* Define or simplify terms where the intended audience is not already deeply technical.

#### 🔵 Minor
- **[A7]** – Single-figure numbers in prose should usually be spelled out.
  - *Found:* "this is 5 years for our 'Main' package archive" in the philosophy section | *Correct:* "this is five years for our 'Main' package archive"

---

## ✅ What looks good

- The main heading structure is clear and follows a logical top-to-bottom narrative from overview to detail.
- Most headings are specific and descriptive rather than generic.
- The two-button pair in the support section is distinct, with no duplicated CTA labels.
- Product naming is mostly strong – for example, "Ubuntu Pro" is correct and consistent.
- The resource links are generally descriptive and make sense out of context.
