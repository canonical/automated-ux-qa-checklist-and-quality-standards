# UX Figma review – Valkey product page

**Figma file:** canonical.com data – Sites, node `5452:6969`
**Copy doc:** data/valkey
**Date:** November 16, 2026
**Checks run:** Exact copy match, UX quality check, Brand & style compliance
**Note:** Source URLs, personal comment details, and internal asset links are omitted.

## Summary

| Check | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review |
|---|---:|---:|---:|---:|
| Exact copy match | 0 | 1 | 2 | 1 |
| UX quality check | 1 | 2 | 1 | 0 |
| Brand & style compliance | 0 | 4 | 0 | 1 |

**Total findings:** One critical, seven needs work, three minor, and two needs review.

## Check 1: Exact copy match

The visible page copy largely matches the copy document. Global navigation and footer content are excluded; the page sub-navigation is included.

### 🟡 Needs work

- **[Navigation]** – The Figma sub-navigation includes “Portfolio,” which is not listed in the copy document’s “Data,” “Services,” and “Docs” navigation copy.
  - *Recommendation:* Confirm whether “Portfolio” is intended and align the navigation specification with the design.

### 🔵 Minor

- **[Punctuation and spacing]** – The Figma statistic displays “~30 minutes,” while the copy document has a space after the tilde: “~ 30 minutes.”
  - *Recommendation:* Align the formatting in both sources.

- **[Punctuation]** – The Data spotlight links add a trailing chevron not present in the copy document: “Contact us ›,” “Check our automation ›,” and “Try it yourself ›.”
  - *Recommendation:* Confirm that the chevrons are intentional link styling or update the copy source to match.

### ❓ Needs review

- **[Hero badge]** – The Figma badge says “Available with Ubuntu Pro.” The copy document refers to a “Supported with Ubuntu Pro” logo but does not clearly specify whether that phrase is the intended badge text.
  - *Question:* Which wording is approved for the badge?

## Check 2: UX quality check

### Hero

#### 🔴 Critical

- **[CTAs]** – The hero “Contact us” button links to the PostgreSQL page’s contact anchor, not the Valkey page. The same label elsewhere in the design correctly targets Valkey.
  - *Found:* Hero link target ends in `/data/postgresql#get-in-touch`.
  - *Recommendation:* Change it to the intended Valkey contact destination and keep repeated “Contact us” links consistent.

#### 🔵 Minor

- **[CTAs]** – “Contact us” does not say what users can discuss or expect.
  - *Recommendation:* Consider a more specific label, such as “Talk to Valkey team,” if that matches the destination.

### Use cases

#### 🟡 Needs work

- **[Accessibility]** – The four use-case illustrations are exposed with empty alt text in the design context.
  - *Recommendation:* Add concise alt text if the illustrations convey information; otherwise confirm they are decorative and should be ignored by assistive technology.

- **[Mobile considerations]** – The four use-case cards contain dense paragraphs in narrow columns. The provided frame is desktop-only, so the mobile reading and layout behavior cannot be confirmed.
  - *Recommendation:* Review the cards at mobile widths and shorten or restructure the copy if it becomes difficult to scan.

### Designer annotations

No unresolved Figma comments were returned for this node.

## Check 3: Brand & style compliance

### 🟡 Needs work

- **[US spelling]** – “Data centre” uses UK spelling.
  - *Correct:* “Data center.”

- **[Product-name capitalization]** – “VMWare” does not use the official spelling.
  - *Correct:* “VMware.”

- **[Acronyms]** – “SLA” appears without its expansion on first use.
  - *Recommendation:* Use “service-level agreement (SLA)” on first mention.

- **[Plain language]** – “Artifacts” may be unfamiliar to the stated executive audience.
  - *Recommendation:* Replace it with a clearer term or define it.

### ❓ Needs review

- **[Claim substantiation]** – The page claims “up to 15 years” of security maintenance and “hundreds of deployments across all IT sectors.”
  - *Question:* Are both claims supported by approved evidence and current service terms?

## ✅ What looks good

- The hero heading and body copy match the copy document.
- Section order and headings form a clear page hierarchy.
- Use-case headings and descriptions match the copy document.
- The page uses sentence case in its visible section headings.
- The design contains no Figma comments requiring follow-up.
