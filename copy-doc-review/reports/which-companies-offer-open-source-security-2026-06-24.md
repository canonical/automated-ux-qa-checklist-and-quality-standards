# UX content audit report – copy doc

**Document:** Which companies offer open source security?  
**Date:** 2026-06-24

---

## Summary
| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | – | two | three | four | one | two |

**Total issues:** nine (two critical, three needs work, four minor) · **Needs review:** one · **N/A sections:** Forms and inputs; interactive states in Completeness

---

## Issues by page section

### Metadata
#### 🔴 Critical
- **[Links]** The URL slug contains a space: `canonical.com/knowledge/security-and-compliance/which-companies-offer-open source-security`. This is a publishing blocker and risks a broken or invalid URL.

#### 🟡 Needs Work
- **[Character limits]** The page description is **181 characters**, exceeding the **160-character** limit. It is likely to truncate in search results.

#### 🔵 Minor
- **[Tone and clarity]** The page description is very dense for an executive audience – it stacks several concepts in one sentence, which reduces scannability.

---

### Hero
#### 🟡 Needs Work
- **[Tone and clarity]** The hero body is too long and abstract. The opening paragraph packs in multiple qualifiers and concepts, making the value proposition harder to absorb quickly.

#### 🔵 Minor
- **[CTAs]** "Learn more about" is weak CTA phrasing. A more direct, value-led phrase would create a stronger next step for executives.

---

### Text section one – "What are the different market areas of open source security?"
#### 🟡 Needs Work
- **[Accessibility / Tone and clarity]** Acronyms are not consistently expanded on first use. Terms such as SCA, SAST, CVE, CNAPP, WAAP, OCI, FIPS, CIS, STIG, DORA, CRA, OVAL, OSV, VEX, and ESM are likely too specialized for a broad executive audience without expansion or brief explanation.

#### 🔵 Minor
- **[Structure and hierarchy]** Inconsistent capitalization of SaaS – the intro list uses "SAAS" while the subsection heading uses "SaaS." This looks unpolished and may reduce trust.

---

### Text section two – "How do you choose the right open source security provider?"
#### 🔵 Minor
- **[Tone and clarity]** The section is conceptually strong, but the copy remains quite dense. Several headings and explanations assume technical familiarity that may be too high for executives in an exploration-stage knowledge hub.

---

### Text section four – detailed Canonical solutions
#### 🔴 Critical
- **[Links]** The Landscape link is malformed: `ubuntu.com/landscape=Ng3xdrG1EuY` is not a valid URL structure and is likely broken. This must be corrected before publishing.

---

### Learn more section
#### 🔵 Minor (severity override – contextual link)
- **[CTAs]** "Get in touch" is too vague. It does not set expectations about what happens next or why an executive should click.

---

## ❓ Needs review
- **[Links]** `_gl` tracking parameters appear on two linked URLs (the "state of open source security" link and the datasheet link). Confirm whether these should remain in the source doc or be cleaned before publishing.

## ⬜ Not applicable
- **Forms and inputs** – N/A for a knowledge hub article.
- **Interactive states in Completeness** – N/A for this page type.

## ✅ What looks good
- The topic is relevant and well aligned to executive-stage discovery intent.
- The overall content flow is logical – market landscape first, buying criteria second, Canonical solution mapping after that.
- Section headings are descriptive and easy to follow.
- CTA links are generally contextual, which supports scan reading.
- Image and video supporting content are present with alt text.
- The breadcrumb is within the 45-character limit at **44 characters**.
- The page title is within the 60-character limit at **46 characters**.
