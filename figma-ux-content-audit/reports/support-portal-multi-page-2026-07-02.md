# UX Content Audit Report – Support Portal (Multi-page)

**Figma file:** [26.10 Support Portal](https://www.figma.com/design/o1p4JCt1YbAAUvZzKj2Yaa/26.10-Support-Portal)
**Copy doc:** Not provided – exact match check skipped
**Date:** July 2, 2026
**Checks run:** UX quality check only

**Pages audited:**

| # | Node | Page |
|---|---|---|
| 1 | 586:36410 | Parent frame (overview of all sub-screens) |
| 2 | 586:37310 | Planned coverage – New request form |
| 3 | 586:37553 | Request detail – with comment thread (variant A) |
| 4 | 586:45244 | Request detail – with Join session buttons (variant B) |
| 5 | 586:46278 | Request detail – with Next session link (variant C) |
| 6 | 586:38156 | Request submission confirmation |
| 7 | 586:46895 | Book your discovery session |
| 8 | 586:38203 | BT planned coverage requests – list view |
| 9 | 586:38523 | BT planned coverage requests – empty state |

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | — | — | — |
| UX quality check | 12 | 5 | 12 | 8 |

**Total issues:** 25 (5 critical, 12 needs work, 8 minor)

---

## Check 1: Exact Copy Match

Not provided – skipped.

---

## Check 2: UX Quality Check

### Issues by page section

---

### Page 1: Parent frame (586:36410)

This is a collection/overview frame containing all sub-screens. Issues are covered under each individual page below. No additional unique content to audit here beyond what appears in the child screens.

---

### Page 2: New request form (586:37310)

#### Top – Breadcrumb and heading

##### 🔵 Minor

- **[Structure & hierarchy]** – Breadcrumb reads "PLANNED COVERAGE / NEW REQUEST" in all caps. Should be sentence case per Canonical style.
  - *Found:* "PLANNED COVERAGE / NEW REQUEST"
  - *Recommendation:* "Planned coverage / New request"

- **[Structure & hierarchy]** – Section heading "MAIN SESSION DETAILS" is in all caps. Should be sentence case.
  - *Found:* "MAIN SESSION DETAILS"
  - *Recommendation:* "Main session details"

#### Form fields

##### 🟡 Needs work

- **[Forms & inputs]** – The "Description" field uses placeholder text as instructional content ("Describe the session you need support for / include the business drivers and impact / describe the risk and expected outcomes…"). This content will disappear once the user starts typing and may be lost. Consider placing these instructions as help text below or above the field instead.
  - *Found:* Placeholder with five bullet points of guidance
  - *Recommendation:* Move the guidance to persistent help text outside the input field

- **[Forms & inputs]** – "T-shirt size" is internal/informal jargon. Users may not understand what "T-shirt size" means in the context of a support request. The placeholder "Estimate the complexity of your request" is clearer than the label.
  - *Found:* "*T-shirt size" with placeholder "Estimate the complexity of your request"
  - *Recommendation:* Rename to "Complexity estimate" or "Request size" – or keep "T-shirt size" with a brief explanation

- **[Forms & inputs]** – "*Time zone" label with placeholder "Select the starting time of your session" – the label says "Time zone" but the placeholder suggests selecting a start time. These are two different concepts. If this field is for time zone selection, the placeholder should say "Select your time zone".
  - *Found:* Label: "*Time zone" / Placeholder: "Select the starting time of your session"
  - *Recommendation:* Align the label and placeholder – either "Time zone: Select your time zone" or separate into two fields

- **[CTAs]** – "Submit" is a generic button label. Consider a more specific verb like "Submit request" or "Create request".
  - *Found:* "Submit"
  - *Recommendation:* "Submit request"

##### 🔵 Minor

- **[Forms & inputs]** – "Coverage deadline" is not marked as required (no asterisk) while the other date/time fields are. If this is intentional, the helper text "This will help us plan more accurately" is good. If it is required, add the asterisk.
  - *Found:* "Coverage deadline" (no asterisk) vs "*Coverage start date and time"
  - *Recommendation:* Confirm whether this is optional; if so, consider adding "(optional)" for clarity

#### Allowance section

##### 🟡 Needs work

- **[Structure & hierarchy]** – "ALLOWANCE" heading is in all caps.
  - *Found:* "ALLOWANCE"
  - *Recommendation:* "Allowance"

- **[Accessibility]** – The info banner "Label your allowances – To distinguish easily between allowances assign a label to them" contains a link "assign a label" – the link text is descriptive, which is good, but the banner's dismiss button (×) has no visible accessible label.
  - *Found:* × button on info banner
  - *Recommendation:* Add an aria-label like "Dismiss label allowances tip"

---

### Page 3: Request detail – variant A (586:37553)

#### Header area

##### 🔵 Minor

- **[Structure & hierarchy]** – Status badge "Waiting on customer" and "Updated 12 Apr 2023, 12:33" – this is clear and well-structured. No issue.

##### 🟡 Needs work

- **[Links]** – "Skip to latest comment ↓" – good accessibility feature. However, the download icon (↓) next to it could be confused with a download action. Consider using just the text link or a down-arrow icon instead of what appears to be a download icon.
  - *Found:* "Skip to latest comment ↓"
  - *Recommendation:* Use a clear down-arrow (↓) or anchor icon, not a download icon

- **[Links]** – "Expand description" link – good pattern for long descriptions. No issue with the text itself.

#### Sessions timeline

##### 🔴 Critical

- **[Accessibility]** – "Join session" links in the sessions list – the first session (completed) still shows "Join session" as a clickable link. If the session is completed, this link should either be removed, disabled, or relabelled (e.g. "View session notes").
  - *Found:* "Join session" next to a "completed" session
  - *Recommendation:* Remove or disable the "Join session" link for completed sessions, or change to "View session"

##### 🟡 Needs work

- **[CTAs]** – Three "Join session" links appear with no differentiation. A screen reader user tabbing through would hear "Join session, Join session, Join session". Each should include the session name.
  - *Found:* "Join session" × 3
  - *Recommendation:* "Join Discovery session", "Join Main session day 1", "Join Main session day 2" – or add visually hidden text

#### Files section

##### 🟡 Needs work

- **[Error & feedback states]** – "Files that you add trough comments will appear here. We are unable to display files larger than 30MB." – typo: "trough" should be "through".
  - *Found:* "Files that you add trough comments will appear here."
  - *Recommendation:* "Files that you add through comments will appear here."

#### Comments section

##### 🔵 Minor

- **[Forms & inputs]** – The comment box placeholder says "Describe your issue" – but this is a comment on an existing request, not a new issue description. The placeholder should reflect the actual action.
  - *Found:* "Describe your issue"
  - *Recommendation:* "Add a comment" or "Write your comment"

- **[Error & feedback states]** – "You can't upload files larger than 30 MB in comments. Upload large files here" – the "30 MB" here uses a space between number and unit, while the Files section says "30MB" without a space. Inconsistent.
  - *Found:* "30 MB" (comments) vs "30MB" (files section)
  - *Recommendation:* Pick one format and use it consistently. Per Canonical style, use "30MB" (no space).

##### 🔴 Critical

- **[Accessibility]** – "Upload large files here" – "here" is a non-descriptive link. Users relying on screen readers who tab through links will hear "here" with no context.
  - *Found:* "Upload large files here" (with "here" as the link)
  - *Recommendation:* "Upload large files" (make the full phrase the link) or "Upload large files to your request"

---

### Page 4: Request detail – variant B (586:45244)

This is nearly identical to variant A (586:37553) with minor layout differences. The same issues apply:

- Same typo "trough" in Files section
- Same "Describe your issue" placeholder
- Same "Upload large files here" accessibility issue
- Same undifferentiated "Join session" links

##### Additional observations

##### 🟡 Needs work

- **[CTAs]** – In this variant, "Join session" buttons appear as outlined/ghost buttons rather than text links. The completed session's "Join session" button is greyed out, which is an improvement over variant A – but it would be clearer to remove the button entirely or change the label to "Completed".
  - *Found:* Greyed-out "Join session" button for completed session
  - *Recommendation:* Remove the button or change label to "Session completed"

---

### Page 5: Request detail – variant C (586:46278)

This variant adds a prominent "Next session link" section with a green "Join session" button.

##### 🟡 Needs work

- **[Structure & hierarchy]** – "Next session link" as a label is slightly ambiguous – it could mean "the link to the next session" or "the next link about sessions". Consider "Join your next session" or "Your next session".
  - *Found:* "Next session link"
  - *Recommendation:* "Your next session" or "Upcoming session"

##### 🔵 Minor

- **[CTAs]** – The green "Join session" button is prominent and well-placed. The button label could be more specific: "Join Discovery session" to match the session type.
  - *Found:* "Join session" (green button)
  - *Recommendation:* "Join Discovery session"

*All other issues from variants A and B also apply here (typo, placeholder, "here" link, undifferentiated "Join session" text links in the timeline).*

---

### Page 6: Request submission confirmation (586:38156)

#### Success message

##### 🔵 Minor

- **[Error & feedback states]** – "Your request has been submitted successfully / Request ID: 427887" – clear, specific confirmation. Well done. Minor: the success banner could also mention the request subject for extra clarity.
  - *Found:* "Your request has been submitted successfully"
  - *Recommendation:* Consider including the request subject in the confirmation

#### Next step section

##### 🟡 Needs work

- **[Structure & hierarchy]** – "Next step: Book a discovery session" – good pattern, clearly guides the user. However, the body text starts with "In order to book a planned coverage session" – the phrase "In order to" is wordy per Canonical style. Use "To book" instead.
  - *Found:* "In order to book a planned coverage session, please schedule a discovery session with our team."
  - *Recommendation:* "To book a planned coverage session, schedule a discovery session with our team."

##### 🔴 Critical

- **[Accessibility]** – "Book discovery session" button has an external link icon (↗). This is helpful for indicating the link opens externally, but ensure the icon has an accessible label (e.g. "opens in a new tab") for screen reader users.
  - *Found:* "Book discovery session ↗"
  - *Recommendation:* Add visually hidden text: "Book discovery session (opens in a new tab)"

#### Bottom link

*No issues – "View open requests ›" is clear and descriptive.*

---

### Page 7: Book your discovery session (586:46895)

#### Timeline layout

##### 🟡 Needs work

- **[Structure & hierarchy]** – The label "next" appears in the timeline as a step indicator. This is vague – it should describe what happens next, not just say "next".
  - *Found:* "next"
  - *Recommendation:* "Next step" or remove the label if the visual timeline already communicates sequence

- **[Structure & hierarchy]** – "Book your discovery call" vs page title "Book your discovery session" – inconsistent terminology. Is it a "call" or a "session"? Pick one and use it consistently.
  - *Found:* Page title: "Book your discovery session" / Body: "Book your discovery call"
  - *Recommendation:* Use "session" consistently throughout

##### 🔴 Critical

- **[Accessibility]** – Same external link icon issue on "Book discovery session ↗" button as on the confirmation page (586:38156). Needs accessible label.

*The body text also contains the same "In order to" phrasing as page 6.*

---

### Page 8: BT planned coverage requests – list view (586:38203)

#### Header

##### 🔵 Minor

- **[Structure & hierarchy]** – "BT planned coverage requests" – "BT" is unexplained. If this is a customer/account name, it reads fine. If it is an abbreviation, it should be spelled out on first use.
  - *Found:* "BT planned coverage requests"
  - *Recommendation:* Confirm "BT" is the account name; if it is an abbreviation, spell it out

#### Navigation sidebar

##### 🟡 Needs work

- **[Navigation]** – The sidebar shows "Planed coverage" (missing an "n" – should be "Planned coverage"). This is a typo in the navigation label.
  - *Found:* "Planed coverage"
  - *Recommendation:* "Planned coverage"

#### Table

##### 🔴 Critical

- **[Accessibility]** – Status indicators use colored dots (blue/green) as the only differentiator between statuses like "Upcoming", "Waiting on customer", "In progress", and "Closed". Colorblind users will not be able to distinguish these. The text labels help, but the dots alone are not accessible.
  - *Found:* Colored dots next to status text
  - *Recommendation:* Use distinct icons or shapes alongside color (e.g. open circle, filled circle, checkmark) or rely solely on the text labels

##### 🟡 Needs work

- **[CTAs]** – "start call" links in the "Next session" column – these are lowercase, inconsistent with other button/link styling. Also, several rows show "-" where there is no session link, with no explanation of why.
  - *Found:* "start call" (lowercase) and "-" (dash for no action)
  - *Recommendation:* Capitalize consistently ("Start call") and replace "-" with "No session scheduled" or similar

- **[Mobile considerations]** – This table has eight columns (Request ID, Subject, Status/Date updated, Author/Date created, Canonical engineer, Next session/Duration, Next session link). It will be very difficult to use on smaller screens.
  - *Found:* Eight-column table with long text values
  - *Recommendation:* Flag for responsive design review – consider a card layout on mobile

##### 🔵 Minor

- **[Structure & hierarchy]** – "Showing 20 out of 145 planned coverages" – good pagination feedback. Minor: "planned coverages" reads slightly awkwardly; consider "planned coverage requests" for consistency with the page title.
  - *Found:* "Showing 20 out of 145 planned coverages"
  - *Recommendation:* "Showing 20 of 145 planned coverage requests"

---

### Page 9: BT planned coverage requests – empty state (586:38523)

#### Empty state

##### 🟡 Needs work

- **[Error & feedback states]** – "No requests" is a bare empty state with no guidance. Best practice is to explain why the list is empty and offer a next step.
  - *Found:* "No requests"
  - *Recommendation:* "No requests yet. Create a new request to get started." with a link or button to the "New request" form

#### Navigation sidebar

- **[Navigation]** – This variant shows "Events" in the sidebar, which does not appear in the other screens (which show "Planned coverage"). Confirm whether this is intentional or a design inconsistency.
  - *Found:* Sidebar: Home, Overview, Knowledge base, Tickets, Events, Contact us
  - *Recommendation:* Ensure sidebar navigation is consistent across all pages

---

### Designer annotations

Unresolved Figma comments on node 586:36410:

- **timea.udvarhelyi:** "we need the logic for how entitlements are calculated and what is the renewing policy (logic)"
- **timea.udvarhelyi:** "same w buttons"
- **timea.udvarhelyi:** "external link icon"
- **timea.udvarhelyi:** "try card"
- **timea.udvarhelyi:** "add documentation for snowflake"
- **timea.udvarhelyi:** "remove last line of table"
- **timea.udvarhelyi:** "24 px (with vanila)"
- **timea.udvarhelyi:** "button reorganizing"
- **timea.udvarhelyi:** "@Nina Rojc"

These suggest ongoing design work – particularly around external link icons, button reorganization, and entitlement logic. Several align with issues flagged in this audit (external link accessibility, button labelling).

---

## ✅ What looks good

- **Request detail layout** – the left sidebar metadata (Stage, Service level, Request ID, Coverage type, etc.) is well-structured and scannable. Labels are clear and use natural language.
- **Sessions timeline** – the visual timeline with dates, session types, durations, and status (completed/upcoming) provides excellent context at a glance.
- **New request form structure** – required fields are clearly marked with asterisks. The "Planning documents" upload section with helper text ("Upload any supporting documents that help us understand your session") is well-written.
- **Confirmation page flow** – the success message is specific (includes Request ID), and the next step is clearly presented with a prominent CTA.
- **Comment thread** – the comment history with author names, avatars, and timestamps is clear. The "Search comments" feature is a useful addition.
- **Planned coverage list** – tabs (Open, Awaiting customer input, Upcoming, Closed, All) with badge counts provide excellent filtering. The search bar and sort options (Date updated, Author, Date created, Starting time) are comprehensive.
- **Pagination** – "Showing 20 out of 145 planned coverages" with page controls gives clear feedback on the dataset.
- **Consistent sidebar navigation** – the Support Portal sidebar (Home, Overview, Knowledge base, Tickets, Planned coverage, Contact us) is consistent across most screens.
- **Allowance tip banner** – the dismissible info banner "Label your allowances" on the new request form is a thoughtful onboarding touch.

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** – open the live Support Portal, refresh, and confirm only the intended sections have changed
- [ ] **Keyboard navigation** – tab through the new request form to confirm field order and focus management. Test the "Join session" buttons on the request detail page.
- [ ] **External links** – confirm "Book discovery session" opens in a new tab and that the external link icon communicates this clearly
- [ ] **Responsive check** – verify the planned coverage requests table (eight columns, 145 rows) is usable on tablet and mobile
- [ ] **Comment text editor** – confirm the rich text toolbar (B, I, strikethrough, lists, code, image) is accessible via keyboard
- [ ] **Terminology consistency** – confirm whether the term is "discovery session" or "discovery call" throughout the portal
- [ ] **Navigation consistency** – confirm whether "Events" (page 9) or "Planned coverage" (other pages) is the correct sidebar label
