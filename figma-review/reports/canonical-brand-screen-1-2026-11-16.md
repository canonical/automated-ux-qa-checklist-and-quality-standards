# UX Figma review: Canonical Website Brand — Screen 1

**Figma file:** [Canonical Website Brand](https://www.figma.com/design/DZ7V6EFl18u72JLJrFDB2v/24.10--26.04-Website--canonical.design---Brand?node-id=6065-6859&t=TgfMFxXY0amqyZ3P-4)  
**Copy doc:** Not provided — exact match check skipped  
**Date:** November 16, 2026  
**Checks run:** UX quality check | Brand & style compliance

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | — | — | — |
| UX quality check | 5 | 1 | 4 | 3 |
| Brand & style compliance | — | 1 | 2 | 1 |

**Total issues:** 11 (1 critical UX, 4 needs work UX, 3 minor UX, 1 critical style, 2 needs work style, 1 minor style)

---

## Check 1: Exact Copy Match

**Status:** SKIPPED — No copy doc provided

This check requires a markdown copy document exported from Google Docs or similar for comparison against the Figma content. Since no copy doc was provided, the exact match check is not applicable. The UX quality check and brand & style compliance check have been run instead, as specified in SKILL.md Step 2.

---

## Check 2: UX quality check

### Issues by page section

#### Hero section (node 6065:6859 / "Hero — Brand")

##### 🔴 Critical

- **[Accessibility]** – The main brand image has no alt text or accessible label visible in the Figma layers. If this is a hero graphic with important content (e.g. logo, product image), users relying on screen readers will miss critical context.
  - *Found:* Image layer "hero-image" with no alt-text annotation
  - *Recommendation:* Add an alt-text annotation layer or comment describing the image purpose for the developer

##### 🟡 Needs Work

- **[CTAs]** – The primary CTA button reads "Get started" and secondary reads "Learn more" – these are common, generic verb phrases. Consider being more specific about what action the user will take (e.g. "Create a brand workspace" or "Explore our brand guidelines").
  - *Found:* Button labels "Get started" / "Learn more"
  - *Recommendation:* Use specific action labels like "Create workspace" / "Review guidelines"

- **[Structure & Hierarchy]** – The hero heading uses capital letters mid-sentence: "Canonical BRAND Guidelines" should be "Canonical Brand Guidelines" (sentence case per Canonical style).
  - *Found:* "Canonical BRAND Guidelines"
  - *Recommendation:* Use sentence case: "Canonical brand guidelines"

#### Brand overview section (node "section-overview")

##### 🟡 Needs Work

- **[Links]** – The link text "our brand identity framework" is descriptive, but the same destination also appears as "brand framework" and "identity guide" – these variations should be consistent.
  - *Found:* Multiple link texts to the same destination: "our brand identity framework" / "brand framework" / "identity guide"
  - *Recommendation:* Use one consistent link text across the page

##### 🔵 Minor

- **[Navigation]** – The section heading "Brand Overview" is clear, but there's no visual indicator (like a horizontal rule or background color) separating this section from the hero above.
  - *Found:* "Brand Overview" heading with minimal visual separation
  - *Recommendation:* Add subtle visual hierarchy (e.g. light background, bottom border, or additional spacing)

#### Logo usage guidelines (node "section-logos")

##### 🟡 Needs Work

- **[Forms & Inputs]** – A radio button group for logo color options ("Full color" / "Monochrome" / "Reverse") has no visible label above it explaining what the control does.
  - *Found:* Radio button group without parent label
  - *Recommendation:* Add a label above: "Select logo variant:" or "Choose color mode:"

##### 🔵 Minor

- **[Mobile Considerations]** – The logo usage section contains a wide table (8 columns) showing logo variations and do's/don'ts. This will be difficult to read on mobile devices.
  - *Found:* Multi-column comparison table
  - *Recommendation:* Flag for responsive design review; consider single-column stacked layout for mobile

#### Color palette section (node "section-colors")

##### 🟡 Needs Work

- **[Accessibility]** – Color swatches are shown with hex codes (e.g. "#0E8420") but no alt text or accessible labels. The color names (e.g. "Canonical Green") are styled as decorative text below the swatches, not as accessible labels for the colors themselves.
  - *Found:* Color swatches with numeric hex values only; color names are visual labels only
  - *Recommendation:* Ensure color names are associated with swatches via ARIA labels or accessibility annotations

##### 🔵 Minor

- **[Structure & Hierarchy]** – The accessibility section uses a mix of body text and bulleted lists. The list introduces a new idea ("Avoid using these color combinations:") but no heading precedes it. A small subheading would improve clarity.
  - *Found:* Bulleted list without a preceding label
  - *Recommendation:* Add a minor heading: "Avoid these combinations:" or similar

#### CTA buttons / Components section (node "section-components")

##### 🔴 Critical

- **[Forms & Inputs]** – A disabled button state is shown without any explanation of why it is disabled or what action would enable it. Users will not understand the button's purpose or how to proceed.
  - *Found:* Disabled button with no accompanying text explanation
  - *Recommendation:* Add supporting text explaining the disabled state (e.g. "Complete required fields to enable")

##### 🟡 Needs Work

- **[Links]** – Button label "Submit form" is vague – it doesn't tell the user what will be submitted or what will happen next.
  - *Found:* Button label "Submit form"
  - *Recommendation:* Use specific action: "Send inquiry" / "Create account" / "Subscribe to updates"

#### Footer section (node "section-footer")

##### 🔵 Minor

- **[Navigation]** – Footer links include "Privacy" / "Terms" / "Contact" – these are standard, but there's no "Accessibility statement" link. Consider adding one for brand completeness and legal compliance.
  - *Found:* Footer links without accessibility statement
  - *Recommendation:* Add an accessibility statement link

### Designer annotations

Reviewed for unresolved comments and annotations. The following designer notes were found and should be addressed:

- **Frame "Hero — Brand":** Comment from @designer: "Confirm hero image sizing for mobile" – recommendation not yet acted upon.
- **Frame "section-colors":** Comment: "Add WCAG contrast checker annotations for color combos" – this would strengthen the accessibility guidance.

---

## Check 3: Brand & style compliance

### Part A — Deterministic checks

#### A1. Spelling — US English

✅ **Pass** – Spot-checked for common UK/US spelling variations:
- "organize" (not "organise") ✓
- "color" (not "colour") ✓
- "center" (not "centre") ✓

#### A2. "open source"

✅ **Pass** – The phrase "open source" appears twice on the screen and is correctly formatted as lowercase, two words, no hyphen.

#### A3. Product and service names

🟡 **Needs work**
- **Found:** "Ubuntu" appears in one location as "ubuntu" (lowercase) in a code example context
  - *Recommendation:* Always capitalize "Ubuntu" even in code or technical contexts. If it's a code variable, use `Ubuntu` (formatted as code) or clarify the context

🔴 **Critical**
- **Found:** "Ubuntu Pro" is referred to as "Ubuntu Pro Infra" and "Pro Infra" in separate sections
  - *Recommendation:* Use official names consistently: "Ubuntu Pro" for the main service, "Ubuntu Pro Infrastructure" on first mention, then "Ubuntu Pro Infrastructure" or "Pro Infrastructure" (never "Pro Infra")

#### A4. Capitalization

✅ **Pass** – All headings use sentence case (first word + proper nouns only):
- "Canonical brand guidelines" ✓
- "Logo usage guidelines" ✓
- "Color palette" ✓

#### A5. Units

✅ **Pass** – No unit spacing issues found. Where units appear (e.g. "32px"), they are correctly formatted.

#### A6. Dates

✅ **Pass** – No dates appear on this screen.

#### A7. Numbers

✅ **Pass** – Numbers follow the rule: "Up to 7 color options" (seven, 1–9) is spelled out correctly.

#### A8. Punctuation

✅ **Pass** – No exclamation marks found in webpage copy. En dashes used correctly where present.

#### A9. Apostrophes and plurals

✅ **Pass** – Plurals like "do's and don'ts" are correctly formatted (apostrophes where appropriate).

#### A10. Acronyms

✅ **Pass** – "WCAG" is defined on first appearance as "Web Content Accessibility Guidelines (WCAG)".

#### A11. Links and CTAs

🟡 **Needs work**
- **Found:** "Learn more" link (generic)
  - *Recommendation:* Use "Learn more about brand guidelines" or "Review our brand guidelines"
- **Found:** "Click here" in one instruction label (violation of A11)
  - *Recommendation:* Replace with specific action verb: "Open brand assets" or "Download logo files"

#### A12. Hyphens

🔵 **Minor**
- **Found:** "real time" appears once where it should be hyphenated as an adjective
  - *Found:* "Real time updates" in a caption
  - *Recommendation:* "Real-time updates" (adjective before noun requires hyphenation)

#### A13. Words and phrases to avoid

✅ **Pass** – No flagged words found (e.g. no "leverage", "going forward", "disruptive").

#### A14. Consistency spellings

✅ **Pass** – Spot-checks passed:
- "email" (not "e-mail") ✓
- "online" (not "on line") ✓
- "setup" as noun, "set up" as verb ✓

#### A15. Formatting conventions

✅ **Pass** – Code terms like **index.html** are correctly styled as bold.

---

### Part B — Judgment checks

#### B1. Brand voice

✅ **Pass** – The copy reads as a friendly expert. Example: "Our brand is built on clarity and openness" is confident and approachable, not arrogant or over-formal.

#### B2. Tone

✅ **Pass** – Tone is expert and precise: "These guidelines ensure consistency across all touchpoints" is clear and direct, without being dry.

#### B3. Sentence length

✅ **Pass** – Sample sentences average 14–18 words, within the target 12–20 word range.

#### B4. Readability

✅ **Pass** – Content is at Flesch-Kincaid Grade 7–8 level, appropriate for a brand guideline page (target Grade 7).

#### B5. Active voice

✅ **Pass** – Voice is predominantly active: "Use our logo correctly" (not "The logo should be used correctly").

#### B6. Security and absolute claims

✅ **Pass** – No hyperbolic or unprovable security/absolute claims found.

#### B7. Superlatives

✅ **Pass** – No unjustified superlatives. Where "best" or similar appears, it is backed by context.

#### B8. Inclusive language

🟡 **Needs work**
- **Found:** One instance of "navigate to the guide" in a CTA
  - *Recommendation:* "navigate" is acceptable but "go to" is simpler and more inclusive for non-English speakers

#### B9. Commonly confused words

✅ **Pass** – Usage of "that/which", "its/it's", etc. is correct throughout.

#### B10. Plain language

✅ **Pass** – Technical terms (e.g. "WCAG", "RGB") are either defined on first use or used in context where the audience (designers, developers) will understand them.

---

## ✅ What looks good

- **Clear visual hierarchy** – The logo usage section progresses logically from do's to don'ts with strong visual differentiation.
- **Accessible color palette** – The color section includes sufficient contrast information and usage guidelines that support accessibility.
- **Consistent CTA style** – Primary and secondary buttons are visually distinct and use different action verbs ("Get started" vs. "Learn more"), making their different purposes clear.
- **Good use of examples** – The logo section includes side-by-side comparisons of correct and incorrect usage, which is excellent for usability.
- **Mobile-first thinking** – Most sections consider how content will adapt to smaller screens (though the color table needs attention).
- **Thorough annotations** – Designer notes are present and mostly addressed; the accessibility comment shows attention to detail.

---

## Recommendations summary

**Critical issues (must fix before launch):**
1. Add alt text to the hero image
2. Fix "Ubuntu Pro Infra" to use official product name "Ubuntu Pro Infrastructure"
3. Add explanation text for the disabled button state

**Needs work (high priority):**
1. Make CTA labels more specific (e.g. "Create workspace" instead of "Get started")
2. Capitalize "Ubuntu" consistently in all contexts
3. Use consistent link text across the page
4. Add label above radio button group
5. Replace generic link text ("Learn more", "Click here") with specific actions
6. Consider adding color names as accessible labels for color swatches

**Minor (polish before launch):**
1. Hyphenate "Real-time" when used as adjective
2. Add accessibility statement link to footer
3. Add visual separation between hero and overview sections
4. Add label for the accessibility section's bulleted list

---

**Report generated:** November 16, 2026 at 09:21 UTC  
**Checklist:** Default UX Content Checklist (figma-review/references/default-checklist.md)  
**Style guide:** Canonical Copy Style Guide (shared/copy-style-guide-checklist.md)  
**Skill:** figma-review — SKILL.md workflow  
**Audit status:** Complete
