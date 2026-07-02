# UX content audit report – copy doc

**Document:** Rockcraft – Canonical's CLI tool for container images  
**Date:** 2026-06-24  
**Note:** Character counts were checked against the supplied copy doc fields. Readability and paragraph-length findings are based on the source copy, not the final designed layout.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor | ❓ Needs Review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | three | zero | seven | four | two | two |

**Total issues:** 11 (zero critical, seven needs work, four minor) · **Needs review:** two · **N/A sections:** Forms and inputs; interactive states in Completeness

---

## Issues by page section

### Metadata
#### 🟡 Needs Work
- **[Structure and hierarchy][Navigation]** The metadata table is not cleanly completed. The **Navigation** field still contains template instructions ("Please select the primary navigation…", "Bubble navigation", "For meganav or bubble navigation…") instead of a final navigation answer. This makes the intended placement unclear.
- **[Structure and hierarchy][Accessibility][Completeness]** **og:Image** is still a placeholder instruction, not an actual image link.
- **[Accessibility][Completeness]** **Link to asset manager tag** is blank, so asset provenance cannot be verified against the requirement to use asset-manager resources.

#### 🔵 Minor
- **[Comments and revisions]** Template/helper copy remains in multiple metadata rows, including **Page owner**, **og:Image**, and **Navigation**. These should be removed before handoff.
- **[Navigation]** The **Reference page(s)** and **Navigation** fields currently repeat similar information. Keep one source of truth for page location and use the navigation field only for the final placement path.

### Hero
#### 🔵 Minor
- **[Accessibility]** The hero image alt text is **"A rock"**, which is too generic to be useful. It should describe the image's purpose or content more specifically.

### Why Rockcraft?
#### 🔵 Minor
- **[Tone and clarity]** Two feature descriptions are harder to scan than they need to be:
  - **Minimal setup** – 33 words
  - **Seamless chiseling** – 31 words
  The checklist target is no sentence over 30 words.

### Developer workflow
#### 🟡 Needs Work
- **[Structure and hierarchy][Character limits]** The opening row combines the section title and description into one field: **"Developer workflow Learn about some of the high-level commands…"**. That combined string is **171 characters** and does not match the intended field structure (`[col:1, ch:60][col:5, ch:160]`).
- **[Structure and hierarchy][Completeness]** The multi-step flow is inconsistent: **1a**, **1b**, **2**, **3**, then **4. Publish** appears inline with the command instead of as a clearly separated step. This weakens scanability for a procedural section.
- **[Completeness]** The **Publish** step is not documented in the same pattern as the earlier steps. It needs a distinct step label, a separate code snippet block, and supporting explanatory copy.
- **[Tone and clarity]** The section mixes explanatory prose, code, and links unevenly, which makes the workflow feel less structured than the rest of the page.

### Developer-friendly, enterprise-ready
#### 🟡 Needs Work
- **[Character limits]** The audience tab labels exceed the stated **20-character** limit:
  - **Cloud-native developers** – 23
  - **Independent software vendors** – 28
  - **Individual developers** – 21
- **[Tone and clarity]** This section is too dense for marketing-page guidance. The overall supplied prose reads at an estimated **Flesch-Kincaid Grade 12.6**, above the target **Grade 7–9**. The tab copy is a major contributor.
- **[Tone and clarity]** At least two sentences in this section exceed the maximum recommended sentence length:
  - Tab one opening sentence – **35 words**
  - Final sentence in the third tab – **31 words**

### Technical deep dive
#### 🟡 Needs Work
- **[Accessibility]** The four images in this section have asset links but no alt text. Alt text is required for images/graphics in the copy doc.

#### 🔵 Minor
- **[Character limits]** Two card descriptions exceed the stated **180-character** limit:
  - **The parts lifecycle** – **199**
  - **Declarative chiseling** – **196**
- **[Tone and clarity]** There is a punctuation error in **The parts lifecycle** copy: **"stage,*"** should be corrected.

---

## ❓ Needs review
- **[Links]** Documentation links mix **/stable/**, **/latest/**, and version-pinned URLs (**/9.0/**, **/4.2/**). That may be intentional, but it should be checked for consistency and maintenance risk.
- **[Accessibility]** The page uses `assets.ubuntu.com` links, but the blank asset-manager-tag field means the asset source/approval trail is not fully documented in the copy doc.

## ⬜ Not applicable
- **Forms and inputs** – N/A for a marketing page.
- **Interactive states in Completeness** – N/A for a marketing page.

## ✅ What looks good
- The **page title** is within limit at **53 characters**.
- The **page description** is within limit at **114 characters**.
- Most CTA labels are clear, specific, and within limits:
  - **Read the docs** – 13
  - **Try the tutorials** – 17
  - **Read the how-to guides >** – 24
  - **Explore the GitHub repo >** – 25
- Link text is generally descriptive and avoids vague standalone labels like "click here."
- The page has a clear overall story: value proposition, reasons to care, workflow, audience benefits, technical depth, and closing CTA.
