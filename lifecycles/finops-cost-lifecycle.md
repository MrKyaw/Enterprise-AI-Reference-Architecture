# FinOps & Cost Lifecycle

**Status:** Proposed · **Owner:** Finance / platform · **Last reviewed:** 2026-10-17

How AI cost is forecast, attributed, optimized, and governed. AI introduces **usage-variable, provider-metered, per-token** economics unlike traditional infrastructure — this lifecycle makes that cost visible and controllable.

## Phases

### 1. Forecast
- Unit model: cost per request / per document / per agent run / per user per month
- Inputs: expected volume, token profile (input/output ratio), retrieval and embedding costs, retraining frequency, provider pricing tiers
- Scenario ranges (low/expected/peak), not a single number
- **Artifact:** cost model with assumptions

### 2. Budget
- Budget per workload/project, with owner and alert thresholds (50/80/100%)
- Tiered behavior defined at 100%: throttle, queue, degrade, or block ([reliability ladder](../design-patterns/reliability-resilience.md))
- **Artifact:** budget + alerting configuration

### 3. Attribute
- Every model call tagged with workload/project/tenant identity at the [gateway](../design-patterns/llm-gateway.md)
- Cost split by component: model, embeddings, vector store, retrieval compute, data egress, fine-tuning
- Showback/chargeback reports per owner
- **Artifact:** attribution dashboard

### 4. Optimize
| Lever | Mechanism | Trade-off |
|---|---|---|
| Prompt/context size | Trim context, summarize, compress | Detail loss |
| Caching | Semantic + exact + prompt caching | Staleness, correctness |
| Model cascade | Cheap model first, escalate | Routing complexity, quality risk |
| Batching | Offline/async generation | Latency |
| Embedding reuse | Cache embeddings for unchanged content | Invalidation on model change |
| Output length control | Constrain responses | Usability |
| Index/pruning | Smaller indexes, fewer retries | Recall |
| Retraining frequency | Drift-triggered instead of scheduled | Freshness |

**Rule:** optimization that isn't measured on quality is a quality regression in disguise.

### 5. Govern
- Cost dashboards reviewed on a cadence alongside quality/SLO review
- Anomaly detection for spend spikes (runaway agents, injection loops, retry storms)
- Provider price changes and contract renewals feed the forecast
- Cost per outcome published for business cases ([value framework](../docs/business-case-and-value.md))

### 6. Retire
- Decommission unused endpoints/indexes/agents; revoke credentials; stop reserved capacity; delete stored data with ongoing cost

## Regular review cadence

| Cadence | Question |
|---|---|
| Daily (automated) | Any anomalous spend? |
| Weekly | Which workloads trend over budget? |
| Monthly | Unit economics vs forecast; optimization opportunities |
| Quarterly | Provider/contract strategy; reserved-capacity utilization |
| Annually | Full cost-model assumptions revalidated |

## Anti-patterns

- No per-workload attribution (untaggable spend is unmanageable spend)
- Cost optimization without quality guardrails
- Budget alerts with no defined action at threshold
- Ignoring embedding/retrieval/storage costs (model fees are usually the visible part)
- Runaway-agent cost discovered by finance rather than monitoring
