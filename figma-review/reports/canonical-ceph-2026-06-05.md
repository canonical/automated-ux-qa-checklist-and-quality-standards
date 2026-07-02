# UX content audit report

**Figma file:** canonical.com-ceph---Sites (`d3yDJFcSFPv8baDTWnk0jR`), node `1:5640` (page "canonical.com/ceph")
**Copy doc:** `copy-doc-review/test-fixtures/canonical-ceph.md` (the frozen Ceph copy doc)
**Date:** 2026-06-05
**Checks run:** Both (exact copy match + UX quality check)
**Input mode:** Figma MCP (live file) — extracted via `get_metadata` + `get_design_context`, section by section
**Extraction snapshot:** `test-fixtures/canonical-ceph-figma-extract-2026-06-05.md`

> **Method note:** This was run through the live Figma MCP (the path the SKILL.md documents),
> unlike the April reports which used PDF/screenshot exports. The full page exceeded the MCP
> context limit in one call, so it was pulled section by section. Two checks below (alt text,
> designer annotations) **cannot be verified by this method** — see the ❓ Needs review section.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| Exact copy match | — | 1 | 0 | 2 | 0 | — |
| UX quality check | — | 2 | 1 | 1 | 4 | 2 |

**Total issues:** 7 (3 critical, 1 needs work, 3 minor) · **Needs review:** 4 · **N/A sections:** Forms & Inputs, Error & Feedback States (marketing page)

---

## Check 1: Exact copy match

### 🔴 Critical — Placeholder content in Figma (not matching copy doc)
- **[Frame: Blog / "The latest blogs about Ceph"]** — All four blog blocks contain placeholder content, not the real Ceph blog feed the copy doc specifies.
  - Figma: title "How to enable Real-time Ubuntu on your machine" (repeated ×4) + body "Lorem ipsum dolor sit amet…" (×4)
  - Copy doc: blog section pulls from `ubuntu.com/blog/tag/ceph` (tags: ceph, storage)
  - *Impact:* the section is unfinished — wrong titles, lorem-ipsum bodies, and (see UX check) no links.

### 🔵 Minor — Wording / boundary differences
- **[Frame: Success stories]** — Link boundary differs.
  - Figma link text: "Learn how Wellcome Sanger achieved a cost-effective Ceph infrastructure ›"
  - Copy doc: "Learn how" sits outside the link; only "Wellcome Sanger achieved a cost-effective Ceph infrastructure ›" is linked.
- **[Frame: Resources vs copy doc]** — The copy doc's category label "WHITEPAPERS AND WEBINARS" does not appear in the Figma Resources section. Likely intentional (component drops it), but noted.

*(All other copy — hero, data spotlight, success-story bodies, deployment/operations, the version table, "More choice", "Why choose" + benefits list, and the four resource blocks — matches the copy doc.)*

---

## Check 2: UX quality check

### Structure & hierarchy
✅ Logical section flow; headings use the design system's h1 → h2 → h5 pattern consistently. Benefits are a proper bulleted list (an improvement over the copy doc's run-on text).

### CTAs

#### 🔴 Critical
- **[Frame: More choice / "Install now"]** — Primary-style button has **no destination** (no href in the Figma export). A main action that goes nowhere.

#### 🟡 Needs Work
- **[Frame: More choice — 3 blocks]** — Link verb "Find out more" (on Charmhub / GitHub / Snap Store) is non-specific. Destination context helps, but the verb is vague.

### Links

#### 🔴 Critical
- **[Multiple frames]** — Several links are styled as links but have **no destination** in Figma:
  - "Find out more on Charmhub ›", "Find out more on GitHub ›", "Find out more in the Snap Store ›" (More choice)
  - "Cloud storage cost optimization" (Resources) — the other 3 resources are linked; this one is not
  - All 4 blog titles
  - *Note:* the copy doc supplies destinations for the three "Find out more" links and "Install now" (charmhub.io/microceph, github, snapcraft.io/microceph, ubuntu.com/ceph/install) — so these are wiring gaps in the Figma, not unknown destinations. **This class of issue is invisible to the screenshot/PDF path** — you can only see a missing href by reading the file.

#### 🔵 Minor
- **[Frame: Deployment & operations / "we offer Managed Ceph"]** — Link uses `http://ubuntu.com/ceph/managed` (http, not https). Matches the copy doc, so the error originates upstream.

### Forms & inputs
⬜ **N/A** — marketing page, no form present. (Absence of a form is expected; not flagged.)

### Error & feedback states
⬜ **N/A** — static marketing page, no interactive states. (Absence of error/loading/success copy is expected; not flagged.)

### Navigation
See ❓ Needs review — nav placement lives in the Header/Footer and the Sites file structure, not in this page node.

### Mobile considerations
See ❓ Needs review — only the "Large" breakpoint exists in this node.

### Designer annotations
See ❓ Needs review — comments/annotations are not returned by `get_design_context`/`get_metadata`.

---

## ❓ Needs review

Cannot be determined from this extraction method — a human (or a different method) must confirm.

- **Alt text (Accessibility)** — The MCP **code export always emits `alt=""`** regardless of what the designer set, so this run **cannot verify** image alt text. Hero, success-story, equal-height, and blog images plus the partner logos all need a manual alt-text check (logos likely need the company name as alt). *Do not treat empty alt in the export as a real finding.*
- **Designer annotations / comments** — Not retrievable via the tools used. If the designer left notes, they were not seen. Needs a separate check in Figma.
- **Mobile copy** — Only `Breakpoint=Large` is present in this node. Cannot confirm mobile-specific copy or truncation. Open the mobile frame to verify.
- **Navigation placement** — The page node doesn't contain the meganav path (it's in the shared Header). Confirm "Canonical > Products > Ceph" placement separately.

---

## ⬜ Not applicable

- **Forms & Inputs** — marketing page, no form.
- **Error & Feedback States** — static marketing page, no interactive states.

---

## ✅ What looks good

- **Body copy matches the copy doc almost exactly** across hero, success stories, deployment/operations, the version table, "More choice", "Why choose", and all four resource blocks.
- **Hero and resource links are properly wired** with real destinations (Get in touch, Calculate your storage costs, Learn more about Ceph support, 3 of 4 resources).
- **Benefits are a clean bulleted list** — a structural improvement over the copy doc's run-on block.
- **Heading hierarchy is consistent** with the design system.

---

## Recommended priority order

1. **🔴 Finish the Blog section** — replace lorem-ipsum/placeholder titles with the real Ceph blog feed and add links.
2. **🔴 Wire the missing destinations** — "Install now", the three "Find out more" links, the "Cloud storage cost optimization" resource, and blog titles.
3. **🟡 Reconsider the "Find out more" verb** for specificity.
4. **🔵 Fix the http→https** Managed Ceph link (and upstream in the copy doc).
5. **❓ Resolve the needs-review items** — manual alt-text pass, check designer annotations, verify the mobile breakpoint, confirm nav placement.

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** — open the live page, refresh, and confirm only the intended sections have changed
- [ ] **Keyboard navigation** — for any special or interactive features, manually tab through to confirm correct order
- [ ] **Alt text** — verify alt text on all images/logos directly in Figma (not visible to the MCP code export)
