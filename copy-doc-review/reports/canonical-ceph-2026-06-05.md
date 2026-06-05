# UX content audit report — copy doc

**Document:** canonical-ceph.md (Canonical Ceph product page copy doc)
**Date:** 2026-06-05
**Note:** Marketing product page — no interactive flows (forms, error/loading/empty states) are present, so those checklist sections are largely not applicable. Run is a test/stress run against the default checklist as written.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| UX quality check | — | 0 | 8 | 4 |

**Total issues:** 12 (0 critical, 8 needs work, 4 minor)

---

## UX quality check

### Structure & hierarchy

#### 🟡 Needs Work
- **[Whole doc]** — Heading levels (H1/H2/H3) are not explicitly indicated. The doc uses pattern-template names (`HERO`, `BASIC SECTION`, `EQUAL HEIGHTS ROW`) instead of marked heading levels, so hierarchy is left for the designer to infer.
  - *Found:* section headings like "Success stories with Canonical Ceph", "Why choose Canonical Ceph?" with no level marked | *Recommendation:* mark intended H1/H2/H3 for each heading.
- **[Section: Why choose Canonical Ceph?]** — The benefits are written as one run-on block rather than a list, despite being a list of discrete points.
  - *Found:* "Highly scalable, from Terabytes to Exabytes Highly reliable, with no single point of failure Protect your data with replication and erasure coding…" | *Recommendation:* format as a bulleted list.

#### 🔵 Minor
- **[Section: Metadata]** — Optional metadata fields left as template placeholder text or empty: og:Image (instruction text still present), Link to asset manager tag (empty), Reference page(s) (empty).
  - *Recommendation:* fill or explicitly mark N/A before handoff.

### CTAs

#### 🟡 Needs Work
- **[Section: Metadata vs Hero]** — Declared "Main action for users to take" is **"Try Canonical Ceph"**, but no matching CTA exists on the page. Hero CTAs are "Get in touch" and "Calculate your storage costs".
  - *Found:* Main action = "Try Canonical Ceph"; hero CTAs = "Get in touch" / "Calculate your storage costs" | *Recommendation:* reconcile — either add the primary "Try" action or update the declared main action.
- **[Section: More choice for your infrastructure]** — Three CTAs use the vague phrase "Find out more" ("Find out more on Charmhub / GitHub / Snap Store"). The destination disambiguates them, but the verb itself is non-specific.
  - *Found:* "Find out more on Charmhub" / "…on GitHub" / "…in the Snap Store" | *Recommendation:* consider more specific verbs (e.g. "Get MicroCeph on Charmhub").

#### 🔵 Minor
- **[Hero / multiple sections]** — Destination host inconsistency: page URL is `canonical.com/ceph` but most CTAs/links point to `ubuntu.com/ceph/*`. *Needs review* — may be intentional during a domain migration.
  - *Found:* "[Get in touch](https://ubuntu.com/ceph#get-in-touch)", "[Install now](https://ubuntu.com/ceph/install)" | *Recommendation:* confirm intended domain.

### Links

#### 🟡 Needs Work
- **[Section: The latest blogs about Ceph]** — Link text is a raw URL, not descriptive.
  - *Found:* "[https://ubuntu.com/blog/tag/ceph](https://ubuntu.com/blog/tag/ceph)" | *Recommendation:* use descriptive text, e.g. "Read the latest Ceph blogs".
- **[Section: Learn more about Canonical Ceph]** — One resource ("Cloud storage cost optimization") has no destination link, while the other three resources in the list do.
  - *Found:* "Cloud storage cost optimization" (no URL) | *Recommendation:* add the destination or mark TBD.

#### 🔵 Minor
- **[Section: Canonical Ceph deployment and operations]** — "we offer Managed Ceph" links over `http://` rather than `https://`.
  - *Found:* "(http://ubuntu.com/ceph/managed)" | *Recommendation:* use https.

### Accessibility

#### 🟡 Needs Work
- **[Section: Learn more about Canonical Ceph]** — Resource thumbnail alt text is an unfilled placeholder.
  - *Found:* repeated "[ALT TEXT]" markers next to `![][image14]` | *Recommendation:* write alt text for each thumbnail.
- **[Section: Success stories with Canonical Ceph]** — A resource asset is hosted on Google Drive rather than the asset manager.
  - *Found:* success-story image "[Asset link](https://drive.google.com/file/d/…)" | *Recommendation:* move to assets.ubuntu.com.

### Completeness

#### 🟡 Needs Work
- **[Whole doc]** — Unresolved placeholders remain that block clean handoff: og:Image instruction text, "[ALT TEXT]" thumbnails, generic "[Asset link]" markers in the Resources section.
  - *Recommendation:* resolve all placeholders before design begins.

### Comments & revisions

*(No open comments found in the export. Placeholder markers are captured under Completeness above to avoid double-reporting.)*

---

## ✅ What looks good

- **Navigation placement is fully specified** — meganav path "Canonical > Products > Ceph" is given, satisfying the Navigation checks cleanly.
- **Metadata core fields are complete** — page title, description, URL, owner, audience, and funnel stage are all filled.
- **Most CTAs and links carry destinations** — the large majority of links specify a URL, which is exactly what design needs.
- **Copy is clear and audience-appropriate** — the prose reads as plain, confident product copy; terminology ("software defined storage", "Ceph") is used consistently.

---

## Recommended priority order

1. No 🔴 Critical issues — design is not blocked.
2. Address 🟡 Needs Work: reconcile the declared main action vs. actual CTAs, fix the raw-URL blog link and the missing resource link, fill alt text, move the Google Drive asset, format the benefits list, mark heading levels.
3. Polish 🔵 Minor: confirm canonical.com vs ubuntu.com domain, fix the http link, complete optional metadata fields.

---

## 🔲 Manual checks for reviewer

- [ ] **Cross-reference with design intent:** confirm the copy matches the structure and intent of any related Figma file (if available)
- [ ] **Conditional / dynamic content:** check that all branches of conditional copy are written, not just the default path
- [ ] **Source content:** verify any copy that pulls from external sources (product docs, marketing claims) is accurate and approved
