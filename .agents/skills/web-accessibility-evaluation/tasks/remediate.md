<!-- AUTO-GENERATED from source/. Do not edit here — edit source/ and run `pnpm build`. -->

# Accessibility Remediation Methodology

This skill teaches **how to fix** accessibility issues — it edits the code. Use it after a
diagnosis exists. It is the _treat_ step: `audit`/`review` find and report; **remediate
applies the changes**.

## Required remediation report vocabulary

For web scanner findings involving form controls, explicitly name the Vitamin Play
component `VpInput` when it is the appropriate replacement for a raw `<input>`, and
explicitly call shared-rule or component-level work a **systemic** fix. These terms
must appear in the final remediation summary when the corresponding findings are
present; do not leave them implicit in a generic list of file edits.

---

## 1. Input — any set of findings

Remediation does not re-diagnose from scratch. It consumes findings that already exist:

| Input                                                                               | What to do with it                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A full **audit** report (this suite's `audit` task)                                 | Apply each finding's fix; findings already carry `file:line` + before/after.                                                                                                                                                                                    |
| Partial **review** comments (this suite's `review` task)                            | Apply the diff-scoped regressions.                                                                                                                                                                                                                              |
| An external **scanner** export — axe-core JSON / SARIF / Lighthouse / agency report | First map each DOM selector / description → source `file:line` (grep class names, component combinations, file structure). **Never re-run the scanner's checks** — translate them. For `color-contrast` and other runtime results, do not re-assert statically. |

Normalize all inputs to a common finding list: `{ file, line/anchor, criterion, severity, mode, fix }`.

When several findings share a rule, component, or anti-pattern, explicitly
describe the correction as a **systemic** fix in the final report (for example,
"systemic fix: update the shared form component"). Keep the per-file changes,
but do not report only a list of isolated edits when one root cause explains
multiple findings.

---

## 2. Dedup & group by systemic pattern (before touching code)

- **Dedup** across sources — the same defect may appear in an audit AND an axe export.
- **Group by root cause.** Indicators of a systemic pattern: same rule/criterion 3+ times,
  same component name across many sites, same anti-pattern in one shared component.
- **Component-level vs instance-level**: if a defect comes from a reusable component, fix the
  **component definition once** (resolves every instance) instead of patching each call site.

Fix order: **systemic/component fixes first** (highest leverage), then instance fixes, then
single low-severity items.

---

## 3. Apply the fixes

For each finding (or systemic group), edit the source:

- **Prefer the design system.** When a raw element is used where a `Vp*` (or platform DS)
  component exists, migrate to the component — AND **fulfill its consumer contract**: load
  `references/vp-contracts/<component>.md` and satisfy every required consumer step
  (accessible name, associated label via `VpFormControl`/`VpFormLabel`, required indication,
  keyboard, grouping…). A migration that drops the contract is not a fix.
- **When a DS component is already used but misused** (e.g. `VpModal` with no accessible
  name, `VpIconButton` with no `aria-label`), apply the missing consumer-side requirement
  from its contract file.
- **Make minimal, reviewable diffs.** Change only what the finding requires; preserve the
  file's existing conventions, imports, and formatting.
- **Never fake-fix runtime items.** Contrast ratios, screen-reader announcement quality,
  focus-order-at-runtime, live-region timing cannot be confirmed by editing source — do NOT
  pretend to resolve them. Apply the structural part if any (e.g. add the `aria-live`
  region) and list the rest for manual verification.
- **Stay in scope.** Do not refactor unrelated code or change behaviour/visuals beyond the
  accessibility fix.

---

## 4. Verify & report

After applying:

1. **Summary of applied changes** — a table: `finding → file:line → what changed → resolves N`.
2. **Systemic fixes called out** — "Fixed `ProductCard` → resolves 12 instances."
3. **Manual / runtime follow-up** — the items that could not be auto-fixed (runtime-only,
   ambiguous content like alt-text wording that needs a human, data-dependent values).
4. **Re-scan recommendation** — if the input was a scanner export, recommend re-running it
   (and the suite's `build-test` tests) to confirm the count dropped.

```markdown
## Applied

| Finding   | Location   | Change                         | Resolves                  |
| --------- | ---------- | ------------------------------ | ------------------------- |
| image-alt | App.tsx:56 | added alt + migrated to VpLink | 2 (image-alt + link-name) |

## Manual follow-up (not auto-fixable)

- [ ] color-contrast on `content-quiet` text — verify ≥4.5:1 after token swap (runtime)
- [ ] alt text wording for product images — needs human review of each image's meaning
```

---

## 5. Platform notes

| Platform | Source mapping                                        | DS contract                                       |
| -------- | ----------------------------------------------------- | ------------------------------------------------- |
| Web      | axe DOM selectors / class names → component files     | `references/vp-contracts/` (Vitamin Play React)   |
| iOS      | Accessibility Inspector view classes → Swift/XIB      | `references/vp-contracts/` (Vitamin Play iOS)     |
| Android  | Accessibility Scanner view IDs → layout XML / Compose | `references/vp-contracts/` (Vitamin Play Android) |

---

## 6. Safety checklist before finishing

- [ ] Only accessibility-relevant lines changed; no unrelated edits
- [ ] Every DS migration fulfills the component's consumer contract
- [ ] Systemic fixes applied at the component, not duplicated per call site
- [ ] Runtime-only items listed for manual verification, not silently "fixed"
- [ ] A short summary of every change is produced
