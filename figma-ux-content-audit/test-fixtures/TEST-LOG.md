# figma-ux-content-audit — test log

A running log of test runs of the `figma-ux-content-audit` skill. Newest first. Goal: see
over time whether the agent catches more of the right things, with less noise, more clearly.

## How we test (current method)

- **Input:** a live Figma file via the Figma MCP (the path the SKILL.md documents). For the
  first run: the Ceph Sites file (`d3yDJFcSFPv8baDTWnk0jR`, node `1:5640`), which pairs with
  the frozen Ceph copy doc — so we can run BOTH checks (copy match + UX quality).
- **Reproducibility caveat:** a live Figma file can change between runs. To keep runs
  comparable we save a **frozen text-extraction snapshot** into `test-fixtures/` each run
  (`canonical-ceph-figma-extract-YYYY-MM-DD.md`). The snapshot — not the live file — is the
  stable record.
- **No answer key yet:** like the copy-doc test, this is a smoke test + gap-finder, not a
  score. We can see whether it works and what false positives/negatives appear; we cannot
  yet measure recall/precision.

---

## Run 2026-06-05 — first run (live MCP, both checks)

- **Skill version:** SKILL.md + default checklist as written (NONE of the copy-doc fixes —
  doc-type gate, needs-review bucket — have been ported to this skill yet).
- **Report:** `reports/canonical-ceph-2026-06-05.md`
- **Snapshot:** `test-fixtures/canonical-ceph-figma-extract-2026-06-05.md`
- **Result:** 7 issues (3 critical, 1 needs work, 3 minor) + 4 needs review + 2 N/A sections.

**What worked**
- The MCP path functioned end to end: read structure with `get_metadata`, then text with
  `get_design_context`, and matched it cleanly against the copy doc.
- Caught high-value issues a screenshot **cannot** surface:
  - **Missing link destinations** — "Install now", 3× "Find out more", a resource link, and
    all blog titles have no href. You can only see a missing link by reading the file.
  - **Placeholder blog content** — 4× "How to enable Real-time Ubuntu on your machine" +
    lorem ipsum, instead of the real Ceph blog feed in the copy doc.
- Copy match confirmed the bulk of body copy matches the copy doc exactly.

**Gaps found**

*Same gaps the copy-doc skill had before its fixes (confirmed they exist here too):*
1. **No doc-type gate** → Forms & Inputs and Error & Feedback States would be false-flagged
   as critical on this marketing page. Had to mark N/A by hand.
2. **No needs-review / N/A buckets** in the report template (summary is Pass + 3 severities
   only) → the four "can't verify from this method" items had nowhere honest to go. Added
   the columns by hand, as we did for copy-doc.
3. **Double-reporting risk** — the blog placeholder spans copy-match + structure +
   completeness; deduped by hand.

*New gaps specific to the Figma / MCP path:*
4. **alt="" false-positive trap (important).** The MCP code export ALWAYS emits `alt=""`
   regardless of the designer's actual alt text. A naive run would flag "all images missing
   alt = critical" — a false positive. Alt text must be marked ❓ needs review, not failed.
   The SKILL.md tells the agent to extract "alt text annotations" but the tools used don't
   expose them.
5. **Designer annotations not retrievable.** `get_design_context` / `get_metadata` don't
   return comments/annotations, yet the report template has a "Designer Annotations"
   section. It can't be filled by these tools — needs a different method or an honest
   "not checked".
6. **Large pages exceed the MCP context limit.** The full page failed in one call; had to
   extract section by section. The SKILL.md should tell the agent to chunk by top-level
   section from the start.
7. **Doc/reality mismatch.** SKILL.md is MCP-only and says "do not proceed" without the MCP,
   but 3 of 4 April reports used PDF/screenshot input. The skill should document BOTH paths
   (and note the screenshot path can't see hrefs/alt — exactly what the MCP path is good at).

**Recommended fixes (short term, not yet done)**
- Port the copy-doc fixes to this skill: doc-type gate + needs-review/N/A buckets in the
  report template.
- Add an explicit alt-text caveat: never fail alt text from the code export; route to needs
  review.
- Tell the agent to extract section by section for large pages.
- Document the screenshot/PDF path as a supported fallback, with its limitations.
- (Later) build a seeded Figma fixture with an answer key for real scoring — same as the
  copy-doc plan.
