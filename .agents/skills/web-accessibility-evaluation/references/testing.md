# Accessibility Testing with Vitamin Play

**Purpose**: Complete testing methodology for Vitamin Play accessibility, including automated tools, manual testing, and screen reader testing.

---

## Testing Strategy

### Three-Layer Approach

1. **Automated Testing** (catches ~30% of issues)
   - axe DevTools, Lighthouse, WAVE
2. **Manual Testing** (catches ~50% of issues)
   - Keyboard navigation, focus management
3. **Screen Reader Testing** (catches remaining ~20%)
   - VoiceOver (Mac), NVDA (Windows), JAWS (Windows)

**All three layers are required for complete accessibility.**

---

## Automated Testing

### axe DevTools (Recommended)

**Installation**: Browser extension for Chrome/Edge/Firefox

**Usage**:

1. Open DevTools (F12)
2. Navigate to "axe DevTools" tab
3. Click "Scan ALL of my page"
4. Review violations by severity
5. Fix issues and re-scan

**Common Violations**:

- Missing alt text
- Insufficient color contrast
- Missing form labels
- Improper ARIA usage
- Focus order issues

```tsx
// Fix example: Missing alt text
// ❌ Before
<img src="product.jpg" />

// ✅ After
<img src="product.jpg" alt="Mountain bike with 21 gears" />
```

### Lighthouse

**Built into Chrome DevTools**

**Usage**:

1. Open DevTools (F12)
2. Click "Lighthouse" tab
3. Select "Accessibility"
4. Click "Generate report"
5. Review accessibility score and issues

**Scoring**:

- 90-100: Good
- 50-89: Needs improvement
- 0-49: Poor

---

## Manual Keyboard Testing

### Basic Navigation

**Test with keyboard only** (unplug mouse!):

1. **Tab key** - Navigate to next focusable element
   - [ ] All interactive elements receive focus
   - [ ] Focus order is logical (top to bottom, left to right)
   - [ ] Focus indicator is visible

2. **Shift + Tab** - Navigate backward
   - [ ] Focus moves in reverse order

3. **Enter key** - Activate links and buttons
   - [ ] VpButton activates on Enter
   - [ ] Links navigate on Enter
   - [ ] Form submit works

4. **Space key** - Activate buttons and checkboxes
   - [ ] VpButton activates on Space
   - [ ] VpCheckbox toggles on Space

5. **Escape key** - Close dialogs and menus
   - [ ] VpModal closes on Escape
   - [ ] Menus/dropdowns close on Escape

6. **Arrow keys** - Navigate within components
   - [ ] Tabs navigate with arrows
   - [ ] Menus navigate with arrows
   - [ ] Radio buttons navigate with arrows

### Skip Links

1. Load page
2. Press Tab (first focus)
3. Skip link should appear
4. Press Enter
5. Focus moves to main content

```tsx
// Skip link implementation
<a href="#main-content" className="skip-link">
  Skip to main content
</a>

<main id="main-content" tabIndex={-1}>
  {/* Content */}
</main>
```

### Focus Management

Test these scenarios:

**Opening Modals**:

- [ ] Focus moves into modal
- [ ] Focus trapped within modal
- [ ] Tab cycles through modal elements
- [ ] Escape closes modal
- [ ] Focus returns to trigger button

**Deleting Items**:

- [ ] Focus moves to next item
- [ ] If last item, focus moves to previous
- [ ] If no items left, focus moves to container

**Form Submission**:

- [ ] Focus moves to success message
- [ ] Or focus moves to first error

---

## Screen Reader Testing

### VoiceOver (macOS)

**Enable**: System Preferences → Accessibility → VoiceOver

**Basic Commands**:

- `Cmd + F5` - Toggle VoiceOver on/off
- `Control + Option + A` - Start reading
- `Control + Option + →` - Next item
- `Control + Option + ←` - Previous item
- `Control + Option + Space` - Activate item
- `Control + Option + U` - Rotor (landmarks, headings, links)

**Test Checklist**:

- [ ] Page title announced
- [ ] Headings announced with level
- [ ] Links announced with destination
- [ ] Buttons announced with role
- [ ] Form labels announced
- [ ] Error messages announced
- [ ] Loading states announced
- [ ] Modal role announced

### NVDA (Windows - Free)

**Download**: <https://www.nvaccess.org/download/>

**Basic Commands**:

- `Ctrl + Alt + N` - Start NVDA
- `Insert` - NVDA key
- `NVDA + Down Arrow` - Start reading
- `NVDA + F7` - Elements list
- `NVDA + Q` - Quit NVDA

### JAWS (Windows - Paid)

**Most used** screen reader by professionals.

**Basic Commands**:

- `Insert` - JAWS key
- `JAWS + Down Arrow` - Start reading
- `JAWS + F6` - Headings list
- `JAWS + F7` - Links list

---

## Color Contrast Testing

### Browser DevTools

**Chrome**:

1. Inspect element
2. Click color swatch in Styles panel
3. View contrast ratio
4. See AA/AAA pass/fail indicators

**Firefox**:

1. Inspect element
2. Accessibility panel → Check for contrast

### Online Tools

- **WebAIM Contrast Checker**: <https://webaim.org/resources/contrastchecker/>
  - Enter foreground and background colors
  - View ratios and pass/fail for AA/AAA

- **Color Review**: <https://color.review/>
  - Test color combinations
  - View passing ratios

### Vitamin Play Tokens

```css
/* Always use semantic tokens for guaranteed contrast */
color: var(--vp-semantic-color-content-primary);
background: var(--vp-semantic-color-background-primary);
/* Tokens ensure 4.5:1 minimum for text */
```

---

## Testing Workflow

### 1. Development Phase

```bash
# Run automated tests during development
npm run test:a11y  # If available

# Or use axe-core in tests
import { axe } from 'jest-axe';

test('Component has no accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

### 2. Pre-Commit

- [ ] Run axe DevTools scan
- [ ] Fix critical violations
- [ ] Test keyboard navigation
- [ ] Verify focus indicators

### 3. Pre-Deployment

- [ ] Full Lighthouse audit
- [ ] Complete keyboard test
- [ ] Screen reader spot check
- [ ] Contrast verification

### 4. Post-Deployment

- [ ] axe DevTools scan on live site
- [ ] User testing with assistive technology
- [ ] Gather feedback

---

## Testing Checklist Template

### Page-Level

- [ ] Page title is descriptive
- [ ] Skip link present and functional
- [ ] Heading hierarchy is logical (h1 → h2 → h3)
- [ ] Landmarks present (nav, main, footer)
- [ ] Language attribute set (`<html lang="en">`)

### Interactive Elements

- [ ] All buttons keyboard accessible
- [ ] All links keyboard accessible
- [ ] Focus indicators visible
- [ ] Tab order logical
- [ ] Enter/Space activate elements

### Forms

- [ ] All inputs have labels
- [ ] Required fields marked
- [ ] Error messages linked (aria-describedby)
- [ ] Error messages announced
- [ ] Success messages announced
- [ ] Form can be completed with keyboard only

### Images & Media

- [ ] All images have alt text
- [ ] Decorative images have empty alt
- [ ] Icon-only buttons have aria-label
- [ ] Videos have captions (if applicable)

### Color & Contrast

- [ ] Text meets 4.5:1 contrast (or 3:1 for large text)
- [ ] UI components meet 3:1 contrast
- [ ] Focus indicators meet 3:1 contrast
- [ ] Information not conveyed by color alone

### Modals & Dialogs

- [ ] Dialog role present
- [ ] Title announced
- [ ] Focus moves into modal
- [ ] Focus trapped
- [ ] Escape closes modal
- [ ] Focus restored on close

---

## Common Issues & Fixes

### Issue: Contrast Failure

```css
/* ❌ Problem */
color: #999;
background: #fff;
/* 2.8:1 - FAIL */

/* ✅ Solution */
color: var(--vp-semantic-color-content-primary);
background: var(--vp-semantic-color-background-primary);
/* Guaranteed 4.5:1+ */
```

### Issue: Missing Alt Text

```tsx
// ❌ Problem
<img src="product.jpg" />

// ✅ Solution
<img src="product.jpg" alt="Mountain bike with 21 gears" />
```

### Issue: Unlabeled Input

```tsx
// ❌ Problem
<input type="email" placeholder="Email" />

// ✅ Solution
<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
</VpFormControl>
```

### Issue: No Focus Indicator

```css
/* ❌ Problem */
*:focus {
  outline: none;
}

/* ✅ Solution */
*:focus-visible {
  outline: 2px solid var(--vp-semantic-color-border-focus);
  outline-offset: 2px;
}
```

---

## Resources

### Tools

- **axe DevTools**: <https://www.deque.com/axe/devtools/>
- **Lighthouse**: Built into Chrome DevTools
- **WAVE**: <https://wave.webaim.org/>
- **NVDA**: <https://www.nvaccess.org/>
- **WebAIM Contrast Checker**: <https://webaim.org/resources/contrastchecker/>

### Documentation

- **WCAG 2.2**: <https://www.w3.org/WAI/WCAG22/quickref/>
- **ARIA Authoring Practices**: <https://www.w3.org/WAI/ARIA/apg/>
- **MDN Accessibility**: <https://developer.mozilla.org/en-US/docs/Web/Accessibility>

### Vitamin Play

- **Component Documentation**: Check project docs for accessibility features
- **Design Tokens**: Use semantic tokens for guaranteed contrast
