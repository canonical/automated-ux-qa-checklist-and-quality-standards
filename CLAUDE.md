# Automated UX QA checklist and quality standards

This repo contains three Claude skills for UX content reviews on the Canonical websites team. One skill per stage of the design and publishing workflow.

## The pipeline

| Stage | Skill | Input | Trigger |
|---|---|---|---|
| 1. Copy doc | `copy-doc-review/` | Google Doc exported to markdown | Jira automation pings UX designer to review |
| 2. Figma | `figma-ux-content-audit/` | Figma file URL + optional copy doc | Visual designer comments in Jira requesting UX review |
| 3. Demo | `demo-review/` | Demo URL or GitHub PR URL | Dev opens GitHub PR, UX designer changes label to UX +1 |

Each skill runs independently. Approvals and handoffs are managed in Jira. No Jira or GitHub integration in the skills yet — planned for after testing.

## Skill structure

Each skill follows the same pattern:

```
skill-name/
├── SKILL.md               # Workflow instructions for Claude
├── references/
│   ├── default-checklist.md   # UX best practice checks
│   └── report-template.md     # Output format
└── reports/               # Saved audit reports (slug-YYYY-MM-DD.md)
```

## Current status

- `demo-review/` — working, has real reports from April–May 2026
- `figma-ux-content-audit/` — working, has real reports from April 2026
- `copy-doc-review/` — built, not yet tested

## Next steps

1. Test `copy-doc-review` against a real copy doc
2. Refine checklists and report templates based on test results
3. Build a purpose-made test doc with a known "answer key" — a sample copy doc with a fixed
   set of deliberately-planted issues, written down separately. This lets us *score* how
   many issues the skill catches (e.g. 18/20) and prove it improves when we tweak it, rather
   than eyeballing each run. Without it we can smoke-test but not measure. (Real authoring
   effort — deferred until the skill is otherwise solid.)
4. Clarify copy doc role in Figma audit — when a copy doc is provided at the Figma
   stage, the skill should ask whether it has already been through copy doc review
   (stage 1). If it has, treat it as the approved source of truth and only flag
   differences (not re-review copy quality). If it hasn't, note that in the report.
5. Add Jira and GitHub PR integration as optional inputs once reviews are solid
6. (Future) Turn the checks into a Figma plugin

## Test file

A real Canonical Ceph copy doc export is at:
`/home/sophie/skills/url-ux-audit/canonical.com_ceph.md`

Use this to test `copy-doc-review`.
