# UX Content Audit Report

**Figma file:** [26.10 Pro in Portal](https://www.figma.com/design/cV3fXpLn6aV3i8r7v3dfj2/26.10-Pro-in-Portal?node-id=7229-14730)
**Copy doc:** Not provided – exact match check skipped
**Date:** 25 June 2026
**Checks run:** UX quality check only
**Scope:** Subscriptions list page (node 7229:14730)

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor |
|---|---|---|---|---|
| UX quality check | 10 | 1 | 4 | 3 |

**Total issues:** 8 (one critical, four needs work, three minor)

---

## Check 2: UX Quality Check

### Issues by page section

#### Bulk action bar ("2 selected" row)

##### 🟡 Needs work

- **[CTAs]** – The "Clear" button label is vague. It is unclear whether it clears the selection or clears the auto-renewal settings. Consider "Clear selection" for specificity.
  - *Found:* "Clear" | *Recommendation:* "Clear selection"

##### 🔵 Minor

- **[CTAs]** – "Enable" and "Disable" are action verbs but lack an object. In context the "Auto-renewal:" label provides it, but read out of context (e.g. by a screen reader announcing only the button), the action is ambiguous.
  - *Found:* "Enable", "Disable" | *Recommendation:* Add `aria-label="Enable auto-renewal"` / `aria-label="Disable auto-renewal"`

---

#### Subscriptions table

##### 🔴 Critical

- **[Accessibility]** – The status indicators (green dot for Active, red dot for Cancelled, amber dot for Past due) rely solely on color to communicate status. Users with color vision deficiency cannot distinguish these. The text labels ("Active", "Cancelled", "Past due") mitigate this partially, but the dot itself carries no non-color differentiation (e.g. icon shape).
  - *Found:* Colored dots with text labels | *Recommendation:* Use distinct icons (tick, cross, warning) in addition to – or instead of – colored dots, or ensure the text label alone is sufficient and the dot is purely decorative.

##### 🟡 Needs work

- **[CTAs]** – Every row has an identical "Manage" button. When six rows all say "Manage", a screen reader user tabbing through them hears "Manage, Manage, Manage…" with no way to distinguish which subscription each button controls.
  - *Found:* Six identical "Manage" buttons | *Recommendation:* Add `aria-label="Manage Ubuntu Pro Desktop – 10 machines"` (or similar) to each button so it is unique in context.

- **[Structure & Hierarchy]** – The "BILLING" column shows "-" for two cancelled subscriptions. A dash is ambiguous – it could mean "no billing", "not applicable", or "unknown". Consider "N/A" or "None" for clarity.
  - *Found:* "-" in Billing column for Ubuntu Pro (60 machines) and Ubuntu Pro (70 machines) | *Recommendation:* Replace with "N/A" or "No billing"

- **[Completeness]** – The "SUPPORT SCOPE" column shows "-" for one row (Ubuntu Pro, 60 machines). It is unclear whether this subscription genuinely has no support scope or if the value is missing.
  - *Found:* "-" in Support scope column | *Recommendation:* Use "None" or "No support" if intentional

##### 🔵 Minor

- **[Structure & Hierarchy]** – Column headers use ALL CAPS ("SUBSCRIPTION", "MACHINES", etc.). This is harder to scan than title case and can feel like shouting. Consider title case for readability.
  - *Found:* "SUBSCRIPTION", "MACHINES", "SUPPORT SCOPE", etc. | *Recommendation:* "Subscription", "Machines", "Support scope", etc.

---

#### Footer links

##### 🔵 Minor

- **[Links]** – "Ubuntu Pro Service Description" includes an external link icon, which is good. However, "Support portal" also has an external icon – confirm both truly go to external domains. If Support portal is within the same app, the external icon is misleading.
  - *Found:* "Learn about Ubuntu Pro Service Description ↗" and "Get help through Support portal ↗"

---

#### Search and filter bar

##### 🟡 Needs work

- **[Forms & Inputs]** – The search field uses placeholder text "Search subscription by name" with no visible label above it. While the placeholder is descriptive, it disappears on focus/input, leaving no persistent label. A visually hidden label or a persistent label above the field would improve accessibility.
  - *Found:* Placeholder-only search field | *Recommendation:* Add a visually hidden `<label>` element or a persistent visible label

---

### Designer annotations

The following unresolved comments were found on the Figma file. Comments on node 7229:16295 may relate to a different frame in the same file, but are surfaced here for completeness:

- **Ruizi (24 Jun 2026):** "Additional information on the right side?" – Unresolved; needs design decision.
- **Ruizi (24 Jun 2026):** "Edit button here?" – Unresolved; needs design decision.
- **Ruizi (23 Jun 2026):** "The cancel button is too prominent" – Unresolved; needs design decision on button hierarchy.

---

## ✅ What looks good

- **Page title** – "Subscriptions" is clear and descriptive as the H1.
- **Navigation** – Side navigation clearly shows the user's current location ("Subscriptions" is highlighted). The billing section labels (Orders, Contracts, Invoices, Billing settings, Subscriptions, Payment methods) are all descriptive and consistent.
- **Tab structure** – "Current" and "Expired" tabs provide a clear, logical split for subscription states.
- **Subscription names as links** – Each subscription name (e.g. "Ubuntu Pro Desktop", "Ubuntu Pro") is a link, giving users a clear path to details.
- **CTA hierarchy** – "Buy new subscription" is clearly the primary action, positioned top-right with a prominent green button. The bulk action buttons (Enable, Disable, Clear) are appropriately secondary.
- **Filter dropdown** – "All statuses" dropdown provides a clear filtering mechanism with a descriptive label.
- **Footer help links** – The footer offers three helpful resources (Contact us, Service Description, Support portal) – good for discoverability.
- **Account context** – The organisation name ("Ericsson-UK") and user name ("Jonathan Archer") are visible, so users know which account they are managing.
- **Table date format** – Dates use a clear, unambiguous format ("11 Aug 2026").
- **Checkbox selection** – Bulk selection with a count indicator ("2 selected") is clear and functional.
