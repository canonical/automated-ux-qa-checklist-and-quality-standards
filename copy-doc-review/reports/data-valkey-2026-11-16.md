# UX content audit – Valkey product page

**Document:** data/valkey
**Date:** November 16, 2026
**Page type:** Product or service
**Target audience:** Executives
**Note:** Source URLs, personal comment details, and internal asset links are omitted.

## Summary

**Findings:** Two critical, eight needs work, one minor, and two needs review.
**Not applicable:** Forms and inputs; interactive states – this is a marketing page with no form or interactive flow copy.

## Issues by page section

### Metadata

#### 🔴 Critical

- **[Navigation]** – The navigation field still contains the template prompt instead of a page location. Design cannot confirm how users reach the page.
  - *Found:* “For meganav or bubble navigation, please indicate path.”
  - *Recommendation:* Specify the navigation path, such as the intended Data section and Valkey page.

#### 🟡 Needs work

- **[Character limits]** – The page description is 183 characters, exceeding the 160-character limit.
  - *Found:* The metadata description beginning “Get enterprise-grade Valkey support…” (183 characters).
  - *Recommendation:* Trim it to 160 characters or fewer while retaining the main benefit and audience-relevant detail.

- **[Links]** – The current page URL and existing-page reference use `http://`.
  - *Found:* Two metadata links use the non-secure scheme.
  - *Recommendation:* Use `https://` for both.

### Hero

#### 🔴 Critical

- **[CTAs]** – The hero “Contact us” link points to the PostgreSQL page’s contact anchor, while the other Valkey contact link points to Valkey. The duplicated label therefore leads to different destinations, and the hero route appears to be a copy error.
  - *Found:* Hero CTA route ends in `/data/postgresql#get-in-touch`; the Valkey contact link ends in `/data/valkey#get-in-touch`.
  - *Recommendation:* Point the hero CTA to the intended Valkey contact destination and confirm both “Contact us” links resolve consistently.

### Logo section

#### 🟡 Needs work

- **[Tone and clarity]** – The body copy uses UK spelling and inconsistent product-name capitalization.
  - *Found:* “data centre,” “VMWare,” and “Microcloud.”
  - *Recommendation:* Use “data center,” “VMware,” and “MicroCloud.”

#### 🔵 Minor

- **[Tone and clarity]** – The annotation “Ubuntu Pro logo’s link” uses a possessive apostrophe where the plural is intended.
  - *Found:* “logo’s”
  - *Recommendation:* Change it to “logos.”

### Data spotlight

#### 🟡 Needs work

- **[Character limits]** – The three spotlight strings combine values and labels, so each exceeds the 10-character value limit: “100+ clusters” (13), “10+ automations” (15), and “~ 30 minutes” (12).
  - *Recommendation:* Separate each value from its label in the copy fields, then verify the value and label lengths independently.

- **[Character limits]** – The “To get started” description is 110 characters, exceeding the 100-character data spotlight description limit. The other two descriptions are within the limit at 86 and 99 characters.
  - *Found:* “Get up and running quickly whether in your local lab environment or your live production infrastructure setup.”
  - *Recommendation:* Trim this description to 100 characters or fewer.

### Deployment options

#### 🟡 Needs work

- **[Structure and hierarchy]** – The copy document marks multiple page-section titles as Heading 1, including “Valkey deployment options,” “Popular Valkey use cases,” and “Valkey support services.” The page title should be the sole H1, with section titles beneath it.
  - *Recommendation:* Mark the page title as H1 and page-section titles as H2 in the handoff.

- **[Character limits]** – Two CTA button labels exceed the 20-character limit.
  - *Found:* “Check our software operator” (27 characters) and “Tell us more about your needs” (29 characters).
  - *Recommendation:* Shorten each button label while preserving the action, for example “Try Valkey operator” and “Discuss your needs.”

### Use cases

#### ❓ Needs review

- **[Accessibility]** – The four use-case illustrations have image sources but no alt-text guidance.
  - *Question:* Are these images decorative? If not, add concise descriptions that communicate their relevant content.

### Support and resources

#### 🟡 Needs work

- **[Tone and clarity]** – “SLA” is not expanded on first use, and “artifacts” may be unclear to the stated executive audience.
  - *Found:* “SLA-backed support” and “Valkey automation and artifacts.”
  - *Recommendation:* Spell out “service-level agreement (SLA)” on first use and replace or explain “artifacts.”

## ❓ Needs review

- **[Comments and revisions]** – An open document comment asks for the latest partner-logo assets. Confirm that the comment has been addressed before design handoff.

## ⬜ Not applicable

- **Forms and inputs** – N/A: the page is a marketing page with no form.
- **Completeness (interactive states)** – N/A: this page has no interactive flow requiring hover, focus, error, success, empty, or loading copy.

## ✅ What looks good

- The page title is 49 characters, within its 60-character limit.
- The metadata identifies the page type and executive audience.
- The content follows a clear sequence from the hero through deployment options, use cases, support, and resources.
- Most links have descriptive labels and specified destinations.
- The deployment options use concise, action-oriented CTA labels.
