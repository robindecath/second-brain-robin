# Vitamin Play accessibility guidance — footer (web)

Source: vitamin-play-documentation/src/content/components-accessibility/footer.mdx

Do,
  Dont,
  ColumnLayout,
  Column,
  ContentBlock,
  Callout,
  FigmaImage,
  WebOnly,
  AndroidOnly,
  AppleOnly,
} from "@ui";

## Responsibilities at a glance

## What the design system guarantees

        The Footer component provides these built-in accessibility features out-of-the-box.

          - **Landmark role**: Automatically uses `` element which provides implicit `contentinfo` landmark role for screen readers
          - **Navigation links**: VpFooterNavigation and VpFooterNavigationItem components follow standard link keyboard behavior and accessibility best practices (ARIA attributes, focus management, etc.)
          - **Sub-navigation accordion**: VpFooterSubNavigation uses VpAccordion component with all its accessibility features (keyboard interaction, ARIA attributes)
          - **Design tokens**: Sufficient contrast, appropriate sizing, and consistent spacing through Vitamin Play design tokens

## What you need to do

          **Design / Content**
          - **Multiple footers**: When using multiple `` elements on a page, provide unique accessible names via `aria-label` to differentiate them
          - **Heading structure**: Wrap navigation sections and sub-navigation titles in appropriate heading tags that fit the page's content hierarchy
          - **Content accessibility**: Ensure all footer content is accessible - use clear link text, provide image descriptions, maintain sufficient contrast, and structure content in logical reading order

          **Development**
          - **Unique labels**: Add `aria-label` to differentiate multiple footer landmarks on the same page
          - **Heading levels**: Choose appropriate heading levels for footer sections that continue the page's heading hierarchy
          - **Focus management**: Ensure logical tab order through footer navigation and sub-navigation items
          - **Override caution**: If adding `aria-*` attributes or modifying behavior, validate against this documentation and re-test with keyboard and screen readers

## Accessibility attributes

        The Footer component uses the native `` HTML element, which provides the `contentinfo` landmark role automatically. Screen readers announce this landmark to help users navigate page structure.

        It should contains headings for navigation sections and sub-navigation titles, which should be wrapped in appropriate heading tags (``, ``, etc.) that fit the page's content hierarchy.

        The links are embedded in lists and those lists are embedded in an accordion on mobile view. The accordion uses the VpAccordion component, which provides all necessary ARIA attributes for accessibility.

## Accessible label

        By default, the Footer component uses the implicit `contentinfo` landmark role from the `` element. When you have multiple footer elements on a page, you must differentiate them using the `aria-label` attribute to provide unique accessible names for each landmark.

        **When to provide labels:**

        - **Single footer**: No `aria-label` needed - the implicit `contentinfo` role is sufficient
        - **Multiple footers**: Required - each footer must have a unique `aria-label` to distinguish between them for screen reader users

        Screen readers will announce the label along with the landmark type, helping users understand which footer they're navigating.

        **Example with single footer:**

        ```tsx

                  Terms of use

        ```

        **Example with multiple footers:**

        ```tsx
        {/* Main page footer */}

            {/* ... footer content ... */}

        {/* Article-specific footer */}

          {/* ... article content ... */}

              {/* ... article footer content ... */}

        ```

## Keyboard behaviour

      The Footer component's keyboard interaction depends on its child components:

        **Navigation links** (VpFooterNavigation / VpFooterNavigationItem):
        - Follow standard link keyboard behavior, see [link accessibility documentation](/components/web/link?tab=a11y) for details

        **Sub-navigation accordion** (VpFooterSubNavigation):
        - Inherits all keyboard interactions from VpAccordion component see [accordion accessibility documentation](/components/web/accordion?tab=a11y) for complete keyboard interaction table

        | Key | Action |
        | --- | ------ |
        | `Tab` | Move focus to next interactive element (links, accordion buttons) |
        | `Shift + Tab` | Move focus to previous interactive element |

        The footer itself does not add additional keyboard interactions beyond its interactive child components.

## Design system guarantees

  Below are the accessibility criteria guaranteed by the Footer component. For VpFooterSubNavigation accordion-specific guarantees, refer to the [Accordion accessibility documentation](/components-accessibility/accordion#design-system-guarantees) and for vpNavigation/vpNavigationItem guarantees, refer to the [Link accessibility documentation](/components-accessibility/link#design-system-guarantees).

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | ------------------ | --------------- | :------------------: |
    | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Using Vitamin Play design tokens ensures sufficient contrast between footer content and its background, appropriate sizing for readability, and consistent spacing throughout your application. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When using multiple `` elements on a page, each must have a unique accessible name via `aria-label` to differentiate the landmarks for screen reader users. | 👥 |
    | [12.6](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#12.6) | The component is created to be used as `contentinfo` element on pages. If your page includes several `` elements or elements with the `contentinfo` role, please differentiate them with a different accessible name (`aria-label`, for example). | ✅ |

  **Legend:**

  ✅ = Compliant (component guarantees)

  👥 = User responsibility (documented in previous sections)

  ➖ = Not Applicable

  🚫 = Not Compliant

## Screen readers restitution

  **Tested with:**

  | **Environment**    | **React** | **Svelte** | **Vue** |
  | ------------------ | :-------: | :--------: | :-----: |
  | Firefox + NVDA     |           |            |         |
  | IE + JAWS          |           |            |         |
  | Safari + VoiceOver |    ✅     |            |         |
  | Android + TalkBack |           |            |         |
  | iOS + VoiceOver    |           |            |         |

## Testing and compliance

  The Vitamin Play Footer component is tested with:

  - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
  - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
  - [ARIA Authoring Practices Guide (APG): Contentinfo Landmark Pattern & Examples](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/contentinfo.html)
  - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
