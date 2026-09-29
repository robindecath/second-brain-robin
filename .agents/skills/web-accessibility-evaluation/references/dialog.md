# Dialog & Modal Accessibility with VpModal

**Purpose**: Complete guide to implementing accessible dialogs and modals using Vitamin Play's VpModal component, including focus trap management and keyboard handling.

---

## VpModal Component

`VpModal` provides built-in accessibility features:

- **Focus trap** - Keeps Tab navigation within modal
- **Focus restoration** - Returns focus to trigger element on close
- **Escape key handling** - Closes modal with Esc key
- **ARIA attributes** - Proper `role="dialog"`, `aria-modal="true"`
- **Backdrop click** - Optional close on outside click

---

## Basic Modal Pattern

```tsx
import {
  VpModal,
  VpModalDialog,
  VpModalHeader,
  VpModalBody,
  VpModalFooter,
  VpModalCloseButton,
  VpButton,
} from "@vtmn-play/react";
import { useState } from "react";

function BasicModal() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <VpButton onClick={() => setIsOpen(true)}>Open modal</VpButton>

      <VpModal open={isOpen} onClose={() => setIsOpen(false)}>
        <VpModalDialog aria-labelledby="modal-title">
          <VpModalHeader>
            <h2 id="modal-title">Modal Title</h2>
            <VpModalCloseButton aria-label="Close dialog" />
          </VpModalHeader>

          <VpModalBody>
            <p>Modal content goes here.</p>
          </VpModalBody>

          <VpModalFooter>
            <VpButton variant="primary" onClick={() => setIsOpen(false)}>
              Confirm
            </VpButton>
            <VpButton variant="secondary" onClick={() => setIsOpen(false)}>
              Cancel
            </VpButton>
          </VpModalFooter>
        </VpModalDialog>
      </VpModal>
    </>
  );
}
```

---

## Essential ARIA Attributes

### aria-labelledby

Links dialog to its title:

```tsx
<VpModalDialog aria-labelledby="dialog-title">
  <VpModalHeader>
    <h2 id="dialog-title">Confirm deletion</h2>
  </VpModalHeader>
</VpModalDialog>
```

### aria-describedby

Links dialog to description:

```tsx
<VpModalDialog aria-labelledby="dialog-title" aria-describedby="dialog-desc">
  <VpModalHeader>
    <h2 id="dialog-title">Delete account</h2>
  </VpModalHeader>
  <VpModalBody>
    <p id="dialog-desc">
      This action cannot be undone. All your data will be permanently deleted.
    </p>
  </VpModalBody>
</VpModalDialog>
```

### aria-modal

Indicates modal behavior (VpModal adds automatically):

```tsx
// VpModal automatically adds aria-modal="true"
<div role="dialog" aria-modal="true">
  {/* Dialog content */}
</div>
```

---

## Focus Management

### Initial Focus

VpModal focuses first focusable element by default. Override if needed:

```tsx
import { useRef, useEffect } from "react";

function ModalWithCustomFocus() {
  const [isOpen, setIsOpen] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (isOpen) {
      // Focus specific element when modal opens
      inputRef.current?.focus();
    }
  }, [isOpen]);

  return (
    <VpModal open={isOpen} onClose={() => setIsOpen(false)}>
      <VpModalDialog aria-labelledby="title">
        <VpModalHeader>
          <h2 id="title">Enter your name</h2>
        </VpModalHeader>
        <VpModalBody>
          <VpFormControl>
            <VpFormLabel>Name</VpFormLabel>
            <VpInput ref={inputRef} type="text" name="name" />
          </VpFormControl>
        </VpModalBody>
      </VpModalDialog>
    </VpModal>
  );
}
```

### Focus Trap

VpModal automatically traps focus within the dialog:

- **Tab** cycles through focusable elements
- **Shift+Tab** cycles backward
- Focus wraps from last to first element

### Focus Restoration

```tsx
import { useRef } from "react";

function ModalWithFocusRestore() {
  const [isOpen, setIsOpen] = useState(false);
  const triggerRef = useRef<HTMLButtonElement>(null);

  const handleClose = () => {
    setIsOpen(false);
    // VpModal automatically restores focus to trigger
    // But you can force it if needed:
    setTimeout(() => {
      triggerRef.current?.focus();
    }, 0);
  };

  return (
    <>
      <VpButton ref={triggerRef} onClick={() => setIsOpen(true)}>
        Open modal
      </VpButton>

      <VpModal open={isOpen} onClose={handleClose}>
        {/* Modal content */}
      </VpModal>
    </>
  );
}
```

---

## Keyboard Interactions

### Essential Keys

| Key             | Action                         |
| --------------- | ------------------------------ |
| **Escape**      | Close dialog                   |
| **Tab**         | Move to next focusable element |
| **Shift + Tab** | Move to previous element       |
| **Enter**       | Activate button                |

### Handling Escape Key

```tsx
// VpModal handles Escape automatically
<VpModal open={isOpen} onClose={() => setIsOpen(false)}>
  {/* Pressing Escape calls onClose */}
</VpModal>

// Prevent Escape from closing (when confirmation needed)
<VpModal
  open={isOpen}
  onClose={(reason) => {
    if (reason === "backdropClick" && hasUnsavedChanges) {
      // Prevent close on backdrop click if unsaved changes
      return;
    }
    setIsOpen(false);
  }}
  closeOnEscape={false} // If VpModal supports this prop
>
  {/* Modal content */}
</VpModal>
```

---

## Modal Types

### Confirmation Dialog

```tsx
function ConfirmationDialog() {
  const [isOpen, setIsOpen] = useState(false);

  const handleDelete = () => {
    // Perform deletion
    console.log("Deleted");
    setIsOpen(false);
  };

  return (
    <>
      <VpButton onClick={() => setIsOpen(true)}>Delete item</VpButton>

      <VpModal open={isOpen} onClose={() => setIsOpen(false)}>
        <VpModalDialog
          aria-labelledby="confirm-title"
          aria-describedby="confirm-desc"
        >
          <VpModalHeader>
            <h2 id="confirm-title">Confirm deletion</h2>
            <VpModalCloseButton aria-label="Cancel and close" />
          </VpModalHeader>

          <VpModalBody>
            <p id="confirm-desc">
              Are you sure you want to delete this item? This action cannot be
              undone.
            </p>
          </VpModalBody>

          <VpModalFooter>
            <VpButton variant="destructive" onClick={handleDelete}>
              Delete
            </VpButton>
            <VpButton variant="secondary" onClick={() => setIsOpen(false)}>
              Cancel
            </VpButton>
          </VpModalFooter>
        </VpModalDialog>
      </VpModal>
    </>
  );
}
```

### Form Dialog

```tsx
function FormDialog() {
  const [isOpen, setIsOpen] = useState(false);
  const [formData, setFormData] = useState({ name: "", email: "" });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Submit form
    console.log(formData);
    setIsOpen(false);
  };

  return (
    <>
      <VpButton onClick={() => setIsOpen(true)}>Add contact</VpButton>

      <VpModal open={isOpen} onClose={() => setIsOpen(false)}>
        <VpModalDialog aria-labelledby="form-title">
          <form onSubmit={handleSubmit}>
            <VpModalHeader>
              <h2 id="form-title">Add new contact</h2>
              <VpModalCloseButton aria-label="Close dialog" />
            </VpModalHeader>

            <VpModalBody>
              <VpFormControl isRequired>
                <VpFormLabel>Name</VpFormLabel>
                <VpInput
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={(e) =>
                    setFormData({ ...formData, name: e.target.value })
                  }
                />
              </VpFormControl>

              <VpFormControl isRequired>
                <VpFormLabel>Email</VpFormLabel>
                <VpInput
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={(e) =>
                    setFormData({ ...formData, email: e.target.value })
                  }
                />
              </VpFormControl>
            </VpModalBody>

            <VpModalFooter>
              <VpButton type="submit" variant="primary">
                Add contact
              </VpButton>
              <VpButton
                type="button"
                variant="secondary"
                onClick={() => setIsOpen(false)}
              >
                Cancel
              </VpButton>
            </VpModalFooter>
          </form>
        </VpModalDialog>
      </VpModal>
    </>
  );
}
```

### Alert Dialog

```tsx
function AlertDialog() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <VpButton onClick={() => setIsOpen(true)}>Show alert</VpButton>

      <VpModal open={isOpen} onClose={() => setIsOpen(false)}>
        <VpModalDialog
          role="alertdialog"
          aria-labelledby="alert-title"
          aria-describedby="alert-desc"
        >
          <VpModalHeader>
            <h2 id="alert-title">Error</h2>
          </VpModalHeader>

          <VpModalBody>
            <p id="alert-desc">
              An error occurred while processing your request. Please try again.
            </p>
          </VpModalBody>

          <VpModalFooter>
            <VpButton variant="primary" onClick={() => setIsOpen(false)}>
              OK
            </VpButton>
          </VpModalFooter>
        </VpModalDialog>
      </VpModal>
    </>
  );
}
```

---

## Backdrop and Overlay

### Background Scroll Prevention

VpModal prevents background scrolling automatically:

```tsx
// VpModal adds overflow: hidden to body when open
<VpModal open={isOpen}>{/* Background scrolling is disabled */}</VpModal>
```

### Backdrop Click Behavior

```tsx
// Close on backdrop click (default)
<VpModal open={isOpen} onClose={() => setIsOpen(false)}>
  {/* Clicking outside closes modal */}
</VpModal>

// Prevent close on backdrop click
<VpModal
  open={isOpen}
  onClose={(e, reason) => {
    if (reason === "backdropClick") return; // Ignore backdrop clicks
    setIsOpen(false);
  }}
>
  {/* Must use close button to dismiss */}
</VpModal>
```

---

## Nested Modals

Avoid nested modals when possible. If necessary:

```tsx
function NestedModalExample() {
  const [isFirstOpen, setIsFirstOpen] = useState(false);
  const [isSecondOpen, setIsSecondOpen] = useState(false);

  return (
    <>
      <VpButton onClick={() => setIsFirstOpen(true)}>Open first modal</VpButton>

      <VpModal open={isFirstOpen} onClose={() => setIsFirstOpen(false)}>
        <VpModalDialog aria-labelledby="first-title">
          <VpModalHeader>
            <h2 id="first-title">First Modal</h2>
          </VpModalHeader>
          <VpModalBody>
            <VpButton onClick={() => setIsSecondOpen(true)}>
              Open second modal
            </VpButton>
          </VpModalBody>
        </VpModalDialog>
      </VpModal>

      <VpModal open={isSecondOpen} onClose={() => setIsSecondOpen(false)}>
        <VpModalDialog aria-labelledby="second-title">
          <VpModalHeader>
            <h2 id="second-title">Second Modal</h2>
          </VpModalHeader>
          <VpModalBody>
            <p>Nested modal content</p>
          </VpModalBody>
        </VpModalDialog>
      </VpModal>
    </>
  );
}
```

**Warning**: Nested modals are complex. Consider alternative UX patterns.

---

## Testing Checklist

### Keyboard Testing

- [ ] Modal opens when trigger activated
- [ ] Focus moves to modal when opened
- [ ] Tab cycles through focusable elements
- [ ] Shift+Tab cycles backward
- [ ] Focus wraps from last to first element
- [ ] Escape key closes modal
- [ ] Focus returns to trigger on close

### Screen Reader Testing

- [ ] Dialog role announced
- [ ] Title announced on open
- [ ] Description announced (if present)
- [ ] Close button has accessible name
- [ ] Modal state (open/closed) communicated

### Visual Testing

- [ ] Focus indicators visible
- [ ] Background content inert (not interactive)
- [ ] Modal centered and responsive
- [ ] Scrollable content if needed

---

## Common Issues

### ❌ Missing Close Button Label

```tsx
// WRONG - No accessible name
<VpModalCloseButton />

// CORRECT - aria-label provides name
<VpModalCloseButton aria-label="Close dialog" />
```

### ❌ No Heading

```tsx
// WRONG - No title
<VpModalDialog>
  <VpModalBody>Content</VpModalBody>
</VpModalDialog>

// CORRECT - Always include heading
<VpModalDialog aria-labelledby="title">
  <VpModalHeader>
    <h2 id="title">Modal Title</h2>
  </VpModalHeader>
  <VpModalBody>Content</VpModalBody>
</VpModalDialog>
```

### ❌ Focus Not Restored

```tsx
// WRONG - Focus lost after close
<VpButton onClick={() => setIsOpen(false)}>Close</VpButton>;

// CORRECT - VpModal handles focus restoration automatically
// Or manually manage focus if needed:
const handleClose = () => {
  setIsOpen(false);
  setTimeout(() => triggerRef.current?.focus(), 0);
};
```

---

## Quick Reference

| Feature           | Implementation                                  |
| ----------------- | ----------------------------------------------- |
| **Basic modal**   | `<VpModal open={isOpen} onClose={handleClose}>` |
| **Title**         | `<h2 id="...">` + `aria-labelledby`             |
| **Description**   | `<p id="...">` + `aria-describedby`             |
| **Close button**  | `<VpModalCloseButton aria-label="...">`         |
| **Focus trap**    | Automatic with VpModal                          |
| **Escape key**    | Automatic with VpModal                          |
| **Focus restore** | Automatic with VpModal                          |
| **Confirmation**  | Two buttons: confirm + cancel                   |
| **Alert**         | `role="alertdialog"` + single OK button         |

---

## Resources

- **ARIA Dialog Pattern**: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- **WCAG 2.4.3 Focus Order**: https://www.w3.org/WAI/WCAG22/Understanding/focus-order
- **Modal Best Practices**: Focus trap, Escape key, focus restoration
