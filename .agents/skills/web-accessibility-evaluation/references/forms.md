# Accessible Forms with Vitamin Play

**Purpose**: Complete guide to implementing accessible forms using Vitamin Play components, validation patterns, and error handling.

---

## Sommaire

- [VpFormControl Pattern](#vpformcontrol-pattern)
- [Required Fields](#required-fields)
- [Input Types and Autocomplete](#input-types-and-autocomplete)
- [Field Instructions and Help Text](#field-instructions-and-help-text)
- [Error Handling](#error-handling)
- [Checkbox and Radio Groups](#checkbox-and-radio-groups)
- [Select Dropdowns](#select-dropdowns)
- [Textarea](#textarea)
- [Form Submission](#form-submission)
- [Live Validation](#live-validation)
- [Fieldsets and Legends](#fieldsets-and-legends)
- [File Upload](#file-upload)
- [Complete Form Example](#complete-form-example)
- [Best Practices Summary](#best-practices-summary)

---

## VpFormControl Pattern

`VpFormControl` is the foundation of accessible forms in Vitamin Play. It automatically handles:

- Label association via context
- Error message linking (`aria-describedby`)
- Invalid state (`aria-invalid`)
- Required field indication

### Basic Structure

```tsx
import {
  VpFormControl,
  VpFormLabel,
  VpFormHelper,
  VpFormError,
  VpInput,
} from "@vtmn-play/react";

<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
  <VpFormHelper>We'll never share your email</VpFormHelper>
</VpFormControl>;
```

---

## Required Fields

### Marking Required Fields

```tsx
// ✅ Visual and programmatic indication
<VpFormControl isRequired>
  <VpFormLabel>Full name</VpFormLabel>
  <VpInput type="text" name="name" />
</VpFormControl>
// VpFormControl adds aria-required="true" automatically

// ✅ With helper text
<VpFormControl isRequired>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" />
  <VpFormHelper>Required for account creation</VpFormHelper>
</VpFormControl>

// ✅ Required indicator in form header
<form>
  <p>
    <span aria-label="required">*</span> indicates required field
  </p>

  <VpFormControl isRequired>
    <VpFormLabel>Name</VpFormLabel>
    <VpInput type="text" name="name" />
  </VpFormControl>
</form>
```

---

## Input Types and Autocomplete

Search terms: autocomplete attribute, identify input purpose WCAG 1.3.5, email name tel.

### Use Correct Input Types

```tsx
// Text inputs
<VpFormControl>
  <VpFormLabel>Full name</VpFormLabel>
  <VpInput type="text" name="name" autoComplete="name" />
</VpFormControl>

// Email
<VpFormControl>
  <VpFormLabel>Email address</VpFormLabel>
  <VpInput type="email" name="email" autoComplete="email" />
</VpFormControl>

// Phone
<VpFormControl>
  <VpFormLabel>Phone number</VpFormLabel>
  <VpInput type="tel" name="phone" autoComplete="tel" />
</VpFormControl>

// Password
<VpFormControl>
  <VpFormLabel>Password</VpFormLabel>
  <VpInput
    type="password"
    name="password"
    autoComplete="current-password"
  />
</VpFormControl>

<VpFormControl>
  <VpFormLabel>New password</VpFormLabel>
  <VpInput
    type="password"
    name="newPassword"
    autoComplete="new-password"
  />
</VpFormControl>

// Numbers
<VpFormControl>
  <VpFormLabel>Age</VpFormLabel>
  <VpInput type="number" name="age" min="18" max="120" />
</VpFormControl>

// Dates
<VpFormControl>
  <VpFormLabel>Birth date</VpFormLabel>
  <VpInput type="date" name="birthdate" autoComplete="bday" />
</VpFormControl>
```

### Common Autocomplete Values

- `name` - Full name
- `given-name` - First name
- `family-name` - Last name
- `email` - Email address
- `tel` - Phone number
- `street-address` - Full address
- `postal-code` - ZIP/postal code
- `country` - Country name
- `cc-number` - Credit card number
- `bday` - Birthday

---

## Field Instructions and Help Text

### Using VpFormHelper

```tsx
// ✅ Helper text provides instructions
<VpFormControl>
  <VpFormLabel>Username</VpFormLabel>
  <VpInput type="text" name="username" />
  <VpFormHelper>
    3-20 characters, letters and numbers only
  </VpFormHelper>
</VpFormControl>

// ✅ Helper for password requirements
<VpFormControl>
  <VpFormLabel>Password</VpFormLabel>
  <VpInput type="password" name="password" />
  <VpFormHelper>
    <ul>
      <li>At least 8 characters</li>
      <li>One uppercase letter</li>
      <li>One number</li>
    </ul>
  </VpFormHelper>
</VpFormControl>
```

---

## Error Handling

### Showing Validation Errors

```tsx
import { useState } from "react";
import {
  VpFormControl,
  VpFormLabel,
  VpInput,
  VpFormError,
} from "@vtmn-play/react";

function EmailField() {
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  const handleBlur = () => {
    if (!email.includes("@")) {
      setError("Please enter a valid email address");
    } else {
      setError("");
    }
  };

  return (
    <VpFormControl isInvalid={!!error}>
      <VpFormLabel>Email address</VpFormLabel>
      <VpInput
        type="email"
        name="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        onBlur={handleBlur}
      />
      {error && <VpFormError>{error}</VpFormError>}
    </VpFormControl>
    // VpFormControl automatically adds:
    // - aria-invalid="true" to input when isInvalid
    // - aria-describedby linking to error message
  );
}
```

### Error Summary

```tsx
import { useRef, useEffect } from "react";
import { VpButton } from "@vtmn-play/react";

function FormWithErrorSummary() {
  const [errors, setErrors] = useState<Record<string, string>>({});
  const errorSummaryRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Focus error summary when errors appear
    if (Object.keys(errors).length > 0) {
      errorSummaryRef.current?.focus();
    }
  }, [errors]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const formErrors: Record<string, string> = {};
    // Validate fields...

    if (Object.keys(formErrors).length > 0) {
      setErrors(formErrors);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.keys(errors).length > 0 && (
        <div
          ref={errorSummaryRef}
          role="alert"
          aria-labelledby="error-summary-title"
          tabIndex={-1}
        >
          <h2 id="error-summary-title">
            There are {Object.keys(errors).length} errors in this form
          </h2>
          <ul>
            {Object.entries(errors).map(([field, message]) => (
              <li key={field}>
                <a href={`#${field}`}>{message}</a>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Form fields */}

      <VpButton type="submit">Submit</VpButton>
    </form>
  );
}
```

---

## Checkbox and Radio Groups

### VpCheckbox

```tsx
import { VpCheckbox } from "@vtmn-play/react";

// ✅ Single checkbox
<VpCheckbox name="terms" required>
  I accept the terms and conditions
</VpCheckbox>

// ✅ Multiple checkboxes (related choices)
<fieldset>
  <legend>Select your interests</legend>
  <VpCheckbox name="interests" value="cycling">
    Cycling
  </VpCheckbox>
  <VpCheckbox name="interests" value="hiking">
    Hiking
  </VpCheckbox>
  <VpCheckbox name="interests" value="running">
    Running
  </VpCheckbox>
</fieldset>
```

### Radio Groups (when available in Vitamin Play)

```tsx
// Use native HTML with proper structure if VpRadioGroup not available
<fieldset>
  <legend>Shipping method</legend>
  <div>
    <input
      type="radio"
      id="standard"
      name="shipping"
      value="standard"
      defaultChecked
    />
    <label htmlFor="standard">Standard (5-7 days)</label>
  </div>
  <div>
    <input type="radio" id="express" name="shipping" value="express" />
    <label htmlFor="express">Express (2-3 days)</label>
  </div>
</fieldset>
```

---

## Select Dropdowns

```tsx
import { VpFormControl, VpFormLabel, VpSelect } from "@vtmn-play/react";

// ✅ Basic select
<VpFormControl>
  <VpFormLabel>Country</VpFormLabel>
  <VpSelect name="country">
    <option value="">Select a country</option>
    <option value="fr">France</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
  </VpSelect>
</VpFormControl>

// ✅ With error state
<VpFormControl isInvalid={!country}>
  <VpFormLabel>Country</VpFormLabel>
  <VpSelect name="country" value={country} onChange={handleChange}>
    <option value="">Select a country</option>
    <option value="fr">France</option>
  </VpSelect>
  {!country && (
    <VpFormError>Please select your country</VpFormError>
  )}
</VpFormControl>
```

---

## Textarea

```tsx
import { VpFormControl, VpFormLabel, VpTextarea } from "@vtmn-play/react";

<VpFormControl>
  <VpFormLabel>Message</VpFormLabel>
  <VpTextarea name="message" rows={4} placeholder="Enter your message..." />
  <VpFormHelper>Maximum 500 characters</VpFormHelper>
</VpFormControl>;

// With character counter
function MessageField() {
  const [message, setMessage] = useState("");
  const maxLength = 500;

  return (
    <VpFormControl isInvalid={message.length > maxLength}>
      <VpFormLabel>Message</VpFormLabel>
      <VpTextarea
        name="message"
        rows={4}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <VpFormHelper>
        {message.length} / {maxLength} characters
      </VpFormHelper>
      {message.length > maxLength && (
        <VpFormError>Message exceeds maximum length</VpFormError>
      )}
    </VpFormControl>
  );
}
```

---

## Form Submission

### Accessible Submit Flow

```tsx
import { useState } from "react";
import { VpButton } from "@vtmn-play/react";

function ContactForm() {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<
    "idle" | "success" | "error"
  >("idle");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setSubmitStatus("idle");

    try {
      // Submit form data
      await submitForm();
      setSubmitStatus("success");
    } catch (error) {
      setSubmitStatus("error");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Form fields */}

      {/* Status messages */}
      {submitStatus === "success" && (
        <div
          role="status"
          aria-live="polite"
          style={{
            padding: "1rem",
            backgroundColor: "var(--vp-semantic-color-background-positive)",
          }}
        >
          Form submitted successfully!
        </div>
      )}

      {submitStatus === "error" && (
        <div
          role="alert"
          aria-live="assertive"
          style={{
            padding: "1rem",
            backgroundColor: "var(--vp-semantic-color-background-negative)",
          }}
        >
          Error submitting form. Please try again.
        </div>
      )}

      {/* Submit button */}
      <VpButton type="submit" disabled={isSubmitting} aria-busy={isSubmitting}>
        {isSubmitting ? "Submitting..." : "Submit"}
      </VpButton>
    </form>
  );
}
```

---

## Live Validation

### Real-time Validation Pattern

```tsx
import { useState, useEffect } from "react";
import {
  VpFormControl,
  VpFormLabel,
  VpInput,
  VpFormError,
} from "@vtmn-play/react";

function PasswordField() {
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState<string[]>([]);

  useEffect(() => {
    const newErrors: string[] = [];

    if (password.length > 0 && password.length < 8) {
      newErrors.push("Password must be at least 8 characters");
    }
    if (!/[A-Z]/.test(password)) {
      newErrors.push("Password must contain an uppercase letter");
    }
    if (!/[0-9]/.test(password)) {
      newErrors.push("Password must contain a number");
    }

    setErrors(newErrors);
  }, [password]);

  const hasError = password.length > 0 && errors.length > 0;

  return (
    <VpFormControl isInvalid={hasError}>
      <VpFormLabel>Password</VpFormLabel>
      <VpInput
        type="password"
        name="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      {hasError && (
        <div role="alert" aria-live="polite">
          {errors.map((error, index) => (
            <VpFormError key={index}>{error}</VpFormError>
          ))}
        </div>
      )}
    </VpFormControl>
  );
}
```

---

## Fieldsets and Legends

### Grouping Related Fields

```tsx
// ✅ Address form group
<fieldset>
  <legend>Shipping address</legend>

  <VpFormControl>
    <VpFormLabel>Street address</VpFormLabel>
    <VpInput type="text" name="street" autoComplete="street-address" />
  </VpFormControl>

  <VpFormControl>
    <VpFormLabel>City</VpFormLabel>
    <VpInput type="text" name="city" autoComplete="address-level2" />
  </VpFormControl>

  <VpFormControl>
    <VpFormLabel>Postal code</VpFormLabel>
    <VpInput type="text" name="postal" autoComplete="postal-code" />
  </VpFormControl>
</fieldset>

// ✅ Payment information group
<fieldset>
  <legend>Payment information</legend>

  <VpFormControl>
    <VpFormLabel>Card number</VpFormLabel>
    <VpInput type="text" name="cardNumber" autoComplete="cc-number" />
  </VpFormControl>

  <div style={{ display: "flex", gap: "1rem" }}>
    <VpFormControl>
      <VpFormLabel>Expiry date</VpFormLabel>
      <VpInput type="text" name="expiry" autoComplete="cc-exp" />
    </VpFormControl>

    <VpFormControl>
      <VpFormLabel>CVV</VpFormLabel>
      <VpInput type="text" name="cvv" autoComplete="cc-csc" />
    </VpFormControl>
  </div>
</fieldset>
```

---

## File Upload

```tsx
import { VpFormControl, VpFormLabel, VpFormHelper } from "@vtmn-play/react";

<VpFormControl>
  <VpFormLabel htmlFor="avatar">Profile picture</VpFormLabel>
  <input
    id="avatar"
    type="file"
    name="avatar"
    accept="image/png, image/jpeg"
    aria-describedby="avatar-helper"
  />
  <VpFormHelper id="avatar-helper">PNG or JPG, max 2MB</VpFormHelper>
</VpFormControl>;
```

---

## Complete Form Example

```tsx
import { useState } from "react";
import {
  VpButton,
  VpCheckbox,
  VpFormControl,
  VpFormLabel,
  VpFormHelper,
  VpFormError,
  VpInput,
  VpSelect,
  VpTextarea,
} from "@vtmn-play/react";

type FormData = {
  name: string;
  email: string;
  country: string;
  message: string;
  terms: boolean;
};

type FormErrors = Partial<Record<keyof FormData, string>>;

function ContactForm() {
  const [formData, setFormData] = useState<FormData>({
    name: "",
    email: "",
    country: "",
    message: "",
    terms: false,
  });

  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validate = (): boolean => {
    const newErrors: FormErrors = {};

    if (!formData.name) newErrors.name = "Name is required";
    if (!formData.email) newErrors.email = "Email is required";
    else if (!formData.email.includes("@"))
      newErrors.email = "Invalid email address";
    if (!formData.country) newErrors.country = "Country is required";
    if (!formData.message) newErrors.message = "Message is required";
    if (!formData.terms) newErrors.terms = "You must accept the terms";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validate()) return;

    setIsSubmitting(true);

    try {
      // Submit form
      await new Promise((resolve) => setTimeout(resolve, 1000));
      alert("Form submitted!");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <VpFormControl isRequired isInvalid={!!errors.name}>
        <VpFormLabel>Full name</VpFormLabel>
        <VpInput
          type="text"
          name="name"
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        />
        {errors.name && <VpFormError>{errors.name}</VpFormError>}
      </VpFormControl>

      <VpFormControl isRequired isInvalid={!!errors.email}>
        <VpFormLabel>Email address</VpFormLabel>
        <VpInput
          type="email"
          name="email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        />
        {errors.email && <VpFormError>{errors.email}</VpFormError>}
      </VpFormControl>

      <VpFormControl isRequired isInvalid={!!errors.country}>
        <VpFormLabel>Country</VpFormLabel>
        <VpSelect
          name="country"
          value={formData.country}
          onChange={(e) =>
            setFormData({ ...formData, country: e.target.value })
          }
        >
          <option value="">Select a country</option>
          <option value="fr">France</option>
          <option value="us">United States</option>
        </VpSelect>
        {errors.country && <VpFormError>{errors.country}</VpFormError>}
      </VpFormControl>

      <VpFormControl isRequired isInvalid={!!errors.message}>
        <VpFormLabel>Message</VpFormLabel>
        <VpTextarea
          name="message"
          rows={4}
          value={formData.message}
          onChange={(e) =>
            setFormData({ ...formData, message: e.target.value })
          }
        />
        {errors.message && <VpFormError>{errors.message}</VpFormError>}
      </VpFormControl>

      <VpCheckbox
        name="terms"
        checked={formData.terms}
        onChange={(e) => setFormData({ ...formData, terms: e.target.checked })}
      >
        I accept the terms and conditions
      </VpCheckbox>
      {errors.terms && (
        <div
          role="alert"
          style={{ color: "var(--vp-semantic-color-content-negative)" }}
        >
          {errors.terms}
        </div>
      )}

      <VpButton type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Submitting..." : "Submit"}
      </VpButton>
    </form>
  );
}
```

---

## Best Practices Summary

1. **Always use VpFormControl** - Handles label association and ARIA automatically
2. **Mark required fields** - Use `isRequired` prop on VpFormControl
3. **Show errors clearly** - Use `VpFormError` with `isInvalid` state
4. **Provide helpful instructions** - Use `VpFormHelper` for guidance
5. **Use correct input types** - Enables better mobile keyboards and autofill
6. **Add autocomplete** - Helps users fill forms faster
7. **Group related fields** - Use `<fieldset>` and `<legend>`
8. **Focus management** - Focus error summary on submit failure
9. **Announce changes** - Use `role="status"` or `role="alert"` for dynamic messages
10. **Test with keyboard** - Ensure all fields are Tab-accessible
