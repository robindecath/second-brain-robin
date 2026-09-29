# Vitamin Play accessibility guidance — search (web)

Source: vitamin-play-documentation/src/content/components-accessibility/search.mdx

## Responsibilities at a glance

## What the design system guarantees

The Search component provides these built-in accessibility features out-of-the-box.

- **Semantic role:** The component uses `role="search"` on the search input.
- **Keyboard navigation:** When the dialog opens, focus moves to an element inside the dialog, and keyboard navigation (Tab, Shift+Tab, Escape) is supported.
- **Focus trap:** Focus is trapped within the modal dialog when opened.
- **Focus restoration:** After the dialog is closed, focus is returned to the element that triggered it.

## What you need to do

**Design / Content**

- **Accessible label:** Provide a clear, descriptive label for the search input using `aria-label` or `aria-labelledby`.
- **Dialog label:** When the dialog is open, provide an accessible description using `aria-label` or `aria-labelledby` (defaults to "Search").
- **Cancel button label:** Provide an accessible label for the cancel button via `cancelAriaLabel` (defaults to "Cancel").
- **Help text:** Provide clear feedback when no results are found, including instructions and examples.

**Development**

- **Input type:** Use the appropriate HTML input type attribute (e.g., `type="text"`).
- **Descriptive text:** If additional descriptive text is provided, link it using `aria-describedby`.
- **Testing:** Test with keyboard navigation and screen readers.
- **Override caution:** If you add `aria-*` attributes or change behavior, validate against this doc and re-test with keyboard and screen readers.

## Accessibility attributes

The search component requires specific ARIA roles and attributes to ensure proper accessibility:

**Role:** The search input has `role="search"` to identify it as a search landmark.

**Dialog attributes:** When the modal dialog opens:
- The container receives appropriate focus management
- Focus is trapped within the modal
- Escape key closes the dialog

**Label:** The search input should have an accessible label provided by `aria-label` or `aria-labelledby`.

**Description:** Additional context can be provided via `aria-describedby` if descriptive text is present.

## Accessible label

By default, there is no `aria-label` on the search input. You should provide a semantic label using either `aria-label` or `aria-labelledby`:

````tsx
// Using aria-label

// Using aria-labelledby
Search products

// Dialog label (when open)

````

**Best practices:**

- Keep labels concise and descriptive
- Avoid redundant words like "search box" or "search field" (the role conveys this)
- Provide context when multiple search fields exist on the same page
- Ensure cancel button labels are clear and actionable

## Keyboard behaviour

The search bar is included in the tab order. The user can type text directly into the search field as soon as it is focused.

**Default search field (closed state):**

| Key | Action |
| --- | ------ |
| `Tab` | Focuses the search input |
| `Enter` | Submits the search |
| `Escape` | Clears the input field |
| `Space` or `Enter` | Activates the clear button ('x') when focused |

- To launch the search, the user presses the `Enter` key
- To clear the contents of the field, the user can press the `Escape` key
- As soon as the user starts typing text, a cancel icon ('x') appears. This icon becomes the next tab stop and provides another way to clear the field, via a click, the `Space` bar or the `Enter` key

**Expanded search field (open state):**

| Key | Action |
| --- | ------ |
| `Tab` | Moves focus to clear button, then close 'x' button, then loops through suggestion list |
| `Shift + Tab` | Moves focus backwards through the elements |
| `Enter` | Selects a suggestion when focused on a result |
| `Escape` | Closes the search bar results display |
| `Down Arrow` | Navigates to the next suggestion in the list |
| `Up Arrow` | Navigates to the previous suggestion in the list |
| `Space` or `Enter` | Activates clear or close 'x' button when focused |

- After the user starts typing, a 'clear' and close 'x' option appear
- Clear is the next tab stop, it allows the user to clear the input in the search bar without completely closing it via a click, the `Space` bar or the `Enter` key
- Close 'x' is the next tab stop after clear, it provides another way (in addition with `Escape` key) to close the search bar results display via click, the `Space` bar or the `Enter` key
- To reach and navigate through the results, the user presses the arrow keys. Tabbing with its keys loops through the list, the user can exit at any time via the `Escape` key or choose a suggestion by pressing `Enter` key

## Outcomes and status

**Provide feedback and help:**

If the user submits the field without any input it will return "No results". In that case we should give instructions on how to do a search with examples. If the user submits something and gets "no results" we should also give help.

## Design system guarantees

### Keyboard interaction

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When a dialog opens, focus moves to an element inside the dialog | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Tab moves focus to the next tabbable element inside the dialog, looping to the first when reaching the last | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Shift+Tab moves focus to the previous tabbable element inside the dialog, looping to the last when reaching the first | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Escape closes the dialog | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | After the dialog is closed, focus is returned to the element that triggered the dialog | ✅ |

### ARIA and accessibility attributes

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Appropriate HTML input types (text, email, password, number, etc.) are used | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The search input has an accessible label (via label element, aria-labelledby, aria-label, or title attribute) | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If a set of inputs is presented as a logical group with a visible label, they are in a group element with aria-labelledby | ➖ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If additional descriptive text is provided, the input has aria-describedby set to the description's ID | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The button has an accessible label (text content, aria-labelledby, or aria-label) | 👥 |

### Visual accessibility

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Sufficient color contrast between text and background (4.5:1 for normal text, 3:1 for large text) | ✅ |
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
| Safari + VoiceOver | ✅ | ✅ | ✅ |
| Android + TalkBack | | | |
| iOS + VoiceOver | | | |

## Expected implementation details

- By default, there is no `aria-label` on the inner input field. A semantic label should be added using `aria-label` or `aria-labelledby`.
- When the dialog is open, an accessible description must be provided using `aria-label` or `aria-labelledby` (defaults to "Search").
- The cancel button requires an accessible label via the `cancelAriaLabel` property (defaults to "Cancel").
- When disabled (`disabled` prop is `true`), the component is neither interactive nor focusable. However, if the disabled state serves as a visual indicator, setting `isFocusable` to `true` allows keyboard focus while maintaining `aria-disabled="true"`.

## Implementation notes

The Search component implements accessibility through a modal dialog pattern. Focus is trapped within the dialog when open, and keyboard navigation follows the WAI-ARIA modal dialog pattern. The component uses appropriate semantic HTML input types and supports customizable ARIA attributes for labels and descriptions.

## Testing and compliance

The Vitamin Play Search component is tested with:

- Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
- Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide (APG): Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources
