# UX content audit report – copy doc

**Document:** Knowledge hub – How do you manage CVEs in Ubuntu?
**Date:** July 3, 2026
**Page type:** Knowledge hub article
**Target audience:** Executives
**Note:** This is a knowledge hub article, not a standard product/service page. Character limits for the knowledge hub template differ from the standard webpage template – the text section is long-form by design. Checks are adapted accordingly.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 16 | 3 | 7 | 6 | 2 | 2 |

**Total issues:** 16 (three critical, seven needs work, six minor) · **Needs review:** two · **N/A sections:** Forms and inputs – knowledge hub article; Completeness (interactive states) – static article

---

## Issues by page section

### Metadata

#### 🔴 Critical
- **[Completeness]** – The "Approvals" field still contains the placeholder "Choose" instead of a named approver or approval status.
  - *Found:* "Please indicate approvals needed before the page goes into development: Choose"
  - *Recommendation:* Specify the required approvers before this doc goes to design.

- **[Completeness]** – The og:Image field is still a placeholder. No thumbnail image has been provided.
  - *Found:* "Please include a link to the image you would like as the page thumbnail."
  - *Recommendation:* Add a link to the desired social sharing thumbnail image.

#### 🔵 Minor
- **[Tone and clarity]** – The page description contains a double space after "Canonical's."
  - *Found:* "with Canonical's  structured tracking"
  - *Recommendation:* Remove the extra space.

---

### Hero

#### 🟡 Needs work
- **[Character limits]** – The hero paragraph is 422 characters. While the knowledge hub template does not specify a strict hero paragraph limit, this is significantly longer than the standard 300-character limit for hero supporting text. For a knowledge hub article this may be acceptable, but it is long for a hero introduction – consider whether it can be tightened.
  - *Found:* 422-character hero paragraph.
  - *Recommendation:* Consider trimming to approximately 300 characters. The second and third sentences could be condensed.

---

### Text section – "Managing CVEs in Ubuntu: an overview"

#### 🔴 Critical
- **[Links]** – The "Canonical" and "Landscape" links in the air-gapped environments section are broken. "Canonical" is incorrectly hyperlinked to `http://www.ubuntu.com/landscape`, and there is a double space between the two links, suggesting a copy-paste error.
  - *Found:* `[Canonical](http://www.ubuntu.com/landscape)  [Landscape](http://www.ubuntu.com/landscape)`
  - *Recommendation:* Remove the erroneous "Canonical" link. The sentence should read: "…[Landscape](https://ubuntu.com/landscape) enables you to mirror…"

#### 🟡 Needs work
- **[Completeness]** – An incomplete sentence appears in the "Canonical provides comprehensive security coverage and support" section. The sentence "…so that your teams know" is cut off with no continuation.
  - *Found:* "Ubuntu LTS releases are supported for 5 years as standard, with a consistent and predictable release cadence, so that your teams know"
  - *Recommendation:* Complete the sentence before sending to design.

- **[Links]** – Six links use `http://` instead of `https://`. All Canonical and Ubuntu domains support HTTPS.
  - *Found:* `http://www.canonical.com/landscape`, `http://www.ubuntu.com/landscape` (×2), `http://www.canonical.com/solutions/open-source-security`, `http://www.ubuntu.com/pro/why-pro`, `http://www.ubuntu.com/pro`
  - *Recommendation:* Update all to `https://` and use the canonical domain format (e.g. `https://canonical.com/landscape`, `https://ubuntu.com/pro`).

- **[Tone and clarity]** – The heading "Kernel & real-time patching status" uses an ampersand. The style guide says not to use `&` for `and`.
  - *Found:* "Kernel & real-time patching status"
  - *Recommendation:* Change to "Kernel and real-time patching status."

- **[Tone and clarity]** – Three instances of `e.g.` appear in the text. The style guide recommends avoiding Latin abbreviations on webpages – use "for example" instead.
  - *Found:* "e.g., 20.04, 22.04, 24.04", "e.g., openssl or linux-azure", "e.g., *Focal*, *Jammy*, *Noble*"
  - *Recommendation:* Replace each `e.g.` with "for example" or "such as." Note: the formatting is correct (with comma after `e.g.`), but the abbreviation itself should be avoided on web pages.

- **[Tone and clarity]** – Several sentences exceed 30 words, and some paragraphs are dense walls of text. This is a long-form article so some latitude is expected, but the target audience is executives who benefit from scannable content.
  - *Found:* Multiple long sentences throughout (for example, the "Automated patching in Ubuntu" paragraph, and the "Canonical provides long-term security maintenance" paragraph).
  - *Recommendation:* Break the longest sentences into two shorter ones. Consider adding more line breaks to improve scannability.

- **[CTAs]** – The link "Learn more" in section 2 (architecture variants) is a non-descriptive CTA. While it is followed by "about AMD64v3," the link text itself is just "Learn more."
  - *Found:* "[Learn more](https://discourse.ubuntu.com/…) about AMD64v3"
  - *Recommendation:* Make the full phrase the link text: "[Learn more about AMD64v3 ›](…)" – or better: "[Explore the AMD64v3 architecture variant ›](…)."

#### 🔵 Minor
- **[Tone and clarity]** – A missing space before "In" in the "How to patch CVEs" section.
  - *Found:* "…or limit impact.In some low-risk scenarios…"
  - *Recommendation:* Add a space: "…or limit impact. In some low-risk scenarios…"

- **[Accessibility]** – The article contains no images (aside from the og:Image placeholder), so image alt text is N/A. However, the code examples (`pro security-status`, `pro fix <CVE-ID>`, `canonical-livepatch status --verbose`) should be in proper code blocks for accessibility and readability. The doc uses backtick formatting, which is correct.
  - *Found:* Code commands are formatted in backticks.
  - *Recommendation:* No action needed – this is a positive note.

- **[Tone and clarity]** – "the widest collection of the most popular and used software" is awkward phrasing.
  - *Found:* "Ubuntu Pro expands security coverage to the widest collection of the most popular and used software"
  - *Recommendation:* Consider: "Ubuntu Pro expands security coverage to tens of thousands of packages across the open source ecosystem."

- **[Tone and clarity]** – "providing stability for the fix" is unclear. The fix itself is stable – the intent is that the system remains stable.
  - *Found:* "…apply it to the older version of the package you are already running, providing stability for the fix."
  - *Recommendation:* Consider: "…keeping your system stable while closing the vulnerability."

- **[Tone and clarity]** – "neutralized in-memory" is an unusual phrasing for patching. Consider a more standard term.
  - *Found:* "every specific CVE ID that has been neutralized in-memory"
  - *Recommendation:* Consider: "every CVE that has been patched in memory" or "addressed via live patching."

---

### Learn more section

#### 🔵 Minor
- **[CTAs]** – "Explore our OSS security" uses the abbreviation "OSS" without expansion. The target audience is executives who may not know this acronym.
  - *Found:* "Explore our OSS security"
  - *Recommendation:* Change to "Explore our open source security" or expand "OSS" on first use earlier in the article.

---

## ❓ Needs review

- **[Text section]** – The article mentions "Ubuntu 26.04 LTS" and "Ubuntu 25.04." Confirm these are the correct, current release names at time of publication.
  - *Found:* "the Ubuntu Security Center in Ubuntu 26.04 LTS" and "as a default app starting from Ubuntu 25.04"
  - *Question:* Are these version numbers accurate and intended?

- **[Text section]** – The "Explore our OSS security" CTA links to `http://www.canonical.com/solutions/open-source-security`. Confirm this URL is correct and should not be `https://canonical.com/solutions/open-source-security`.
  - *Found:* `http://www.canonical.com/solutions/open-source-security`
  - *Question:* Is this the correct destination URL? Should it use `https://`?

---

## ⬜ Not applicable

- **Forms and inputs** – N/A: this is a knowledge hub article with no form or interactive input.
- **Completeness (interactive states)** – N/A: this is a static long-form article with no interactive flows.

---

## ✅ What looks good

- **Structure and hierarchy** – The article follows a clear, logical flow through the CVE management lifecycle: overview → mapping → prioritization → patching → verification → air-gapped environments → older releases → system status → Canonical's role. Headings are well structured and descriptive.
- **Metadata** – Page title (33 chars), breadcrumb (33 chars), and page description (131 chars) are all within their respective character limits.
- **Tone and voice** – The overall tone is authoritative, clear, and approachable – well aligned with the Canonical brand voice. The article explains technical concepts without being condescending.
- **Active voice** – The article predominantly uses active voice throughout, which reads well for the target audience.
- **Serial comma** – Consistently used in lists throughout the doc.
- **Product names** – "Ubuntu Pro," "Landscape," "Livepatch," "Expanded Security Maintenance (ESM)" are all correctly named and capitalized. ESM is correctly expanded on first use.
- **US English** – No UK spelling variants detected in the copy.
- **Links** – Link text is generally descriptive and actionable throughout (e.g. "Learn more about patching automation," "Discover three ways to apply security fixes in Linux," "Get a detailed breakdown of how backporting protects established systems").
- **"open source"** – Correctly written as lowercase, two words, no hyphen throughout the visible copy (the only `open-source` instance is in a URL, which is fine).
- **Acronyms** – CVE, USN, CLI, GUI, ESM, LTS, FIPS, CIS, DISA-STIG, and ISA are either commonly understood by the target audience or are expanded on first use.
- **Code formatting** – CLI commands are properly formatted in backticks, making them easy to identify and copy.
