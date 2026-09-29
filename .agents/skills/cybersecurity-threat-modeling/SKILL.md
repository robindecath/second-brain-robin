---
name: cybersecurity-threat-modeling
description: Build and maintain a threat model from architecture through testing. Produce actionable security requirements, prioritized risks, and design-phase evidence for downstream work. Use when designing a new system or major capability, when data flow / identity / access / external integrations change, or for sensitive or business-critical capabilities.
license: Apache-2.0
compatibility: No external dependencies required.
metadata:
  owner: Decathlon Security SIG
  category: Cybersecurity
  version: "1.1.0"
  last-updated: "2026-07-24"
---

# Cybersecurity Threat Modeling

Use this skill to run threat modeling during the SDLC and turn security concerns into concrete, trackable delivery work. It is process-agnostic: it works with any SDLC or agent workflow and does not assume a specific methodology or tool.

## What this skill does

- Identifies threats from design artifacts
- Prioritizes risks with a simple score model
- Produces security requirements for implementation and testing
- Maintains the evidence needed for release discussions

## When to use

- Architecture/design of a new system or major capability built from scratch (primary use case)
- Major changes in data flow, identity, access, or external integrations
- Sensitive or business-critical capabilities

## Operating mode

- Agent-to-agent by default
- Human input only when data is missing or formal approval is required
- Non-blocking by default: risks must be visible, owned, and tracked

## Inputs

- Design artifacts first: user stories, requirements documents, business cases, architecture notes
- Code is optional enrichment, not the primary entry point
- Use [references/threat-modeling-workflow.md](references/threat-modeling-workflow.md) as the detailed source of truth for input priority

## SDLC flow

### Planning

- Define scope, assets, assumptions, and reviewers

### Architecture / Design

- Model trust boundaries and data flows
- Identify threats (STRIDE), score risks, choose mitigations
- Publish security requirements and risks for downstream work

### Implementation

- Convert mitigations into stories/tasks and acceptance criteria
- Track unresolved risks with owner and due date

### Testing / Release

- Map each mitigation to test evidence
- Produce a release security summary with open risks

## Mandatory outputs

Generate these artifacts in your project's security documentation directory (for example `docs/security/`):

- `threat-model.md` - system context, trust boundaries, threats, scores, mitigations
- `security-requirements.md` - actionable controls with acceptance criteria
- `security-verification-checklist.md` - tests, evidence, owner, and status

Optional:

- `abuse-cases.md` - attacker stories and misuse paths
- `security-debt.md` - deferred mitigations with risk rationale

## Core rules

- Use STRIDE per trust boundary
- Risk formula: `Risk = Likelihood x Impact`
- Priority bands: `P0` (16-25), `P1` (9-15), `P2` (4-8), `P3` (1-3)
- Every risk must have owner, due date, and verification method
- Every mitigation must become delivery work (ADR, story/task, or test)

## Prompt examples

### Example 1: New system in the design phase

```text
Perform threat modeling for this new architecture:
- Public API Gateway -> Orders service -> Payment provider -> Data warehouse
- Assets: customer profile, order details, payment token
- Constraints: FedID for employees, OAuth2 for service-to-service

Generate:
1) docs/security/threat-model.md
2) docs/security/security-requirements.md
3) docs/security/security-verification-checklist.md
```

### Example 2: Brownfield review before release

```text
Analyze this existing project and build/update its threat model.
Focus on authentication flows, secrets handling, and external dependencies.
Map findings to the project's security evidence requirements.
Create a security-debt backlog with priorities P0-P3.
```

## What to avoid

- Generic threat lists with no architecture context
- Risks without owner/due date/verification
- Security findings that are not converted into delivery work

## References

- [references/threat-modeling-workflow.md](references/threat-modeling-workflow.md) - End-to-end workflow, checklists, and artifact format
- [references/threat-catalog-stride.md](references/threat-catalog-stride.md) - Reusable threat catalog by component type
- [references/design-phase-security-evidence-checklist.md](references/design-phase-security-evidence-checklist.md) - Generic design-phase security evidence checklist
- [references/templates/threat-model-template.md](references/templates/threat-model-template.md) - Copy-ready threat model template
