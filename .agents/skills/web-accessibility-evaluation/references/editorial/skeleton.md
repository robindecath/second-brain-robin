# Vitamin Play accessibility guidance — skeleton (web)

Source: vitamin-play-documentation/src/content/components-accessibility/skeleton.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Skeleton component provides these built-in accessibility features out-of-the-box.

          - **Hidden from accessibility tree:** Component is automatically removed from the accessibility tree with `aria-hidden="true"`
          - **Visual loading indicator:** Provides visual feedback during content loading
          - **Design tokens:** Sufficient contrast and appropriate sizing for users with low vision

## What you need to do

        **Design / Content**
        - **Loading duration:** Use skeletons only for loading times longer than 200ms
        - **Shape matching:** Ensure skeleton shapes match the final content layout
        - **Simplified shapes:** Keep skeleton shapes simple and representative
        - **Complete layouts:** Show full layout skeletons, not partial content
        - **Clear transitions:** Ensure smooth transition from skeleton to actual content

          **Development**
          - **Loading state container:** Wrap skeleton in a container with `aria-busy="true"` or place inside an `aria-live="polite"` region
          - **Loading announcement:** Ensure screen readers announce loading state changes
          - **Content replacement:** Replace skeleton with actual content when data is ready
          - **Testing:** Verify that screen readers announce loading states and content availability

## Accessibility attributes

        The Skeleton component is automatically removed from the accessibility tree using `aria-hidden="true"`, ensuring screen readers skip over the placeholder content.

        The component must be wrapped in a loading state container:
        - Use `aria-busy="true"` on the container to indicate loading
        - Or place within an `aria-live="polite"` region to announce state changes
        - This ensures screen readers inform users that content is being loaded

        When content is ready, the skeleton is replaced with actual content and `aria-busy` is removed.

## Accessible label

        ```tsx
        {/* Best practice: aria-busy with polite live region */}

        {/* Alternative: aria-busy alone */}

          {isLoading ?  : }

        {/* With loading message */}

        ```

      **How to provide loading state context:**

        The Skeleton component itself has no accessible label because it's hidden from the accessibility tree. Instead:

        - Wrap in a container with `aria-busy="true"` to indicate loading
        - Use `aria-live="polite"` to announce state changes
        - Optionally add `aria-label` to the container for context
        - Screen readers will announce when content transitions from loading to ready

## Design system guarantees

    ### ARIA and accessibility attributes

    | **RGAA criterion** | **Requirement** | **React Wrapper** | **Svelte Wrapper** | **Vue Wrapper** |
    | ------------------ | --------------- | :---------------: | :----------------: | :---------------: |
    |.  | The component has to be removed from the accessibility tree with a `aria-hidden` attribute. | ✅ | ✅ | ✅ |
    | [7.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.5) | The component should be encapsulated in a loading state by adding the `aria-busy` attribute or putting it inside an `aria-live` region. | 👥 | 👥 | 👥 |

  Using Decathlon Vitamin's design tokens guarantees several essential requirements for accessibility like sufficient contrast between the skeleton and its background for users with low vision or color vision deficiencies, and ensuring that skeleton shapes are of appropriate size to represent the content being loaded.

## Screen readers restitution

      | Environment | React | Svelte |
      |-------------|:-----:|:------:|
      | Firefox + NVDA |  |  |
      | IE + JAWS |  |  |
      | Safari + VoiceOver |  |  |
      | Android + TalkBack |  |  |
      | iOS + VoiceOver |  |  |

Using Vitamin Play design tokens ensures consistent sizing and spacing for skeleton components across all platforms, providing a uniform loading experience.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Expected implementation details

    - The Skeleton component must be wrapped in a loading state container with `aria-busy="true"` or placed inside an `aria-live="polite"` region
    - Screen readers should announce when loading starts and when content becomes available
    - The skeleton itself is hidden from the accessibility tree and not announced
    - When data is ready, replace the skeleton with actual content and remove `aria-busy`
    - Use skeletons only for loading times longer than 200ms to avoid unnecessary announcements

## Testing and compliance

    - The component is tested through [Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core) for WCAG Level A & AA compliance
    - Meets [RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/) (French accessibility) standards
    - Loading states must follow ARIA live region patterns

## Additional resources

    - [ARIA live regions](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA19)
