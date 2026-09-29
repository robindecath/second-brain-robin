<!-- AUTO-GENERATED from source/. Do not edit here — edit source/ and run `pnpm build`. -->

# Accessibility Build-Test Methodology

This skill **establishes accessibility testing as a practice** in the project: it sets up
the infrastructure and **scaffolds the files directly** (it does not just suggest them). It
is the *protect* step — turning fixes into permanent, codebase-wide protection.

It produces **two layers of coverage**:
- **Global** — per-route/screen automated scans and critical user-journey tests.
- **Precise** — component/widget-level keyboard / ARIA / focus / announcement tests.

---

## 1. Understand the codebase first

Do not generate generic tests. Read the project:

- **Stack & runner**: dependency manifests (`package.json`, `build.gradle`, `Package.swift`,
  `Podfile`) and config files — identify which test runner is already installed or expected.
  Read CI workflows to understand what already runs.
- **Existing tests**: read 2–3 tests to learn conventions (imports, describe/it nesting,
  assertions, helpers, file placement) and the app's **real scenarios** (which flows are
  covered, which user journeys matter).
- **App structure**: routes/screens, critical journeys (e.g. browse → product → checkout),
  reusable components/widgets, and which **design-system components** are used.

Generated tests must read like a teammate wrote them.

---

## 2. Establish the infrastructure (scaffold it)

Consult `references/` for the exact tool names and install commands for this platform.

| Capability | If present | If missing |
| ---------- | ---------- | ---------- |
| Unit/component runner | use it | scaffold the minimal setup (see `references/` for this platform's stack) |
| **Automated scanner in CI** | reuse | add a CI job that runs automated a11y checks across every route/screen |
| **Score/severity threshold** | reuse | configure a threshold gate for category-level trend monitoring |
| **End-to-end / UI test runner** | reuse for journeys + per-route scans | **offer to install** the standard runner for this platform and scaffold it on agreement |

When the e2e/UI runner is absent, explicitly propose installing it (it is the right home for
full-app scans and journey tests) and, on agreement, scaffold it.

---

## 3. Design the test strategy — global AND precise

### Global (breadth)
- **Per-route/screen scan** — automated a11y check with no-violations gate (WCAG A/AA tags where supported).
- **Score threshold** where the platform supports it (category-level, CI-enforced).
- **Critical user journeys**: real flows, asserting accessibility at each step (focus moves
  correctly, status messages announced, keyboard/switch-control completion possible).

### Precise (depth)
- **Keyboard / switch-control flow** — tab order and operability of interactive components.
- **Focus management** — focus enters overlays/dialogs and is restored on close.
- **Semantic state** — `aria-expanded`, `aria-selected`, `aria-invalid` (web) or equivalent
  accessibility traits/states (iOS/Android) update correctly on interaction.
- **Screen-reader announcement** — live regions / accessibility notifications fire with the right text.
- **Design-system contract assertions** — for each DS component used, assert its consumer
  requirements from `references/` are met (e.g. buttons have accessible names, modals have
  labels, inputs have associated labels). This protects against the most common DS misuse.

Tests assert the **accessible (fixed) behaviour**, so they fail on broken code and pass once
fixed — real regression protection, not snapshots of the current state.

---

## 4. Scaffold the files

- Match naming conventions found in existing tests; place files following the project's conventions.
  Consult `references/` for the idiomatic test file extension and structure for this platform.
- Write runner config / setup files, the test files, the **CI workflow** (a job for unit
  a11y + automated scans + journey tests), and a routes/screens inventory when needed.
- **Do not modify application source** — only add test/config/CI files. List everything
  created and the exact commands to run it.

---

## 5. Platform-specific tooling

Consult `references/` for install commands, test patterns, and scaffold templates. The table
below is a quick-reference summary — the detail lives in the platform skill's bundled files.

| Platform | Primary stack |
| -------- | ------------- |
| Web | Vitest + React Testing Library + `jest-axe` (component) · Playwright + `@axe-core/playwright` (route scans + journeys) · Lighthouse-CI (score threshold) |
| iOS | XCTest / XCUITest — `accessibilityIdentifier`, traits, focus, Dynamic Type · Accessibility Inspector (manual) · `isAccessibilityElement` / `accessibilityLabel` assertions |
| Android | Espresso + `compose-ui-test` · `AccessibilityChecks.enable()` (Espresso a11y checks) · Accessibility Scanner / `accessibility-test-framework` |

---

## 6. Generation rules

### DO
- Establish missing infra for this platform (consult `references/`).
- Global per-route/screen scans + critical-journey tests AND precise component/widget tests.
- DS-contract assertions for every design-system component in use.
- Tests red on current broken code.

### DON'T
- Don't only test what an audit already found one-off — cover routes/screens and journeys broadly.
- Don't duplicate scanner checks in bespoke unit tests where the scan already covers them.
- Don't modify application source code.
- Don't install web tooling (axe, Lighthouse, Playwright) in an iOS or Android project.

### Output
A short infrastructure summary, the created files (with header comments noting what each
protects), the CI workflow, and the exact commands to run the suite.
