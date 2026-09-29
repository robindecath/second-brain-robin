# WCAG 2.2 Level AA Checklist

Complete checklist of all 50 WCAG 2.2 Level A and AA success criteria with practical implementation examples.

**Use this checklist when:**

- Conducting complete accessibility audit
- Preparing for WCAG 2.2 AA compliance certification
- Need comprehensive understanding of all success criteria
- Training team on accessibility requirements

> **Multi-standard mapping**: This checklist covers WCAG 2.2. To find the equivalent criteria in other standards:
> - **RGAA 4.1** (French, 106 criteria) → see `cross-references/RGAA_CROSS_REFERENCE.toon`
> - **RAAM 1.1** (Luxembourg mobile, ~83 criteria) → see `cross-references/RAAM_CROSS_REFERENCE.toon`
> - **EN 301 549** (European, ~200+ clauses) → see `cross-references/WCAG_CROSS_REFERENCE.toon`

**Note**: Web examples use Vitamin Play components where applicable. Platform-specific implementation details are in the relevant platform skill (`../references/`, `../references/`, `../references/`).

---

## 1. Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

### 1.1 Text Alternatives

#### 1.1.1 Non-text Content (Level A)

All non-text content has a text alternative.

```tsx
// Images
<img src="logo.png" alt="Decathlon" />
<img src="decoration.png" alt="" role="presentation" />  {/* Decorative */}

// Icon-only buttons - Use VpIconButton
import { VpIconButton } from "@vtmn-play/react";
import { VpCloseIcon, VpSearchIcon } from "@vtmn-play/icons/react";

<VpIconButton aria-label="Close dialog" onClick={handleClose}>
  <VpCloseIcon />
</VpIconButton>

<VpIconButton aria-label="Search products" onClick={handleSearch}>
  <VpSearchIcon />
</VpIconButton>

// Charts/graphs - provide detailed alt text
<img
  src="sales-chart.png"
  alt="Bar chart showing 25% increase in sales from Q1 ($40k) to Q2 ($50k)"
/>

// Form controls with VpFormControl
import { VpFormControl, VpFormLabel, VpInput } from "@vtmn-play/react";

<VpFormControl>
  <VpFormLabel>Search</VpFormLabel>
  <VpInput type="text" name="search" placeholder="Search products..." />
</VpFormControl>
```

**Pass**: Every image, icon, and control has appropriate text alternative
**Fail**: Images missing alt, `VpIconButton` without `aria-label`, icon buttons with no label

---

### 1.2 Time-based Media

#### 1.2.1 Audio-only and Video-only (Level A)

Provide transcript for audio-only or video-only content.

```html
<audio src="podcast.mp3" controls></audio>
<a href="transcript.html">Read transcript</a>
```

#### 1.2.2 Captions (Level A)

Provide captions for all video with audio.

```html
<video controls>
  <source src="video.mp4" type="video/mp4" />
  <track kind="captions" src="captions.vtt" srclang="en" label="English" />
</video>
```

#### 1.2.3 Audio Description or Media Alternative (Level A)

Provide audio description or transcript for video.

#### 1.2.4 Captions (Live) (Level AA)

Captions provided for live audio content.

#### 1.2.5 Audio Description (Level AA)

Audio description for all video content.

---

### 1.3 Adaptable

#### 1.3.1 Info and Relationships (Level A)

Information, structure, and relationships can be programmatically determined.

```html
<!-- ✅ Proper heading hierarchy -->
<h1>Main Page Title</h1>
<h2>Section Title</h2>
<h3>Subsection</h3>

<!-- ✅ Proper form labels with VpFormControl -->
import { VpFormControl, VpFormLabel, VpInput } from "@vtmn-play/react";

<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
</VpFormControl>

<!-- VpFormControl automatically handles label association -->

<!-- ✅ Proper table headers -->
<table>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Email</th>
    </tr>
  </thead>
</table>

<!-- ❌ WRONG - skipped heading -->
<h1>Title</h1>
<h3>Subsection</h3>
<!-- Skipped h2 -->
```

#### 1.3.2 Meaningful Sequence (Level A)

Reading and navigation order is logical.

```html
<!-- Source order matches visual order -->
<nav>Navigation</nav>
<main>Content</main>
<aside>Sidebar</aside>
<footer>Footer</footer>
```

#### 1.3.3 Sensory Characteristics (Level A)

Instructions don't rely solely on sensory characteristics.

```html
<!-- ❌ WRONG -->
<p>Click the round button on the right</p>

<!-- ✅ CORRECT -->
<p>Click the Submit button</p>
<button>Submit</button>
```

#### 1.3.4 Orientation (Level AA)

Content doesn't restrict to single orientation unless essential.

```css
/* Don't lock orientation */
/* Allow both portrait and landscape */
```

#### 1.3.5 Identify Input Purpose (Level AA)

Input purpose can be programmatically determined.

```html
<input type="email" autocomplete="email" name="email" />
<input type="tel" autocomplete="tel" name="phone" />
<input type="text" autocomplete="given-name" name="first-name" />
```

---

### 1.4 Distinguishable

#### 1.4.1 Use of Color (Level A)

Color is not the only visual means of conveying information.

```tsx
import { VpXCircleIcon, VpCheckCircleIcon } from "@vtmn-play/icons/react";

// ❌ WRONG - color only
<span style={{ color: 'var(--vp-semantic-color-content-negative)' }}>
  Error
</span>

// ✅ CORRECT - icon + color + text
<div style={{
  color: 'var(--vp-semantic-color-content-negative)',
  display: 'flex',
  gap: '0.5rem',
  alignItems: 'center'
}}>
  <VpXCircleIcon aria-hidden="true" />
  <span>Error: Invalid email address</span>
</div>

// ✅ CORRECT - Success with icon
<div style={{
  color: 'var(--vp-semantic-color-content-positive)',
  display: 'flex',
  gap: '0.5rem',
  alignItems: 'center'
}}>
  <VpCheckCircleIcon aria-hidden="true" />
  <span>Success: Changes saved</span>
</div>
```

**Key principle**: Status must be conveyed through icon + text, not color alone.

#### 1.4.2 Audio Control (Level A)

Mechanism to pause/stop/control audio that plays >3 seconds.

```html
<audio controls>
  <source src="background-music.mp3" />
</audio>
```

#### 1.4.3 Contrast (Minimum) (Level AA)

**Contrast ratios:**

- Normal text: 4.5:1
- Large text (18pt+ or 14pt+ bold): 3:1
- UI components: 3:1

```tsx
// ❌ FAIL - Hardcoded colors, likely fails contrast
<p style={{ color: '#999999', background: '#ffffff' }}>
  Gray text on white - 2.8:1 (fails WCAG AA)
</p>

// ✅ PASS - Vitamin Play semantic tokens guarantee 4.5:1+
<p style={{
  color: 'var(--vp-semantic-color-content-primary)',
  background: 'var(--vp-semantic-color-background-primary)'
}}>
  Primary text with guaranteed contrast
</p>

// ✅ PASS - Status colors with paired backgrounds
<div style={{
  color: 'var(--vp-semantic-color-content-negative)',
  background: 'var(--vp-semantic-color-background-negative)',
  border: '1px solid var(--vp-semantic-color-border-negative)'
}}>
  Error message with accessible contrast
</div>
```

**Testing**: Use axe DevTools, browser contrast checker, or WebAIM Contrast Checker.
**Best practice**: Always use `--vp-semantic-color-*` tokens to guarantee WCAG AA compliance.

#### 1.4.4 Resize Text (Level AA)

Text can be resized to 200% without loss of content or functionality.

```css
/* Use relative units */
font-size: 1rem; /* Not px */
max-width: 60ch; /* Not fixed px */
```

#### 1.4.5 Images of Text (Level AA)

Use real text instead of images of text (unless essential).

```html
<!-- ❌ Avoid -->
<img src="heading.png" alt="Welcome" />

<!-- ✅ Use real text -->
<h1>Welcome</h1>
```

#### 1.4.10 Reflow (Level AA)

Content reflows without horizontal scrolling at 320px width.

```css
/* Responsive design */
@media (max-width: 768px) {
  /* Stack instead of overflow */
}
```

#### 1.4.11 Non-text Contrast (Level AA)

UI components and graphics have 3:1 contrast.

```css
/* Button border contrast */
button {
  border: 1px solid #757575; /* 3:1 on white */
  background: #f0f0f0;
}
```

#### 1.4.12 Text Spacing (Level AA)

Content doesn't break when text spacing is increased.

```css
/* Support user text spacing overrides */
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
  /* Content should still work */
}
```

#### 1.4.13 Content on Hover or Focus (Level AA)

Additional content on hover/focus is dismissible, hoverable, and persistent.

```html
<!-- Tooltip that can be dismissed with Escape -->
<button aria-describedby="tooltip">Info</button>
<div id="tooltip" role="tooltip" hidden>Additional information</div>
```

---

## 2. Operable

User interface components and navigation must be operable.

### 2.1 Keyboard Accessible

#### 2.1.1 Keyboard (Level A)

All functionality available via keyboard.

```html
<!-- ✅ CORRECT -->
<button onclick="doThing()">Click me</button>
<a href="/page">Link</a>

<!-- ❌ WRONG -->
<div onclick="doThing()">Click me</div>
<!-- Not keyboard accessible -->
```

#### 2.1.2 No Keyboard Trap (Level A)

Keyboard focus can move away from any component.

```javascript
// ✅ Dialog with Escape key to close
function Dialog() {
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === "Escape") closeDialog();
    };
    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, []);
}
```

#### 2.1.4 Character Key Shortcuts (Level A)

If single-character shortcuts exist, they can be turned off or remapped.

---

### 2.2 Enough Time

#### 2.2.1 Timing Adjustable (Level A)

Time limits can be turned off, adjusted, or extended.

```html
<!-- Session timeout warning -->
<div role="alert">
  <p>Your session will expire in 2 minutes.</p>
  <button>Extend session</button>
</div>
```

#### 2.2.2 Pause, Stop, Hide (Level A)

Moving, blinking, or scrolling content can be paused.

```html
<div class="carousel">
  <button aria-label="Pause carousel">⏸</button>
  <!-- Carousel content -->
</div>
```

---

### 2.3 Seizures and Physical Reactions

#### 2.3.1 Three Flashes or Below Threshold (Level A)

No content flashes more than 3 times per second.

---

### 2.4 Navigable

#### 2.4.1 Bypass Blocks (Level A)

Mechanism to skip repeated content (skip links).

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
<nav><!-- Navigation --></nav>
<main id="main-content" tabindex="-1">
  <!-- Content -->
</main>
```

#### 2.4.2 Page Titled (Level A)

Pages have descriptive titles.

```html
<title>Contact Us - Company Name</title>
```

#### 2.4.3 Focus Order (Level A)

Focusable components receive focus in logical order.

```html
<!-- Tab order: 1 → 2 → 3 (natural order) -->
<input type="text" name="name" />
<input type="email" name="email" />
<button type="submit">Submit</button>
```

#### 2.4.4 Link Purpose (In Context) (Level A)

Purpose of each link can be determined from link text or context.

```html
<!-- ❌ WRONG -->
<a href="/article">Click here</a>

<!-- ✅ CORRECT -->
<a href="/article">Read our accessibility guide</a>

<!-- ✅ CORRECT - aria-label adds context -->
<a href="/article" aria-label="Read our accessibility guide">Read more</a>
```

#### 2.4.5 Multiple Ways (Level AA)

More than one way to locate pages (menu, search, sitemap).

#### 2.4.6 Headings and Labels (Level AA)

Headings and labels describe topic or purpose.

```html
<h2>Contact Form</h2>
<label for="name">Full Name</label>
<input type="text" id="name" />
```

#### 2.4.7 Focus Visible (Level AA)

Keyboard focus indicator is visible.

```css
*:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* ❌ WRONG */
*:focus {
  outline: none; /* Never do this without replacement */
}
```

---

### 2.5 Input Modalities

#### 2.5.1 Pointer Gestures (Level A)

Functionality that uses multipoint or path-based gestures has single-pointer alternative.

#### 2.5.2 Pointer Cancellation (Level A)

For single-pointer functionality, activation happens on up-event.

#### 2.5.3 Label in Name (Level A)

For components with labels, the accessible name contains the visible text.

```html
<!-- Visible label: "Submit" -->
<button>Submit</button>
<!-- Accessible name: "Submit" ✅ -->

<!-- ❌ WRONG -->
<button aria-label="Send form">Submit</button>
<!-- Accessible name doesn't match -->
```

#### 2.5.4 Motion Actuation (Level A)

Functionality operated by device motion can also be operated by UI components.

---

## 3. Understandable

Information and operation of user interface must be understandable.

### 3.1 Readable

#### 3.1.1 Language of Page (Level A)

Default language of page is programmatically determined.

```html
<html lang="en"></html>
```

#### 3.1.2 Language of Parts (Level AA)

Language of each passage is programmatically determined.

```html
<p>The French word for hello is <span lang="fr">bonjour</span>.</p>
```

---

### 3.2 Predictable

#### 3.2.1 On Focus (Level A)

Receiving focus doesn't initiate change of context.

```html
<!-- ❌ WRONG - opens new page on focus -->
<input onfocus="window.location='/new-page'" />

<!-- ✅ CORRECT - user must activate -->
<button onclick="window.location='/new-page'">Go to page</button>
```

#### 3.2.2 On Input (Level A)

Changing setting doesn't automatically cause change of context.

```html
<!-- ❌ WRONG - auto-submit on change -->
<select onchange="this.form.submit()">
  <!-- ✅ CORRECT - explicit submit -->
  <select name="category"></select>
  <button type="submit">Apply filter</button>
</select>
```

#### 3.2.3 Consistent Navigation (Level AA)

Navigation mechanisms that are repeated appear in same relative order.

#### 3.2.4 Consistent Identification (Level AA)

Components with same functionality are identified consistently.

```html
<!-- Same icon/label for same action across pages -->
<button aria-label="Close">×</button>
<!-- Consistent everywhere -->
```

---

### 3.3 Input Assistance

#### 3.3.1 Error Identification (Level A)

Errors are identified and described in text.

```html
<input type="email" aria-invalid="true" aria-describedby="email-error" />
<span id="email-error" role="alert">
  Error: Please enter a valid email address
</span>
```

#### 3.3.2 Labels or Instructions (Level A)

Labels or instructions provided when content requires user input.

```html
<label for="password"> Password (minimum 8 characters) </label>
<input type="password" id="password" minlength="8" />
```

#### 3.3.3 Error Suggestion (Level AA)

If error is detected, suggestions for correction are provided.

```html
<span id="email-error" role="alert">
  Error: Email format is incorrect. Example: name@example.com
</span>
```

#### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)

For legal/financial/data submissions, one of the following is true:

- Reversible
- Checked
- Confirmed

```html
<form>
  <!-- Step 1: Enter data -->
  <input type="text" name="account" />

  <!-- Step 2: Review -->
  <div class="review">
    <p>Please review: Account number 12345</p>
    <button type="button" onclick="goBack()">Edit</button>
    <button type="submit">Confirm</button>
  </div>
</form>
```

---

## 4. Robust

Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.

### 4.1 Compatible

#### 4.1.1 Parsing (Level A)

HTML is valid (no duplicate IDs, proper nesting).

```html
<!-- ✅ Valid HTML -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- ❌ WRONG - invalid nesting -->
<ul>
  <div>Not allowed here</div>
</ul>
```

#### 4.1.2 Name, Role, Value (Level A)

For all UI components, name, role, and value can be programmatically determined.

```html
<!-- Native elements have this built-in -->
<button>Click me</button>
<!-- Role: button, Name: "Click me" -->

<!-- Custom elements need ARIA -->
<div role="button" tabindex="0" aria-pressed="false">Toggle</div>
```

#### 4.1.3 Status Messages (Level AA)

Status messages can be programmatically determined through role or properties.

```html
<!-- Success message -->
<div role="status" aria-live="polite">Form submitted successfully</div>

<!-- Error message -->
<div role="alert" aria-live="assertive">Error: Please fix the errors above</div>
```

---

## Quick Testing Checklist

Use this for rapid audits:

### Automated (5 minutes)

- [ ] Run axe DevTools scan
- [ ] Run Lighthouse accessibility audit
- [ ] Fix all critical violations

### Keyboard (10 minutes)

- [ ] Tab through entire page
- [ ] Activate all interactive elements with Enter/Space
- [ ] Close dialogs with Escape
- [ ] Navigate menus with arrows
- [ ] Verify focus visible at all times

### Screen Reader (15 minutes)

- [ ] Turn on NVDA or VoiceOver
- [ ] Navigate page with arrow keys
- [ ] Verify all images described
- [ ] Verify form labels read
- [ ] Verify dynamic updates announced
- [ ] Check heading structure makes sense

### Visual (5 minutes)

- [ ] Check color contrast with picker
- [ ] Zoom to 200% - content still works
- [ ] Resize window to 320px - no horizontal scroll
- [ ] Verify focus indicators visible

---

**Total audit time**: ~35 minutes per page
**Result**: WCAG 2.2 AA compliance verification
