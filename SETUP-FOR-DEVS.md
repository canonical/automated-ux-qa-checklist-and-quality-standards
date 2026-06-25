# How to add automated UX review to your repo

## What it does

When a PR gets the `Review: UX needed` label, a workflow automatically:

1. Reads your PR description to find the demo URL, Figma link, and copy doc link
2. Runs a UX content and design fidelity check
3. Posts a checklist report as a PR comment that a UX designer can tick off

## What you need to do

### 1. Add a caller workflow to your repo

Create `.github/workflows/ux-review.yml`:

```yaml
name: UX demo review

on:
  pull_request_target:
    types: [labeled]

jobs:
  ux-review:
    if: github.event.label.name == 'Review: UX needed'
    uses: canonical/automated-ux-qa-checklist-and-quality-standards/.github/workflows/ux-demo-review.yml@main
    with:
      pr_number: ${{ github.event.pull_request.number }}
    secrets: inherit
```

That is the only file you need to add.

### 2. Make sure your PR description includes these links

The automation detects inputs by URL domain – it does not matter where in the PR body they appear or what you call them:

| Link | How it's detected | Example |
|---|---|---|
| Demo URL | Any `*.demos.haus/*` URL | `https://ubuntu-com-16495.demos.haus/security/nis2` |
| Figma design | Any `figma.com/design/*` URL | `https://www.figma.com/design/abc123/...?node-id=5228-2818` |
| Copy doc | Any `docs.google.com/document/*` URL | `https://docs.google.com/document/d/1M3V.../edit` |

**Important:** Link to the specific Figma frame using a URL that includes `node-id=`. If you link to the top-level file without a node ID, the review may not target the correct frame.

### 3. Confirm the `Review: UX needed` label exists

Both `canonical/ubuntu.com` and `canonical/canonical.com` already have this label. If your repo does not, create it:

```bash
gh label create "Review: UX needed" --color cdcdcd
```

## What you do not need to change

- Your existing PR template already includes demo, Figma, and copy doc links
- No new fields or metadata are required
- The `Review: UX needed` label is already part of the existing review workflow

## What the report looks like

The automation posts a PR comment with:

- **Copy fidelity checks** – text mismatches between the demo and the copy doc
- **Design fidelity checks** – spacing, typography, and color differences vs. Figma
- **UX quality checks** – CTAs, accessibility, navigation, structure
- **Manual checks** – checkboxes for things only a human can verify (responsive layout, keyboard navigation, form submission)

Every issue is a checkbox. The UX designer ticks off items as they verify or confirm fixes.

## Questions

If something is not working or the automation is not picking up your links, check:

1. Does your PR body contain a `demos.haus` URL? (The parser looks for this domain specifically.)
2. Does your Figma link include a `node-id` parameter? (Right-click a frame in Figma and select "Copy link" to get this.)
3. Is the `Review: UX needed` label applied to the PR? (The workflow only triggers on this label.)

For issues with the review itself, reach out to the UX team or file an issue in [automated-ux-qa-checklist-and-quality-standards](https://github.com/canonical/automated-ux-qa-checklist-and-quality-standards).
