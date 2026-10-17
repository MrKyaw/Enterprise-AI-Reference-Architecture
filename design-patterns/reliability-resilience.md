# Reliability & Resilience Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns that keep AI systems working when dependencies fail, load spikes, and outputs misbehave. AI systems are *more* dependent on external services (model providers, vector stores, data platforms) than most software, and their failures are often silent.

## Failure-handling patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Timeout** | Bound every external call | Always | Timeouts must be shorter than the caller's budget |
| **Retry with exponential backoff + jitter** | Recover from transient faults | Idempotent operations only | Retrying non-idempotent writes duplicates effects |
| **Circuit breaker** | Stop calling a failing dependency | Provider/DB degradation | Needs half-open probing and recovery criteria |
| **Bulkhead** | Isolate resource pools per dependency/tenant | One workload must not starve others | Pool sizing; rejected requests need behavior |
| **Load leveling (queue)** | Absorb bursts | Spiky AI demand | Latency vs. stability trade-off; queue depth alerts |
| **Rate limiting & quotas** | Protect self and dependencies | Multi-tenant, shared providers | Fairness policy; clear 429 semantics |
| **Graceful degradation** | Serve reduced functionality | Any user-facing AI | Degraded mode must be **tested** |
| **Fallback chain** | Primary → secondary model → deterministic path | Model/decision-critical paths | Divergent behavior between fallbacks |
| **Deadline propagation** | Context budgets across calls | Multi-stage pipelines | Every stage must honor the deadline |
| **Hedged requests** | Reduce tail latency | Latency-critical, idempotent reads | Cost multiplication |

## Consistency & correctness patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Idempotency keys** | Safe retries for writes (incl. agent actions) | Key scope and expiry must be defined |
| **At-least-once + dedup** | Reliable processing | Dedup store must be durable |
| **Exactly-once semantics (pragmatic)** | Where supported by the platform | Often "effectively once" — verify |
| **Transactional outbox** | Atomic state + event | Relay process needed |
| **Compensating transactions (saga)** | Undo partial multi-step work | Business meaning of "undo" |
| **Read-repair / reconciliation jobs** | Fix drift between copies | Must be monitored, not silent |
| **Eventual consistency contracts** | Consumers tolerate propagation delay | Documented, measured staleness bounds |

## Health & recovery patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Health checks (liveness/readiness/startup)** | Correct traffic routing and restarts | Readiness must include dependency checks selectively |
| **Warm-up / pre-warm pools** | Avoid cold-start latency | Cost of idle capacity |
| **Progressive rollout** | Limit blast radius of change | Requires rollback automation |
| **Automatic rollback on SLO breach** | Fast recovery | Quality-based triggers need reliable signals |
| **Chaos/game-day exercises** | Verify failure behavior | Schedule and scope carefully ([ops lifecycle](../lifecycles/operations-incident-lifecycle.md)) |
| **Cell/zone isolation** | Contain failures by partition | Data placement and routing complexity |
| **Static fallback content** | Never show a blank failure to users | Freshness expectations |

## AI-specific resilience concerns

| Concern | Pattern |
|---|---|
| Provider outage | Fallback chain + contingency provider ([model-provider standards](../standards/model-provider-standards.md)) |
| Quality collapse (silent) | Sampled quality SLO with alerting, not just latency/errors |
| Index unavailable | Cached retrieval results; keyword fallback; abstain gracefully |
| Guardrail dependency down | Default to **deny/abstain**, never fail-open for safety filters |
| Cost runaway | Hard budget ceilings + step/loop limits + kill switch |
| Prompt injection at scale | Input filtering + tool authorization (defense in depth) |
| Non-deterministic retries | Idempotency + effect verification |
| Provider-side model change | Pinned versions + change detection + scheduled eval |

## Degradation ladder (define explicitly)

```
Full capability → Cached/older answers → Smaller/cheaper model → Keyword-only retrieval
   → Deterministic non-AI path → Static message + retry guidance
```

Write the ladder per system; test the bottom two rungs at least.

## Anti-patterns

- Retrying without backoff or jitter (thundering herd)
- Circuit breakers that never close again (permanent degradation)
- Safety filters failing open when a dependency is unavailable
- Fallback paths never exercised
- Timeouts longer than the client's timeout
- Health checks that only test "process is alive"
