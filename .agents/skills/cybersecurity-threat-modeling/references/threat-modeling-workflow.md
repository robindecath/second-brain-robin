# Threat Modeling Workflow

Detailed method behind the SDLC steps defined in [../SKILL.md](../SKILL.md). Operating mode and per-phase actions live in `SKILL.md`; this file covers the modeling procedure.

## Usage priority

- Primary: greenfield projects (from scratch)
- Secondary: brownfield projects (feature additions, refactors, modernization)

## Inputs (priority order)

1. Product/design artifacts: user stories, requirements documents, business cases, architecture notes
2. Prior security artifacts and outputs
3. Existing project security documents
4. Code/config/CI/IaC (optional enrichment)

For greenfield projects, complete planning/design threat modeling from design artifacts even when no code exists yet.

## Workflow

### 1. Define scope

- Define scope, assumptions, assets, and stakeholders

### 2. Model architecture and trust boundaries

- Build data-flow and trust-boundary view

### 3. Identify threats (STRIDE)

- Enumerate threats per component and boundary crossing

### 4. Assess existing controls

- Record existing controls and weaknesses

### 5. Score risk

- Score risks with `Likelihood x Impact` and assign priority (see Core rules in [../SKILL.md](../SKILL.md))

### 6. Define mitigations

- Define mitigation, owner, due date, and verification

### 7. Convert to delivery work

- Convert mitigations into ADRs, stories/tasks, tests, or security debt

### 8. Validate and maintain

- Publish release security summary with open risks
- Update threat model after major changes


## Quality checklist

- Every threat references a concrete component or flow
- Every risk has explicit score rationale
- Every mitigation has owner, due date, and status
- Every unresolved risk has acceptance owner and expiry
- Evidence links are present for required project security expectations
