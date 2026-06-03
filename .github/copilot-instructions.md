# Automated UX QA checklist and quality standards

This repo contains three skills for UX content reviews on the Canonical websites team. One skill per stage of the design and publishing workflow.

## The pipeline

| Stage | Skill | Input | Trigger |
|---|---|---|---|
| 1. Copy doc | `copy-doc-review/` | Google Doc exported to markdown | Jira automation pings UX designer to review |
| 2. Figma | `figma-ux-content-audit/` | Figma file URL + optional copy doc | Visual designer comments in Jira requesting UX review |
| 3. Live/demo URL | `url-ux-audit/` | Live or demo URL | Dev opens GitHub PR, UX designer changes label to UX +1 |

Each skill runs independently. Approvals and handoffs are managed in Jira. No Jira or GitHub integration in the skills yet — planned for after testing.

## Skill structure

Each skill follows the same pattern:

```
skill-name/
├── SKILL.md               # Workflow instructions
├── references/
│   ├── default-checklist.md   # UX best practice checks
│   └── report-template.md     # Output format
└── reports/               # Saved audit reports (slug-YYYY-MM-DD.md)
```

## Current status

- `url-ux-audit/` — working, has real reports from April–May 2026
- `figma-ux-content-audit/` — working, has real reports from April 2026
- `copy-doc-review/` — built, not yet tested

## Next steps

1. Test `copy-doc-review` against a real copy doc
2. Refine checklists and report templates based on test results
3. Add Jira and GitHub PR integration as optional inputs once reviews are solid
