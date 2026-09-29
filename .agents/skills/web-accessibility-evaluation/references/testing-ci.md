# Web Accessibility — CI Testing Setup

Concrete tooling and scaffold for the **build-test** workflow on web projects (React / Vue / Svelte).
This is the org's standard setup — replicate it exactly, adapting pnpm commands to the project's
package manager if needed.

---

## Stack — 4 CI jobs

| Job | Tool | What it catches |
|---|---|---|
| `unit-a11y` | Vitest + RTL + `jest-axe` | Component-level ARIA / keyboard / focus regressions |
| `validate-web` | `dktunited/a11y/actions/validate-web@v1` | Full-page axe-core scan per route, PR comment with violations |
| `playwright-a11y` | Playwright + `@axe-core/playwright` | Real-browser route scans, focus trapping, computed contrast |
| `lighthouse-a11y` | Lighthouse-CI | Category-level a11y score gate (trendable) |

**Priority**: `validate-web` is the primary regression gate — set it up first. The other jobs deepen coverage.

---

## 1. Routes file — `a11y-routes.json`

Create this file at the project root. List **every route** the app exposes:

```json
[
  { "path": "/", "name": "Homepage" },
  { "path": "/catalog", "name": "Catalog" },
  { "path": "/product/123", "name": "Product detail" },
  { "path": "/cart", "name": "Cart" },
  { "path": "/checkout", "name": "Checkout" },
  { "path": "/account", "name": "Account" }
]
```

Rules:
- One entry per distinct route/screen — include all authenticated and unauthenticated routes.
- Use real-looking IDs for parameterized routes (`/product/123`, not `/product/:id`).
- Keep `name` human-readable — it appears in PR comments.

---

## 2. GitHub Actions workflow — `.github/workflows/a11y.yml`

```yaml
name: Accessibility

on:
  pull_request:
    paths:
      - "**/*.tsx"
      - "**/*.jsx"
      - "**/*.ts"
      - "**/*.vue"
      - "**/*.svelte"

jobs:
  # Component-level regression tests (Vitest + RTL + jest-axe).
  unit-a11y:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - uses: pnpm/action-setup@v4
        with:
          version: "10"
      - run: pnpm install --frozen-lockfile
      - run: pnpm test --run

  # Full-page axe-core scan against the running app — posts violations as PR comments.
  validate-web:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - uses: pnpm/action-setup@v4
        with:
          version: "10"
      - run: pnpm install --frozen-lockfile && pnpm build && pnpm preview --port 4173 &
      - uses: dktunited/a11y/actions/validate-web@v1
        with:
          base-url: http://localhost:4173
          routes-file: ./a11y-routes.json
          wait-strategy: networkidle

  # Real-browser per-route axe scans + keyboard-only critical journeys.
  playwright-a11y:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - uses: pnpm/action-setup@v4
        with:
          version: "10"
      - run: pnpm install --frozen-lockfile
      - run: pnpm exec playwright install --with-deps chromium
      - run: pnpm test:e2e
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 7

  # Lighthouse accessibility CATEGORY score per route (trendable gate).
  lighthouse-a11y:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - uses: pnpm/action-setup@v4
        with:
          version: "10"
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
      - run: pnpm preview --port 4173 --strictPort &
      - run: pnpm exec lhci autorun --config=./lighthouserc.cjs
        env:
          A11Y_BASE_URL: http://localhost:4173
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: lighthouse-reports
          path: .lighthouseci/
          retention-days: 7
```

Adapt `pnpm` commands to the project's package manager (npm, yarn) if pnpm is not used.

---

## 3. Component tests — Vitest + jest-axe

Install:
```bash
pnpm add -D jest-axe @types/jest-axe
```

Setup (`vitest.setup.ts`):
```ts
import { configureAxe } from 'jest-axe';
configureAxe({ rules: { 'color-contrast': { enabled: false } } }); // tune as needed
```

Component test pattern (`Button.a11y.test.tsx`):
```tsx
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { expect } from 'vitest';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

it('has no axe violations', async () => {
  const { container } = render(<Button>Save</Button>);
  expect(await axe(container)).toHaveNoViolations();
});

it('is keyboard operable', async () => {
  const { getByRole } = render(<Button onClick={vi.fn()}>Save</Button>);
  const btn = getByRole('button', { name: 'Save' });
  btn.focus();
  expect(document.activeElement).toBe(btn);
});
```

File naming: `ComponentName.a11y.test.tsx` co-located with the component.

---

## 4. Playwright — route scans + journeys

Install:
```bash
pnpm add -D @playwright/test @axe-core/playwright
pnpm exec playwright install --with-deps chromium
```

Playwright config (`playwright.config.ts`) — the `webServer` block builds and serves automatically:
```ts
import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: './e2e',
  use: { baseURL: 'http://localhost:4173' },
  webServer: {
    command: 'pnpm preview --port 4173',
    url: 'http://localhost:4173',
    reuseExistingServer: !process.env.CI,
  },
});
```

Route scan (`e2e/a11y-routes.spec.ts`):
```ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import routes from '../a11y-routes.json';

for (const { path, name } of routes) {
  test(`${name} (${path}) — no axe violations`, async ({ page }) => {
    await page.goto(path);
    const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa']).analyze();
    expect(results.violations).toEqual([]);
  });
}
```

Journey pattern (`e2e/checkout.a11y.spec.ts`):
```ts
test('checkout journey is keyboard-completable', async ({ page }) => {
  await page.goto('/catalog');
  await page.keyboard.press('Tab');
  await page.keyboard.press('Enter'); // add to cart
  // assert focus moved, status announced, etc.
});
```

File naming: `*.a11y.spec.ts` in `e2e/`.

---

## 5. Lighthouse-CI — score threshold

Install:
```bash
pnpm add -D @lhci/cli
```

Config (`lighthouserc.cjs`):
```js
module.exports = {
  ci: {
    collect: {
      url: ['http://localhost:4173/'],
      numberOfRuns: 1,
      settings: { preset: 'desktop' },
    },
    assert: {
      assertions: { 'categories:accessibility': ['error', { minScore: 0.9 }] },
    },
    upload: { target: 'temporary-public-storage' },
  },
};
```

---

## 6. Scaffold checklist

- [ ] `a11y-routes.json` — all routes listed with human-readable names
- [ ] `.github/workflows/a11y.yml` — 4-job workflow
- [ ] `vitest.setup.ts` — jest-axe configuration
- [ ] `ComponentName.a11y.test.tsx` — per component with accessibility requirements
- [ ] `playwright.config.ts` — with `webServer` block
- [ ] `e2e/a11y-routes.spec.ts` — reads from `a11y-routes.json`, no duplication
- [ ] `e2e/<journey>.a11y.spec.ts` — one per critical user journey
- [ ] `lighthouserc.cjs` — score threshold ≥ 0.9
