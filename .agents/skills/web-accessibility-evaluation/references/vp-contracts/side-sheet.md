# side-sheet — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpSideSheet } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpDrawer accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpDialog/VpDrawer/ACCESSIBILITY.md).

### Contain dialog controls

All elements required to operate the dialog are descendants of the element that has role `dialog`.

### Label the dialog

The dialog has either a value set for the `aria-labelledby` property that refers to a visible dialog title, or a label specified by `aria-label`.

### Content Accessibility

Please ensure that content within the Dialog are accessible, including proper use of headings, readable text, and meaningful descriptions for images and interactive elements. If possible, please also maintain a logical reading order for screen readers by structuring the content appropriately.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
