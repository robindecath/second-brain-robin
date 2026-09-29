# Threat Catalog (STRIDE)

Use this catalog to accelerate threat discovery. Always adapt entries to the actual architecture and context.

## API Gateway / Edge

- Spoofing: forged identity token, weak client authentication
- Tampering: request parameter manipulation, header injection
- Repudiation: insufficient audit trail for privileged actions
- Information disclosure: verbose errors exposing internal details
- Denial of service: unauthenticated endpoint flooding
- Elevation of privilege: bypass of role checks in route policy

## Web or Mobile Frontend

- Spoofing: session fixation, stolen tokens
- Tampering: client-side state tampering
- Repudiation: missing user action audit on sensitive flows
- Information disclosure: secrets in frontend bundle or logs
- Denial of service: expensive rendering/event abuse
- Elevation of privilege: hidden-route access without server checks

## Backend Service

- Spoofing: weak service-to-service authentication
- Tampering: unvalidated payloads, command injection
- Repudiation: missing immutable logs for business actions
- Information disclosure: PII in logs or metrics
- Denial of service: uncontrolled retries and resource exhaustion
- Elevation of privilege: over-permissive internal endpoints

## Messaging / Event Bus

- Spoofing: unauthorized producer identity
- Tampering: message alteration in transit or at rest
- Repudiation: no producer/consumer traceability
- Information disclosure: sensitive payloads without encryption
- Denial of service: queue flooding and consumer starvation
- Elevation of privilege: unauthorized topic subscription

## Data Stores

- Spoofing: shared credentials across services
- Tampering: unauthorized write paths
- Repudiation: no audit for schema/admin changes
- Information disclosure: over-broad read permissions
- Denial of service: lock contention and expensive queries
- Elevation of privilege: admin access through app runtime identity

## Third-Party Integration

- Spoofing: fake provider endpoint or webhook sender
- Tampering: unsigned or unverifiable callback payloads
- Repudiation: insufficient traceability for external events
- Information disclosure: overexposed data in partner payloads
- Denial of service: dependency outage cascading failures
- Elevation of privilege: over-scoped API keys

## Secrets and Key Management

- Spoofing: stolen machine identity for secret retrieval
- Tampering: secret rotation process bypass
- Repudiation: no access logs for secret reads
- Information disclosure: plaintext secrets in CI variables
- Denial of service: key vault dependency outage
- Elevation of privilege: broad secret path permissions

## Prompting checklist for each identified threat

- What asset is impacted?
- Which trust boundary is crossed?
- What attack path is realistic?
- Which controls already exist?
- What residual risk remains?
- Which test/evidence proves mitigation effectiveness?
