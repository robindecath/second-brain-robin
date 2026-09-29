# Design-Phase Security Evidence Checklist

Use this checklist to ensure threat-modeling outputs are usable by downstream work and release reviewers.

## Evidence sources

Same priority order as the workflow inputs (see [threat-modeling-workflow.md](threat-modeling-workflow.md)). Ask humans only when mandatory data is still missing.

## Evidence mapping summary

- Threat-modeling evidence (design phase): project context + threat model activity + traceability
- Risk-assessment evidence (design phase): risk/criticality/ownership evidence
- Access-right-management evidence (design phase, when access controls apply): identity and authorization evidence for protected resources

## Required threat-modeling evidence

- Link to threat model document
- Security stakeholder participation (name/team/date)
- Scope definition and trust boundaries
- Threat list with risk scoring method
- Mitigation decisions and owners
- Review date and next review trigger

## Required risk-assessment evidence

- Security assessment reference (ID/record link where applicable)
- Application criticality level
- Named security owner / security contact
- Risk acceptance decisions and approvers
- Escalation path for unresolved high risks

## Required access-right-management evidence (when applicable)

- Identity provider and access model decision
- Protected resources list
- Role and permission model summary
- Proof of access control verification tests

## Evidence quality checks

- Evidence is linked, not only described
- Dates and owners are explicit
- Risk exceptions are time-bound
- High-risk items include remediation or approved exception

## Release review questions

- Are all P0 risks resolved or formally accepted?
- Is threat-modeling evidence complete and reviewable?
- Is risk-assessment evidence current for this release?
- Are access controls verified for all protected resources?
