# Vitamin Play accessibility guidance — progress-bar (web)

Source: vitamin-play-documentation/src/content/components-accessibility/progress-bar.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Progress Bar component provides these built-in accessibility features out-of-the-box.

          - **Correct semantics**: Proper `role="progressbar"` with managed ARIA attributes for value, min, and max
          - **State communication**: Automatic handling of determinate vs. indeterminate states
          - **Label association**: Intelligent label handling with `aria-label` for circular/indeterminate variants and `aria-labelledby` for linear determinate variants

## What you need to do

          **Design / Content**
          - **Label text:** Provide clear, descriptive labels that explain what process is being tracked (e.g., "Uploading document", "Processing payment").
          - **Value text:** For custom progress descriptions, ensure `aria-valuetext` values are meaningful and updated appropriately (e.g., "Step 2 of 5" instead of just "40%").

          **Development**
          - **Value updates:** Update the `value` prop as the task progresses to ensure the `aria-valuenow` attribute reflects current progress.
          - **Live regions:** When the progress bar describes loading of a specific page region, use `aria-describedby` to reference the progress bar and set `aria-busy="true"` on the loading region.
          - **Custom text:** Provide `aria-valuetext` when the numeric percentage doesn't adequately describe progress (e.g., multi-step processes, file uploads with time remaining).
          - **Override caution:** If you add custom `aria-*` attributes or change behavior, validate against the accessibility expectations described in this documentation and re-test with screen readers.

## Accessibility attributes

        The Progress Bar element has `role="progressbar"` to communicate its purpose to assistive technologies.

        **Required ARIA attributes:**
        - `aria-valuemin`: Indicates the minimum value (defaults to 0)
        - `aria-valuemax`: Indicates the maximum value (defaults to 100)
        - `aria-valuenow`: Present for determinate progress, indicates current value (omitted for indeterminate state)
        - `aria-label` or `aria-labelledby`: Provides an accessible name
          - Circular and indeterminate variants use `aria-label` directly
          - Linear determinate variant uses `aria-labelledby` referencing the visible label element

        **Optional ARIA attributes:**
        - `aria-valuetext`: Provides human-readable text describing the current value (e.g., "Step 2 of 5", "50 MB of 100 MB")
        - `aria-describedby`: When progress describes a loading region, points to the progress bar from the loading region
        - `aria-busy`: Set to `true` on the region being loaded until loading completes

        **Important:** The component automatically manages these attributes based on the provided props (`value`, `min`, `max`, `label`, `variant`, `indeterminate`).

## Accessible label

            Every Progress Bar must have an accessible label that describes what process or task is being tracked. The labeling approach varies by variant:

            **Linear determinate variant:**
            - Uses visible label text associated via `aria-labelledby`
            - Label element has a unique ID that the progress bar references
            - Ensures visible label and accessible name match

            **Circular and indeterminate variants:**
            - Use `aria-label` directly on the progress bar element
            - Necessary because these variants typically don't have visible labels in the same hierarchical structure

            **Value text customization:**
            - Use the `aria-valuetext` attribute to provide context beyond raw percentages
            - Especially useful for multi-step processes, file transfers, or time-based operations
            - Examples: "Step 3 of 6", "Uploading: 45 MB of 100 MB, 2 minutes remaining"

            ```tsx
            // Linear with visible label (aria-labelledby)

            // Circular with aria-label

            // Indeterminate with aria-label

            // With custom aria-valuetext

            ```

## aria-valuetext for enhanced descriptions

            The `aria-valuetext` attribute provides human-readable text to describe progress when the numeric `aria-valuenow` value alone isn't meaningful. Use it to add context that a percentage can't convey.

            **When aria-valuetext is necessary:**
            - **Multi-step processes**: "Step 2 of 5" instead of "40%"
            - **File transfers**: "45 MB of 100 MB" instead of "45%"
            - **Time estimates**: "2 minutes remaining" with progress percentage
            - **Non-standard scales**: Custom ranges where percentages aren't intuitive

            **Best practices:**
            - Update `aria-valuetext` whenever the progress value changes
            - Keep text concise and focused on what users need to know
            - Don't duplicate the label or aria-valuenow percentage
            - Omit it when the percentage and label are adequately describing progress

            **Reference:** MDN: aria-valuetext

## Design system guarantees

    ### ARIA and accessibility attributes

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Progress Bar has `role="progressbar"` to identify itself as a progress indicator to assistive technologies. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Progress Bar provides `aria-valuemin` (default: 0) and `aria-valuemax` (default: 100) to define the value range. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | For determinate progress, `aria-valuenow` is set to the current value; for indeterminate progress, `aria-valuenow` is omitted. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Linear determinate variants use `aria-labelledby` to reference the visible label element; circular and indeterminate variants use `aria-label` directly. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When provided, `aria-valuetext` offers human-readable progress description; if omitted, screen readers calculate percentage from `aria-valuenow` / `aria-valuemax`. | 👥 / ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When progress describes loading of a page region, developer uses `aria-describedby` on the region to reference the progress bar, and sets `aria-busy="true"` until complete. | 👥 |

    ### Visual accessibility

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: |
    | [3.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.1) | Information about progress is not conveyed solely through color; progress percentage or descriptive text must accompany visual indicators. | 👥 / ✅ |
    | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Label text, when visible, meets minimum contrast requirements (4.5:1 for normal text). | ✅ |
    | [3.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.3) | The progress indicator provides sufficient contrast against its background to be perceivable. | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between the progress indicator and its background, appropriate sizing for readability, and consistent spacing throughout your application.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)
- 👥 / ✅ = Shared responsibility (Design system provides mechanism, developer provides content)

## Screen readers restitution

**Tested with:**

| **Environment**    | **React** | **Svelte** | **Vue** |
| ------------------ | :-------: | :--------: | :-----: |
| Firefox + NVDA     |           |            |         |
| IE + JAWS          |           |            |         |
| Safari + VoiceOver |           |            |         |
| Android + TalkBack |           |            |         |
| iOS + VoiceOver    |           |            |         |
