# progress-bar — Vitamin Play accessibility contract (web)

> Source: Vitamin Play component documentation. This is the **consumer-side**
> accessibility contract: what YOU must provide when using this component.
> When this component is used in code, verify every requirement below is met.

```tsx
import { VpProgressBar } from "@vtmn-play/react"
```

## Accessibility

All accessibility features and expected behaviors are described in the [VpProgressBar accessibility implementation details](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpProgressBar/ACCESSIBILITY.md).

### Determine current value

The Progress Bar element should supply a `value`property unless the value is `undefined` or the state is set as `indeterminate`. Property `value` is automatically translated to `aria-valuenow` as determinate, and will be ommitted as indeterminate. The user should update this value when the visual progress indicator is updated.

### Determine value range

The Progress bar element uses `aria-valuemin` and `aria-valuemax` to indicate the minimum and maximum progress indicator values.

- If `aria-valuemin` is missing or not a `number`, it defaults to **0** (zero).
- If `aria-valuemax` is missing or not a `number`, it defaults to **100**.

### Live region and description

If the Progress Bar element is describing the loading progress of a particular region of a page, the user should use `aria-describedby` to point to the status, and set the `aria-busy` attribute to true on the region until it is finished loading.

### Assistive text value

The user can define specific text value which can be read by assistive technologies generally with the `aria-valuetext` attribute. If it is not specified, they will render the value of `aria-valuenow` as a percent of a range between the value of `aria-valuemin` and `aria-valuemax`.

### Overriding accessibility

If you would override some accessibility features (by adding `aria-*` attributes for instance) or modify the component's behavior in such a way that there is a risk of altering the component's accessibility, please ensure that you comply with the accessibility expectations described in the accessibility implementation details.
