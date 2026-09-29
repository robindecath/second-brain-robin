# Web Scan Patterns

Grep patterns for web accessibility audits. Used by the Scout agent when the detected platform is Web.

---

## Core Patterns

```bash
# Interactive elements (keyboard accessibility)
grep -r "div.*onClick" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "span.*onClick" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "<a.*onClick" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Images (alt text)
grep -r "<img" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Form inputs (labeling)
grep -r "<input" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "<textarea" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "<select" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Buttons (semantic usage)
grep -r "<button" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Focus styles
grep -r "outline.*none" . --include="*.css" --include="*.scss" --include="*.sass" --exclude-dir={node_modules,build,dist,.git}
grep -r "outline: 0" . --include="*.css" --include="*.scss" --include="*.sass" --exclude-dir={node_modules,build,dist,.git}
grep -r ":focus-visible" . --include="*.css" --include="*.scss" --include="*.sass" --exclude-dir={node_modules,build,dist,.git}

# ARIA attributes
grep -r "aria-" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "role=" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Color contrast (hardcoded colors)
grep -r "color: #" . --include="*.css" --include="*.scss" --include="*.sass" --exclude-dir={node_modules,build,dist,.git}
grep -r "background: #" . --include="*.css" --include="*.scss" --include="*.sass" --exclude-dir={node_modules,build,dist,.git}
grep -r "rgb\|rgba\|hsl" . --include="*.css" --include="*.scss" --include="*.sass" --exclude-dir={node_modules,build,dist,.git}

# Headings (hierarchy)
grep -r "<h[1-6]" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Landmarks
grep -r "<nav\|<main\|<aside\|<header\|<footer" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Skip links
grep -r "href=\"#\"\|Skip to main\|skip-link" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Labels and form association
grep -r "placeholder=\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "htmlFor=\|for=\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "fieldset\|legend" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Status and live regions
grep -r "aria-current\|role=\"status\"\|role=\"alert\"\|aria-live" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# SPA title management
grep -r "document.title" . --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --exclude-dir={node_modules,build,dist,.git}
grep -r "<html" . --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# Duplicate IDs and autocomplete
grep -r "id=\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
grep -r "autocomplete=\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
```

---

## Advanced Patterns (P1)

```bash
# List structure — check for role="list" with CSS stripping
grep -r "role=\"list\"\|role=\"listitem\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
# IMPORTANT: if list-style:none/flex/grid applied, role="list" may be REQUIRED (Safari strips semantics)
grep -r "list-none\|list-style.*none" . --include="*.css" --include="*.scss" --exclude-dir={node_modules,build,dist,.git}

# Meter and progressbar — flag if missing aria-label/aria-labelledby
grep -r "role=\"meter\"\|role=\"progressbar\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}

# Headings inside <summary> (invisible to heading navigation)
grep -rn "<summary" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}
# Manually review: are there <h1>-<h6> inside <summary> tags?

# disabled on non-form interactive elements (should often be aria-disabled)
grep -r " disabled" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
# Cross-check: toolbar button, nav link, or similar non-form element → aria-disabled instead

# Assertive live regions (should be rare — only for critical errors)
grep -r "aria-live=\"assertive\"\|role=\"alert\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}

# aria-label containing role name (reads "navigation navigation")
grep -r "aria-label=\".*navigation\|aria-label=\".*button\|aria-label=\".*link" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}

# State repeated in accessible name (redundant with aria-expanded/pressed/checked/selected)
grep -r "aria-label=\".*expanded\|aria-label=\".*collapsed\|aria-label=\".*checked\|aria-label=\".*selected" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}

# Conditional alt text (CMS pattern — empty fallback = RUNTIME_REQUIRED)
grep -r "alt={" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
# Review for: alt={variable ?? ""} or alt={variable || ""}

# SVG as interactive element without keyboard handler
grep -r "<svg.*onClick\|<svg.*tabIndex" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
# Flag: no onKeyDown handler alongside tabIndex/role="button"

# autoComplete on personal data inputs (WCAG 1.3.5)
grep -r "type=\"email\"\|type=\"tel\"\|name=\"email\"\|name=\"phone\"\|name=\"firstName\"\|name=\"lastName\"\|name=\"address\"" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
# Cross-check: do these inputs have an autocomplete attribute?

# inert attribute — verify it's on the background, NOT on the overlay itself
grep -r " inert" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --exclude-dir={node_modules,build,dist,.git}

# prefers-reduced-motion coverage
grep -r "animation\|transition" . --include="*.css" --include="*.scss" --exclude-dir={node_modules,build,dist,.git}
# Cross-check: is there a @media (prefers-reduced-motion: reduce) override?

# color-scheme property (UA-rendered surfaces in dark mode)
grep -r "prefers-color-scheme" . --include="*.css" --include="*.scss" --exclude-dir={node_modules,build,dist,.git}
# Flag: dark mode via prefers-color-scheme but no color-scheme CSS property set
```

---

## Design System Patterns (Vitamin Play)

Only run these when Vitamin Play (`@vtmn-play/*`) is detected in `package.json`:

```bash
# Vitamin Play component usage
grep -r "VpButton\|VpIconButton" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
grep -r "VpInput\|VpTextarea\|VpSelect" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
grep -r "VpFormControl\|VpFormLabel\|VpFormError" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
grep -r "VpAsset" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}
grep -r "VpModal\|VpCombobox\|VpTabs\|VpAccordion\|VpBreadcrumbs" . --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --exclude-dir={node_modules,build,dist,.git}

# Color tokens vs hardcoded
grep -r "var(--vp-semantic-color" . --include="*.css" --include="*.scss" --exclude-dir={node_modules,build,dist,.git}
```

When Vitamin Play is detected, also load `../rules/vitamin-play-a11y.md` for auto-correction rules 1-27.
