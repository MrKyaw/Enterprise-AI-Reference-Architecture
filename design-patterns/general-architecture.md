# General Software & Architecture Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Foundation patterns for structuring applications — including the AI components inside them. Applied in [software development lifecycle](../lifecycles/software-development-lifecycle.md) design phases.

## Structural patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Layered architecture** | Separate presentation, application, domain, infrastructure | Straightforward systems, small teams | Layers leak; avoid layer-for-layering's-sake |
| **Hexagonal / ports & adapters** | Keep domain logic independent of frameworks and I/O | Testability matters; external dependencies shift (models, providers) | Requires discipline at adapter boundaries |
| **Clean / onion architecture** | Dependency direction points inward to the domain | Long-lived systems with material business rules | Over-abstraction for simple CRUD |
| **Modular monolith** | Strong module boundaries in one deployable | Early stage, small team, unclear extraction points | Modules erode without enforcement |
| **Microservices** | Independently deployable services per capability | Scaling/delivery autonomy needs are proven | Distributed complexity; don't start here by default |
| **Service mesh / sidecar** | Cross-cutting concerns (mTLS, telemetry) off the app path | Many services with uniform networking needs | Operational overhead; not for a handful of services |
| **Backend-for-frontend (BFF)** | Tailored API per client experience | Multiple client types with divergent needs | Fragmentation of business logic |
| **Serverless** | Event-driven, auto-scaled functions | Spiky workloads, glue, event processing | Cold starts, vendor coupling, local dev difficulty |

## Integration & data-flow patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **API gateway** | Single entry point: auth, rate limits, routing | Multiple consumers/providers | Becomes a bottleneck and a single point of failure |
| **Pub/sub & event-driven** | Producers and consumers decoupled by events | Async workflows, many consumers, AI enrichment pipelines | Event schema governance; ordering guarantees |
| **Outbox pattern** | Atomically persist state + emit event | Reliable event publication from a transaction | Needs a relay/cleanup process |
| **CQRS** | Separate read and write models | Read/write load or shape differ materially | Eventual consistency surprises consumers |
| **Event sourcing** | State as an append-only event log | Audit trail and temporal queries are first-class | Replay cost, versioning of events, learning curve |
| **Saga / process manager** | Distributed transaction via compensating steps | Multi-service workflows (including agent actions) | Compensation logic complexity; needs idempotency |
| **Cache-aside** | Application manages cache population | Read-heavy, tolerable staleness | Invalidation bugs; stale answers in AI paths |
| **Strangler fig** | Incrementally replace a legacy system behind a facade | Modernizing without a rewrite ([detail](../docs/legacy-modernization.md)) | Transitional architecture needs retirement dates |
| **Anti-corruption layer** | Isolate a new domain from legacy models | Integrating with legacy/third-party semantics | Boundary translation must be owned |

## AI-specific structural considerations

- **Model access is an adapter**, not scattered SDK calls — see [llm-gateway](llm-gateway.md)
- **Guardrails and policy live at the boundary**, outside domain logic and outside the model
- **Non-determinism is a first-class concern:** retries must be safe when outputs vary; idempotency keys for any AI-triggered write
- **AI components are rate-limited dependencies** like any external service — apply [resilience patterns](reliability-resilience.md)
- **Cost is a runtime resource:** budget/ceiling behavior belongs in the design, not discovered in finance

## Choosing a structure

```
Team size < ~15 and one domain        → modular monolith
Clear independent scaling/deploy needs → microservices (extract from modular monolith)
Spiky/event workloads                 → serverless or event-driven services
Client experiences diverge            → add a BFF
Legacy system of record involved      → strangler fig + anti-corruption layer
```

## Anti-patterns

- Microservices-first for a small team (distributed monolith)
- Shared database across services (coupling disguised as decoupling)
- Chatty synchronous chains with no resilience
- Abstraction layers that leak provider specifics everywhere anyway
- Event-driven systems with no schema governance
