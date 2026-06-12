# Default UX Content Checklist — Live Pages

UX best practice checks for live URL reviews. These are independent of any brand or style guide rules.

---

## 1. Structure & Hierarchy

- [ ] Headers flow logically down the page (H1 → H2 → H3, no skipped levels)
- [ ] All headings are meaningful and descriptive — not vague, generic, or placeholder text
- [ ] Lists and bullet groups have a heading, title, or intro text above them
- [ ] The most important information or action is visually and hierarchically first
- [ ] Multi-step flows have clear step labels or progress indicators
- [ ] Modal and overlay titles clearly describe the task or content

---

## 2. CTAs

- [ ] CTAs use specific, honest action verbs — not vague phrases like "learn more", "click here", "find out more", "submit"
- [ ] Destructive actions (delete, remove, cancel) are clearly and specifically labelled
- [ ] Primary and secondary CTAs on the same screen are not identically labelled
- [ ] CTAs read naturally and make sense out of context (a user should know what will happen when they click)

---

## 3. Links

- [ ] Link text is descriptive and meaningful
- [ ] Entire lines or sentences are not hyperlinked — only the relevant phrase should be linked
- [ ] Links with the same text on the same page go to the same destination

---

## 4. Forms & Inputs

- [ ] Every input field has a visible label (not just placeholder text)
- [ ] Placeholder text does not substitute for a label
- [ ] Required fields are clearly marked
- [ ] Field labels use natural, user-facing language

---

## 5. Error & Feedback States

- [ ] Every error state has a message — no silent failures
- [ ] Error messages explain what went wrong in plain language
- [ ] Error messages tell the user how to fix the problem
- [ ] Success/confirmation messages confirm the specific action that was completed
- [ ] Empty states have explanatory text and a CTA or next step where appropriate
- [ ] Loading states have descriptive text, not just a spinner

---

## 6. Accessibility

- [ ] All images, graphs, and graphics have alt text
- [ ] Icon-only elements have a visible or accessible label
- [ ] Link text is descriptive — no "click here" or "read more" as standalone link labels
- [ ] Instructions do not rely solely on visual position ("the button on the right") — use labels

---

## 7. Navigation

- [ ] Navigation labels are clear and consistent across the page
- [ ] Users can identify where they are in a flow or site at all times
- [ ] Breadcrumbs or back links are present where expected

---

## 8. Mobile Considerations (flag for review)

- [ ] Tables, dense copy, or complex layouts are flagged for mobile review
- [ ] Any content that may be truncated or hard to read at small sizes is noted

---

## 9. Manual Checks (remind reviewer)

These cannot be checked via static fetch and should be completed by the reviewer:

- [ ] **Authenticated states** — log in and check any copy that only appears after authentication
- [ ] **JS-rendered content** — interact with the page to trigger dynamic states (errors, success messages, empty states)
- [ ] **Keyboard navigation** — tab through the page to confirm correct focus order and accessible labels
- [ ] **Mobile view** — resize or use device emulation to check layout and readability
