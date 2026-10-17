# Pattern — LLM Gateway

**Status:** Proposed · **Type:** structural

## Context

Many applications need to call foundation models. Without a chokepoint, each app embeds provider SDKs, hardcodes keys, and skips guardrails — making observability, spend control, and data-loss prevention impossible.

## Forces

- Multiple providers with different APIs and pricing
- Security requires centralized egress control and audit
- Finance requires per-project cost attribution
- Applications want simple, stable interfaces

## Solution

Route **all** model traffic through a single AI gateway that provides:

1. **Authentication & authorization** — workload identity; per-app permissions per model
2. **Guardrails** — input/output filtering (injection, PII, topic policy) applied uniformly
3. **Routing & failover** — model selection, canary versions, contingency-provider failover
4. **Cost attribution** — every request tagged with project/workload identity
5. **Observability** — traces, token metrics, latency, sampled quality logs

Applications integrate with the gateway's stable API; swapping providers becomes a gateway configuration change, not a code change.

## Consequences

- ✅ Central policy enforcement and spend visibility with zero app-level effort
- ✅ Provider portability at the boundary
- ⚠️ Gateway becomes critical infrastructure — needs its own SLOs and capacity planning
- ⚠️ Lowest-common-denominator risk if the gateway API is too restrictive

## Known uses

- Maps to the gateway component in the [inference reference architecture](../reference-architectures/inference/README.md)
- Pattern 1 in [integration patterns](../standards/integration-patterns.md)
