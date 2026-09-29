# Environment Detection Specification

> **Usage**: This template defines the automatic environment detection logic that all accessibility agents (Scout, Bridge, Guard, Crafter, Mentor) execute silently at the start of any invocation. The output is an internal context map — never shown to users — that determines which checks to skip, what to enrich, and where coverage gaps exist.

---

## Detection Categories

### 1. Runtime Testing Tools

Scan all `**/package.json` files (web) or build files (mobile) for:

| Dependency               | Platform | What it means                         |
| ------------------------ | -------- | ------------------------------------- |
| `@axe-core/playwright`   | Web      | Playwright + axe integration exists   |
| `@axe-core/react`        | Web      | Component-level axe tests exist       |
| `jest-axe`               | Web      | Jest-based axe assertions exist       |
| `axe-core` (direct)      | Web      | axe available as library              |
| `pa11y`                  | Web      | Alternative accessibility scanner     |
| `@axe-core/cli`          | Web      | CLI-based accessibility scanner       |
| `AccessibilitySnapshot`  | iOS      | SwiftUI snapshot testing              |
| `ViewInspector`          | iOS      | SwiftUI view inspection testing       |
| `espresso-accessibility` | Android  | Espresso accessibility checks         |
| `accessibility-test-framework` | Android | Google ATF integration         |

### 2. CI/CD Workflows

Scan `.github/workflows/**/*.yml` (or equivalent CI config) for:

- Steps or actions referencing `axe`, `accessibility`, `a11y`, `deque-systems`
- Determine: is axe already running in CI? On which routes/screens?
- If present → Guard agent skips axe-detectable checks entirely

### 3. Existing Reports

Search the workspace for:

- `**/*.a11y.json`, `**/axe-results.*`, `**/accessibility-report.*`
- SARIF files containing axe rule IDs
- HTML reports from axe/pa11y
- If found → Bridge agent can ingest and enrich immediately

### 4. Existing Accessibility Tests

Search for:

- Files matching `**/*.a11y.{test,spec}.*`
- Test files containing `axe`, `toHaveNoViolations`, `checkA11y`
- iOS: files containing `AccessibilitySnapshot`, `accessibilityLabel` assertions
- Android: files containing `AccessibilityChecks`, `atf_`
- Determine: which components/routes/screens already have a11y test coverage

### 5. Visual Regression Infrastructure

Check for:

- Percy, Chromatic, Playwright screenshot baselines
- `**/screenshots/`, `**/__snapshots__/`
- `playwright.config.*` with screenshot settings
- Xcode UI test screenshots
- If found → high-contrast mode and dark mode visual checks may already exist

### 6. Platform Detection

From file extensions and framework markers:

| Signal | Platform | Route to |
| ------ | -------- | -------- |
| `.tsx`, `.jsx`, `.vue`, `.svelte` | Web | `web-accessibility-evaluation` |
| `.swift`, `.xib`, `.storyboard` | iOS | `ios-accessibility-evaluation` |
| `.kt`, `.java` + `res/layout/` or `@Composable` | Android | `android-accessibility-evaluation` |

### 7. Design System Detection

| Signal | Design System |
| ------ | ------------- |
| `@vtmn-play/react`, `@vtmn-play/vue`, `@vtmn-play/svelte` | Vitamin Play |
| `@mui/material` | Material UI |
| `@chakra-ui/react` | Chakra UI |
| `@radix-ui/*` | Radix UI |
| Custom: check for `components/` or `ui/` directories with shared primitives | In-house DS |

---

## Output Format (Internal — Never Shown to User)

```
Detected infrastructure:
  [✅|⚠️|❌] Runtime testing: <tool name> in <file path>
  [✅|⚠️|❌] CI workflow: <workflow file> (<what it checks>)
  [✅|⚠️|❌] Visual regression: <tool> in <location>
  [✅|⚠️|❌] Existing a11y tests: <location> (<count> files)
  [✅|⚠️|❌] Component-level tests: <present|absent>

Platform: <Web|iOS|Android> (<framework>)
Design System: <name> (<package>)

Routing decisions:
  → Scout: <what to focus on / what to skip>
  → Bridge: <what existing results to enrich>
  → Guard: <what to complement vs existing CI>
  → Crafter: <what gaps to fill with tests>
```

---

## Agent Behavior Based on Detection

### Scout (Full Audit)

- If axe-core in CI → skip axe-detectable issues, focus on patterns axe structurally cannot catch (intent analysis, cross-component reasoning, convention compliance)
- If no runtime tools detected → **prompt the user** with 3 options:
  1. "Run axe-core now" → execute one-time axe scan via Playwright MCP CLI (`npx @axe-core/cli`)
  2. "Set up axe-core in CI" → invoke Crafter to integrate `dktunited/a11y/actions/validate-web@v1`
  3. "Skip axe-core" → continue static-only, include axe-detectable items as best-effort
- Always: run full static analysis regardless of existing tools
- Always: load platform-specific references from the detected platform skill (web/iOS/Android) for accurate fix code

### Bridge (Enrichment)

- If existing axe reports found → offer to enrich immediately
- If SARIF format detected → parse and map to source files
- If no reports → inform user Bridge needs runtime results as input
- Always: load platform-specific references for fix suggestions

### Guard (PR Review)

- If axe GHA exists → skip those check categories entirely, append "✅ axe-core CI active" footer
- If no CI accessibility checks → run broader check set, append "⚠️ No axe-core CI detected" footer
- **Never** ask user to install axe-core (CI is non-interactive)
- Always: only review changed files in diff
- Always: load platform-specific references for fix suggestions

### Crafter (Test Generation)

- Match existing test framework (Playwright/Vitest/Jest/XCTest/Espresso)
- Match existing file naming conventions
- Only generate tests for untested gaps
- If visual regression exists → skip contrast test generation
- If invoked by Scout with CI integration instruction → generate `dktunited/a11y/actions/validate-web` workflow (Web only)
- For iOS/Android: load platform-specific test references

### Mentor (Real-time Guidance)

- If Design System detected → suggest DS components over raw HTML/native elements
- If team has existing conventions (detected from test patterns) → reinforce them
- Always: lightweight advice on current file only
- Always: load platform-specific references for the file currently being edited
