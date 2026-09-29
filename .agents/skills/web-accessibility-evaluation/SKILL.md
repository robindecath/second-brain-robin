---
name: web-accessibility-evaluation
description: "Audit, fix, review, and set up testing for web accessibility (WCAG 2.2 AA / RGAA) in React, Vue, and Svelte with Vitamin Play. Use WHEN: \"audit accessibility\", \"fix a11y violations\", \"review a PR for accessibility\", \"set up axe/Lighthouse/Playwright tests\". Skip if it targets iOS/Android, is a11y theory with no code, or is non-accessibility (performance, SEO)."
allowed-tools: [read, write, bash, glob, grep]
license: Apache-2.0
metadata:
  owner: "Digital Accessibility SIG & Design System team"
  version: "1.0.0"
  last-updated: "2026-03-28"
---

<!-- AUTO-GENERATED from source/. Do not edit here — edit source/ and run `pnpm build`. -->

# web (React/Vue/Svelte) Accessibility — all workflows

This skill is the single entry point for accessibility on **web (React/Vue/Svelte)**. Identify the user's intent and follow the matching workflow — each is complete and bundled here. Apply the web remediation in `references/` and the standards in `standards/`.

| If the user wants to… | Follow |
| --- | --- |
| Audit / assess a codebase for WCAG 2.2 AA compliance (find everything) | `tasks/audit.md` |
| Set up accessibility testing: axe + Lighthouse CI + dktunited/a11y — global & precise tests | `tasks/build-test.md` |
| Apply accessibility fixes from audit / review / scanner findings — edits the code | `tasks/remediate.md` |
| Review a PR / diff for accessibility regressions (gate the merge) | `tasks/review.md` |
| Fix / implement an accessible component (ad-hoc) | the platform remediation below + `references/` |

---

## Platform remediation

Detailed web (React/Vue/Svelte) remediation patterns and fix code live in `references/platform-remediation-guide.md` and the other `references/` modules — load them when applying fixes (see the bundled index below).

---

## Bundled (self-contained)

**Workflows** (platform-agnostic methodology, applied to this platform)
- `tasks/audit.md` — Audit / assess a codebase for WCAG 2.2 AA compliance (find everything)
- `tasks/build-test.md` — Set up accessibility testing: axe + Lighthouse CI + dktunited/a11y — global & precise tests
- `tasks/remediate.md` — Apply accessibility fixes from audit / review / scanner findings — edits the code
- `tasks/review.md` — Review a PR / diff for accessibility regressions (gate the merge)

**Platform remediation (web (React/Vue/Svelte))**
- `references/platform-remediation-guide.md` — remediation methodology & fix patterns for this platform
- `references/` — fix modules for this platform
- `rules/` — design-system accessibility rules

**Standards (platform-agnostic)**
- `standards/wcag-checklist.md` — WCAG 2.2 AA checklist (50 success criteria)
- `standards/cross-references/` — WCAG ↔ RGAA ↔ RAAM ↔ EN 301 549 mappings (TOON)
- `standards/patterns/` — universal, platform-agnostic accessibility patterns
- `standards/templates/` — RGAA / RAAM audit templates, domain profiles, disclaimers
