# UX content audit report – live page

**URL:** [page URL]
**Date:** [today's date]
**Note:** [omit, or note if JS-rendered content may not have been captured]

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | X | X | X | X | X | X |

**Total issues:** N (X critical, X needs work, X minor) · **Needs review:** X · **N/A sections:** [list]

---

## Issues by page section

Organise issues in the order they appear on the page, top to bottom. Tag each issue with its check category in brackets (e.g. [CTAs], [Accessibility]) so the category is still visible. Group by page section, not by check category.

### [Section name — e.g. Navigation, Hero, Section title, Form, Footer]

**[Check category] 🔴 Critical – [short description]**
Evidence: "[text found or element observed]"
[Why it matters and what to fix.]

**[Check category] 🟡 Needs Work – [short description]**
Evidence: "[text found or element observed]"
[Recommendation.]

**[Check category] 🔵 Minor – [short description]**
Evidence: "[text found or element observed]"
[Suggestion.]

---

## ❓ Needs review

Items that cannot be confirmed from the fetched HTML alone (e.g. JS-rendered content, intentional redirects, authenticated states).

---

## ⬜ Not applicable

List any checklist sections that do not apply to this page and why (e.g. "Forms and inputs – no form present on this page").

---

## ✅ What looks good

Specific, genuine observations about content that is well done. List passes grouped by page section.

---

## 🔲 Manual checks for reviewer

- [ ] **Responsive behavior** – resize the browser or use device emulation to check layout and readability at mobile, tablet, and desktop breakpoints
- [ ] **Keyboard navigation** – tab through the page to confirm correct focus order, visible focus indicators, and accessible labels on interactive elements
- [ ] **Authenticated states** – log in and check any copy that only appears after authentication
- [ ] **JS-rendered content** – interact with the page to trigger dynamic states (errors, success messages, empty states)
- [ ] **Discourse post (case studies only)** – confirm that the dev has also created a corresponding Discourse post for the case study
