# Vitamin Play accessibility guidance — toggle (web)

Source: vitamin-play-documentation/src/content/components-accessibility/toggle.mdx

## Responsibilities at a glance

## What the design system guarantees

The Toggle component provides these built-in accessibility features out-of-the-box.

- **Semantic role:** The component uses `role="switch"` with a native input element.
- **State management:** The toggle's checked/unchecked state is properly announced through `aria-checked` attribute.
- **Keyboard navigation:** Space key activates the toggle when focused.
- **Required field indicators:** Asterisks are used to mark mandatory fields in both visible name and accessible label.

## What you need to do

**Design / Content**

- **Accessible label:** Provide a clear, descriptive label for the toggle using a visible label element, `aria-labelledby`, or `aria-label`.
- **Label stability:** Ensure the label does not change when the toggle state changes.
- **Group labels:** If presenting multiple toggles as a logical group, provide a visible group label.

**Development**

- **Label implementation:** Ensure the toggle has an accessible label through one of the supported methods (label element, `aria-labelledby`, or `aria-label`).
- **Group structure:** If toggles are in a logical group with a visible label, wrap them in an element with `role="group"` and `aria-labelledby`.
- **Descriptive text:** If additional descriptive text is provided, link it using `aria-describedby`.
- **Testing:** Test with keyboard navigation and screen readers.
- **Override caution:** If you add `aria-*` attributes or change behavior, validate against this doc and re-test with keyboard and screen readers.

## Accessibility attributes

The toggle component requires specific ARIA roles and attributes to ensure proper accessibility:

**Role:** The toggle has `role="switch"` to identify it as a switch control.

**State:** The toggle uses `aria-checked` to indicate its state:
- When checked: `aria-checked="true"`
- When not checked: `aria-checked="false"`

**Label:** The toggle should have an accessible label provided by:
- A visible label element with matching `for` and `id` attributes
- `aria-labelledby` referencing a label element's ID
- `aria-label` directly on the toggle

**Group:** If toggles are presented as a logical group with a visible label, they are wrapped in an element with `role="group"` and `aria-labelledby` pointing to the group label's ID.

**Description:** Additional descriptive text can be linked via `aria-describedby`.

## Accessible label

The toggle should have an accessible label provided by one of the following methods:

```tsx
// 1. Using a visible label referenced by aria-labelledby
Dark mode

// 2. Using aria-label

// 3. Using with FormControl for better structure

  Dark mode

  Enable dark theme

```

**Best practices:**

- Keep labels concise and descriptive
- Do not change the label when the toggle state changes
- Use the state (on/off) to convey the current value, not the label
- Provide context when multiple related toggles exist
- For toggle groups, ensure the group label clearly describes the relationship

## Grouping toggles

```tsx
// Using role="group" and aria-labelledby

  Notification preferences

// Or using fieldset/legend

  Notification preferences

```

## Keyboard behaviour

The toggle is included in the tab order. When focused, users can activate it with the keyboard.

| Key | Action |
| --- | ------ |
| `Tab` | Moves focus to the next focusable element |
| `Shift + Tab` | Moves focus to the previous focusable element |
| `Space` | Changes the state of the toggle (checked/unchecked) |

## Design system guarantees

### Keyboard interaction

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When the switch has focus, pressing the Space key changes the state of the switch | ✅ |

### ARIA and accessibility attributes

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The toggle has `role="switch"` | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The toggle has an accessible label (via label element with `for` attribute, `aria-labelledby`, or `aria-label`) | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When checked, the toggle has `aria-checked` set to `true` | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When not checked, the toggle has `aria-checked` set to `false` | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Mandatory fields are clearly marked with asterisk in both visible name and accessible label | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | For fields with controlled input format, the expected format is visibly indicated before submission | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If toggles are presented as a logical group with a visible label, they are in an element with `role="group"` and `aria-labelledby` | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If additional descriptive text is provided, the toggle has `aria-describedby` set to the description's ID | 👥 |

### Visual accessibility

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Sufficient color contrast between toggle and background (4.5:1 for normal text, 3:1 for large text) | ✅ |
| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | Focus is visible and has sufficient contrast | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast, appropriate sizing, and consistent spacing across all platforms, helping meet accessibility requirements for color contrast, touch targets, and visual clarity.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment** | **React** | **Svelte** | **Vue** |
| --------------- | :-------: | :--------: | :-----: |
| Firefox + NVDA | | | |
| IE + JAWS | | | |
| Safari + VoiceOver | ✅ | ✅ | |
| Android + TalkBack | | ✅ | |
| iOS + VoiceOver | | | |

## Expected implementation details

- The label of the toggle should not change when the state changes.
- The toggle is better used with the `FormControl` component that offers clear and understandable error messages when there are issues with the input's value or format.
- When disabled (`disabled` prop is `true`), the component is neither interactive nor focusable. However, if the disabled state serves as a visual indicator, setting `isFocusable` to `true` allows keyboard focus while maintaining `aria-disabled="true"`.

## Testing and compliance

The Vitamin Play Toggle component is tested with:

- Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
- Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide (APG): Switch Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
