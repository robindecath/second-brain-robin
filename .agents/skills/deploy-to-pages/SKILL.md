---
name: deploy-to-pages
description: >
  Deploys the current repository's static site or docs to Decathlon Pages,
  publishing a private site (gated behind Decathlon SSO) at
  https://<subdomain>.pages.dktapp.cloud. Activate when the user says "deploy to
  pages", "publish to Decathlon Pages", "ship this site/docs to pages", or asks
  to set up pages deployment for a repo. Ensures the repo has a GitHub upstream
  in the dktunited org (creating one if needed), adds a GitHub Actions workflow
  that uses the `dktunited/pages/.github/actions/deploy-pages@main` action if
  missing, triggers the deployment via workflow_dispatch, follows the run to
  completion using the gh CLI, then shares and opens the resulting pages URL.
  Also covers Markdown-only repos with no index.html, which Pages renders
  itself from index.md, README.md and the repo's assets.
license: MIT
metadata:
  audience: developers
  domain: platform-engineering
  api: github-actions+gh-cli
  mcp_required: false
---

# Deploy to Pages Skill

Publishes a repo's static site or documentation to **Decathlon Pages**
(`https://<subdomain>.pages.dktapp.cloud`) via a self-hosted GitHub Actions
workflow, then follows the run and opens the result.

Decathlon Pages is the internal, SSO-gated equivalent of GitHub Pages: every
published site lives on its own subdomain, is private by default (behind
Decathlon login), serves any static content (HTML, Markdown, TXT, PDF), and has
built-in full-text search across published pages. Learn more at
https://pages.dktapp.cloud.

**A site does not have to ship HTML.** If the repo has no `index.html`, Pages
renders the content itself: push the Markdown files with their assets (images,
PDFs) and source files, and every page is served with navigation, a file tree
and syntax highlighting. Two things to know before deploying such a repo:

- **`index.md` is the homepage.** A root `index.md` answers
  `https://<subdomain>.pages.dktapp.cloud`, and `docs/index.md` answers
  `/docs` — the same role `index.html` plays on a classic static host. This is
  the file to get right: without it the site root falls back to a listing
  instead of a real landing page.
- **`README.md` is rendered too.** A folder with no index shows a browsable
  file listing, with that folder's `README.md` rendered underneath it, the way
  GitHub displays a repository. Useful, but a deliberate `index.md` still reads
  much better as an entry point.

Source and configuration files (`.ts`, `.py`, `.yaml`, …) get a highlighted
view, and media files a preview, so a repo of docs plus assets is browsable
as-is. Sites that do ship their own `index.html` keep full control of their
rendering — Pages serves them untouched.

⚠️ **Hard requirement:** this only works for repositories under the
**`dktunited`** GitHub org. The `deploy-pages` action refuses to run for any
other owner, and it relies on self-hosted `decathlon`-tagged runners plus a
shared GCS bucket (`pages-dkt-fktf`) and a workload-identity provider that are
only wired up for that org. If the repo's upstream is anywhere else, **stop and
explain this** instead of trying to deploy.

---

## When to Activate

- User says "deploy to pages", "publish to pages", "ship this to Decathlon Pages"
- User asks to set up/configure pages deployment for the current repo
- User asks to re-trigger or check a pages deployment

Pages vs Protos: **Protos** (`deploy-to-protos`) is for throwaway
prototypes/demos on `*.protos.dktapp.cloud`. **Pages** is for longer-lived,
SSO-gated internal sites and documentation on `*.pages.dktapp.cloud` with
built-in search. Pick the one the user actually asked for.

---

## Step 1 — Preconditions

1. Confirm `gh` CLI is authenticated: `gh auth status`. If not, ask the user
   to run `gh auth login` first and stop.
2. From the repo root, check for an upstream: `git remote -v`.

---

## Step 2 — No upstream: create the GitHub repo

1. Derive a candidate repo name from the current directory name: lowercase,
   kebab-case, strip characters that aren't `[a-z0-9-]`. This name also becomes
   the site's subdomain (`<name>.pages.dktapp.cloud`) unless a custom `folder`
   is set in Step 4.
2. Check availability: `gh repo view dktunited/<name>` — a 404/`GH_ERR` means
   it's free; any success output means it's taken.
3. **Always confirm the name with the user before creating anything** using
   `ask_user` with the proposed name as a suggested choice, plus room for a
   freeform override. Remind them the name is also the public subdomain. Do not
   silently pick a fallback name.
4. Create the repo under the org (never personal account):
   ```bash
   gh repo create dktunited/<name> --private --source=. --remote=origin
   ```
5. Push the current branch as `main` so the workflow's `push: branches: [main]`
   trigger and `--ref main` dispatch both have something to target:
   ```bash
   git push -u origin HEAD:main
   ```

---

## Step 3 — Has upstream: validate it's in-scope

1. Parse the `origin` remote URL (supports both `git@github.com:org/repo.git`
   and `https://github.com/org/repo.git` forms).
2. If the org is not `dktunited`, **stop** and tell the user: pages deploys need
   the `deploy-pages` action (which hard-checks `dktunited` ownership),
   self-hosted `decathlon` runners, and a shared bucket only available to
   `dktunited` org repos — this repo can't be deployed as-is. Do not attempt to
   fork or transfer the repo automatically.

---

## Step 4 — Ensure the workflow file exists

1. Check for an existing pages workflow: look for any `.github/workflows/*.yml`
   or `*.yaml` file that uses `dktunited/pages/.github/actions/deploy-pages`
   (grep the workflows directory — the filename itself may vary).
2. **If found:** leave it as-is. Don't overwrite a working config. Note its
   path and move to Step 5.
3. **If missing:**
   - Auto-detect a candidate build/output directory by checking, in order,
     whether these exist at the repo root: `dist`, `build`, `out`, `public`,
     `_site`, `site`. A repo may also ship a pre-built static folder that is
     committed directly (no build step).
   - **No build and no HTML?** A documentation repo made of Markdown and assets
     needs no build directory at all: point `directory` at the folder holding
     the docs (often `.` for the repo root, or `docs`) and Pages renders it.
     Before deploying that way, check the folder has an `index.md` at its root;
     if it doesn't, tell the user their site root will be a file listing and
     offer to add one (a short landing page linking to the main documents).
   - Ask the user (via `ask_user`) to confirm or override the detected
     directory, and to confirm the **subdomain** to publish under (defaults to
     the repo name; only set a custom `folder` if they want a different
     subdomain).
   - Check whether the detected directory is **already committed to the repo**
     (a pre-built static output) or needs to be **produced by a build step**
     (there's a `package.json` with a `build` script but the output directory
     isn't tracked in git).
   - The `deploy-pages` action inputs are:
     - `directory` (**required**) — local folder containing the static files to
       upload.
     - `folder` (optional) — destination folder in the bucket, which becomes the
       subdomain. Defaults to the repository name (lowercased). Must be a
       relative path with no `..` segments.
   - If a build step is needed, use this template (adapt the install/build
     commands to the repo's actual toolchain/package manager):
     ```yaml
     name: Deploy site to Decathlon Pages

     on:
       push:
         branches: [main]
       workflow_dispatch:

     permissions:
       contents: read
       id-token: write

     jobs:
       deploy:
         runs-on: [self-hosted, decathlon]
         steps:
           - uses: actions/checkout@v6
           - uses: actions/setup-node@v6
             with:
               node-version: 24
           - uses: pnpm/action-setup@v6
           - run: pnpm install --frozen-lockfile
           - run: pnpm build

           - name: Deploy to Decathlon Pages
             uses: dktunited/pages/.github/actions/deploy-pages@main
             with:
               directory: <confirmed-directory>
               # folder: <custom-subdomain>   # optional; defaults to repo name
     ```
   - If the directory is already committed (nothing to build), omit the
     setup-node/pnpm/build steps and go straight from checkout to deploy:
     ```yaml
     name: Deploy site to Decathlon Pages

     on:
       push:
         branches: [main]
       workflow_dispatch:

     permissions:
       contents: read
       id-token: write

     jobs:
       deploy:
         runs-on: [self-hosted, decathlon]
         steps:
           - name: Checkout
             uses: actions/checkout@v6

           - name: Deploy to Decathlon Pages
             uses: dktunited/pages/.github/actions/deploy-pages@main
             with:
               directory: <confirmed-directory>
               # folder: <custom-subdomain>   # optional; defaults to repo name
     ```
   - Optionally scope the `push` trigger with `paths:` (e.g. the site directory
     and the workflow file) so unrelated commits don't redeploy — mirror the
     repo's existing conventions if any.
   - Commit and push directly to `main`:
     ```bash
     git add .github/workflows/deploy-pages.yaml
     git commit -m "Add Decathlon Pages deployment workflow"
     git push origin HEAD:main
     ```
   - No repo secrets are required — the action authenticates via direct
     workload identity (`id-token: write`), which is pre-configured at the org
     level. The action writes the deployment URL and bucket path to the job
     summary on success.

---

## Step 5 — Trigger the deployment

Prefer `workflow_dispatch` over pushing unrelated code — it works even if
there's nothing new to deliver:

```bash
gh workflow run "Deploy site to Decathlon Pages" --repo dktunited/<name> --ref main
```

Then resolve the run id of the run you just queued (poll briefly if it
hasn't appeared yet):

```bash
gh run list --repo dktunited/<name> --workflow "Deploy site to Decathlon Pages" \
  --limit 1 --json databaseId,status,event,createdAt
```

---

## Step 6 — Follow the run to completion

```bash
gh run watch <run-id> --repo dktunited/<name> --exit-status
```

If `gh run watch` isn't available or behaves oddly, fall back to a poll loop
using `gh run view <run-id> --repo dktunited/<name> --json status,conclusion`.

**On failure:**
- Fetch failing logs: `gh run view <run-id> --repo dktunited/<name> --log-failed`.
- Common gotchas:
  - **Repo not in `dktunited`** — the action's owner check fails fast with
    `This action only supports repositories owned by dktunited.` Nothing to
    retry; explain the limitation.
  - **`directory` does not exist** — the build step didn't run or produced a
    different output path. Fix the workflow's `directory` (or the build) rather
    than retrying blindly.
  - **A brand-new repo may not yet be granted access to the `decathlon`
    self-hosted runner group** — this shows up as the job staying queued
    indefinitely or an authorization error. This requires a platform/org admin
    to add the repo to the runner group; it cannot be fixed via the `gh` CLI.
- Otherwise, surface the actual failing step's error output verbatim.

---

## Step 7 — Report success

1. **Preferred:** the `deploy-pages` action writes the real deployment URL and
   bucket path to the job summary — read it from there:
   ```bash
   gh run view <run-id> --repo dktunited/<name> --log | grep -iE "pages.dktapp.cloud"
   ```
   The summary contains a line like
   `**URL:** [https://<folder>.pages.dktapp.cloud](...)`.
2. If that line isn't found, fall back to the documented pattern
   `https://<folder-or-repo-name>.pages.dktapp.cloud` (folder lowercased) — but
   prefer the action-reported URL since it's authoritative.
3. Share the URL in chat. Remind the user the site is **private behind Decathlon
   SSO** — visitors must be logged in.
4. Open it for the user in the **browser canvas** (`open_canvas` with
   `canvasId: "browser"`, passing the URL as input) so they can see the live
   result without leaving the app.

---

## Edge Cases

| Situation | Handling |
|---|---|
| Repo upstream not in `dktunited` org | Stop, explain the action owner check + self-hosted runner/bucket limitation — don't deploy |
| No upstream at all | Propose a name (= subdomain), confirm via `ask_user`, create under `dktunited`, push to `main` |
| Workflow file already exists | Leave untouched, just trigger + follow |
| Build directory ambiguous/missing | Ask the user explicitly — never guess silently |
| Repo needs a build step (not pre-built static output) | Use the node/pnpm build template variant, adapted to the repo's actual toolchain |
| Markdown-only repo (no `index.html`, no build) | Deploy the docs folder as-is (often `.`); Pages renders the Markdown, assets and source files |
| No `index.md` at the site root | Warn that the root will show a file listing (with the folder's `README.md` rendered below it) and offer to add an `index.md` |
| Custom subdomain wanted | Set the action's `folder` input; otherwise it defaults to the repo name |
| Run stays queued / runner group error | Explain the org-admin-only runner group access gotcha; don't loop retrying |
| URL line missing from logs | Fall back to `https://<folder-or-repo>.pages.dktapp.cloud`, note the assumption |
| Re-running on an already-configured repo | Skip repo/workflow creation, go straight to trigger + follow |

## Hard Rules

1. **Never deploy repos outside the `dktunited` org** — the action refuses and the platform doesn't support it.
2. **Never overwrite an existing working workflow file** without being asked.
3. **Never silently guess** the build directory, repo name, or subdomain — always confirm with `ask_user`.
4. **Never fabricate the pages URL** — extract it from run logs when possible.
5. **Always use the `gh` CLI** for repo/workflow/run operations, never raw GitHub API calls that require crafting auth headers manually.
