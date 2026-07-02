# UX Content Audit Report

**Figma file:** [26.10 Support Portal](https://www.figma.com/design/o1p4JCt1YbAAUvZzKj2Yaa/26.10-Support-Portal?node-id=437-27481&t=EbSzNFYuagmfATyR-4)
**Node:** 437:27481 (Support Portal – Overview / Dashboard)
**Copy doc:** Not provided – exact match check skipped
**Date:** July 2, 2026
**Checks run:** UX quality check only

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | — | — | — |
| UX quality check | 8 | 2 | 7 | 5 |

**Total issues:** 14 (2 critical, 7 needs work, 5 minor)

---

## Check 1: Exact Copy Match

Not provided – skipped.

---

## Check 2: UX Quality Check

### Issues by page section

#### Search / "What can we help you with?"

##### 🟡 Needs work

- **[CTAs]** – The search input placeholder reads "Describe your issue for the Knowbot to provide an answer" – this introduces the term "Knowbot" without explanation. Users unfamiliar with this product term will not understand what it means. Consider "Describe your issue to get help" or defining "Knowbot" on first use.
  - *Found:* "Describe your issue for the Knowbot to provide an answer"
  - *Recommendation:* "Describe your issue to find an answer" or add a brief explanation of what the Knowbot is

- **[Links]** – "Knowledge base" in the left navigation and "Search for Knowledge base articles" in the search placeholder – if users are unfamiliar with this term, a more general label like "Help articles" or "Related articles" could be clearer.
  - *Found:* "Search for Knowledge base articles"
  - *Recommendation:* Consider whether "Knowledge base" is well understood by the target audience; if not, use "Help articles" or "Articles"

##### 🔵 Minor

- **[Accessibility]** – "Tips for search" with a lightbulb icon (💡) – the icon has no visible label or tooltip explaining its function.
  - *Found:* "Tips for search 💡"
  - *Recommendation:* Ensure the icon has an accessible label or tooltip

- **[CTAs]** – "Deep thinking mode" toggle – no explanation of what this mode does. A tooltip or help text would aid discoverability.
  - *Found:* "Deep thinking mode"
  - *Recommendation:* Add a brief description or tooltip explaining what deep thinking mode does

#### Ticket status

##### 🔵 Minor

- **[Structure & hierarchy]** – The three status counts (21 Open, 8 Awaiting customer input, 27 Closed) use inconsistent link styles – "Open ›" and "Closed ›" use a single chevron, while "Awaiting customer input ›" wraps to two lines. Ensure consistent formatting.
  - *Found:* "Open ›" / "Awaiting customer input ›" / "Closed ›"
  - *Recommendation:* Keep labels concise and visually consistent; consider "Awaiting input ›"

#### Tickets table

##### 🔴 Critical

- **[Accessibility]** – The severity column uses a flag icon (🏳) as the only indicator of severity level. Users relying on screen readers or who are colorblind may not be able to distinguish severity. The icon needs an accessible text label.
  - *Found:* Flag icon + "Sev2", "Sev3", "Sev4" – icon-only differentiation
  - *Recommendation:* Add visible text labels or ARIA labels to the severity icons

##### 🟡 Needs work

- **[CTAs]** – "View all tickets" (ghost button) and "Create ticket" (green button) – "View all tickets" is vague. Consider specifying what "all" means (e.g. "View open tickets" or "View all your tickets").
  - *Found:* "View all tickets" / "Create ticket"
  - *Recommendation:* Be more specific about what "all tickets" includes

- **[Structure & hierarchy]** – Tab labels "Awaiting customer input 🔴", "Assigned to you 🔴", "Followed by you 🔴" use badge counts. The counts overlap visually with tab text. Ensure the badge count is clearly separate and accessible.
  - *Found:* Tab labels with inline badge numbers
  - *Recommendation:* Ensure badge counts have accessible labels (e.g. "Awaiting customer input, 3 tickets")

#### Allowance status

##### 🟡 Needs work

- **[Structure & hierarchy]** – "ALLOWANCE STATUS" uses all-caps styling. This is harder to read than sentence case and does not follow Canonical heading conventions.
  - *Found:* "ALLOWANCE STATUS"
  - *Recommendation:* Use sentence case: "Allowance status"

- **[Structure & hierarchy]** – The three allowance cards all show "Lidia Luna Puerta / Firefighting for Team Name" – "Team Name" appears to be placeholder text that was not replaced.
  - *Found:* "Firefighting for Team Name"
  - *Recommendation:* Replace with actual team name or use a more realistic placeholder

##### 🔴 Critical

- **[Error & feedback states]** – The middle allowance card shows "8/34 hours available" with an info icon (ℹ️), but there is no explanation of why this allowance exceeds the standard 30-hour allocation. If this represents an overage or special allocation, the user needs context.
  - *Found:* "8/34 hours available ℹ️"
  - *Recommendation:* Add a tooltip or footnote explaining non-standard allocations

#### Planned coverage requests

##### 🟡 Needs work

- **[Structure & hierarchy]** – "PLANNED COVERAGE REQUESTS" is in all caps. Should be sentence case per Canonical style.
  - *Found:* "PLANNED COVERAGE REQUESTS"
  - *Recommendation:* "Planned coverage requests"

- **[CTAs]** – "Join" links in the table – "Join" alone is not descriptive enough out of context. A screen reader user tabbing through links would hear "Join, Join, Join" with no differentiation.
  - *Found:* "Join" (repeated seven times)
  - *Recommendation:* Use "Join session" or add visually hidden text like "Join session for [subject]"

##### 🔵 Minor

- **[Mobile considerations]** – The planned coverage requests table has seven columns (Request ID, Subject, Next session duration, Phase, Join session). This will be difficult to read on smaller screens.
  - *Found:* Seven-column table layout
  - *Recommendation:* Flag for responsive/mobile design review

- **[Structure & hierarchy]** – The "starting in 2 hours" tooltip on one row is helpful context but appears inconsistently – it only shows on one session. Consider applying this pattern to all upcoming sessions.
  - *Found:* "starting in 2 hours" (on one row only)
  - *Recommendation:* Apply consistently to all upcoming sessions

#### Entitlements

##### 🟡 Needs work

- **[Structure & hierarchy]** – "ENTITELMENTS" heading is in all caps and should be sentence case.
  - *Found:* "ENTITELMENTS"
  - *Recommendation:* "Entitlements" – and also check for a possible typo ("ENTITELMENTS" vs "ENTITLEMENTS")

##### 🔵 Minor

- **[Links]** – Entitlement names are links (e.g. "CUE Exam Activation Key", "Ubuntu Pro (Apps-only) - Virtual") but it is not clear where they lead. Ensure the link destination is communicated.
  - *Found:* Linked entitlement names with no indication of destination
  - *Recommendation:* Add a visual indicator or tooltip showing where these links go

#### Feedback section

##### 🟡 Needs work

- **[Links]** – "We appreciate your feedback" is the linked text in "Let us know what you think. We appreciate your feedback." – the link text should describe the action, not be a pleasantry.
  - *Found:* "We appreciate your feedback." (as link text)
  - *Recommendation:* "Give us your feedback" or "Share your feedback"

#### Navigation (left sidebar)

*No issues found – navigation labels are clear and consistent.*

---

### Designer annotations

Unresolved comments on this node:

- **Sophie Felder:** "I think they probably know about knowledge base here, but if not, a general term might actually be more helpful, 'related articles' etc"
- **Sophie Felder:** "Introducing a term here 'Knowbot' – will users know what this is?"

Both comments align with issues flagged in this audit (see Search section above).

---

## ✅ What looks good

- **Navigation sidebar** – clear, concise labels (Home, Overview, Knowledge base, Tickets, Planned coverage, Contact us). Hierarchy is logical.
- **Ticket table structure** – well-organized with clear column headers (Ticket ID, Subject, Last updated, Assignee, Severity). Sortable columns indicated.
- **Search area** – prominent placement at the top of the page with category browsing chips (Landscape, Juju, Maas, All categories) for quick filtering.
- **Consistent CTA pairing** – "View all" (secondary) and "Create" (primary) button pairs are used consistently in both the Tickets and Planned coverage sections.
- **Planned coverage details** – the expanded request view (showing session timeline with Discovery session and Main session) provides good context for upcoming sessions.
- **Welcome personalization** – "Welcome Simon" adds a personal touch to the dashboard.
- **Feedback prompt** – proactively asking for feedback on the redesign is a good UX practice.
- **Tab navigation** – ticket filtering via tabs (Awaiting customer input, Assigned to you, Followed by you) is intuitive.

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** – open the live Support Portal, refresh, and confirm only the intended sections have changed
- [ ] **Keyboard navigation** – tab through the dashboard, especially the ticket table rows, "Join" links, and search input, to confirm correct keyboard navigation order
- [ ] **Responsive check** – verify the tickets and planned coverage tables are usable on tablet/mobile widths
- [ ] **Knowbot explanation** – confirm whether "Knowbot" is defined elsewhere in the portal or if users will encounter it without context
