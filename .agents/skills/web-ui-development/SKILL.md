---
name: web-ui-development
description: Use this whenever you create web interfaces. It uses Vitamin Play Web, Decathlon's design system for React, Vue, and Svelte applications.
license: Apache-2.0
compatibility: Requires GitHub CLI `gh` or GitHub MCP server to access the Vitamin Play Web repository content.
metadata:
  owner: Design System team
  version: "1.0.0"
  last-updated: "2026-06-11"
---

# Web UI Development with Vitamin Play

Use **Vitamin Play Web** as the standard design system for building UI on the web at Decathlon.

Vitamin Play Web is Decathlon's official design system for building consistent, accessible, and performant web user interfaces. It provides a comprehensive suite of packages including React, Vue, and Svelte components, design tokens, CSS utilities, icons, and theme integrations for popular libraries like Ant Design, shadcn/ui, and Tailwind CSS.

## When to use this skill

Use this skill when:

- Build or update web user interfaces for Decathlon applications
- Implement UI components following Decathlon's design standards
- Work with React, Vue, or Svelte frameworks
- Integrate with Ant Design, shadcn/ui, or Tailwind CSS
- Apply design tokens, typography, colors, or spacing
- Handle theming (wonder/legacy), dark mode, or RTL support
- Ensure accessibility compliance in web interfaces

Do NOT use this skill when:

- Building UI for iOS/Apple platforms (use Apple-specific design system)
- Building UI for Android platforms (use Android-specific design system)
- Working on backend/API development

## Available Packages

| Package                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| `@vtmn-play/design-tokens` | Core, semantic, and component design tokens |
| `@vtmn-play/css`           | CSS classes for components and utilities    |
| `@vtmn-play/logic`         | Shared component logic                      |
| `@vtmn-play/react`         | React components                            |
| `@vtmn-play/svelte`        | Svelte components                           |
| `@vtmn-play/icons`         | Icon library                                |
| `@vtmn-play/assets`        | Assets library                              |
| `@vtmn-play/fonts`         | Decathlon fonts                             |
| `@vtmn-play/antd`          | Ant Design theme                            |
| `@vtmn-play/shadcn-ui`     | shadcn/ui theme                             |
| `@vtmn-play/tailwindcss`   | Tailwind CSS preset/theme                   |
| `@vtmn-play/utils`         | Shared utilities                            |

## Installation

### Prerequisites

1. Install [pnpm](https://pnpm.io/installation), npm, or yarn
2. Install [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
3. Authenticate to Decathlon's Google Artifact Registry

### Registry Configuration

Create or update your `.npmrc` file:

```
registry=https://registry.npmjs.org/
@vtmn-play:registry=https://europe-npm.pkg.dev/tnt-managed-wtbe/global-npm/
//https://europe-npm.pkg.dev/tnt-managed-wtbe/global-npm/:always-auth=true
```

### Local Authentication

```bash
gcloud auth login && npx google-artifactregistry-auth
```

### CI/CD Authentication

```yaml
runs-on: [self-hosted, decathlon]
permissions:
  id-token: write
  contents: read

steps:
  - name: npm auth GAR before gcloud authentication
    uses: dktunited/.github/actions/npm-authenticate-gar@main

  - name: Install dependencies
    run: pnpm install
```

### Install Packages

```bash
# React applications
pnpm add @vtmn-play/design-tokens @vtmn-play/react

# Svelte applications
pnpm add @vtmn-play/design-tokens @vtmn-play/svelte

# Vue applications
pnpm add @vtmn-play/design-tokens @vtmn-play/vue
```

## Available Components

All components use the `Vp` prefix and are available in React and Svelte packages:

| Component            | Description               |
| -------------------- | ------------------------- |
| `VpAccordion`        | Expandable content panels |
| `VpArticleCard`      | Article preview card      |
| `VpBadge`            | Status or count badge     |
| `VpBreadcrumbs`      | Navigation breadcrumbs    |
| `VpButton`           | Primary action button     |
| `VpCheckbox`         | Checkbox input            |
| `VpChip`             | Chip/tag component        |
| `VpDivider`          | Visual separator          |
| `VpDrawer`           | Side drawer panel         |
| `VpFooter`           | Page footer               |
| `VpIconButton`       | Icon-only button          |
| `VpInput`            | Text input field          |
| `VpInputQuantity`    | Quantity selector         |
| `VpLink`             | Hyperlink component       |
| `VpLinkList`         | List of links             |
| `VpLoader`           | Loading indicator         |
| `VpModal`            | Modal dialog              |
| `VpNavigationHeader` | Navigation header         |
| `VpPrice`            | Price display             |
| `VpProductCard`      | Product preview card      |
| `VpProgressBar`      | Progress indicator        |
| `VpRadioGroup`       | Radio button group        |
| `VpScoreRating`      | Score rating display      |
| `VpSearch`           | Search input              |
| `VpSelect`           | Dropdown select           |
| `VpSkeleton`         | Loading skeleton          |
| `VpStarRating`       | Star rating input/display |
| `VpSticker`          | Sticker/label component   |
| `VpTabs`             | Tabbed navigation         |
| `VpTextarea`         | Multiline text input      |
| `VpToggle`           | Toggle switch             |

## Theme Configuration

### Themes

| Theme    | Font                        | Description      |
| -------- | --------------------------- | ---------------- |
| `wonder` | Decathlon + Decathlon Brand | Current identity |
| `legacy` | Roboto                      | Former identity  |

### Wonder Theme (Recommended)

```bash
pnpm add @vtmn-play/fonts
```

```javascript
import "@vtmn-play/fonts/decathlon";
import "@vtmn-play/fonts/decathlon-brand";
```

### Dark Mode

Add the `.vp--dark-mode` CSS class on the main HTML element:

```html
<body class="vp--dark-mode">
  <!-- Your application -->
</body>
```

## Framework Integration

### React Usage

```tsx
import "@vtmn-play/design-tokens/foundations";
import { VpButton } from "@vtmn-play/react";

function App() {
  return (
    <VpButton variant="primary" size="medium">
      Click me
    </VpButton>
  );
}
```

#### React Server Components (Next.js App Router)

```tsx
// layout.tsx
import "@vtmn-play/design-tokens/foundations";
import "@vtmn-play/fonts/decathlon";
import "@vtmn-play/fonts/decathlon-brand";
```

#### The `asChild` Pattern

```tsx
import { VpButton } from "@vtmn-play/react";
import Link from "next/link";

<VpButton asChild>
  <Link href="/products">View Products</Link>
</VpButton>;
```

### Svelte Usage

```svelte
<script>
  import { VpButton } from "@vtmn-play/svelte";
</script>

<VpButton variant="primary" size="medium">
  Click me
</VpButton>
```

#### Headless Components

```typescript
import { VpButton } from "@vtmn-play/svelte/headless";
```

## Alternative Theme Integrations

### Ant Design Theme

For projects using Ant Design v5+:

```bash
pnpm add @vtmn-play/antd antd
```

```tsx
import { ConfigProvider } from "antd";
import VTMN_PLAY_ANTD_THEME from "@vtmn-play/antd";

function App() {
  return (
    <ConfigProvider theme={VTMN_PLAY_ANTD_THEME}>
      {/* Your Ant Design components */}
    </ConfigProvider>
  );
}
```

Demo repository: [dktunited/vp-antd-demo](https://github.com/dktunited/vp-antd-demo)

### shadcn/ui Theme

For projects using shadcn/ui with Tailwind CSS v4+:

```bash
pnpm add @vtmn-play/shadcn-ui @vtmn-play/tailwindcss
```

```css
@import "@vtmn-play/design-tokens";
@import "tailwindcss";
@import "@vtmn-play/tailwindcss/theme";
@import "@vtmn-play/shadcn-ui";
```

Demo repository: [dktunited/vp-shadcn-ui-demo](https://github.com/dktunited/vp-shadcn-ui-demo)

### Tailwind CSS Integration

#### Tailwind CSS v4

```css
@import "@vtmn-play/fonts/decathlon";
@import "@vtmn-play/fonts/decathlon-brand";
@import "@vtmn-play/design-tokens";
@layer theme, base, components, vitamin-play, utilities;
@import "tailwindcss";
@import "@vtmn-play/tailwindcss/theme";
```

**IMPORTANT - Tailwind v4 Theme Values:**

The Tailwind v4 theme configuration (colors, spacing, typography, etc.) is defined in CSS custom properties. The exact theme values are located in:

- **Theme values file**: [vtmn-play-tailwindcss-theme.css](https://github.com/dktunited/vitamin-play-web/blob/main/packages/themes/tailwindcss/build/vtmn-play-tailwindcss-theme.css)

**Always refer to this file for accurate theme values**. Do not hallucinate or invent theme values that are not defined in this file.

#### Tailwind CSS v2/v3

```javascript
// tailwind.config.js
module.exports = {
  presets: [require("@vtmn-play/tailwindcss/preset")],
  // ...
};
```

**Tailwind v2/v3 Preset Configuration:**

The preset configuration for Tailwind v2 and v3 is located in:

- **Preset file**: [vtmn-play-tailwindcss-preset.js](https://github.com/dktunited/vitamin-play-web/blob/main/packages/themes/tailwindcss/build/vtmn-play-tailwindcss-preset.js)

Demo repository: [dktunited/vp-tailwindcss-demo](https://github.com/dktunited/vp-tailwindcss-demo)

### Design Tokens & CSS Custom Properties

The design tokens are exported as CSS custom properties (CSS variables). These are the actual values behind the Tailwind theme configuration.

**Design Token Files:**

- **Semantic tokens (Wonder theme)**: [wonder.css](https://github.com/dktunited/vitamin-play-web/blob/main/packages/design-tokens/build/css/semantic/wonder.css) - Contains theme-specific semantic tokens
- **Core tokens**: [core.css](https://github.com/dktunited/vitamin-play-web/blob/main/packages/design-tokens/build/css/core/core.css) - Contains the base core tokens

These CSS custom properties define the actual color values, spacing, typography, and other design system values that are referenced in the Tailwind theme configuration.

**Important:** When working with Tailwind CSS, always refer to these token files to understand the underlying values behind the theme configuration.

#### Typography Utilities

Available typography classes from the Tailwind plugin:

- `.text-subtitle-m`, `.text-subtitle-l`
- `.text-body-s`, `.text-body-m`, `.text-body-l` (or `.text-s`, `.text-m`, `.text-l`)
- `.text-caption`, `.text-overline`
- `.text-title-s`, `.text-title-m`, `.text-title-l`, `.text-title-xl`
- `.text-inspiring-title-xl`
- `.text-link-s`, `.text-link-m`, `.text-link-l`, `.text-link-caption`

## Icons & Assets

### Using Standalone Icon Components (Recommended)

**IMPORTANT:** Use standalone icon components instead of the generic `VpIcon` component.

Each icon is available as its own named component:

```tsx
import {
  VpAccessibilityIcon,
  VpAddIcon,
  VpArrowRightIcon,
} from "@vtmn-play/icons/react";

function MyComponent() {
  return (
    <>
      <VpAccessibilityIcon />
      <VpAddIcon />
      <VpArrowRightIcon />
    </>
  );
}
```

### Using Standalone Asset Components (Recommended)

Similarly, use standalone asset components with the pattern `Vp<AssetName>Asset`:

```tsx
import { VpLogoAsset, VpBrandAsset } from "@vtmn-play/assets/react";

function MyComponent() {
  return (
    <>
      <VpLogoAsset />
      <VpBrandAsset />
    </>
  );
}
```

### Available Icons & Assets

For a complete list of available icons and assets, refer to the build directories:

**Icons:**

- React: [packages/icons/build/react](https://github.com/dktunited/vitamin-play-web/tree/main/packages/icons/build/react)
- Svelte: [packages/icons/build/svelte](https://github.com/dktunited/vitamin-play-web/tree/main/packages/icons/build/svelte)
- Vue: [packages/icons/build/vue](https://github.com/dktunited/vitamin-play-web/tree/main/packages/icons/build/vue)

**Assets:**

- React: [packages/assets/build/react](https://github.com/dktunited/vitamin-play-web/tree/main/packages/assets/build/react)
- Svelte: [packages/assets/build/svelte](https://github.com/dktunited/vitamin-play-web/tree/main/packages/assets/build/svelte)
- Vue: [packages/assets/build/vue](https://github.com/dktunited/vitamin-play-web/tree/main/packages/assets/build/vue)

**Example Icons:** `VpAccessibilityIcon`, `VpAddIcon`, `VpAlertIcon`, `VpArrowLeftIcon`, `VpArrowRightIcon`, `VpCalendarIcon`, `VpCheckIcon`, `VpCloseIcon`, `VpDeleteIcon`, `VpDownloadIcon`, `VpEditIcon`, `VpErrorIcon`, `VpHeartIcon`, `VpHomeIcon`, `VpInfoIcon`, `VpMenuIcon`, `VpSearchIcon`, `VpSettingsIcon`, `VpStarIcon`, `VpUserIcon`, and many more.

**Naming Convention:**

- Icons: `Vp<IconName>Icon` (e.g., `VpAccessibilityIcon`, `VpAddIcon`)
- Assets: `Vp<AssetName>Asset` (e.g., `VpLogoAsset`, `VpBrandAsset`)

## What to avoid

- **Don't skip design tokens**: Always import `@vtmn-play/design-tokens/foundations` before using components
- **Don't forget fonts**: Fonts are not auto-loaded; install and import `@vtmn-play/fonts` for the wonder theme
- **Don't mix themes**: Use either `wonder` or `legacy` theme consistently across your application
- **Don't ignore accessibility**: Use semantic HTML and follow component accessibility patterns
- **Don't hardcode colors**: Use design tokens and CSS custom properties instead of hex values
- **Don't bypass the layer order**: When using Tailwind CSS v4, maintain the correct `@layer` order
- **Don't use the generic VpIcon component**: Use standalone icon components like `VpAccessibilityIcon`, `VpAddIcon` instead
- **Don't use the generic VpAsset component**: Use standalone asset components like `Vp<AssetName>Asset` instead
- **Don't hallucinate Tailwind theme values**: Always refer to the official theme files (vtmn-play-tailwindcss-theme.css for v4, vtmn-play-tailwindcss-preset.js for v2/v3) for accurate configuration values

## Component Documentation

Each component has its own `README.md` file with detailed documentation (props, usage examples, variants).

**Component documentation pattern:**

```
https://github.com/dktunited/vitamin-play-web/blob/main/packages/frameworks/{FrameworkName}/src/components/{ComponentName}/README.md
```

Where `{FrameworkName}` is `react`, `svelte`, or `vue`.

Example: [VpButton React README.md](https://github.com/dktunited/vitamin-play-web/blob/main/packages/frameworks/react/src/components/VpButton/README.md)

## Accessibility

Vitamin Play components are built with accessibility in mind. Each component has its own `ACCESSIBILITY.md` file documenting:

- ARIA attributes and accessibility criteria compliance
- Screen reader restitution tests (NVDA, JAWS, VoiceOver, TalkBack)
- User implementation responsibilities
- RGAA (French accessibility framework) compliance

**Component accessibility documentation pattern:**

```
https://github.com/dktunited/vitamin-play-web/blob/main/packages/logic/src/components/{ComponentName}/ACCESSIBILITY.md
```

Example: [VpSticker ACCESSIBILITY.md](https://github.com/dktunited/vitamin-play-web/blob/main/packages/logic/src/components/VpSticker/ACCESSIBILITY.md)

### Additional Resources

- [SIG Digital Accessibility Wiki](https://decathlon.atlassian.net/wiki/spaces/TO/pages/187564961/SIG+DIGITAL+ACCESSIBILITY)
- [web.dev Learn Accessibility](https://web.dev/learn/accessibility/)
- [W3C WCAG Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [RGAA (French Accessibility Framework)](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

### Recommended Tools

- Screen readers: NVDA (Windows), VoiceOver (macOS), JAWS
- Browser extensions: axe DevTools, WAVE, Lighthouse
- Testing: @axe-core/react, jest-axe

## Vitamin Play Documentation

The comprehensive documentation for Vitamin Play is available in the [vitamin-play-documentation](https://github.com/dktunited/vitamin-play-documentation) repository.

### Design Guidelines (Foundations)

Design principles, colors, typography, spacing, accessibility, and other foundational guidelines:

- **Foundations documentation**: [src/content/pages/foundations](https://github.com/dktunited/vitamin-play-documentation/tree/main/src/content/pages/foundations)
  - Accessibility, Color System, Eco-Design, Iconography, Typography, Tokens, Layout & Spacing, Motion, Shape & Radius, etc.

### Component Design Guidelines

Design specifications, usage guidelines, and best practices for each component:

- **Components documentation**: [src/content/components](https://github.com/dktunited/vitamin-play-documentation/tree/main/src/content/components)
  - Button, Badge, Checkbox, Input, Link, Loader, Modal, Price, Radio, Search, Select, Skeleton, Tabs, Toggle, etc.

### Technical Documentation (Web)

Implementation details, props, and code examples for web frameworks:

- **Web technical docs**: [src/content/technical-docs/web](https://github.com/dktunited/vitamin-play-documentation/tree/main/src/content/technical-docs/web)
  - **React**: [web/react/{component}.md](https://github.com/dktunited/vitamin-play-documentation/tree/main/src/content/technical-docs/web/react) (e.g., `button.md`, `input.md`, `modal.md`)
  - **Svelte**: [web/svelte/{component}.md](https://github.com/dktunited/vitamin-play-documentation/tree/main/src/content/technical-docs/web/svelte) (e.g., `button.md`, `input.md`, `modal.md`)
  - **Vue**: [web/vue/{component}.md](https://github.com/dktunited/vitamin-play-documentation/tree/main/src/content/technical-docs/web/vue) (e.g., `button.md`, `input.md`, `modal.md`)

## References

- [Vitamin Play Web Repository](https://github.com/dktunited/vitamin-play-web) — Source code and documentation
- [Vitamin Play Documentation](https://github.com/dktunited/vitamin-play-documentation) — Comprehensive design and technical documentation
- [React Playground](https://special-adventure-p85wlrj.pages.github.io/playgrounds/next-js-pages-router-app) — Interactive React component demos
- [Svelte Playground](https://special-adventure-p85wlrj.pages.github.io/playgrounds/svelte-kit-app) — Interactive Svelte component demos
- [Sample Applications](https://github.com/dktunited/vitamin-play-web-sample-apps) — Example implementations
- [Vitamin Play Web UI Kit (Figma)](https://www.figma.com/design/lFF1tcCVcGgyExwWiSmpqv/Vitamin-Play---Web-UI-kit) — Design reference
- [Vitamin Play Foundations (Figma)](https://www.figma.com/design/ZNTn7GWGW1mCYXtsgEpT6s/Vitamin-Play---Foundations) — Design tokens and foundations

## Getting help

- **Slack**: [#design-system-vitamin-play](https://decathlondigital.slack.com/archives/C05J39MMK2M)
- **Feature requests**: [Jira Feature Request](https://decathlon.atlassian.net/jira/software/c/projects/DSVP/form/5780)
- **Bug reports**: [Jira Bug Report](https://decathlon.atlassian.net/jira/software/c/projects/DSVP/form/5747)
- **Open feedback**: [Jira Open Feedback](https://decathlon.atlassian.net/jira/software/c/projects/DSVP/form/5613)
