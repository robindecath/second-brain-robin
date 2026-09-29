# Color Contrast

**Purpose**: Complete guide to WCAG color contrast requirements and Vitamin Play semantic color tokens for accessible color usage.

---

## Sommaire

- [WCAG Contrast Requirements](#wcag-contrast-requirements)
- [Vitamin Play Semantic Color Tokens](#vitamin-play-semantic-color-tokens)
- [Using Tokens in Components](#using-tokens-in-components)
- [Testing Color Contrast](#testing-color-contrast)
- [Common Patterns](#common-patterns)
- [Dark Mode Support](#dark-mode-support)
- [Color-Independent Design](#color-independent-design)
- [Troubleshooting Contrast Issues](#troubleshooting-contrast-issues)
- [Quick Reference](#quick-reference)
- [Manual Contrast Verification](#manual-contrast-verification)
- [Resources](#resources)

---

## WCAG Contrast Requirements

### Text Contrast (WCAG 1.4.3 - Level AA)

| Text Type                               | Minimum Ratio | Example                       |
| --------------------------------------- | ------------- | ----------------------------- |
| **Normal text** (< 18pt or < 14pt bold) | **4.5:1**     | Body copy, paragraphs, labels |
| **Large text** (18pt+ or 14pt+ bold)    | **3:1**       | Headings, hero text           |

### UI Component Contrast (WCAG 1.4.11 - Level AA)

| Component Type        | Minimum Ratio | Example                                              |
| --------------------- | ------------- | ---------------------------------------------------- |
| **UI components**     | **3:1**       | Button borders, form field borders, focus indicators |
| **Graphical objects** | **3:1**       | Icons, chart elements, required visual info          |
| **States**            | **3:1**       | Hover, focus, active states                          |

---

## Vitamin Play Semantic Color Tokens

Always use semantic tokens instead of hardcoded colors. Tokens ensure:

- **Theme support** (light/dark mode)
- **Accessibility compliance** (tested contrast ratios)
- **Design consistency** across the system

### Content (Text) Colors

```css
/* Primary text - Highest contrast for body copy */
color: var(--vp-semantic-color-content-primary);
/* Use for: Main text, headings, important content */

/* Secondary text - Medium contrast for supporting text */
color: var(--vp-semantic-color-content-secondary);
/* Use for: Subtitles, metadata, less prominent text */

/* Tertiary text - Lower contrast for subtle text */
color: var(--vp-semantic-color-content-tertiary);
/* Use for: Captions, timestamps, hints (ensure > 18pt for AA) */

/* Disabled text - Lowest contrast */
color: var(--vp-semantic-color-content-disabled);
/* Use for: Disabled form fields, inactive states */
/* WARNING: May not meet 4.5:1 - use only for disabled elements */
```

### Status Colors (Feedback)

```css
/* Negative - Errors and critical states */
color: var(--vp-semantic-color-content-negative);
background: var(--vp-semantic-color-background-negative);
border-color: var(--vp-semantic-color-border-negative);
/* Use for: Error messages, destructive actions, critical alerts */

/* Positive - Success states */
color: var(--vp-semantic-color-content-positive);
background: var(--vp-semantic-color-background-positive);
border-color: var(--vp-semantic-color-border-positive);
/* Use for: Success messages, confirmations, completed states */

/* Warning - Caution states */
color: var(--vp-semantic-color-content-warning);
background: var(--vp-semantic-color-background-warning);
border-color: var(--vp-semantic-color-border-warning);
/* Use for: Warnings, important notices, pending actions */

/* Informational - Neutral information */
color: var(--vp-semantic-color-content-info);
background: var(--vp-semantic-color-background-info);
border-color: var(--vp-semantic-color-border-info);
/* Use for: Tips, informational messages, help text */
```

### Background Colors

```css
/* Primary background - Main page background */
background: var(--vp-semantic-color-background-primary);

/* Secondary background - Cards, panels, sections */
background: var(--vp-semantic-color-background-secondary);

/* Tertiary background - Subtle differentiation */
background: var(--vp-semantic-color-background-tertiary);

/* Elevated background - Modals, dropdowns, overlays */
background: var(--vp-semantic-color-background-elevated);
```

### Border Colors

```css
/* Primary border - Default borders */
border-color: var(--vp-semantic-color-border-primary);

/* Secondary border - Subtle borders */
border-color: var(--vp-semantic-color-border-secondary);

/* Focus border - Keyboard focus indicator */
outline: 2px solid var(--vp-semantic-color-border-focus);
outline-offset: 2px;
/* CRITICAL: Must have 3:1 contrast against background */
```

### Interactive Colors

```css
/* Brand/Primary actions */
color: var(--vp-semantic-color-content-brand);
background: var(--vp-semantic-color-background-brand);
/* Use for: Primary buttons, links, CTAs */

/* Interactive elements (hover states) */
color: var(--vp-semantic-color-content-interactive);
/* Use for: Clickable elements, hoverable items */
```

---

## Using Tokens in Components

### VpButton Example

```tsx
import { VpButton } from "@vtmn-play/react";

// ✅ Uses tokens automatically
<VpButton variant="primary">Primary action</VpButton>
<VpButton variant="secondary">Secondary action</VpButton>
<VpButton variant="destructive">Delete</VpButton>

// Custom styled button (when needed)
<VpButton
  style={{
    color: "var(--vp-semantic-color-content-primary)",
    backgroundColor: "var(--vp-semantic-color-background-secondary)",
    borderColor: "var(--vp-semantic-color-border-primary)",
  }}
>
  Custom button
</VpButton>
```

### Error Message Example

```tsx
import { VpFormError } from "@vtmn-play/react";

// ✅ VpFormError uses negative tokens automatically
<VpFormError>Invalid email address</VpFormError>

// Custom error message
<div
  role="alert"
  style={{
    color: "var(--vp-semantic-color-content-negative)",
    backgroundColor: "var(--vp-semantic-color-background-negative)",
    borderLeft: "4px solid var(--vp-semantic-color-border-negative)",
    padding: "1rem",
  }}
>
  Form contains errors
</div>
```

### Status Badge Example

```tsx
function StatusBadge({
  status,
}: {
  status: "error" | "success" | "warning" | "info";
}) {
  const colorMap = {
    error: {
      bg: "var(--vp-semantic-color-background-negative)",
      text: "var(--vp-semantic-color-content-negative)",
      border: "var(--vp-semantic-color-border-negative)",
    },
    success: {
      bg: "var(--vp-semantic-color-background-positive)",
      text: "var(--vp-semantic-color-content-positive)",
      border: "var(--vp-semantic-color-border-positive)",
    },
    warning: {
      bg: "var(--vp-semantic-color-background-warning)",
      text: "var(--vp-semantic-color-content-warning)",
      border: "var(--vp-semantic-color-border-warning)",
    },
    info: {
      bg: "var(--vp-semantic-color-background-info)",
      text: "var(--vp-semantic-color-content-info)",
      border: "var(--vp-semantic-color-border-info)",
    },
  };

  return (
    <span
      style={{
        backgroundColor: colorMap[status].bg,
        color: colorMap[status].text,
        border: `1px solid ${colorMap[status].border}`,
        padding: "0.25rem 0.5rem",
        borderRadius: "0.25rem",
      }}
    >
      {status}
    </span>
  );
}
```

---

## Testing Color Contrast

### Browser DevTools

#### Chrome DevTools

1. Inspect element
2. In Styles panel, click color swatch
3. Color picker shows contrast ratio
4. ✅ or ❌ icons indicate AA/AAA pass/fail
5. View accessible color suggestions

#### Firefox DevTools

1. Inspect element
2. Click color value
3. Contrast ratio displayed in picker
4. Accessibility panel flags issues

### Online Tools

- **WebAIM Contrast Checker**: <https://webaim.org/resources/contrastchecker/>
- **Coolors Contrast Checker**: <https://coolors.co/contrast-checker>
- **Color Review**: <https://color.review/>

### Browser Extensions

- **axe DevTools** - Automated contrast testing
- **WAVE** - Visual overlay of contrast issues
- **Accessibility Insights** - Microsoft's testing tool

---

## Common Patterns

### Text on Background

```css
/* ✅ CORRECT - Primary text on primary background */
.container {
  background: var(--vp-semantic-color-background-primary);
  color: var(--vp-semantic-color-content-primary);
}
/* Vitamin Play ensures this meets 4.5:1 minimum */

/* ✅ CORRECT - Text on colored backgrounds */
.error-box {
  background: var(--vp-semantic-color-background-negative);
  color: var(--vp-semantic-color-content-negative);
}
/* Status tokens are paired for sufficient contrast */

/* ❌ WRONG - Hardcoded colors */
.container {
  background: #f5f5f5;
  color: #999999; /* May fail contrast! */
}
```

### Links and Interactive Elements

```css
/* ✅ CORRECT - Using brand colors for links */
a {
  color: var(--vp-semantic-color-content-brand);
  text-decoration: underline; /* Always underline links for non-color identification */
}

a:hover {
  color: var(--vp-semantic-color-content-interactive);
}

a:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}
```

### Focus Indicators

```css
/* ✅ CORRECT - Accessible focus ring */
*:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}
/* Focus border token ensures 3:1 contrast on all backgrounds */

/* ❌ WRONG - Removing focus indicator */
*:focus {
  outline: none; /* NEVER do this */
}

/* ❌ WRONG - Insufficient contrast */
*:focus {
  outline: 1px solid #cccccc; /* Likely fails 3:1 */
}
```

### Buttons

```css
/* ✅ CORRECT - Using VpButton component */
/* VpButton handles all color states automatically */

/* If custom button needed: */
.custom-button {
  background: var(--vp-semantic-color-background-brand);
  color: var(--vp-semantic-color-content-brand);
  border: 1px solid var(--vp-semantic-color-border-brand);
}

.custom-button:hover {
  background: var(--vp-semantic-color-background-brand-hover);
}

.custom-button:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}

.custom-button:disabled {
  background: var(--vp-semantic-color-background-disabled);
  color: var(--vp-semantic-color-content-disabled);
  cursor: not-allowed;
}
```

---

## Dark Mode Support

Vitamin Play semantic tokens automatically adapt to dark mode:

```tsx
// ✅ Automatically theme-aware
function Card() {
  return (
    <div
      style={{
        background: "var(--vp-semantic-color-background-secondary)",
        color: "var(--vp-semantic-color-content-primary)",
        border: "1px solid var(--vp-semantic-color-border-primary)",
      }}
    >
      Content adapts to light/dark theme automatically
    </div>
  );
}

// ❌ WRONG - Hardcoded colors break in dark mode
function BadCard() {
  return (
    <div
      style={{
        background: "#ffffff",
        color: "#000000",
      }}
    >
      Always shows light colors, even in dark mode
    </div>
  );
}
```

---

## Color-Independent Design

**Never rely on color alone to convey information** (WCAG 1.4.1)

### ❌ Bad: Color Only

```tsx
// WRONG - Only color indicates status
<span style={{ color: "red" }}>Error</span>
<span style={{ color: "green" }}>Success</span>
```

### ✅ Good: Color + Icon/Text

```tsx
import { VpCheckCircleIcon, VpXCircleIcon } from "@vtmn-play/icons/react";

// CORRECT - Color + icon + text
<div style={{ color: "var(--vp-semantic-color-content-positive)" }}>
  <VpCheckCircleIcon aria-hidden="true" />
  <span>Success: Form submitted</span>
</div>

<div style={{ color: "var(--vp-semantic-color-content-negative)" }}>
  <VpXCircleIcon aria-hidden="true" />
  <span>Error: Invalid email address</span>
</div>
```

### ✅ Good: Required Field Indication

```tsx
// CORRECT - Multiple indicators
<VpFormControl isRequired>
  <VpFormLabel>
    Email address
    <span
      aria-label="required"
      style={{ color: "var(--vp-semantic-color-content-negative)" }}
    >
      {" "}
      *
    </span>
  </VpFormLabel>
  <VpInput type="email" name="email" aria-required="true" />
</VpFormControl>
// Indicators: *, aria-required, visual styling from isRequired
```

---

## Troubleshooting Contrast Issues

### Issue: Text on Background Fails

```tsx
// ❌ Problem
<div style={{ background: "#f0f0f0", color: "#999999" }}>
  Text might fail contrast
</div>

// ✅ Solution: Use semantic tokens
<div
  style={{
    background: "var(--vp-semantic-color-background-secondary)",
    color: "var(--vp-semantic-color-content-primary)",
  }}
>
  Text meets contrast requirements
</div>
```

### Issue: Button Border Not Visible

```tsx
// ❌ Problem
<VpButton
  variant="secondary"
  style={{ borderColor: "#e5e5e5" }} // Low contrast
>
  Button
</VpButton>

// ✅ Solution: Use border token
<VpButton
  variant="secondary"
  style={{ borderColor: "var(--vp-semantic-color-border-primary)" }}
>
  Button
</VpButton>
```

### Issue: Focus Indicator Too Subtle

```css
/* ❌ Problem */
button:focus {
  outline: 1px solid #d1d1d1; /* Fails 3:1 */
}

/* ✅ Solution */
button:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}
```

---

## Quick Reference

### Token Categories

| Category       | Token Prefix                                           | Example                |
| -------------- | ------------------------------------------------------ | ---------------------- |
| Content (text) | `--vp-semantic-color-content-*`                        | `content-primary`      |
| Background     | `--vp-semantic-color-background-*`                     | `background-secondary` |
| Border         | `--vp-semantic-color-border-*`                         | `border-primary`       |
| Status         | `--vp-semantic-color-*-negative/positive/warning/info` | `content-negative`     |
| Brand          | `--vp-semantic-color-*-brand`                          | `background-brand`     |

### Contrast Ratios Quick Check

- **4.5:1** = Normal text (most common)
- **3:1** = Large text, UI components, focus indicators
- **7:1** = AAA level (aim for this when possible)

### Testing Checklist

- [ ] All text meets 4.5:1 (or 3:1 for large text)
- [ ] All buttons/borders meet 3:1
- [ ] Focus indicators meet 3:1

---

## Manual Contrast Verification

### Using Browser DevTools

**Chrome/Edge DevTools:**

1. Right-click element → **Inspect**
2. In Elements panel, click color square next to `color` property
3. Color picker shows contrast ratio with background
4. Look for ✅ (passes AA) or ❌ (fails)
5. Adjust lightness slider to find passing colors

**Firefox DevTools:**

1. Right-click element → **Inspect**
2. In Inspector, find `color` property
3. Click color value to open picker
4. Contrast ratio displayed at bottom
5. Shows AA/AAA compliance badges

### Using Contrast Checker Tools

#### WebAIM Contrast Checker (Online)

- **URL**: <https://webaim.org/resources/contrastchecker/>
- **Input**: Foreground color, background color (hex values)
- **Output**: Exact ratio + pass/fail for AA/AAA at normal/large text

```bash
# Example check
Foreground: #595959
Background: #ffffff
Result: 7.0:1 ✅ (Passes AAA for all text sizes)

Foreground: #999999
Background: #ffffff
Result: 2.8:1 ❌ (Fails AA for all text sizes)
```

#### Colour Contrast Analyser (Desktop App)

- **Download**: <https://www.tpgi.com/color-contrast-checker/>
- **Features**: Eyedropper tool to pick colors from screen
- **Best for**: Testing designs before implementation

#### axe DevTools (Browser Extension)

- **Install**: Chrome/Firefox/Edge extension
- **Usage**: F12 → axe DevTools → Scan → Filter "Color Contrast"
- **Advantage**: Scans entire page automatically

### Manual Calculation Formula

If you need to calculate manually:

```
Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)

Where:
- L1 = relative luminance of lighter color
- L2 = relative luminance of darker color
- Relative luminance = 0.2126*R + 0.7152*G + 0.0722*B
- R, G, B = normalized values (sRGB ÷ 255, then gamma corrected)
```

**In practice**: Use tools instead of calculating manually!

### Checking Custom Color Combinations

When using non-semantic colors (not recommended), verify manually:

```tsx
// Custom brand color - must verify contrast
<div style={{
  background: '#ff5500',  // Custom orange
  color: '#ffffff'         // White text
}}>
  // Check manually: https://webaim.org/resources/contrastchecker/
  // #ffffff on #ff5500 = 3.6:1
  // ✅ Passes AA for large text (18pt+)
  // ❌ Fails AA for normal text
</div>

// Solution: Use semantic token instead
<div style={{
  background: 'var(--vp-semantic-color-background-brand)',
  color: 'var(--vp-semantic-color-content-on-brand)'
}}>
  // Guaranteed to pass WCAG AA (4.5:1+)
</div>
```

### Gradient Background Verification

Gradients require special attention:

```tsx
// ❌ Problem: Text might fail on part of gradient
<div style={{
  background: 'linear-gradient(to right, #ffffff, #e0e0e0)',
  color: '#666666'
}}>
  Text might fail at light end of gradient
</div>

// ✅ Solution 1: Verify contrast at both ends
// Check #666666 on #ffffff AND #666666 on #e0e0e0

// ✅ Solution 2: Add text shadow or background
<div style={{
  background: 'linear-gradient(to right, #ffffff, #e0e0e0)',
  color: '#333333',
  textShadow: '0 0 4px rgba(255,255,255,0.8)'
}}>
  Text readable across entire gradient
</div>
```

### Dark Mode Verification

Always test both light and dark themes:

```tsx
// Light mode check
color: var(--vp-semantic-color-content-primary)
background: var(--vp-semantic-color-background-primary)
// Typically: #000000 on #ffffff (21:1) ✅

// Dark mode check (same tokens, different values)
color: var(--vp-semantic-color-content-primary)
background: var(--vp-semantic-color-background-primary)
// Typically: #ffffff on #1a1a1a (17.8:1) ✅
```

**Testing workflow:**

1. Toggle dark mode in browser/OS
2. Rerun axe DevTools scan
3. Verify semantic tokens adapt correctly
4. Check custom colors (if any) work in both modes

### Image Text Verification

Text in images must also meet contrast requirements:

```tsx
// ❌ Problem: Image with low-contrast text
<img src="hero-banner.jpg" alt="Summer Sale - 50% Off" />
// If image has light gray text on white background, it fails

// ✅ Solution 1: Fix the image (increase contrast)
// ✅ Solution 2: Provide alternative
<figure>
  <img src="hero-banner.jpg" alt="" role="presentation" />
  <figcaption style={{
    color: 'var(--vp-semantic-color-content-primary)',
    fontSize: '2rem'
  }}>
    Summer Sale - 50% Off
  </figcaption>
</figure>
```

### Quick Verification Checklist

Use this when reviewing designs or implementing custom colors:

- [ ] Open WebAIM Contrast Checker: <https://webaim.org/resources/contrastchecker/>
- [ ] Test foreground color against background
- [ ] Verify 4.5:1 for normal text (< 18pt regular, < 14pt bold)
- [ ] Verify 3:1 for large text (18pt+ regular, 14pt+ bold)
- [ ] Verify 3:1 for UI components (buttons, borders, focus indicators)
- [ ] Test hover/focus states
- [ ] Test both light and dark modes
- [ ] Check gradients at both extremes
- [ ] Verify text in images
- [ ] Rerun automated scan (axe DevTools) to confirm

### Common Contrast Failures and Fixes

| Scenario           | Failing Colors         | Ratio    | Fix                                             |
| ------------------ | ---------------------- | -------- | ----------------------------------------------- |
| Gray text on white | `#999999` on `#ffffff` | 2.8:1 ❌ | Use `#595959` (7.0:1 ✅)                        |
| Light blue link    | `#6CB4EE` on `#ffffff` | 2.4:1 ❌ | Use `#0066CC` (7.0:1 ✅)                        |
| Yellow warning     | `#FFFF00` on `#ffffff` | 1.1:1 ❌ | Use dark bg: `#FFFF00` on `#333333` (12.6:1 ✅) |
| Placeholder text   | `#AAAAAA` on `#ffffff` | 2.3:1 ❌ | Use `#767676` (4.5:1 ✅)                        |
| Disabled button    | `#CCCCCC` on `#ffffff` | 1.6:1 ❌ | Acceptable for disabled (not required)          |

**Note**: Disabled elements are exempt from contrast requirements, but best practice is to maintain readability.

---

## Resources

- **WCAG 2.2 Color Contrast**: <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum>
- **WebAIM Color Contrast Checker**: <https://webaim.org/resources/contrastchecker/>
- **Vitamin Play Design Tokens**: Check `@vtmn-play/design-tokens` package documentation
