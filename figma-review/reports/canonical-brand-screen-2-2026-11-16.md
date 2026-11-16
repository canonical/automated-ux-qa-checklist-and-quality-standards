# UX Figma review: Canonical Website Brand — Screen 2

**Figma file:** [Canonical Website Brand](https://www.figma.com/design/DZ7V6EFl18u72JLJrFDB2v/24.10--26.04-Website--canonical.design---Brand?node-id=6065-7327&t=TgfMFxXY0amqyZ3P-4)  
**Copy doc:** Not provided — exact match check skipped  
**Date:** November 16, 2026  
**Checks run:** UX quality check | Brand & style compliance

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | — | — | — |
| UX quality check | 4 | 2 | 3 | 2 |
| Brand & style compliance | — | 1 | 1 | 1 |

**Total issues:** 10 (2 critical UX, 3 needs work UX, 2 minor UX, 1 critical style, 1 needs work style, 1 minor style)

---

## Check 1: Exact Copy Match

**Status:** SKIPPED — No copy doc provided

This check requires a markdown copy document exported from Google Docs or similar for comparison against the Figma content. Since no copy doc was provided, the exact match check is not applicable. The UX quality check and brand & style compliance check have been run instead, as specified in SKILL.md Step 2.

---

## Check 2: UX quality check

### Issues by page section

#### Hero section (node 6065:7327 / "Hero — Brand guidelines")

##### 🔴 Critical

- **[Accessibility]** – The main hero illustration has no alt text visible in layer annotations. This is a branded visual with editorial importance (brand guidelines context) that should have descriptive alt text for screen reader users.
  - *Found:* Illustration layer "hero-graphic" with no alt-text annotation
  - *Recommendation:* Add an alt-text annotation: "Illustration showing Canonical brand colors and design elements in context"

##### 🟡 Needs Work

- **[CTAs]** – The main CTA reads "Download brand guidelines" (specific action) which is good, but the secondary button is "Contact us" – this is generic and unclear what the contact is about from context alone.
  - *Found:* Secondary CTA button: "Contact us"
  - *Recommendation:* Use context-specific text: "Contact our brand team" or "Request brand support"

#### Typography section (node "section-typography")

##### 🔴 Critical

- **[Forms & Inputs]** – A font family selector dropdown shows options ("Display", "Heading", "Body", "Code") but has no visible label above explaining what this control does. The purpose is unclear without additional context.
  - *Found:* Dropdown menu without parent label
  - *Recommendation:* Add a label: "Select font category:" or "Choose typeface style:"

##### 🟡 Needs Work

- **[Accessibility]** – Font size examples are shown with pixel values (e.g. "24px", "18px") but no description of their intended use or hierarchy role (e.g. "Display — Large headings" vs "Body — Paragraph text").
  - *Found:* Font sizes shown numerically without semantic labels
  - *Recommendation:* Pair each size with its use case: "Display (24px) – for page titles" / "Body (16px) – for paragraph text"

#### Icon library section (node "section-icons")

##### 🔵 Minor

- **[Navigation]** – The icon library is presented as a large grid. No section heading precedes it, and no search or categorization UI is visible. Users may struggle to find specific icons in a long list.
  - *Found:* Icon grid without heading or filtering UI
  - *Recommendation:* Add a heading "Icon library" or "Available icons" and consider adding category filters if many icons are present

#### Button states and patterns (node "section-components")

##### 🟡 Needs Work

- **[Structure & Hierarchy]** – Three button states are shown (default, hover, active) but they're arranged horizontally without labels. It's unclear which state is which without color or visual indicators being explained.
  - *Found:* Button state variations with no state labels
  - *Recommendation:* Label each state clearly: "Default state", "Hover state", "Active state" or use annotations

##### 🔵 Minor

- **[Mobile Considerations]** – A button component example shows with a 48px height for desktop. No note about mobile touch target sizing (recommended 44–48px minimum). Should flag for mobile design review.
  - *Found:* Button sizing shown for desktop only
  - *Recommendation:* Add annotation confirming 44–48px minimum for mobile touch targets

#### Shadow and elevation patterns (node "section-shadows")

##### 🔴 Critical

- **[Accessibility]** – Shadow and elevation are used to show depth, but no alternative visual or textual cues are provided for users who may not perceive color or shadow depth (e.g. colorblind or low vision users). The layers appear to show only visual styling without semantic meaning.
  - *Found:* Elevation shown via shadow only
  - *Recommendation:* Document the shadow/elevation purpose in accompanying text or annotations: "Shadows indicate interactive states" or "Use elevation to show component priority"

### Designer annotations

Reviewed for unresolved comments and annotations:

- **Frame "section-typography":** Comment from designer: "Confirm font weights match production" – action pending
- **Frame "section-icons":** Comment: "Icon sizes vary — verify against design system spec" – needs review

---

## Check 3: Brand & style compliance

### Part A — Deterministic checks

#### A1. Spelling — US English

✅ **Pass** – Spot-checked for common UK/US spelling variations:
- "customize" (not "customise") ✓
- "organize" (not "organise") ✓
- "center" (not "centre") ✓

#### A2. "open source"

✅ **Pass** – The phrase "open source" does not appear on this screen.

#### A3. Product and service names

🔴 **Critical**
- **Found:** "Ubuntu" appears in one instance as "ubuntu mono" (lowercase "ubuntu") in the typography section
  - *Recommendation:* Always capitalize "Ubuntu" even when referencing font names. Use "Ubuntu Mono" (product name) or `ubuntu-mono` (code/CSS context, in code formatting)

#### A4. Capitalization and sentence case

🟡 **Needs work**
- **Found:** Section heading "BUTTON STATES AND PATTERNS" uses all caps
  - *Recommendation:* Use title case or sentence case: "Button states and patterns" or "Button states & patterns"

#### A5. Punctuation and dashes

🔵 **Minor**
- **Found:** Tooltips and inline notes use inconsistent punctuation. Some end with periods, others do not.
  - *Recommendation:* Apply consistent punctuation: all tooltips and UI copy either end with a period or none do (Canonical style generally omits periods in UI microcopy)

### Part B — Judgment checks

✅ **Pass** – Voice and tone checks:
- Copy is clear, direct, and actionable
- No superlatives or unproven claims detected
- Language is inclusive and jargon-free

---

## ✅ What looks good

- **Typography guidance** – The font pairing examples (Display + Body) are well-structured and show clear visual hierarchy
- **Component consistency** – Button, input, and form element styles follow a coherent visual pattern
- **Color usage** – The color palette demonstration includes practical examples of color combinations in context
- **Icon library** – A comprehensive, well-organized set of icons suitable for a modern design system
- **Accessibility awareness** – Several frames include notes about WCAG compliance and contrast ratios, showing attention to inclusive design
- **Developer handoff** – Code snippet annotations (font sizes, shadow values, spacing units) help engineering implementation

---

## Recommendations for next review

1. Add full alt text annotations to all illustrations and graphics before handoff to development
2. Create a typography legend pairing font sizes with semantic roles (Display, Heading, Body, Caption)
3. Label button states explicitly (Default, Hover, Active, Disabled) with annotations
4. Add mobile design considerations throughout (touch targets, responsive spacing)
5. Document the shadow/elevation system semantically (what does each level mean?)
