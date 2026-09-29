---
name: incident-investigation
description: >
  Investigate a production incident: correlate recent deploys, error-rate spikes,
  and logs to find the likely root cause of an outage or a service acting flaky.
  Use whenever a user reports something is down, erroring, slow, or behaving
  unexpectedly and wants to know why.
  ⚠️ This is NOT a tool — do NOT call the skill name as a tool. Always use read_skill first.
license: MIT
compatibility: opencode
metadata:
  audience: all
  domain: sre
---

# Incident Investigation (test fixture)

Minimal fixture skill used only by the `knowledge-graph-query-trigger-benchmark.yml`
benchmark to simulate a plausible competing skill for "something is broken" style
prompts. Not a real, functional skill.
