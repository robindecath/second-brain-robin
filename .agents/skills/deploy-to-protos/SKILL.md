---
name: deploy-to-protos
description: >
  Deploys the current repository's prototype/demo to Decathlon's internal
  Protos platform, publishing a static site at https://<repo>.protos.dktapp.cloud.
  Activate when the user says "deploy to protos", "publish to protos", "ship this
  prototype", or asks to set up protos deployment for a repo. Ensures the repo has
  a GitHub upstream in the dktunited org (creating one if needed), adds the
  `dktunited/protos/actions/publish-prototype@main` GitHub Actions workflow if
  missing, triggers the deployment via workflow_dispatch, follows the run to
  completion using the gh CLI, then shares and opens the resulting protos URL.
license: MIT
metadata:
  audience: developers
  domain: platform-engineering
  api: github-actions+gh-cli
  mcp_required: false
---

# Deploy to Protos Skill

Publishes a repo's static prototype/demo to Decathlon's Protos platform
(`https://<repo>.protos.dktapp.cloud`) via a self-hosted GitHub Actions
workflow, then follows the run and opens the result.

⚠️ **Hard requirement:** this only works for repositories under the
**`dktunited`** GitHub org. The workflow relies on self-hosted
`decathlon`-tagged runners and a shared GCS bucket that are only wired up for
that org. If the repo's upstream is anywhere else, **stop and explain this**
instead of trying to deploy.

---

## When to Activate

- User says "deploy to protos", "publish to protos", "push this to protos"
- User asks to set up/configure protos deployment for the current repo
- User asks to re-trigger or check a protos deployment

Not for dev-time work: if the prototype still needs Decathlon API access or
persisted `/data/*` storage wired up, use the sibling
**`protos-data-and-api-access`** skill first, then come back here to publish.

---

## Step 1 — Preconditions

1. Confirm `gh` CLI is authenticated: `gh auth status`. If not, ask the user
   to run `gh auth login` first and stop.
2. From the repo root, check for an upstream: `git remote -v`.

---

## Step 2 — No upstream: create the GitHub repo

1. Derive a candidate repo name from the current directory name: lowercase,
   kebab-case, strip characters that aren't `[a-z0-9-]`.
2. Check availability: `gh repo view dktunited/<name>` — a 404/`GH_ERR` means
   it's free; any success output means it's taken.
3. **Always confirm the name with the user before creating anything** using
   `ask_user` with the proposed name as a suggested choice, plus room for a
   freeform override. Do not silently pick a fallback name.
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
2. If the org is not `dktunited`, **stop** and tell the user: protos deploys
   need self-hosted `decathlon` runners and a shared bucket only available to
   `dktunited` org repos — this repo can't be deployed as-is. Do not attempt
   to fork or transfer the repo automatically.

---

## Step 4 — Ensure the workflow file exists

1. Check for an existing protos workflow: look for any `.github/workflows/*.yml`
   or `*.yaml` file that uses `dktunited/protos/actions/publish-prototype@main`
   (grep the workflows directory — the filename itself may vary).
2. **If found:** leave it as-is. Don't overwrite a working config. Note its
   path and move to Step 5.
3. **If missing:**
   - Auto-detect a candidate build/output directory by checking, in order,
     whether these exist at the repo root: `_proto`, `dist`, `build`,
     `public`, `out`.
   - Ask the user (via `ask_user`) to confirm or override the detected
     directory, and to provide a short one-line `demonstrated-idea`
     description of what the prototype demonstrates.
   - Check whether the detected directory is **already committed to the
     repo** (a pre-built static output, like `dktunited/kontext`'s `_proto`)
     or needs to be **produced by a build step** (there's a `package.json`
     with a `build` script but the output directory isn't tracked in git).
   - If a build step is needed, use the official template (adapt the
     install/build commands to the repo's actual toolchain/package manager):
     ```yaml
     name: Build and deploy site

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

           - id: publish
             uses: dktunited/protos/actions/publish-prototype@main
             with:
               directory: <confirmed-directory>
               demonstrated-idea: "<user-provided description>"
               decisions: "-"

           - name: Report publication URL
             run: echo "Prototype published at ${{ steps.publish.outputs.url }}" >> "$GITHUB_STEP_SUMMARY"
     ```
   - If the directory is already committed (nothing to build), omit the
     setup-node/pnpm/build steps and go straight from checkout to publish —
     still keep the `id: publish` step and the "Report publication URL" step:
     ```yaml
     name: Build and deploy site

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

           - id: publish
             uses: dktunited/protos/actions/publish-prototype@main
             with:
               directory: <confirmed-directory>
               demonstrated-idea: "<user-provided description>"
               decisions: "-"

           - name: Report publication URL
             run: echo "Prototype published at ${{ steps.publish.outputs.url }}" >> "$GITHUB_STEP_SUMMARY"
     ```
   - Commit and push directly to `main`:
     ```bash
     git add .github/workflows/protos.yaml
     git commit -m "Add protos deployment workflow"
     git push origin HEAD:main
     ```
   - No repo secrets are required — the action authenticates via OIDC
     (`id-token: write`), which is pre-configured at the org level.
   - If the prototype needs Decathlon API calls or persisted `/data/*`
     storage, use the sibling **`protos-data-and-api-access`** skill to wire
     that up *before* publishing — this skill only handles CI/deployment.

---

## Step 5 — Trigger the deployment

Prefer `workflow_dispatch` over pushing unrelated code — it works even if
there's nothing new to deliver:

```bash
gh workflow run "Build and deploy site" --repo dktunited/<name> --ref main
```

Then resolve the run id of the run you just queued (poll briefly if it
hasn't appeared yet):

```bash
gh run list --repo dktunited/<name> --workflow "Build and deploy site" \
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
- Common gotcha: a **brand-new repo may not yet be granted access to the
  `decathlon` self-hosted runner group** — this shows up as the job staying
  queued indefinitely or an authorization error. This requires a platform/org
  admin to add the repo to the runner group; it cannot be fixed via the `gh`
  CLI. Explain this clearly to the user rather than retrying blindly.
- Otherwise, surface the actual failing step's error output verbatim.

---

## Step 7 — Report success

1. **Preferred:** the workflow template's "Report publication URL" step writes
   the action's real `steps.publish.outputs.url` output to the job summary —
   read it from there:
   ```bash
   gh run view <run-id> --repo dktunited/<name> --json jobs \
     --jq '.jobs[].steps[] | select(.name=="Report publication URL")'
   ```
   or simply grep the step summary / log for the line it produces:
   ```bash
   gh run view <run-id> --repo dktunited/<name> --log | grep -i "Prototype published at"
   ```
   (this now reflects `steps.publish.outputs.url` verbatim, not a guess).
2. If that line isn't found (e.g. an older workflow file without the report
   step), fall back to the documented pattern
   `https://<repo-name>.protos.dktapp.cloud` — but prefer the action-derived
   URL since it's authoritative.
3. Share the URL in chat.
4. Open it for the user in the **browser canvas** (`open_canvas` with
   `canvasId: "browser"`, passing the URL as input) so they can see the live
   result without leaving the app.

---

## Edge Cases

| Situation | Handling |
|---|---|
| Repo upstream not in `dktunited` org | Stop, explain the self-hosted runner/bucket limitation — don't deploy |
| No upstream at all | Propose a name, confirm via `ask_user`, create under `dktunited`, push to `main` |
| Workflow file already exists | Leave untouched, just trigger + follow |
| Build directory ambiguous/missing | Ask the user explicitly — never guess silently |
| Repo needs a build step (not pre-built static output) | Use the node/pnpm build template variant, adapted to the repo's actual toolchain |
| Run stays queued / runner group error | Explain the org-admin-only runner group access gotcha; don't loop retrying |
| `Prototype published at ...` log line missing | Fall back to `https://<repo>.protos.dktapp.cloud`, note the assumption |
| Re-running on an already-configured repo | Skip repo/workflow creation, go straight to trigger + follow |
| Prototype needs Decathlon API calls or `/data/*` persistence | Use the sibling `protos-data-and-api-access` skill first, before publishing |

## Hard Rules

1. **Never deploy repos outside the `dktunited` org** — the platform doesn't support it.
2. **Never overwrite an existing working workflow file** without being asked.
3. **Never silently guess** the build directory or repo name — always confirm with `ask_user`.
4. **Never fabricate the protos URL** — extract it from run logs when possible.
5. **Always use the `gh` CLI** for repo/workflow/run operations, never raw GitHub API calls that require crafting auth headers manually.
