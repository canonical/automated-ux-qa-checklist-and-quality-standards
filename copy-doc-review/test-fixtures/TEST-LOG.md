# copy-doc-review — test log

A running log of test runs of the `copy-doc-review` skill, what each run surfaced, and
what changed as a result. Newest entries at the top. The goal is to see, over time,
whether the agent is catching more of the right things, with less noise, more clearly.

## How we test (current method)

- **Fixture:** `test-fixtures/canonical-ceph.md` — a real Canonical Ceph product-page copy
  doc (Google Docs markdown export, table layout + embedded image blobs). Marketing page,
  no interactive flows.
- **Run:** apply the skill (default checklist + report template) to the fixture; save the
  output to `reports/canonical-ceph-YYYY-MM-DD.md`.
- **Caveat:** there is **no answer key** for this fixture, so runs are a *smoke test +
  gap-finder*, not a score. We can see whether the skill functions and whether obvious
  false positives/negatives appear — we cannot yet measure recall/precision. A seeded
  fixture with a known answer key is the planned next step for real measurement.

---

## Run 2026-06-05 (run 2) — after fixes #1 and #2

- **Skill version:** doc-type gate + needs-review bucket added.
- **Report:** `reports/canonical-ceph-2026-06-05-run2.md`
- **Result:** 10 findings (0 critical, 8 needs work, 2 minor) + 1 needs review + 2 N/A sections.
- **Input unchanged** — only the checklist/template rules changed, so differences are
  attributable to the fixes, not the doc.

**Delta vs baseline — both fixes verified working:**
- ✅ **Fix #1 (doc-type gate):** read Page type = "Product or service", and Forms & Inputs
  + Error & Feedback States now appear in a **⬜ Not applicable** section with reasons —
  *no false-critical*. The naive "missing error states = critical" failure is gone.
- ✅ **Fix #2 (needs-review bucket):** the canonical.com-vs-ubuntu.com domain question
  moved out of 🔵 Minor into **❓ Needs review** as an open question for a human —
  exactly the honest handling we wanted. Also bumped to priority #2 since it affects every
  link.
- Counts shifted (12→10 issues) only because the domain item left the severity buckets for
  needs-review; the substantive findings are otherwise stable run-to-run. Good sign for
  consistency.

**Process note (skill limitation found while testing):** the skill auto-saves to
`reports/[slug]-YYYY-MM-DD.md`, so a same-day re-run *overwrites* the previous report. For
testing we manually suffixed `-run2`. Worth deciding whether the skill should add a run
counter or timestamp when a file for that date already exists.

**Still open:** ~~double-reporting instruction (#1),~~ ~~thresholds for subjective checks (#3),~~
~~misplaced asset rule (#5),~~ and the bigger one — ~~a seeded fixture with an answer key so we
can actually score recall/precision rather than eyeball deltas.~~

**Closed 2026-06-17:** #1 (double-reporting) and #5 (misplaced asset rule) resolved by the
page-order reporting change — issues are now listed by page section, not by category, so
the same text no longer gets reported under multiple headings.

---

## Run 2026-06-05 — first run (baseline)

- **Skill version:** default checklist + template *as originally written* (before the
  fixes below).
- **Report:** `reports/canonical-ceph-2026-06-05.md`
- **Result:** 12 findings (0 critical, 8 needs work, 4 minor). Ran end-to-end.

**What worked**
- Parsed the Google Docs table scaffolding (`[col:1, ch:60]` markers) and saw past the
  embedded base64 image blobs to the real copy.
- Caught genuinely useful issues: declared main action ("Try Canonical Ceph") not matching
  any on-page CTA; raw-URL blog link text; a resource missing its destination; unfilled
  `[ALT TEXT]` placeholders; an asset hosted on Google Drive instead of the asset manager.
- Citations pointed to real text; "what looks good" was specific.

**Gaps found (confirmed live)**
1. **False-critical risk on a static page.** Error #1 + the SKILL edge case "missing error
   copy is a critical gap" would, run naively, flag absent error states as critical on a
   marketing page. Had to override to N/A by hand.
2. **No "needs review" bucket in output.** The canonical.com-vs-ubuntu.com domain question
   is unverifiable from the text; the template had only Pass + 3 severities, so it got
   buried as a Minor.
3. **Double-reporting.** Placeholders legitimately hit both Completeness and
   Comments&Revisions; alt text hit both Accessibility and Completeness. Deduped by hand.
4. **No thresholds for subjective checks** (e.g. "scannable, not too dense") — judgment
   calls without an anchor, so not repeatable.

**Changes made after this run**
- **Fix #1 — doc-type gate.** SKILL Step 1 now captures Page type; Step 2 gates sections
  by doc type (marketing pages mark Forms / Error states / interactive Completeness as
  N/A, don't flag their absence). Edge-case row made doc-type-aware. Applicability notes
  added to checklist sections 4, 5, 8.
- **Fix #2 — needs-review bucket.** Report template gained a ❓ Needs Review column in the
  summary, a Needs review section, and a Not applicable section (with reasons). SKILL
  Step 2 instructs the agent to use ❓ needs review for anything unverifiable from text.

**Still open (not yet fixed)**
- ~~Double-reporting / "report each finding once" instruction (gap #3).~~ Closed 2026-06-17 — resolved by page-order reporting.
- ~~Thresholds for subjective checks (gap #4).~~ Closed 2026-06-17 — replaced vague tone/clarity items with measurable thresholds (sentence length, paragraph length, reading grade, acronym rule, active voice).
- ~~No seeded fixture with answer key~~ — done: `test-fixtures/test-copy-doc.md` + `test-copy-doc-answer-key.md`.

**Next run should check:** that the doc-type gate removes the false-critical (Error states
shows as N/A, not critical) and that the domain question lands in ❓ Needs review.
