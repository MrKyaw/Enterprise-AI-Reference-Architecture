# API Lifecycle

**Status:** Proposed · **Owner:** Platform / API · **Last reviewed:** 2026-10-17

How APIs are designed, published, versioned, and retired — including the AI gateway API and agent tool contracts.

## Phases

| Phase | Activities | Artifacts | Exit gate |
|---|---|---|---|
| **1. Design** | Domain + use case analysis; contract-first spec; naming, pagination, error semantics; auth model | OpenAPI/typed contract; ADR | Design review for new public/consumer-facing APIs |
| **2. Review** | Consumer feedback; consistency with published style; security review of auth/rate limits/data exposure | Reviewer sign-off | Style + security conformance |
| **3. Implement** | Code + contract tests; mock server for consumers | Implementation; contract test suite | Contract tests green on both sides |
| **4. Publish** | Documentation, examples, SDKs, changelog; discoverability (catalog) | Published docs; version tag | Consumer can self-serve integration |
| **5. Observe** | Usage, error rates, latency, quota consumption per consumer | Dashboards; per-consumer metrics | — |
| **6. Evolve** | Backward-compatible additions preferred; breaking change ⇒ new major version | Deprecation notice; migration guide | Consumers migrated |
| **7. Deprecate** | Sunset date announced, usage monitored, blocking new adoption | Deprecation record | Zero production consumers |
| **8. Retire** | Remove endpoint; delete keys/quotas; archive docs | Decommission record | — |

## Compatibility rules

| Change | Compatibility | Action |
|---|---|---|
| Add optional field | Backward compatible | Publish, note in changelog |
| Add required request field | Breaking | New major version |
| Remove/rename field | Breaking | New major version |
| Change semantics (same shape) | Breaking in practice | New major version + migration notes |
| Tighten validation | Breaking | New major version |
| Relax validation | Compatible | Publish |
| Change rate limits downward | Effectively breaking | Announce + grace period |

## AI-specific considerations

- **Agent tools are APIs.** Every tool has a typed contract, versioning, and an owner ([agent protocols](../standards/agent-protocols.md))
- **Model-facing interfaces** (structured output schemas, function-calling definitions) are contracts too — schema changes can break agents silently
- **Streaming semantics** (SSE/chunked) need explicit contracts for partial results, cancellation, and errors mid-stream
- **Non-determinism disclosure:** consumers must know which endpoints are probabilistic so they design accordingly
- **Cost as a contract element:** token/price limits per consumer are part of the API agreement
- **Gateway-mediated access:** the AI gateway is the public surface; provider SDKs are not

## Anti-patterns

- Contracts written after implementation
- Silent semantic changes under an unchanged version
- One giant unversioned "internal" API with many consumers
- No usage telemetry, so deprecation is guesswork
- Agent tools without owners or versioning
