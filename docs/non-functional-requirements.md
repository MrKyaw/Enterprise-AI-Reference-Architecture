# Non-Functional Requirements (NFRs) for AI Systems

**Status:** Proposed · **Last reviewed:** 2026-10-17

Every AI design review must state how the system meets these NFRs. "Not applicable" is a valid answer — silence is not.

## The NFR set

### Scalability
- Expected and peak load (requests/sec, tokens/sec, concurrent sessions, document volume)
- Scaling strategy per component (gateway, serving endpoints, retrieval, workers)
- Behavior under 10× load: degrade gracefully or fail fast — decide explicitly

### Availability
- Tier-based availability targets aligned with [inference RA SLOs](../reference-architectures/inference/README.md)
- Single points of failure identified; no unbounded dependencies on one provider (multi-provider contingency per [model-provider-standards](../standards/model-provider-standards.md))

### Resiliency
- Failure modes enumerated: provider outage, index corruption, quota exhaustion, poisoned input, dependency timeout
- Timeouts, retries with backoff, circuit breakers, bulkheads
- Graceful degradation path (fallback model or non-AI path) tested, not theoretical
- BCP/DR: RTO/RPO stated for systems whose loss interrupts business operations

### Performance
- Latency budgets decomposed: gateway overhead, retrieval, model time, guardrails — each with a number
- p95/p99 targets, not averages
- Batch vs real-time classification; backpressure design

### Observability
- Golden signals for AI: quality, latency, cost, safety per workload
- Correlation IDs end-to-end (request → agent steps → tool calls → outputs)
- Drift monitoring (input, output, and quality) with alert thresholds
- Dashboards and runbooks exist before go-live

### Security & compliance
- The mandatory control set in [ai-security-controls.md](../security/ai-security-controls.md)
- Data classification, residency, and retention stated per data element
- Identity: workload identity, least privilege, rotation

### Cost
- Unit economics: cost per request / per document / per agent run at expected volume
- Budgets and alerting per project (cost attribution via gateway)
- Cost ceiling behavior: throttle, queue, or degrade — decide explicitly

### Operability
- On-call ownership, runbook, and escalation path
- Model/prompt change process with evaluation gates ([evaluation-in-ci](../design-patterns/evaluation-in-ci.md))
- Deployability: canary/shadow rollout capability

## How to use in review

Section 5 of the [design review checklist](design-review-checklist.md) maps to this document. T0/T1 designs fill a one-page NFR summary; T2/T3 designs require the full treatment with evidence.
