# UX content audit report

**Figma file:** ubuntu.com-download---Sites / `/download/wsl` (node 3734:7839)
**Copy doc:** `_download_wsl - _Get Ubuntu on WSL_.md`
**Date:** 2026-04-21
**Checks run:** Both (copy doc check + UX quality check)

> **Note:** The copy doc contains Google Docs suggesting mode artifacts — unresolved track changes exported as concatenated text (e.g. `Ubuntu 26.0424.04 LTS`, `[Press Release ›Release notes ›]`). Matching has been made lenient. Apparent concatenation artifacts are not flagged as copy errors. Where the Figma string matches either variant, it is treated as a match.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Copy doc check | — | 0 | 3 | 2 |
| UX quality check | — | 0 | 3 | 4 |

**Total issues:** 12 (0 critical, 6 needs work, 4 minor, 2 unverified)

---

## Check 1: Exact copy match

### 🟡 Needs Work — Missing from Figma / version ambiguity

- **Frame: Tab section — H2 heading**
  - Figma: `"Ubuntu 24.04 LTS"`
  - Copy doc: `"Ubuntu 26.0424.04 LTS"` *(suggesting mode artifact — the version number is being updated from 24.04 to 26.04)*
  - The Figma still shows 24.04. Clarify with the page owner whether this design is targeting 24.04 or 26.04 before publishing. The download URLs in the copy doc still reference `ubuntu-24.04.4-wsl-amd64.wsl` — so either the version or the URLs need updating.

- **Frame: Tab section — "What's new" tab body text**
  - Figma: `"An updated set of language toolchains and compilers."`
  - Copy doc: `"An updated set of language toolchains and compilers. Rust 1.78, .NET 8 and OpenJDK 21 with TCK certification in addition to other toolchain upgrades"`
  - The second sentence is absent from the Figma. Developers will use the copy doc version, which is more detailed — the design should reflect this.

- **Frame: Blog — section heading**
  - Figma: `"Latest from our blog"` — rendered as a plain small-caps category label, no link, no chevron
  - Copy doc: `"Latest from our blog ›"` — formatted as a linked heading pointing to the blog tag page
  - The copy doc intent is a linked section heading. The Figma does not include the link or `›`. Developer will follow the copy doc, creating a discrepancy with the design.

### 🔵 Minor — Capitalisation / punctuation

- **Frame: Tab section — "What's new" tab, first link**
  - Figma: `"Press release ›"` (lowercase r)
  - Copy doc: `"Press Release ›"` (capital R)
  - Low risk — developer uses copy doc. Update Figma for accuracy.

- **Frame: Tab section — "Release notes ›" link URL**
  - Figma links to: `https://discourse.ubuntu.com/t/noble-numbat-release-notes/39890`
  - Copy doc specifies: `https://documentation.ubuntu.com/release-notes/26.04/`
  - Developer will use the copy doc URL. Update Figma to match.

### ⚠️ Unverified — Tab content not visible

- **Frame: Tab section — "System requirements" and "How to install" tabs**
  - Only the "What's new" tab was active in the Figma. The content for the other two tabs could not be verified against the copy doc.
  - Copy doc content for these tabs:
    - **System requirements:** "Windows 11 (recommended) or Windows 10 with minimum version 21H2 on a physical machine" + link "Detailed requirements ›"
    - **How to install:** "To install, you can download and double-click the `.wsl` image, or open the PowerShell terminal and run `wsl --install`" + link "Detailed installation steps ›"
  - Recommend opening the other tab states in Figma and verifying.

---

## Check 2: UX quality check

### CTAs

#### 🟡 Needs Work
- **Frame: Tab section — Intel/AMD and ARM Download buttons**
  - Both green primary buttons are labelled `"Download"` with no further differentiation in the button text itself. Visual context comes from the architecture subheadings above (`"Intel or AMD 64-bit architecture"` and `"ARM 64-bit architecture"`), but the buttons are not self-labelling.
  - Screen reader users navigating by button will hear "Download, Download" with no way to distinguish. Implementation should use `aria-label` (e.g. "Download Ubuntu for Intel or AMD 64-bit") or reword the button labels to be descriptive.
  - *Found:* Two buttons: `"Download"` / `"Download"` | *Recommendation:* `"Download for Intel/AMD"` and `"Download for ARM"`, or add `aria-label` in code.

### Links

#### 🟡 Needs Work
- **Frame: Basic section — bullet 2, inline link**
  - *Found:* `"Estate monitoring and management of WSL instances"` — only `"monitoring and management"` is hyperlinked.
  - Mid-sentence partial linking is ambiguous when read out of context (e.g. in a screen reader link list, the user hears "monitoring and management" with no surrounding context).
  - *Recommendation:* Link the full phrase "Estate monitoring and management of WSL instances", or restructure as a standalone link below the bullet.

### Accessibility

#### 🟡 Needs Work
- **Frame: Blog — all three blog post images**
  - All three images have `alt=""` (empty alt text). If the blog images are meaningful (e.g. editorial header images), they need descriptive alt text.
  - The copy doc specifies `[Latest 3 posts tag: ubuntu-wsl]` — these images are dynamically loaded. Engineering must ensure alt text is passed through from the CMS or blog platform for each post.
  - *Recommendation:* Add a note to the implementation ticket to verify alt text is populated dynamically. Do not launch with all-empty alt on editorial images.

#### 🔵 Minor
- **Frame: Equal heights — product logo images (Landscape, LXD, Juju, Multipass)**
  - All four logos use `alt=""`. These are decorative since each product name appears as a text heading below the image, so empty alt is acceptable per WCAG 2.1 (decorative images).
  - However, if any logo is also used as a link target or interactive element, it must have a text alternative. Verify in implementation.

### Structure & hierarchy

#### 🔵 Minor
- **Frame: Tab section — "System requirements " tab label**
  - The tab label has a trailing space: `"System requirements "`. Remove before implementation.

### Mobile considerations

#### 🔵 Flag for review
- **Frame: Tab section** — The 50/50 layout with side-by-side architecture download rows and tabs below will require careful mobile handling. Two download rows with buttons and file size labels may stack awkwardly on small screens.

#### 🔵 Flag for review
- **Frame: Equal heights** — The 4-column Landscape/LXD/Juju/Multipass grid needs to be verified at tablet (2-col) and mobile (1-col) breakpoints. The equal-heights treatment may produce very tall cards at narrow widths.

---

## ✅ What looks good

- **Heading hierarchy** is clean throughout: H1 ("Get Ubuntu on WSL") → H2 section headings, no levels skipped.
- **Ubuntu Pro section** is well-structured: a clear value proposition sentence, a tight bulleted list of benefits, and two clearly differentiated CTAs ("Download the Ubuntu Pro for WSL app" + "Learn more about Ubuntu on WSL for enterprises ›").
- **Resources section** is cleanly categorised with DOCUMENTATION and COMMUNITY labels, descriptive link titles, and supporting body copy for each resource — exactly as the copy doc specifies.
- **All "More from Canonical" card copy and links** match the copy doc precisely with no issues.
- **No forms** on this page — forms, inputs, error states, and success states are N/A and cleanly absent.

---

## Recommended priority order

1. **Clarify version number** — confirm whether this is a 24.04 or 26.04 page and update heading and download URLs consistently (copy doc, Figma, and implementation).
2. **Restore missing "What's new" body text** — add the toolchain detail sentence back to the Figma.
3. **Fix "Latest from our blog ›" heading** — make it a linked heading with chevron as the copy doc intends.
4. **Address Download button accessibility** — add descriptive labels or `aria-label` for the architecture-specific Download buttons.
5. **Fix inline link scope** — extend "monitoring and management" link to cover the full bullet phrase.
6. **Ensure blog image alt text is populated** by the CMS dynamically.
7. **Polish minor items** — Press release capitalisation, Release notes URL, trailing space on tab label.
8. **Verify hidden tab content** — open and check "System requirements" and "How to install" tab states against the copy doc.

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** — open the live ubuntu.com/download/wsl page and confirm only the intended sections have changed
- [ ] **Tab keyboard navigation** — tab through the What's new / System requirements / How to install tabs to confirm correct focus order and keyboard activation
- [ ] **Download button screen reader test** — verify that the two Download buttons are distinguishable when navigated by screen reader
