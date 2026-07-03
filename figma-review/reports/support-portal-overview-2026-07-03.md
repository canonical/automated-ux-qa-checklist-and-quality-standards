# UX Figma review: Support Portal – Overview

**Figma file:** 26.10-Support-Portal (node 437:27480)
**Copy doc:** Not provided – exact match check skipped
**Date:** July 3, 2026
**Checks run:** UX quality check | Brand & style compliance

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | — | — | — |
| UX quality check | 10 | 2 | 7 | 4 |
| Brand & style compliance | — | 1 | 3 | 2 |

**Total issues:** 19 (three critical, 10 needs work, six minor)

**Note:** This review is based on visible frames in the Figma file at the specified node. The primary frames reviewed are: Overview dashboard (full page with sidebar), Overview dashboard (content area only), session request form component, and sidebar navigation. Several other frames in the section (ticket detail pages, modals, smaller component states) could not be individually accessed via the Figma MCP and are not covered in this report.

---

## Check 2: UX quality check

### Issues by page section

#### Sidebar navigation

##### 🔵 Minor
- **[Navigation]** – The sidebar label "SUPPORT PORTAL" is in all caps. While this may be a deliberate design choice for section labels, confirm that the all-caps treatment is intentional and consistent with the design system.

---

#### Search / "What can we help you with?"

##### 🟡 Needs work
- **[Accessibility]** – The section heading "WHAT CAN WE HELP YOU WITH?" is phrased as a question but displayed in all caps. Combined with the Knowbot search below, it is unclear whether this is a general help section or a chatbot entry point. Consider a clearer heading such as "Search" or "Get help." (See also the open Figma comment: "Introducing a term here 'Knowbot' – will users know what this is?")
  - *Found:* "WHAT CAN WE HELP YOU WITH?"
  - *Recommendation:* Use a clearer, more descriptive heading. If the Knowbot is an AI assistant, briefly explain it (e.g. "Ask our AI assistant or search the Knowledge base").

- **[Accessibility]** – The downward arrow icon next to "Tips for search" resembles a download icon, which could confuse users. An open Figma comment also flags this: "a little confusing that it looks like our download icon but copy is about skipping to a section."
  - *Found:* Arrow/chevron icon next to "Tips for search"
  - *Recommendation:* Use an info icon or a question mark icon instead, or make the tips expandable inline.

---

#### Ticket status

##### 🔵 Minor
- **[Structure & hierarchy]** – The ticket status counters (21 Open, 8 Awaiting customer input, 27 Closed) use a "›" chevron as a link indicator. This is functional but subtle – ensure the chevrons meet contrast requirements and are clearly tappable/clickable targets.

---

#### Tickets table

##### 🟡 Needs work
- **[CTAs]** – "Create ticket" is a green button – good. However, "View all tickets" is an outlined button that sits next to it. Both are the same size, which may create confusion about which is the primary action. Consider making "View all tickets" a text link instead.
  - *Found:* "View all tickets" (outlined button) next to "Create ticket" (green button)
  - *Recommendation:* Differentiate more clearly – use a text link for "View all tickets" and keep the green button for "Create ticket."

---

#### Allowance status

##### 🟡 Needs work
- **[Accessibility]** – The information icon (ⓘ) next to "8/34 hours available" has no visible label or tooltip explanation in the design. Users may not understand why one allowance shows 34 hours while others show 30.
  - *Found:* ⓘ icon with no visible label
  - *Recommendation:* Add a tooltip or helper text explaining the discrepancy (e.g. "Includes 4 bonus hours").

- **[Structure & hierarchy]** – All three allowance cards show identical placeholder text: "Lidia Luna Puerta / Firefighting for Team Name." This appears to be placeholder/sample data, but the label "Firefighting for Team Name" suggests the team name field has not been finalized. Confirm whether this is intentional sample data or an incomplete design.
  - *Found:* "Firefighting for Team Name" repeated three times
  - *Recommendation:* If this is sample data, use distinct team names to demonstrate how the UI handles variation.

---

#### Planned coverage requests

##### 🟡 Needs work
- **[Accessibility]** – The "starting in 2 hours" badge on the "Network topology upgrade" row uses a dark background with white text. Verify that this badge meets WCAG AA contrast requirements and that the information is also conveyed to screen readers.
  - *Found:* Dark badge overlaying table content
  - *Recommendation:* Ensure the badge is accessible and does not obscure other content on smaller viewports.

- **[CTAs]** – Same pattern as tickets: "View all requests" (outlined) next to "Create request" (green). See the same recommendation above about differentiating primary and secondary actions.

##### 🔵 Minor
- **[Structure & hierarchy]** – An expanded request detail (session timeline for "Production cloud twin deployment – DR environment") appears below the table. It is unclear whether this is an inline expansion or a separate section. The visual hierarchy could be clearer – consider indenting or boxing the expanded detail.

---

#### Entitlements

##### 🔴 Critical
- **[Accessibility]** – The section heading appears to read "ENTITELMENTS" – a misspelling of "ENTITLEMENTS" (missing the second "E"). This is a critical typo in a section heading.
  - *Found:* "ENTITELMENTS"
  - *Recommendation:* Correct to "ENTITLEMENTS."

---

#### Feedback

##### 🔵 Minor
- **[CTAs]** – "We appreciate your feedback" contains a link but the link text is not visually distinguishable in the thumbnail. Ensure the link text is clearly styled and descriptive.

---

#### Session request form

##### 🔴 Critical
- **[Forms & inputs]** – The "T-shirt size" label is agile/engineering jargon that may not be understood by all support portal users. An open Figma comment also flags this: "Will all users understand what this means? Otherwise use 'Estimate the complexity' as the section label."
  - *Found:* "T-shirt size" with placeholder "Estimate the complexity of your session"
  - *Recommendation:* Change the label to "Complexity estimate" or "Session complexity" and keep the descriptive placeholder.

##### 🟡 Needs work
- **[Forms & inputs]** – The "Allocate from entitlement" dropdown has the placeholder "Select the allowance to be deducted from" – this mixes terminology ("entitlement" in the label, "allowance" in the placeholder). An open Figma comment also notes: "what does coverage mean in this case? since the description is session again."
  - *Found:* Label: "Allocate from entitlement" / Placeholder: "Select the allowance to be deducted from"
  - *Recommendation:* Use consistent terminology throughout. Pick either "entitlement" or "allowance" and use it in both the label and placeholder.

- **[Forms & inputs]** – The "Description" field placeholder lists five bullet points of guidance. While helpful, there is no indication of whether the description is required. Confirm whether this should be marked as required.
  - *Found:* Description field with no required indicator
  - *Recommendation:* If required, add an asterisk or "(required)" to the label.

---

### Designer annotations

The following open Figma comments were found and should be resolved before development:

- "suggest 'we can't' instead of we are unable"
- "no space per canonical copy style guide" (unit formatting)
- "existing issue, already has description suggest placeholder text 'add a comment' or 'write your comment'"
- "is this system-based? we don't use italics for placeholder text in other contexts"
- "typo – through"
- "Or – user thinks this applies to one of the sessions listed below but has to figure out which one"
- "does this show all the time when they have another session?"
- "does 'main' distinguish it from other sessions? or from the section 'allowance' below"
- "checking since the other time related things are required?"
- "suggest being clear what happens here and use 'submit request' so there's no ambiguity"
- "these are maybe two different selections – one is the time zone and then choose the time?"
- "again there's coverage and session – worth clarifying the distinction"
- "we need the logic for how entitlements are calculated and what is the renewing policy (logic)"

---

## Check 3: Brand & style compliance

### Issues by severity

#### 🔴 Critical
- **[A3 – Product names]** – The entitlements section lists "Ubuntu Advantage Standard Server - 36 months." "Ubuntu Advantage" is a deprecated/legacy product name. The style guide says to flag it – the correct name is "Ubuntu Pro."
  - *Found:* "Ubuntu Advantage Standard Server - 36 months" in Entitlements
  - *Recommendation:* Update to the current product name. If this is a legacy entitlement that genuinely uses the old name in the backend, add a note explaining this is a historical label.

#### 🟡 Needs work
- **[A3 – Product names]** – "Maas" appears as a category chip in the search section. The official product name is "MAAS" (all caps).
  - *Found:* "Maas" category chip
  - *Recommendation:* Change to "MAAS."

- **[A7 – Numbers]** – "Desktop support 24 x 7" uses a non-standard format. The style guide specifies "24/7," not "24x7" or "24 x 7."
  - *Found:* "Desktop support 24 x 7"
  - *Recommendation:* Change to "Desktop support 24/7."

- **[A8 – Punctuation]** – The hyphens used in table subject lines (e.g. "Network topology upgrade – spine-leaf redesign") correctly use en dashes with spaces, which is good. However, the entitlement "Ubuntu Advantage Standard Server - 36 months" uses a hyphen as a separator, not an en dash. If this is a sentence break or a separator, use an en dash with spaces ( – ).
  - *Found:* "Ubuntu Advantage Standard Server - 36 months"
  - *Recommendation:* Change to "Ubuntu Pro Standard Server – 36 months" (fixing both the product name and the dash).

#### 🔵 Minor
- **[A4 – Capitalization]** – Section headings are all in uppercase (TICKET STATUS, TICKETS, ALLOWANCE STATUS, etc.). The style guide calls for sentence case in headings. If this is a deliberate design system pattern for dashboard section labels, it may be acceptable – but it should be documented as an intentional deviation.

- **[B1 – Brand voice]** – The feedback message "We've redesigned. Let us know what you think. We appreciate your feedback." is functional but could be more on-brand. Consider a warmer, more specific call to action (e.g. "We've redesigned the Support Portal. Share your thoughts to help us improve.").

---

## ✅ What looks good

- **Navigation** – The sidebar navigation is clean, well-organized, and clearly labeled. The five navigation items (Overview, Knowledge base, Tickets, Planned coverage, Contact us) cover the key user journeys. The user name and logout option are properly placed at the bottom.
- **Dashboard structure** – The Overview page follows a logical information hierarchy: search → ticket status → ticket list → allowance status → planned coverage → entitlements → feedback. This mirrors a natural support workflow.
- **Search** – The search section offers multiple entry points: free text, deep thinking mode toggle, category browsing. This supports different user mental models.
- **Tables** – Ticket and planned coverage request tables are well-structured with clear column headers (Ticket ID, Subject, Last Updated, Assignee, Severity). The sortable/filterable tabs (Awaiting customer input, Assigned to you, Followed by you) help users find relevant items quickly.
- **Status indicators** – The colored progress bars above ticket status numbers (Open, Awaiting, Closed) provide quick visual feedback.
- **Form design** – The session request form uses clear labels, helpful placeholders, and appropriate input types (dropdowns for selection, rich text editor for description, file upload for documents). Helper text below fields ("We will estimate the remaining hours," "This will help us plan more accurately") is well written and useful.
- **CTAs** – Primary actions ("Create ticket," "Create request") are clearly differentiated with green buttons. The "Join" links in the planned coverage table are appropriately subtle.
- **Serial comma** – Correctly used in lists throughout the visible content.
- **En dashes** – Correctly used with spaces in table subject lines (e.g. "Network topology upgrade – spine-leaf redesign," "Disk layout changes – LVM to Ceph migration").
