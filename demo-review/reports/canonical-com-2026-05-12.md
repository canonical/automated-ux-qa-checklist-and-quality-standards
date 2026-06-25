# UX content audit report — live page

**URL:** https://canonical.com
**Date:** 2026-05-12
**Note:** This page uses JavaScript-powered tab components. Only content present in the initial static HTML was captured. JS-rendered states (tab panel switching, dynamic content) could not be audited and should be checked manually.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Structure & hierarchy | 3 | 1 | 0 | 0 |
| CTAs | 6 | 0 | 1 | 4 |
| Links | 6 | 0 | 1 | 3 |
| Accessibility | 5 | 0 | 2 | 0 |
| Navigation | 3 | 0 | 0 | 0 |
| Mobile considerations | — | 0 | 1 | 0 |

**Total issues:** 13 (1 critical, 5 needs work, 7 minor)

---

## UX quality check

### Structure & hierarchy

#### 🔴 Critical
- **Section: Hero** — No H1 is present in the extracted page content. The hero tagline ("Simple, cost-effective, supported – expand the Ubuntu philosophy to every layer of your enterprise stack.") appears as plain text with no heading role. If this is intentional (decorative paragraph above a visual), there is likely no H1 on the page at all, which is a significant accessibility and SEO issue.
  - *Found:* Untagged text — "Simple, cost-effective, supported – expand the Ubuntu philosophy to every layer of your enterprise stack."
  - *Recommendation:* Confirm whether an H1 is present in the rendered DOM. If not, assign H1 to the primary page headline — either the hero tagline or the section heading "Innovate on your own terms".

#### ✅ Passes

- **Heading flow** — The visible heading sequence (H2 → H3 throughout) is logical and consistent. No skipped levels observed in the extracted content.
- **Section headings are meaningful** — "Innovate on your own terms", "Do more with trusted open source", "Accelerate innovation on any platform", and "News and insights from the source" are descriptive and not placeholder text.
- **Lists have contextual intro** — The tab navigation links ("Start with Ubuntu", "Take control of your infrastructure", etc.) are preceded by an H2 and intro paragraph.

---

### CTAs

#### 🟡 Needs Work
- **Section: Case studies — Lucid** — "Get Lucid's view" is semi-opaque as a standalone link. "Lucid" is a company name that may not be recognised by all visitors; out of context (e.g., for a screen reader listing links), it gives no signal about what the content is or why to click.
  - *Found:* "Get Lucid's view" → `/case-study/lucid-aws-fedramp-compliance-case-study`
  - *Recommendation:* "Read the Lucid case study" or "See how Lucid achieved FedRAMP compliance" — descriptive and navigable without surrounding context.

#### 🔵 Minor
- **Section: Cloud-native tab panel** — "Break the mold – build composable" leads with a marketing idiom rather than a clear action. A visitor scanning CTAs may not immediately understand what they're clicking into.
  - *Found:* "Break the mold – build composable" → `/solutions/cloud-native-development`
  - *Recommendation:* Something like "Explore composable app development" or "See our cloud-native approach" keeps the energy while being navigable.

- **Section: Case studies — ESA** — "Launch into the details" is a playful astronomy pun, but as a CTA it communicates neither the content type nor what the user will find.
  - *Found:* "Launch into the details" → `/case-study/esa`
  - *Recommendation:* "Read the ESA case study" is clearer, or keep the pun and add context: "Launch into the ESA case study".

- **Section: Case studies — SBI BITS** — "Consult the story" is an unusual verb. "Consult" implies advisory rather than reading.
  - *Found:* "Consult the story" → `/case-study/sbi-bits`
  - *Recommendation:* "Read the SBI BITS story" or "Read the case study".

- **Section: Case studies — Grundium** — "Inspect the case study" is technically correct but slightly clinical; it creates a tone mismatch with the warmer storytelling copy above it.
  - *Found:* "Inspect the case study" → `/case-study/grundium-ubuntu-pro-for-devices`
  - *Recommendation:* "Read the Grundium case study" for consistency with other case study CTAs.

#### ✅ Passes
- "Why innovators prefer Ubuntu" — specific and value-focused ✓
- "Cloudify your data center" — action-clear and destination-clear ✓
- "Simplify database management" — direct and descriptive ✓
- "Race ahead with AI" — energetic but the destination (/solutions/ai) is unambiguous ✓
- "Speed up your IoT journey" — clear ✓
- "Learn how BT unlocked scalability" — specific outcome stated ✓

---

### Links

#### 🟡 Needs Work
- **Section: Case studies — ESA** — "Launch into the details" also fails as link text. Without surrounding context, a user navigating by links cannot determine what "the details" refers to.
  - *Found:* "Launch into the details" → `/case-study/esa`
  - *Recommendation:* "Read the ESA case study" (see CTA note above — same element).

#### 🔵 Minor
- **Section: Case studies** — CTA links are duplicated within each case study card (same text, same URL appearing twice — once as an image link, once as text). If the image links have empty alt text, the duplication is non-harmful, but should be confirmed so screen readers don't announce the destination twice.
  - *Recommendation:* Verify image links in case study cards have `alt=""` to mark them as decorative. If not, they may announce an uninformative link to assistive technology.

- **Section: Cloud-native tab panel** — "Break the mold – build composable" (see CTA section) also applies here as vague link text.

- **Section: Case studies — SBI BITS** — "Consult the story" (see CTA section) is an unusual standalone link label.

#### ✅ Passes
- Most feature section links are descriptive and make sense out of context.
- No same-text-different-destination issues observed on the visible page.
- No entire sentences are hyperlinked.

---

### Accessibility

#### 🟡 Needs Work
- **Hero images** — The two hero images (desktop and mobile variants) have no alt text in the extracted content (`![](…)`). If these are decorative, they should have `alt=""` explicitly in the HTML. If they carry meaning (illustrative content relevant to the tagline), they need descriptive alt text.
  - *Found:* Two `<img>` elements with no alt text at the top of the page.
  - *Recommendation:* Confirm in source: if decorative, add `alt=""`. If illustrative, describe the content (e.g., "An engineer reviewing system architecture diagrams").

- **Feature section images** — Each of the five tab panels contains a pair of responsive images (desktop and mobile) with no alt text. These illustrate the product areas (Ubuntu OS, infrastructure, cloud-native, data/AI, IoT). It is unclear whether they are purely decorative or carry informational value.
  - *Found:* Ten `<img>` elements across the tab panels with no alt attributes.
  - *Recommendation:* Audit each image against its surrounding text. If the image adds context not described in the text, add descriptive alt text. If purely illustrative, add `alt=""`.

#### ✅ Passes
- Customer company logos all have descriptive alt text (e.g., `alt="BT Group"`, `alt="ESA"`) ✓
- Link text is generally descriptive — no "click here" or "read more" as standalone labels ✓
- No instructions relying on visual position observed ✓

---

### Navigation

#### ✅ Passes
- Tab navigation labels are clear and consistent in phrasing.
- No breadcrumbs expected on a homepage — not applicable.
- No "you are here" indicator needed on the homepage — not applicable.

---

### Mobile considerations

#### 🟡 Flag for review
- **Tab navigation** — The five tab navigation items include long labels such as "Take control of your infrastructure" and "Build apps at speed and stay secure". On small screens, these may wrap awkwardly, be truncated, or create a cramped tap target if rendered as a horizontal list.
  - *Recommendation:* Test tab navigation at 375px viewport. Consider shortened labels or a different navigation pattern for mobile (e.g., a select dropdown or vertical stack).

---

## ✅ What looks good

- **Strong, specific CTAs in the feature section** — "Why innovators prefer Ubuntu", "Cloudify your data center", "Speed up your IoT journey" and similar links are specific, value-focused, and navigable without context.
- **Customer logos have meaningful alt text** — All five company logos correctly describe the company name, which is the right level of detail for logo images.
- **Attributed quotes** — Each customer quote is attributed with full name, title, and company, adding credibility and specificity.
- **Logical content flow** — The page moves clearly from value proposition → product capabilities → social proof → ecosystem → news. The narrative arc is purposeful.
- **Consistent heading structure** — The visible H2 → H3 hierarchy is clean and does not skip levels.
- **No vague or placeholder copy** — All headings and body copy appear to be production-ready. No lorem ipsum or "[placeholder]" text found.

---

## Recommended priority order

1. **Fix 🔴 Critical:** Confirm whether an H1 exists in the rendered DOM and add one if missing.
2. **Address 🟡 Needs Work:** Resolve image alt text gaps (audit all `<img>` elements lacking alt attributes); rewrite "Get Lucid's view" and "Launch into the details" for clarity; flag tab navigation for mobile testing.
3. **Polish 🔵 Minor:** Standardise case study CTA verbs ("Read the [company] case study"); review "Break the mold – build composable" for clarity; verify image link duplication in case study cards.

---

## 🔲 Manual checks for reviewer

- [ ] **H1 in DOM** — Inspect the rendered page source to confirm whether an H1 element is present. WebFetch may not have captured it if it is set dynamically or visually styled to look like hero text.
- [ ] **Image alt attributes** — Inspect source for all `<img>` elements without visible alt text. Confirm `alt=""` is present for decorative images; add descriptive alt text for informational ones.
- [ ] **JS-rendered content** — Tab panel content may differ when tabs are activated via JavaScript. Click each tab and audit copy for new CTAs, headings, or text not visible in static HTML.
- [ ] **Authenticated states** — Not applicable for this public homepage.
- [ ] **Keyboard navigation** — Tab through the page to confirm correct focus order, especially within the tab component which requires keyboard-accessible tab switching (arrow keys).
- [ ] **Mobile view** — Resize to 375px and check tab navigation, hero tagline readability, and long CTA wrapping.
