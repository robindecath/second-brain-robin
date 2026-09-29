# loader — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpLoader } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpLoader accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpLoader/ACCESSIBILITY.md).

### Provide alternative text

An alternative text should be provided for information that are only conveyed through shape, size, or position. The Loader component accepts children that will be visually hidden but accessible to screen readers.

### Use ARIA live regions

A `role="status"` and `aria-live="polite"` should be provided on the parent element wrapping the loading spinner. The live region must be present in the DOM before the loading indicator has rendered.

### Indicate loading state completion

If some loading content isn't rendered in place of the spinner, the completion of the loading state should still be conveyed to assistive technologies. A non-visible status message such as "loading complete" could be put in the `aria-live` section.

### Use aria-busy attribute

The `aria-busy` state attribute may be used to indicate an element is being modified and that assistive technologies may want to wait until the changes are complete before informing the user about the update.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
