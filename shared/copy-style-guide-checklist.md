---
title: Canonical copy style guide — review checklist
type: Checklist
status: Unofficial
source_of_truth: false
derived_from: copy-style-guide-ai.md (unofficial mirror of the official Google Doc)
provenance: Distilled for automated/agentic review. Added 2026-06-03.
---

> **⚠️ Unofficial — derived file.** This is a condensed, checkable version of the
> Canonical copy style guide, built for the UX QA review skills to apply
> consistently. It is **derived from** `copy-style-guide-ai.md`, which is itself an
> **unofficial** markdown mirror of the official Google Doc. The Google Doc is the
> source of truth. If anything here conflicts with the official guide, the official
> guide wins. When the official guide changes, re-sync the mirror first, then update
> this checklist.

# Canonical copy style guide — review checklist

Brand and house-style checks, separate from the UX best-practice checklists. Report
findings under their own **Brand & style compliance** heading, not mixed in with UX
quality issues.

The checks are split into two kinds, because an agent should treat them differently:

- **Deterministic checks** — exact, string-level rules. High precision: an agent (or a
  simple regex pass) can flag these reliably and cite the exact text. Default to
  flagging any match.
- **Judgment checks** — require reading and reasoning. Lower precision: apply the
  examples and thresholds given, and when genuinely unsure mark **needs review**
  rather than guessing.

### Severity note for style findings

Unlike UX issues, most style issues do **not** block design or development — they are
polish. Use this scale:

- 🔴 **Critical** — creates legal, compliance, or brand-integrity risk: unprovable
  security/absolute claims, or wrong official product names.
- 🟡 **Needs work** — banned words/phrases, wrong capitalization, voice/tone misses,
  passive-heavy copy, non-descriptive link text.
- 🔵 **Minor** — punctuation, units, number/date formatting, dash style.

---

# Part A — Deterministic checks

## A1. Spelling — US English

- [ ] US spellings used throughout (external copy). Flag UK variants:

| Flag (UK) | Correct (US) |
|---|---|
| licence (noun) | license |
| defence | defense |
| programme (IT/software) | program |
| per cent | percent |
| data centre | data center |
| sceptical | skeptical |
| catalogue | catalog |
| travelling / travelled | traveling / traveled |
| -ise (organise, virtualise) | -ize (organize, virtualize) |
| -our (colour, behaviour, favour) | -or (color, behavior, favor) |
| -eable | -able |

## A2. "open source"

- [ ] Lowercase, two words, no hyphen — **except** in proper names (Open Source Initiative, Open Source Definition).
- [ ] Flag: `open-source`, `opensource`, and capitalized `Open Source` used as a common term mid-sentence.

## A3. Product and service names

- [ ] `Ubuntu`, never `Ubuntu Linux`. Capital U. Singular entity ("Ubuntu is", not "Ubuntu are").
- [ ] Specific releases use the **full** name incl. `LTS`: `Ubuntu 14.04 LTS`, not `Ubuntu 14.04`.
- [ ] First mention uses full product name, later mentions may simplify (e.g. `Ubuntu Server 21.04` → `Ubuntu Server` → `Ubuntu`).
- [ ] `Ubuntu Server` (capital S), never `Ubuntu server`. `Ubuntu on phones`, never `Ubuntu Phone`.
- [ ] `Ubuntu Pro` — flag legacy/incorrect: `Ubuntu Advantage`, `UA`, `UA-I`, `Ubuntu Pro Apps`, `Ubuntu Pro Infrastructure`, `Pro infra`.
- [ ] `Expanded Security Maintenance` / `ESM` — flag `Extended Security Maintenance`.
- [ ] `End of Standard Support` — flag `End of Life` / `EoL`.
- [ ] Lowercase except at start of sentence/heading: `charm`, `snap`, `chiseled`. (`Charm`, `Snap`, `Chisel` only sentence-initial.)
- [ ] `MicroCloud` — capital M, capital C.
- [ ] Other official names capitalized as listed: `Juju`, `Charmhub`, `Snapcraft`, `Snapd`, `Real-time Ubuntu`, `ROCKs`, `MAAS`, `Landscape`, `Windows Subsystem for Linux (WSL)`, `Ubuntu WSL`.

## A4. Capitalization

- [ ] Headings and headlines in **sentence case** (first word + proper nouns only). Flag Title Case headings.
- [ ] Don't capitalize keywords, technical terms, or jargon: `cloud` not `Cloud`, `hyperscale` not `Hyperscale`.
- [ ] Organizations lowercase on second reference: `the university`, `the bank`, `the assembly`.
- [ ] Job titles lowercase mid-sentence; capitalized only as a quote attribution.

## A5. Units

- [ ] No space between value and unit: `3GB`, not `3 GB`. Applies to `b, KB, MB, GB, TB, GHz`.

## A6. Dates

- [ ] Prose format: `January 1, 2013`; same-month range `January 1-2, 2013`; cross-month `January 1 - February 2, 2013`.
- [ ] Technical material: ISO 8601 `YYYY-MM-DD`.
- [ ] Flag: `1st January 2013`, `01 January 2013`, `1 Jan 2013`, and slash dates (`dd/mm/yyyy`, `mm/dd/yyyy`).

## A7. Numbers

- [ ] Spell out single-figure numbers (one–nine); use digits from 10 up. (Exceptions: numbered lists, units of measurement.)
- [ ] Commas in numbers over 999: `7,000`, not `7000`.
- [ ] `24/7`, not `24x7`.

## A8. Punctuation

- [ ] **No exclamation marks** in webpage copy (allowed in blogs/other forms).
- [ ] Single question mark only.
- [ ] Serial (Oxford) comma used in in-sentence lists.
- [ ] Quotation punctuation sits **inside** the quotes: `Mark said "I like that,"` not `"I like that",`.
- [ ] **En dash with spaces** (` – `) for sentence breaks. Flag em dash (`—`) and hyphen (` - `) used as a sentence break.

## A9. Apostrophes, plurals, possessives

- [ ] No apostrophe in decades or plural acronyms: `1990s`, `MPs`, `ISVs` — flag `1990's`, `MP's`, `ISV's`.
- [ ] `it's` = it is / `its` = possessive; `you're` = you are / `your` = possessive. Flag misuse.

## A10. Acronyms and abbreviations

- [ ] Acronyms spelled out in full on first mention with the acronym in brackets, e.g. `Enterprise resource planning (ERP)`; acronym only thereafter. (Exceptions: very common — BBC, IT.)
- [ ] Country/entity acronyms: no periods. `US` not `U.S.`/`USA`; `UK` not `U.K.`/`GB`; `EU`, `UN`, `UAE` likewise.
- [ ] Don't abbreviate company names (`Microsoft`, never `MSFT`); don't use `&` for `and`.
- [ ] Latin abbreviations: avoid `e.g.` / `i.e.` / `etc.` on webpages (use "for example", "meaning that", "and more"). If used, format `e.g.,` and `i.e.,` (two periods + comma).

## A11. Links and CTAs (brand-specific)

- [ ] No `Click here`, `Read more`, or `See more` as link text. Use descriptive text: `Learn more about [Product/use case]`.
- [ ] `download` as a button verb **only** if the click auto-starts the download; otherwise use `get`.

*(Generic link descriptiveness is owned by the UX checklist — report a given link issue in only one place to avoid double-counting.)*

## A12. Hyphens

- [ ] Hyphenate compound adjectives before a noun: `cloud-based`, `cost-effective`, `enterprise-ready`, `high-availability`, `third-party`, `web-based`, `30-day`.
- [ ] `real time` is two words **unless** used as an adjective before a noun (`real-time events`); `Real-time Ubuntu` is the product name.

## A13. Words and phrases to avoid

- [ ] Flag the following (with suggested replacement):

| Avoid | Reason / use instead |
|---|---|
| allow | implies we grant permission |
| the ability to / is able to | "we can" / "Ubuntu can" |
| not only… but also… | wordy |
| metal / bare metal | — |
| eliminate, execute, terminate, kill | negative/violent connotation |
| disruptive, explosive | — |
| leverage | use |
| going forward | — |
| in order to | to |
| form factor | — |
| end user | user |

- [ ] Flag flowery words → plain English: `assist→help`, `alleviate→ease`, `ameliorate→improve`, `approximately→about`, `ascertain→learn`, `attempt→try`, `cease/desist→stop`, `commence/initiate→begin`, `facilitate→help`, `for the purpose of→to`, `in conjunction with→with`, `magnitude→size`, `necessitate→need`, `numerous→many`, `prior to→before`, `possesses→has`, `purchase→buy`, `regarding/with regard to→about`, `requested→asked`, `subsequently→later`, `utilize→use`, `whilst→while`.

## A14. Consistency spellings

- [ ] Use these forms (and stay consistent within a doc): `email`, `online`, `setup` (noun) / `set up` (verb), `backup` (noun) / `back up` (verb), `web`, `website`, `internet`, `systems management`, `virtualization`, `multi-cloud`, `whitepaper`, `dos and don'ts`, `on premises`.

## A15. Formatting conventions

- [ ] Code terms in running text styled **bold** (e.g. **index.html**, **run**). Code snippets in code blocks.
- [ ] List items: capital first letter; same sentence structure across items; **no** end periods when all items are one sentence or less; use periods throughout if **any** item has more than one sentence.
- [ ] Emphasis: double quotes for a coined term; italics for emphasizing a common word; bold for a term being defined (only on first/defining use).

---

# Part B — Judgment checks

Apply with the examples below. When you can't reasonably tell, mark **needs review**.

## B1. Brand voice

- [ ] Reads as a **friendly expert** — confident and authoritative, but approachable:
  - Authoritative, not arrogant (accurate, honest; explains without condescension).
  - Precise, not pedantic (clear and to the point; no convoluted sentences).
  - Approachable, not shallow (accessible but with real depth).
  - Confident, witty, playful — without losing substance.

## B2. Tone

- [ ] Tone is expert, witty, precise, relatable, and clear. Flag copy that is boring/corporate, hedging, or over-formal.

## B3. Sentence length (measurable)

- [ ] Average sentence length is **12–20 words**. Flag sections whose average clearly exceeds 20, and call out individual very long/dense sentences.

## B4. Readability (measurable)

- [ ] Flesch-Kincaid roughly: **Grade 7** for email/website copy; **Grade 12** for articles, ebooks, whitepapers. Flag copy well above target for its type.

## B5. Active voice

- [ ] Prefer active, subject-verb-object sentences. Flag passive constructions (`The company was joined by Fred` → `Fred joined the company`), especially in web copy.

## B6. Security and absolute claims

- [ ] 🔴 Flag hyperbolic / unprovable security and absolute claims. Avoid → use instead:

| Avoid | Use instead |
|---|---|
| Secure open source (software) | Trusted open source |
| Most secure operating system | Designed with security in mind |
| Security-guaranteed / Always secure | Security-maintained / Maintained / Supported |
| Fully secured supply chain | We help you secure your open source supply chain |
| Game-changing, Revolutionary | (state the specific benefit instead) |

## B7. Superlatives

- [ ] Don't use unjustified superlatives. Flag unless backed by a verifiable fact: `unique, first, only, sole, fastest, largest, best, most, unprecedented, exceptional`, and phrases like `best in class`, `best of breed`, `cutting edge`, `state-of-the-art`, `latest and greatest`, `one-of-a-kind`.

## B8. Inclusive language

- [ ] No gendered pronouns — use `they/them`.
- [ ] No ableist words (`see`, `hear`) — use `explore`, `access`, `learn more`.
- [ ] Avoid words with racist/misogynist origins (`middleman` → `middle person`; `outmanned` → `under-resourced`).

## B9. Commonly confused words

- [ ] Check correct usage where context makes it clear: `affect/effect`, `continual/continuous`, `discreet/discrete`, `fewer/less`, `that/which`, `login` (noun) / `log in` (verb), `principle/principal`, `stationary/stationery`, `dependent/dependant`.

## B10. Plain language and jargon

- [ ] Plain language appropriate to the audience; assume nothing. Define unfamiliar terms and acronyms on first use. Use industry jargon sparingly for non-technical audiences.

---

## How to report

- Put all findings under a **Brand & style compliance** section, separate from UX quality.
- Cite the exact text and section, and give the corrected version where there is one.
- For deterministic checks, flag every match. For judgment checks, apply the examples and use **needs review** when genuinely uncertain rather than guessing.
- Report any single piece of text once — if it's also covered by the UX checklist (e.g. link text), don't double-count it across both reports.
