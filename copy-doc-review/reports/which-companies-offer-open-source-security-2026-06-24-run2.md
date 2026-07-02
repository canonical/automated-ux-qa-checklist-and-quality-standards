# UX content audit report – copy doc

**Document:** Which companies offer open source security?
**Date:** 2026-06-24 (run 2 – with updated acronym evidence requirement)

---

## Summary
| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 1 | 2 | 5 | 3 | 1 | 3 |

**Total issues:** 10 (two critical, five needs work, three minor) · **Needs review:** 1 · **N/A sections:** Forms and inputs; Navigation; Interactive states

---

## Issues by page section

### Metadata

**[Character limits] 🟡 Needs Work – Page description exceeds the limit**
Evidence: Page description is "Understand which companies offer open source security, covering key market areas like supply chain, vulnerability management, and cloud security, and what to look for in a provider."
This is **181 characters**, which exceeds the **160-character** limit.

**[Links] 🔴 Critical – Page URL contains a literal space**
Evidence: `canonical.com/knowledge/security-and-compliance/which-companies-offer-open source-security`
The space in "open source-security" would create an invalid URL and is a publishing blocker.

### Hero

**[Tone and clarity] 🔵 Minor – Opening copy is wordy for an executive exploration page**
Evidence: "Countless different companies offer support and security maintenance for open source software, depending on the region, use case, type of technology, and other factors."
This sentence is long and broad. A tighter opening would improve scanability for executive readers.

### Text section 1 – What are the different market areas of open source security?

**[Tone and clarity] 🔵 Minor – SaaS capitalisation is inconsistent**
Evidence: intro list uses "SAAS security" while the subheading uses "SaaS Security Posture Management (SSPM)".
Use one form consistently.

**[Tone and clarity] 🟡 Needs Work – Some acronyms are not expanded for an executive audience**
Evidence from this section: "CVE registry" and "DORA" are used without expansion.
Note: the document correctly expands many acronyms here – including SCA, SAST, CNAPP, WAAP, SSPM – so this is a partial gap, not a blanket failure.

### Text section 2 – How do you choose the right open source security provider?

**[Tone and clarity] 🔵 Minor – CI/CD is used without expansion**
Evidence: "CI/CD pipelines (GitHub Actions, GitLab CI)"
CI/CD is common industry language, so this is minor, but expanding it once would better suit the stated audience.

### Text section 4 – Detailed Canonical solutions

**[Links] 🔴 Critical – Landscape link is malformed**
Evidence: "Landscape" → `ubuntu.com/landscape=Ng3xdrG1EuY`
Using `=` directly after the path makes this URL malformed and likely broken.

**[Tone and clarity] 🟡 Needs Work – Several acronyms are not expanded in solution detail**
Evidence: "OCI-compliant container images", "LTS-backed images", "FIPS-certified cryptographic modules", "CIS Benchmarks", "STIG hardening profiles", "FedRAMP", and "CSA" are all used without expansion.
For an executive exploration-stage audience, these terms should be expanded on first use.

**[Links] 🟡 Needs Work – One link uses http rather than https**
Evidence: "Learn how Ubuntu Pro brings seamless security to open source >" → ubuntu.com/pro/why-pro (http, not https, in source).
Even if it redirects, the source link should use HTTPS.

**[Links / Completeness] 🟡 Needs Work – CSA is mentioned but not explained or linked**
Evidence: "CSA" appears as a standalone reference without expansion (Cloud Security Alliance) or a link.
Readers may not know what it means or where to go next.

### Learn more section

**[CTAs] 🟡 Needs Work – "Get in touch" is too vague out of context**
Evidence: CTA text is "Get in touch".
This does not tell the reader what will happen next. A more specific CTA (e.g. "Talk to our security team") would be clearer.

---

## ❓ Needs review

**[Links] ❓ Needs Review – Tracking parameters appear in linked URLs**
Evidence: "Get the latest insights into the state of open source security" uses a `_gl` tracking parameter, and "Download our open source security datasheet" also includes `_gl` tracking.
These may be intentional marketing links, but they should be checked to confirm they are the intended canonical destinations.

## ⬜ Not applicable

- **Forms and inputs** – knowledge hub article, no form present
- **Navigation** – no nav changes specified
- **Interactive states** – static marketing page

## ✅ What looks good

- Page title "Which companies offer open source security?" fits the 60-character limit (46 characters)
- Breadcrumb fits the 45-character limit (44 characters)
- Many acronyms are correctly expanded on first use – including **SCA, SAST, CNAPP, WAAP, SSPM, ESM, CRA, MIR,** and **MAAS**
- Image and video alt text are present
- Image asset is hosted on `assets.ubuntu.com`
- Content structure is clear – market areas, evaluation criteria, and Canonical solutions flow logically top to bottom
