# Running the UX review locally

This guide explains how to run the automated UX review on your own machine using
[run_review.py](run_review.py) – the single command a designer runs with just a
GitHub PR link. It covers **every dependency** and its setup.

The runner drives the three review skills (copy doc, Figma, demo) through the
GitHub Copilot CLI and saves a report per stage. It is platform-agnostic
(Linux / macOS / Windows).

---

## TL;DR

Easiest: use the interactive launcher. It creates a local `.venv`, installs the
Python dependencies into it, then asks for the PR URL and which review(s) to
run:

```bash
python3 review.py
```

You can also skip the prompts by passing the PR URL (and any flag) straight
through:

```bash
python3 review.py "https://github.com/canonical/canonical.com/pull/1444" --comment
```

Prefer to call the runner directly (managing your own environment)? Once
everything below is set up:

```bash
# Run all applicable stages for a PR
python3 run_review.py "https://github.com/canonical/canonical.com/pull/1444"

# Run and post the combined report back to the PR as a comment
python3 run_review.py "https://github.com/canonical/canonical.com/pull/1444" --comment
```

The designer only ever provides the **PR URL**. The copy doc, Figma, and demo
links are parsed automatically from the PR body.

---

## Dependencies overview

| Dependency | Needed for | Required? |
|---|---|---|
| Python 3.9+ | Running the scripts | Always |
| GitHub Copilot CLI (`copilot`) | Running every review stage | Always |
| GitHub CLI (`gh`) | Reading the PR body, posting the comment | Always |
| Python packages (`google-auth`, `requests`) | Fetching the copy doc from Google | Copy doc stage |
| Google service-account key (`google-auth.json`) | Fetching a private Google Doc headlessly | Copy doc stage |
| Figma MCP server (remote login **or** local PAT server) | Extracting Figma content | Figma stage |

Stages whose dependency is missing are **skipped** automatically – you can run
demo-only reviews without ever setting up Google, for example.

---

## 1. Python 3

Check you have Python 3.9 or newer:

```bash
python3 --version
```

If not, install from [python.org](https://www.python.org/downloads/) or your
package manager (`brew install python`, `sudo apt install python3`, etc.).

---

## 2. GitHub Copilot CLI

The `copilot` binary runs each review. Install it and sign in:

```bash
npm install -g @github/copilot     # requires Node.js 18+
copilot                            # first run: follow the prompt to sign in with GitHub
```

Verify:

```bash
copilot --version
```

You need an active GitHub Copilot subscription. See the
[GitHub Copilot CLI docs](https://github.com/github/copilot-cli) for details.

> **Cost note:** each stage consumes Copilot AI credits (a full Figma review is
> roughly 80 credits / a few minutes). Multi-stage runs cost proportionally more.

---

## 3. GitHub CLI (`gh`)

Used to read the PR body and (with `--comment`) post the report. Install and
authenticate:

```bash
# Install — see https://cli.github.com for your platform
#   macOS:  brew install gh
#   Linux:  sudo apt install gh   (or the official apt repo)
gh auth login
```

Verify:

```bash
gh --version
gh auth status
```

Your account needs read access to the PR's repo, and write access (to post
comments) if you use `--comment`.

---

## 4. Python packages (copy doc stage)

Only needed if you want the copy doc stage to fetch a Google Doc.

**If you use `review.py`, you can skip this** – the launcher creates a local
`.venv` and installs these for you automatically.

To set it up manually instead, install into a virtual environment:

```bash
cd demo-review/scripts
python3 -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -r requirements.txt     # google-auth + requests
```

If you use a venv, run `run_review.py` with that same interpreter (or keep the
venv activated) so the copy doc fetch can import `google-auth`.

---

## 5. Google service-account key (copy doc stage)

The copy doc stage exports a **private** Google Doc without a browser, using a
service-account key.

1. In [Google Cloud Console](https://console.cloud.google.com/), create (or
   reuse) a project and a **service account**.
2. Enable the **Google Drive API** for the project.
3. Create a **JSON key** for the service account and download it.
4. Save it as **`demo-review/scripts/google-auth.json`**.
   - This path is gitignored – the key is never committed.
   - Alternatively set `GOOGLE_AUTH_JSON=/path/to/key.json`, or pass
     `--auth PATH` to `fetch_google_doc.py`.
5. **Share each copy doc** (or a shared Drive folder) with the service account's
   `client_email` (found inside the JSON) as **Viewer**. Without this the fetch
   returns `404 File not found`.

The key resolution order is: `--auth` → `$GOOGLE_AUTH_JSON` →
`demo-review/scripts/google-auth.json`.

> If this step is skipped, the copy doc stage is skipped and the Figma/demo
> stages still run.

---

## 6. Figma MCP server (Figma stage)

The Figma stage extracts design content through a Figma MCP server. The runner
looks for a `figma` server already registered with the CLI and uses it. If none
is registered, it automatically injects the official **remote** server so it
works out of the box.

Pick **one** of the two authentication paths below.

### Option A – Remote server + browser login (default, zero config)

Nothing to register – the runner injects the official remote server
(`https://mcp.figma.com/mcp`). You just authenticate once; the OAuth token is
cached afterwards:

```bash
copilot
# then, at the prompt, ask it to use the Figma MCP against any file you can open:
> Use the figma MCP server to get metadata for https://www.figma.com/design/<a-file-you-can-open>
```

Approve the access request in the browser that opens. After that, the runner
works unattended. You only need to repeat this if the token expires or you sign
out.

> The remote Figma MCP is available on all Figma plans (currently a free beta).

### Option B – Local server + personal access token (no browser)

If you prefer a headless setup with no interactive OAuth, install a local Figma
MCP server and register it with a Figma **personal access token (PAT)**. The
runner detects this registered `figma` server and uses it instead of the remote
default.

```bash
# 1. Install a local Figma MCP server (example package)
npm install -g figma-mcp            # provides the `mcp-figma` command

# 2. Create a PAT in Figma: Settings → Security → Personal access tokens
#    Scope it to read-only file access.

# 3. Register it with the CLI (stored in ~/.copilot/mcp-config.json)
copilot mcp add figma --env FIGMA_ACCESS_TOKEN=<your-token> -- mcp-figma
```

Verify it is registered:

```bash
copilot mcp get figma
```

> **Token safety:** the PAT is stored in **plaintext** in
> `~/.copilot/mcp-config.json`. Never commit that file or paste the token where
> it can be logged (terminal output, screen shares, tickets). If a token is ever
> exposed, revoke and regenerate it in Figma → Settings → Security. Treat the PAT
> like a password.

### Optional: using the Figma review inside VS Code chat

If instead you want to run the figma-review skill through **Copilot Chat in
VS Code** (not the local runner), register the server in your VS Code
`mcp.json` (`~/.config/Code/User/mcp.json` on Linux, or open the file via the
Command Palette → *MCP: Open User Configuration*):

```jsonc
{
  "inputs": [],
  "servers": {
    "figma": {
      "url": "https://mcp.figma.com/mcp",
      "type": "http"
    }
  }
}
```

The same one-time browser login applies. This block is **only** for the VS Code
chat path – it is not used by `run_review.py`.

---

## Usage

### One command (recommended)

```bash
python3 run_review.py "https://github.com/<owner>/<repo>/pull/<number>"
```

The runner:

1. Parses the PR body for the copy doc, Figma, and demo URL(s).
2. Fetches the copy doc from Google (once, reused by the copy doc and Figma stages).
3. Runs each applicable stage through Copilot.
4. Saves a report per stage under that stage's `reports/` folder.
5. Prints a summary. Any stage with a missing input is skipped.

### Post the combined report to the PR

```bash
python3 run_review.py "<PR_URL>" --comment
```

Collects the reports produced this run, combines them into one comment (each
report in a collapsible section), and posts it with `gh pr comment`. Kept opt-in
so posting to a shared PR is always deliberate.

### Run only some stages

```bash
python3 run_review.py "<PR_URL>" --demo-only
python3 run_review.py "<PR_URL>" --figma-only
python3 run_review.py "<PR_URL>" --copy-only
python3 run_review.py "<PR_URL>" --only figma,demo
python3 run_review.py "<PR_URL>" --skip demo
```

The explicit flags are mutually exclusive. If none are provided, the runner uses
its default behavior and runs all applicable stages.

Valid stage names: `copydoc`, `figma`, `demo`.

### Run a single stage directly

Each stage also has a standalone runner if you are not working from a PR:

```bash
# Figma (Figma URL, optional local copy doc for exact-match)
python3 figma-review/scripts/run_figma_review.py "https://www.figma.com/design/<key>/<name>?node-id=1-23"

# Demo (demo URL directly, or a PR URL)
python3 demo-review/scripts/run_demo_review.py "https://canonical-com-1444.demos.haus/data"

# Copy doc (fetch a Google Doc to markdown, then review it manually)
python3 demo-review/scripts/fetch_google_doc.py "https://docs.google.com/document/d/<id>/edit" --out /tmp/copydoc.md
```

---

## Where reports go

| Stage | Folder | Filename |
|---|---|---|
| Copy doc | `copy-doc-review/reports/` | `[slug]-[YYYY-MM-DD].md` |
| Figma | `figma-review/reports/` | `[slug]-[YYYY-MM-DD].md` |
| Demo | `demo-review/reports/` | `[slug]-[YYYY-MM-DD].md` |

---

## Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| `'copilot' … not found` | Copilot CLI not installed or not on `PATH`. See step 2. |
| `'gh' … is required` | GitHub CLI not installed or not authenticated (`gh auth login`). |
| Copy doc stage skipped, `404 File not found` | The doc is not shared with the service account's `client_email`. Share it as Viewer. See step 5. |
| Copy doc stage skipped, import error | `google-auth`/`requests` not installed, or wrong Python interpreter. See step 4. |
| Figma stage reports "MCP not authenticated" | Authenticate Figma – either do the one-time browser login (Option A) or register a local PAT server (Option B). See step 6. |
| No demo URL found for the PR | The PR body has no `demos.haus` URL and no page templates changed. Add a demo URL to the PR, or run the demo stage directly with the URL. |
| Figma review targets the wrong frame | Link to a specific frame – the Figma URL should include a `node-id=` parameter. |

---

## Security notes

- `google-auth.json` is gitignored and must never be committed.
- Reports may contain pre-release copy and design content. When using
  `--comment`, that content is posted to the PR – confirm the target repo's
  visibility is acceptable before posting.
- The runner writes the fetched copy doc to a temp file and deletes it after the
  run, so private copy is not left on disk.
