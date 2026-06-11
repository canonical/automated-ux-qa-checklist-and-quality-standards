---
name: figma-ux-content-audit
description: >
  Use this skill whenever the user wants to audit, review, or check a Figma file
  for UX content quality, or compare Figma copy against a copy document. Triggers
  include: "review my Figma", "audit the copy", "check UX content", "compare against
  a checklist", "content audit", "UX writing review", "check microcopy", "does the
  Figma match the copy doc", "check the design against the copy", or anything
  involving reviewing text/labels/copy in a Figma design file. Also trigger when
  the user provides a markdown copy doc and wants to validate Figma content against
  it. Use this skill even if the user only mentions a Figma link and asks for "a
  review" — always assume a content audit is appropriate.
---

# Figma UX Content Audit Skill

Performs two checks on a Figma file:

1. **Exact copy match** — compares every text string in the Figma file against a markdown copy document, flagging any differences (wording, missing strings, extra strings, minor differences like punctuation or capitalisation)
2. **UX quality check** — reviews Figma content against UX best practice checklist

Outputs a structured markdown report organised by check type, with issues cited to specific Figma frames/layers.

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| Figma file URL or file key | Yes | Used to fetch content via Figma MCP |
| Markdown copy doc | Optional | Required for the exact match check. Exported or copied from Google Doc into .md or .txt format. |
| Custom UX checklist | Optional | Overrides or supplements the default checklist. User may paste inline or provide a file. |

---

## Step 0 — Confirm inputs

1. Check what the user has provided:
   - **Figma file URL/key** — required for both checks. If missing, ask before proceeding.
   - **Markdown copy doc** — if provided, run the exact match check. If not, skip Check 1 and run Check 2 only.
   - **Custom checklist** — if provided, use instead of or alongside the default. If not, load `references/default-checklist.md`.

2. Tell the user which checks will be run based on what was provided.

---

## Step 1 — Extract content from Figma via MCP

Use the Figma MCP to retrieve:
- **All text nodes** across all frames/pages — labels, button text, headings, placeholders, error messages, tooltips, alt text annotations, etc.
- **Frame and component names** — to map content back to screens
- **Layer names** — where they hint at role (e.g. "error-message", "cta-button", "placeholder")
- **Annotations and comments** — designer notes left on frames or layers

### Organise extracted content by screen/frame

```
Page: [Page Name]
  Frame: [Frame Name]
    - [layer role if inferable]: "[text content]"
    - ...
  Annotations/comments:
    - "[annotation text]"
```

Process all pages. Note while extracting:
- Text nodes that are empty or whitespace-only (potential missing copy)
- Icon/image layers with no associated text label (potential accessibility gap)
- Duplicate text strings that appear with slight variations (potential consistency issue)

---

## Step 2 — Check 1: Exact copy match (only if copy doc provided)

Compare the extracted Figma text strings against the markdown copy doc.

### How to match

- Work through the copy doc section by section
- For each string in the copy doc, find the corresponding text in the Figma extraction
- For each text node in Figma, check it exists in the copy doc

### Issue types and severity

| Type | Severity | Description |
|---|---|---|
| Wording difference | 🔴 Critical | The text exists in both but the words differ meaningfully |
| Missing from Figma | 🔴 Critical | Copy doc has text that does not appear in the Figma file |
| Extra in Figma | 🟡 Needs work | Figma has text that does not appear in the copy doc |
| Minor difference | 🔵 Minor | Same wording but differs in punctuation, capitalisation, spacing, or trailing characters |

Always flag minor differences — do not silently ignore them.

---

## Step 3 — Check 2: UX quality check

Work through each section of the checklist (default or custom). For each item:

1. Check the extracted content to determine: **pass / fail / needs review / not applicable**
2. Cite the specific frame and text or missing element as evidence
3. Assign severity:
   - 🔴 **Critical** — functional or accessibility blocker (missing label, silent error, etc.)
   - 🟡 **Needs work** — vague copy, missing best practice, inconsistency
   - 🔵 **Minor** — small wording or pattern improvement

### Severity overrides

The following should always be treated as **🔵 Minor**, regardless of what the default rules would suggest:

- **Logo alt text** — missing or generic alt text on logos (e.g. company logos in partner sections). These are cosmetic, not functional accessibility gaps.
- **"Learn more" links with an ARIA label** — if a "Learn more" link has an `aria-label` that provides context, the accessibility requirement is technically met. Flag as minor for copy improvement, not as a standard accessibility issue.

### Checklist sections (from default-checklist.md)

1. Structure & Hierarchy
2. CTAs
3. Links
4. Forms & Inputs
5. Error & Feedback States
6. Accessibility
7. Navigation
8. Mobile Considerations
9. Designer Annotations
10. Manual Checks (include as reminders in report, not as pass/fail)

---

## Step 4 — Write the audit report

**Report ordering:** For Check 2 (UX quality), organise issues by frame/section in the order they appear in the Figma flow (top to bottom, left to right), not by check category. Tag each issue with its check category in brackets (e.g. [CTAs], [Accessibility]) so the category is still visible. This lets a reviewer read the report alongside the Figma file without jumping around.

**Passing checks:** All checks that pass should go at the bottom of the report in the "✅ What Looks Good" section, not interleaved with issues.

**The report itself must follow the Canonical copy style guide** (`shared/copy-style-guide-checklist.md`). Key rules for report output:
- Use **en dashes with spaces** ( – ) for sentence breaks, not em dashes (—) or hyphens (-).
- Use US English spelling.
- Spell out single-figure numbers (one–nine); use digits from 10 up.
- No gendered pronouns – use they/them.

Output a structured markdown report:

```markdown
# UX Content Audit Report
**Figma file:** [file name or URL]
**Copy doc:** [filename, or "Not provided — exact match check skipped"]
**Date:** [today's date]
**Checks run:** [Exact copy match | UX quality check | Both]

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| Exact copy match | — | X | X | X |
| UX quality check | X | X | X | X |

**Total issues:** N (X critical, X needs work, X minor)

---

## Check 1: Exact Copy Match

### 🔴 Critical — Wording differences
- **[Frame: Name] [Layer: Name]**
  - Figma: "[actual text]"
  - Copy doc: "[expected text]"

### 🔴 Critical — Missing from Figma
- **[Copy doc section]:** "[text]" — not found in Figma

### 🟡 Needs Work — Extra in Figma
- **[Frame: Name]:** "[text]" — not in copy doc

### 🔵 Minor — Punctuation / capitalisation / spacing
- **[Frame: Name] [Layer: Name]**
  - Figma: "[actual]"
  - Copy doc: "[expected]"

---

## Check 2: UX Quality Check

### Issues by page section

List issues in the order they appear on the page / in the Figma flow, top to bottom. Each issue should note its check category in brackets for reference.

#### [Frame / section name]

##### 🔴 Critical
- **[Check category]** – [issue and why it matters]
  - *Found:* "[text]" | *Recommendation:* "[suggestion]"

##### 🟡 Needs Work
- ...

##### 🔵 Minor
- ...

### Designer Annotations
List any unresolved annotations or notes left by the designer in the Figma file:
- **[Frame: Name]:** "[annotation text]"

---

## ✅ What Looks Good

Specific, genuine observations about content that is well done.

---

## 🔲 Manual Checks for Reviewer

- [ ] **Live page compare** — open the live page, refresh, and confirm only the intended sections have changed
- [ ] **Keyboard navigation** — for any special or interactive features, manually tab through to confirm correct order
```

---

## Step 5 — Deliver the report

- Output the report inline in chat as markdown
- Offer to generate a `.md` file download if the user wants to save or share it
- Offer to dive deeper into any specific frame, section, or issue

---

## Edge cases

| Situation | How to handle |
|---|---|
| Figma MCP not connected | Tell the user the Figma MCP needs to be active in VS Code. Do not proceed without it. |
| No copy doc provided | Skip Check 1, run Check 2 only. Note this clearly at the top of the report. |
| Figma file has no text nodes | Warn the user — file may be image-only or the file key may be incorrect. |
| Very large file (100+ frames) | Ask the user if they want all pages audited or specific ones. Default to all. |
| Designer annotations reference people by name | Treat them as open questions to be addressed, surfaced neutrally in the report. |

---

## References

- `references/default-checklist.md` — Full default UX content checklist
