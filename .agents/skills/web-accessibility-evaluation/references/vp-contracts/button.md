# button — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpButton } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpButton accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpButton/ACCESSIBILITY.md).

### Ensure an accessible name

By default, the accessible name (used for screenreaders) is computed from any text content inside the button element. However, it can also be provided with `aria-labelledby` or `aria-label`. Note that [the accessible name should always be containing the text that is presented visually](https://www.w3.org/TR/WCAG22/#label-in-name).

### Connect descriptions

If the component has an associated descriptive text, connect it using the `aria-describedby` attribute set to the ID of the element containing the description.

### Loading screenreader text

When the button is on loading state (`loading` prop set to `true`), it has `aria-busy` set to `true`. As `aria-live` is set to `polite`, users of accessibility tools will be alerted when the state of the button changes. It is expected from users to also set a specific non-visible text through the `loadingScreenReaderText` prop of the component if they are using the button in its loading state. This text will be visible in the DOM but corresponding CSS styles will hide it in the UI. This is because our loader is CSS-dependent. If the users' CSS styles are disabled, they will see this alternative instead. If no text is provided, the default text will be "Loading".

### Focusable and disabled

VpButton can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
