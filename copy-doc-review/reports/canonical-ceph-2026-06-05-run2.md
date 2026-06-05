# UX content audit report — copy doc

**Document:** canonical-ceph.md (Canonical Ceph product page copy doc)
**Date:** 2026-06-05 (run 2 — after doc-type gate + needs-review fixes)
**Note:** Page type = "Product or service" (marketing page, no interactive flows). Forms & Inputs and Error & Feedback States are marked N/A by the doc-type gate.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | — | 0 | 8 | 2 | 1 | 2 |

**Total issues:** 10 (0 critical, 8 needs work, 2 minor) · **Needs review:** 1 · **N/A sections:** Forms & Inputs, Error & Feedback States (marketing page, no interactive states)

---

## UX quality check

### Structure & hierarchy

#### 🟡 Needs Work
- **[Whole doc]** — Heading levels (H1/H2/H3) are not explicitly indicated; the doc uses pattern-template names (`HERO`, `BASIC SECTION`) instead of marked heading levels, leaving hierarchy for the designer to infer.
  - *Found:* headings like "Success stories with Canonical Ceph", "Why choose Canonical Ceph?" with no level marked | *Recommendation:* mark intended H1/H2/H3.
- **[Section: Why choose Canonical Ceph?]** — Benefits written as one run-on block rather than a list.
  - *Found:* "Highly scalable, from Terabytes to Exabytes Highly reliable, with no single point of failure Protect your data…" | *Recommendation:* format as a bulleted list.

#### 🔵 Minor
- **[Section: Metadata]** — Optional metadata fields left as placeholder text or empty: og:Image, Link to asset manager tag, Reference page(s).
  - *Recommendation:* fill or explicitly mark N/A before handoff.

### CTAs

#### 🟡 Needs Work
- **[Section: Metadata vs Hero]** — Declared "Main action" is **"Try Canonical Ceph"**, but no matching CTA exists; hero CTAs are "Get in touch" and "Calculate your storage costs".
  - *Recommendation:* reconcile the declared main action with the actual CTAs.
- **[Section: More choice for your infrastructure]** — Three CTAs use the vague phrase "Find out more" (on Charmhub / GitHub / Snap Store). Destination disambiguates, but the verb is non-specific.
  - *Recommendation:* use more specific verbs, e.g. "Get MicroCeph on Charmhub".

### Links

#### 🟡 Needs Work
- **[Section: The latest blogs about Ceph]** — Link text is a raw URL, not descriptive.
  - *Found:* "[https://ubuntu.com/blog/tag/ceph](https://ubuntu.com/blog/tag/ceph)" | *Recommendation:* "Read the latest Ceph blogs".
- **[Section: Learn more about Canonical Ceph]** — One resource ("Cloud storage cost optimization") has no destination link; the other three do.
  - *Recommendation:* add the destination or mark TBD.

#### 🔵 Minor
- **[Section: Canonical Ceph deployment and operations]** — "we offer Managed Ceph" links over `http://` rather than `https://`.
  - *Recommendation:* use https.

### Accessibility

#### 🟡 Needs Work
- **[Section: Learn more about Canonical Ceph]** — Resource thumbnail alt text is an unfilled placeholder.
  - *Found:* repeated "[ALT TEXT]" markers next to `![][image14]` | *Recommendation:* write alt text per thumbnail.
- **[Section: Success stories with Canonical Ceph]** — A resource asset is hosted on Google Drive rather than the asset manager.
  - *Found:* "[Asset link](https://drive.google.com/file/d/…)" | *Recommendation:* move to assets.ubuntu.com.

### Completeness

#### 🟡 Needs Work
- **[Whole doc]** — Unresolved placeholders block clean handoff: og:Image instruction text, "[ALT TEXT]" thumbnails, generic "[Asset link]" markers.
  - *Recommendation:* resolve all placeholders before design begins.

*(Interactive-state checks — hover/focus/error/success/empty/loading — are N/A for this marketing page.)*

### Comments & revisions

*(No open comments in the export. Placeholder markers reported once, under Completeness.)*

---

## ❓ Needs review

- **[Hero / multiple sections]** — Page URL is `canonical.com/ceph` but most CTAs/links point to `ubuntu.com/ceph/*`. Cannot tell from the text whether this is intentional (e.g. mid-migration) or an error.
  - *Found:* "[Get in touch](https://ubuntu.com/ceph#get-in-touch)", "[Install now](https://ubuntu.com/ceph/install)" | *Question:* is `ubuntu.com/ceph` the intended destination, or should these be `canonical.com/ceph`?

---

## ⬜ Not applicable

- **Forms & Inputs** — N/A: marketing page with no form. ("Get in touch" links out; no input flow in the doc.)
- **Error & Feedback States** — N/A: static marketing page with no interactive states; absence of error/success/loading copy is expected.

---

## ✅ What looks good

- **Navigation placement is fully specified** — meganav path "Canonical > Products > Ceph".
- **Metadata core fields are complete** — title, description, URL, owner, audience, funnel stage.
- **Most CTAs and links carry destinations** — the large majority specify a URL.
- **Copy is clear and audience-appropriate** — plain, confident product copy; terminology used consistently.

---

## Recommended priority order

1. No 🔴 Critical issues — design is not blocked.
2. Resolve the ❓ Needs review item (domain) — it affects every link on the page.
3. Address 🟡 Needs Work: main action vs CTAs, raw-URL blog link, missing resource link, alt text, Google Drive asset, benefits list, heading levels.
4. Polish 🔵 Minor: http link, optional metadata fields.

---

## 🔲 Manual checks for reviewer

- [ ] **Cross-reference with design intent:** confirm the copy matches the structure and intent of any related Figma file (if available)
- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved
