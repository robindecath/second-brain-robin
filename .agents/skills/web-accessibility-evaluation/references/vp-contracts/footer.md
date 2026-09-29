# footer — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpFooter } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpFooter accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpFooter/ACCESSIBILITY.md).

### Differentiating multiple footers

If your page includes several `<footer>` elements or elements with the `contentinfo` role, please differentiate them with a different accessible name (using `aria-label`, for example).

### Wrap with heading tags

Each `<VpFooterSubNavigationHeader>` should be wrapped in an HTML Heading tag (`h2`, `h3`, `h4`, etc.) or in element with `role="heading"` that has a value set for `aria-level` that is appropriate for the information architecture of the page.

### Content Accessibility

Please ensure that content within the Sub Navigation List is accessible, including proper use of headings, readable text, and meaningful descriptions for images and interactive elements. If possible, please also maintain a logical reading order for screen readers by structuring the content appropriately.

### Focusable and disabled

VpFooterAccordion can be focusable even when disabled. This can be done by setting the `isFocusable` and `isDisabled` properties to `true`. The component will still be visible for users of screen reader and keyboard navigation. It is recommended to do this when the presence of the component gives important context to a user, such as knowing all the possible options inside a menu. Read [our ADR on disabling interactive components](https://special-adventure-p85wlrj.pages.github.io/docs/react/adrs/008-disabling-for-accessibility) for more information.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
