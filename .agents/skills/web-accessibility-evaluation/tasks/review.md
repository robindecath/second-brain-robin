<!-- AUTO-GENERATED from source/. Do not edit here — edit source/ and run `pnpm build`. -->

# Accessibility Review Methodology

This skill teaches **how to review pull requests for accessibility issues**. It focuses exclusively on what automated runtime scanners (axe-core) structurally cannot detect — intent analysis, cross-component reasoning, convention compliance, and architectural decisions.

---

## 1. Core Principle: Complement, Don't Duplicate

```
PR opened
  ├── axe-core GHA → runtime checks (contrast, alt, roles)
  └── Review skill → source-level (intent, patterns, conventions)
```

Auto-detect existing axe-core GitHub Actions and **skip** any check category axe already covers.

---

## 2. Scoping to Changed Files

Review **only** files in the PR diff:

- Get the list of changed files
- Filter to relevant file types (components, styles, tests)
- **Skip**: documentation, configs, lockfiles, test snapshots

---

## 3. Infrastructure Detection

Before reviewing, check:

| Question | If Yes | If No |
| -------- | ------ | ----- |
| axe-core GHA exists in `.github/workflows/`? | Skip axe-detectable categories | Include basic runtime-detectable checks |
| Design system installed? | Flag raw HTML when DS component exists | Skip DS-related checks |
| a11y test conventions exist? (`*.a11y.test.*`) | Flag missing co-located tests | Skip convention check |

---

## 4. Review Rules

### 4.1 Structural Rules (always checked)

| ID | Rule | Severity |
| -- | ---- | -------- |
| G-001 | Interactive element uses non-semantic HTML (`<div onClick>`, `<span onClick>`) | HIGH |
| G-002 | `aria-label` contains element's role name ("navigation", "button") | MEDIUM |
| G-003 | `aria-label` contains state words ("expanded", "collapsed") | MEDIUM |
| G-004 | Heading inside `<summary>` element | MEDIUM |
| G-005 | Positive `tabIndex` (> 0) introduced | HIGH |
| G-006 | `outline: none` without `:focus-visible` replacement | HIGH |
| G-007 | `aria-hidden="true"` on element containing focusable elements | CRITICAL |
| G-008 | `role="alert"` or `aria-live="assertive"` for non-critical info | MEDIUM |
| G-009 | Image `alt` with empty fallback (`alt={x ?? ""}`) on informative image | MEDIUM |
| G-010 | Interactive SVG (`onClick` + `tabIndex`) without `onKeyDown` handler | HIGH |
| G-011 | `disabled` on non-form element (should be `aria-disabled`) | MEDIUM |
| G-012 | Form input without associated label mechanism | HIGH |
| G-013 | `inert` on the overlay instead of the background | HIGH |

### 4.2 Convention Rules (checked when conventions detected)

| ID | Rule | Condition |
| -- | ---- | --------- |
| G-C01 | New interactive component without co-located `.a11y.test` file | When `*.a11y.test.*` pattern exists |
| G-C02 | Raw HTML element when design system component exists | When DS detected |
| G-C03 | Hardcoded color value when design tokens used elsewhere | When CSS custom properties detected |
| G-C04 | Missing `autocomplete` on personal data input | Always (WCAG 1.3.5) |
| G-C05 | Animation/transition without `prefers-reduced-motion` | When motion queries exist |
| G-C06 | Design-system component used but its **consumer contract** is unmet (e.g. `VpModal` with no accessible name, `VpInput` not wrapped in `VpFormControl`/`VpFormLabel`, `VpIconButton` with no `aria-label`) — verify against `references/vp-contracts/<component>.md` | When DS detected |

### 4.3 Platform-Specific Rules

**Web** (`.tsx`/`.jsx`/`.vue`/`.svelte`):
- Load rules from design system (e.g., Vitamin Play a11y rules)
- Check interactive SVG patterns

**iOS** (`.swift`):
- Missing `.accessibilityLabel()` on interactive views
- `Image` without `.accessibilityHidden(true)` or `.accessibilityLabel()`

**Android** (`.kt`/`.java`/`res/layout/*.xml`):
- Missing `contentDescription` on interactive views
- Touch target < 48dp

---

## 5. Decision Logic: Flag vs. Skip

### DO Flag

- New violations introduced in the diff
- Convention violations that prevent future regressions
- Architectural decisions that lock in inaccessibility

### DO NOT Flag

- Pre-existing issues (not introduced by this PR)
- Issues that axe-core GHA already catches (when detected)
- `RUNTIME_REQUIRED` items (for manual verification, never PR gates)
- Purely stylistic preferences without WCAG basis
- Test files, documentation, configs

---

## 6. Pass/Fail Decision

| Findings | Decision |
| -------- | -------- |
| 0 issues | ✅ PASS — "No accessibility concerns in this PR" |
| Only MEDIUM issues | ⚠️ PASS WITH NOTES — "Consider addressing before merge" |
| Any HIGH or CRITICAL issue | ❌ FAIL — "Accessibility issues must be resolved" |

---

## 7. Output Format

Produce inline comments on specific lines:

```markdown
### ⚠️ [Rule ID]: [Short title]

**WCAG**: [SC number] — or — **Convention**: [team rule]
**Confidence**: [HIGH | MEDIUM]

[One sentence: what's wrong + user impact]

**Suggestion**:
\`\`\`[language]
[fix code]
\`\`\`
```

---

## 8. axe-core Status Footer (MANDATORY)

Every review output MUST end with an axe-core status line:

| Detection | Footer |
| --------- | ------ |
| axe-core GHA found | "✅ **axe-core CI active** — this review complements automated runtime checks" |
| Not found | "⚠️ **No axe-core CI detected** — this review covers source-level patterns only. Runtime violations are NOT covered." |

---

## 9. What This Skill Catches (That axe Cannot)

| Category | Example | Why axe misses it |
| -------- | ------- | ---------------- |
| Architectural decisions | `<div onClick>` vs `<button>` | axe sees rendered DOM, not intent |
| Cross-component reasoning | Heading level skip when composed | axe sees page, not component |
| Convention violations | Missing `.a11y.test` file | Not a WCAG violation, team rule |
| Pattern misuse | "navigation navigation" label | axe doesn't evaluate label quality |
| Design system drift | Raw HTML when DS component exists | axe doesn't know the DS |
| Keyboard architecture | SVG onClick without onKeyDown | axe can't test keyboard without render |
| Conditional compliance | `alt={data?.caption}` no fallback | axe only sees runtime values |
