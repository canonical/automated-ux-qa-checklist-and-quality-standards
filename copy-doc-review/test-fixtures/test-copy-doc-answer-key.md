# Answer key: test-copy-doc.md

Test fixture for the `copy-doc-review` skill. This file lists every deliberately
planted issue, its location, checklist section, expected severity, and what the skill
should report.

**Scoring method:** compare the skill's report against this key.

- **Detection score** — did the skill find the issue? (primary metric)
- **Severity score** — did the severity match? (secondary; allow ±1 tier)
- **Critical recall** — did it catch all 🔴 issues? (most important single metric)
- **N/A correctness** — did it correctly skip Forms & Error States?
- **False positives** — count issues reported that are not in this key

---

## Planted issues (27 total)

### 1. Structure & hierarchy

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| S1 | Page description is empty | Metadata table, "Page description" row | 🔴 Critical | Required metadata field left blank |
| S2 | Heading jumps from H1 to H3 (no H2) | "Why choose Canonical CloudRun" — marked `###` but appears under the H1 hero with no H2 | 🟡 Needs work | Skipped heading level |
| S3 | Vague/generic heading | "More information" section heading | 🟡 Needs work | Not descriptive — what information? |
| S4 | Bullet list has no intro sentence | "Why choose…" section — list starts immediately after paragraph | 🔵 Minor | Best practice: lists need a lead-in |

### 2. CTAs

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| C1 | Vague CTA: "Learn more" | Hero section, second CTA | 🟡 Needs work | Non-specific verb |
| C2 | CTA with empty destination | Hero section, "Learn more" has `href=""` (empty) | 🔴 Critical | CTA destination undefined |
| C3 | Duplicate CTA labels in same page | Hero "Learn more" and CTA Band "Learn more" — identical text | 🟡 Needs work | Technically different sections, but same page |
| C4 | "Click here" CTA | CTA Band, "Click here to contact us" | 🟡 Needs work | Banned pattern |

### 3. Links

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| L1 | Entire sentence as link text | "More information" section — full sentence is the link | 🟡 Needs work | Only the relevant phrase should be linked |
| L2 | "Read more" as standalone link text | Resources section, bare "Read more" link | 🟡 Needs work | Not descriptive on its own |
| L3 | Link text matches across categories | "Read more" also overlaps with accessibility (no context for screen readers) | — | Overlap with A4; count once under Links |

### 4. Forms & inputs — N/A

| # | Expected result | Notes |
|---|---|---|
| N1 | Section should be marked **N/A** | Page type is "Product or service" (marketing). No form fields present. If the skill flags missing forms, that's a **false positive**. |

### 5. Error & feedback states — N/A

| # | Expected result | Notes |
|---|---|---|
| N2 | Section should be marked **N/A** | Marketing page with no interactive/transactional flows. If the skill flags missing error states, that's a **false positive**. |

### 6. Accessibility

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| A1 | Image with no alt text | "More information" section, `image2` — no alt text or description | 🟡 Needs work | All images need alt text in the copy doc |
| A2 | Resource hosted on Google Drive | Resources section, whitepaper linked to `drive.google.com` | 🟡 Needs work | Should be on asset manager |
| A3 | Visual-position-only instruction | CTA Band, "click the button on the right" | 🔵 Minor | Should reference the button by label |
| A4 | "Read more" / "Click here" as link text | Resources + CTA Band | 🟡 Needs work | Not accessible for screen readers. Overlap with L2/C4; count once if found under any category. |

### 7. Navigation

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| V1 | Navigation placement missing entirely | Metadata table, "Navigation" row is blank | 🔴 Critical | Required metadata — no nav path specified |
| V2 | Meganav label not specified | No meganav path or label anywhere in metadata | 🟡 Needs work | If page is in meganav, label and description are required |

### 8. Completeness

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| P1 | TBD placeholder | "Why choose…" section: "trusted by TBD enterprises" | 🟡 Needs work | Unresolved placeholder |
| P2 | TK placeholder | Customer stories: "— TK, VP Engineering" | 🟡 Needs work | Name not filled in |
| P3 | Open author comment | Resources section: "[AUTHOR: needs updated stats…]" | 🟡 Needs work | Unresolved comment |

### 9. Tone & clarity

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| T1 | Inconsistent product name | "CloudRun" (hero, CTAs) vs "Cloud Run" (data spotlight heading) vs "cloud-run" (More information body) | 🟡 Needs work | Pick one and use it consistently |
| T2 | Dense jargon / unexpanded acronyms | "More information" section — CNCF, K8s, OCI, CSI, CNI all unexpanded | 🟡 Needs work | Target audience is "Platform engineers" but copy doc should still expand on first use |
| T3 | Overly long sentence | Hero description — single sentence, 50+ words | 🔵 Minor | Break into shorter scannable sentences |
| T4 | Unsupported superlative claim | Hero: "The world's most reliable container management platform" | 🟡 Needs work | Unprovable absolute claim; brand/legal risk |
| T5 | Conflicting stats | Hero section/data spotlight says "50% cost reduction"; Why choose section says "40%" | 🟡 Needs work | Stats contradict each other |

### 10. Comments & revisions

| # | Issue | Location | Severity | Notes |
|---|---|---|---|---|
| R1 | Unresolved TODO | CTA Band: "TODO: check with legal before publishing pricing claims" | 🟡 Needs work | Must be resolved before design |
| R2 | Open author comment (same as P3) | Resources section: "[AUTHOR: needs updated stats…]" | — | Already counted under Completeness (P3); skill may flag in either or both sections |

---

## Summary

| Metric | Expected |
|---|---|
| Unique planted issues | 27 (some overlap across categories) |
| Distinct countable issues | 25 (after de-duping L3, A4, R2) |
| 🔴 Critical | 3 (S1, C2, V1) |
| 🟡 Needs work | 18 |
| 🔵 Minor | 3 (S4, A3, T3) |
| ❓ Needs review | 0 planted (but skill may legitimately flag some) |
| N/A sections | 2 (Forms & inputs, Error & feedback states) |

---

## Scoring guide

After running the skill, compare its report to this key:

1. **For each issue in this key**, check if the skill found it (detection)
2. **For each issue found**, check if the severity matches (±1 tier is acceptable)
3. **Count false positives** — issues the skill reported that aren't in this key
4. **Check N/A handling** — did it correctly mark Forms and Error States as N/A?

### Metrics to record

```
Detection:       __/25 (issues found out of 25 countable)
Critical recall: __/3  (🔴 issues found)
Severity match:  __/__ (of detected issues, how many had correct severity)
False positives: __    (findings not in this key)
N/A correct:     __/2  (Forms N/A, Error States N/A)
```

### Interpretation

- **Detection ≥ 20/25** and **Critical recall 3/3** = skill is working well
- **Detection 15–19** = functional but missing patterns; review which categories were missed
- **Detection < 15** = significant gaps; checklist or skill instructions may need revision
- **False positives > 5** = skill may be over-flagging; review for systematic bias
