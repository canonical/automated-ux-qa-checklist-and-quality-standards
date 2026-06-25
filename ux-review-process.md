# UX content review process

## Purpose

This process keeps UX content quality high across Canonical websites by catching issues before pages go live. It provides a structured, repeatable review at three stages of the design and publishing workflow – copy doc, Figma design, and demo – so that problems are found early and do not compound downstream. UX designers on the Canonical websites team run AI-assisted skills that produce standardized audit reports at each stage.

---

## Inputs

| Input | Source | Notes |
|---|---|---|
| Copy document (markdown export) | Content author via Google Docs | Exported or copied into **.md** format before review begins |
| Figma file URL | Visual designer | The Figma draft created from the approved copy doc |
| Copy doc (optional, at Figma stage) | Content author | Provided alongside the Figma file for exact match comparison |
| Demo URL or GitHub PR URL | Developer | A deployed demo of the implemented page, or a PR that can be converted to a demo URL |
| Custom UX checklist (optional) | UX designer | Overrides or supplements the default checklist at any stage |

---

## Steps

### Stage 1 – Copy doc review

**Trigger:** Jira automation notifies the UX designer that a copy doc is ready for review.

1. Export the copy doc from Google Docs to markdown
2. Run the **copy-doc-review** skill with the markdown file as input
3. The skill parses the document, identifies the page type, gates checklist sections by type, and checks content against the UX best-practice checklist
4. The skill produces a structured audit report organized by page section order and saves it to **copy-doc-review/reports/**
5. Review the report and resolve critical and needs-work issues with the content author before the doc moves to design

### Stage 2 – Figma review

**Trigger:** The visual designer comments in Jira to request a UX review of the Figma draft.

1. Get the Figma file URL from the designer
2. Optionally, provide the approved copy doc for exact match comparison
3. Run the **figma-review** skill with the Figma URL and copy doc if available
4. The skill extracts all text content from the Figma file via MCP, runs an exact copy match if a copy doc is provided, and checks content against the UX checklist
5. The skill produces a structured audit report and saves it to **figma-review/reports/**
6. Review the report and resolve issues with the visual designer before the design moves to development

### Stage 3 – Demo review

**Trigger:** A developer opens a GitHub PR and the UX designer changes the label to indicate UX review is needed.

1. Get the demo URL directly, or provide the GitHub PR URL – the skill converts it automatically
2. Run the **demo-review** skill with the URL
3. The skill fetches the live page, extracts visible text content, and checks it against the UX checklist
4. The skill produces a structured audit report and saves it to **demo-review/reports/**
5. Review the report and resolve issues with the developer before the page is approved for launch

---

## Acceptance criteria

- [ ] Every checklist section applicable to the page type has been evaluated at each stage
- [ ] All 🔴 critical issues are resolved before the deliverable moves to the next stage
- [ ] All 🟡 needs-work issues are resolved – or explicitly accepted with justification – before the deliverable moves to the next stage
- [ ] 🔵 Minor issues are logged; resolution is encouraged but not blocking
- [ ] An audit report has been saved for each stage that was run
- [ ] The report follows the Canonical copy style guide – en dashes with spaces, US English, serial commas, and no gendered pronouns

---

## Outputs

| Output | Description |
|---|---|
| Audit report (per stage) | A structured markdown report listing issues by page section with severity, evidence citations, and recommendations |
| Approval to proceed | Confirmation that acceptance criteria are met and the deliverable can move to the next stage |

---

## Artifacts

| Artifact | Location | Format |
|---|---|---|
| Copy doc audit report | **copy-doc-review/reports/[slug]-[YYYY-MM-DD].md** | Markdown |
| Figma audit report | **figma-review/reports/[slug]-[YYYY-MM-DD].md** | Markdown |
| Demo audit report | **demo-review/reports/[slug]-[YYYY-MM-DD].md** | Markdown |
| Default UX checklists | **[skill]/references/default-checklist.md** | Markdown |
| Report templates | **[skill]/references/report-template.md** | Markdown |
| Jira ticket (approval record) | Jira | Updated with review status and link to report |
