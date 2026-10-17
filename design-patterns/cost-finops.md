# Cost & FinOps Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Implementation patterns that make AI spend visible and controllable. Complements the [FinOps lifecycle](../lifecycles/finops-cost-lifecycle.md) and the cost sections of the [inference](../reference-architectures/inference/README.md) and [GenAI](genai-prompting.md) pattern sets.

## Visibility patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Request tagging with workload identity** | Attribute every call to an owner | Untagged = unmanageable |
| **Cost per outcome metric** | Cost per resolved ticket, per document, per task | Requires outcome instrumentation |
| **Stage-decomposed cost** | Model vs. retrieval vs. embedding vs. egress | Retrieval/storage often exceed expectations |
| **Showback/chargeback dashboards** | Make owners see their spend | Without action paths it becomes theater |
| **Budget alarms with defined actions** | 50/80/100% thresholds each with a behavior | Alarms with no action are noise |
| **Anomaly detection on spend** | Catch runaway agents/retry storms early | Tune to avoid alert fatigue |
| **Token accounting per request** | Input/output tokens, cached vs. uncached | Needed to model optimizations |

## Reduction patterns

| Pattern | Intent | Quality trade-off |
|---|---|---|
| **Semantic + exact caching** | Serve repeated/similar requests cheaply | Staleness; must respect ACLs |
| **Provider-side prompt caching** | Reuse stable prefixes | Prefix stability constraint |
| **Model cascade/routing** | Cheap model for easy cases | Routing errors hurt quality |
| **Output length control** | Bound completion cost | Truncation must be handled |
| **Context minimization** | Send only necessary context | Missing signal degrades answers |
| **Context compression/summarization** | Fit long histories | Detail loss |
| **Embedding reuse** | Avoid re-embedding unchanged content | Invalidate on model change |
| **Retrieval tightening (fewer, better chunks)** | Less context = lower cost + often better quality | Over-tightening increases misses |
| **Batch/async offload** | Cheaper bulk processing | Not interactive |
| **Right-sized models** | Match capability to task | Requires per-task evaluation |
| **Quantization/distillation** | Lower serving cost | Quality regression on edge cases |
| **Retry budget caps** | Prevent cost amplification | Fewer successful retries |
| **Loop/step ceilings for agents** | Bound worst-case spend | Premature termination risk |
| **Index pruning & tiering** | Reduce storage and query cost | Recall impact |

## Governance patterns

| Pattern | Intent |
|---|---|
| **Pre-approved unit economics per workload** | Design within a cost envelope, not after |
| **Cost gate in design review** | Cost model required for high-volume systems |
| **Provider price-change watch** | Treat pricing changes as change events |
| **Reserved/committed capacity review** | Match commitments to measured baseline, not projections |
| **Kill switch for cost anomalies** | Automatic throttle/stop on spend spikes |
| **Cost in release gates** | Regress cost like latency when it matters |

## Cost-quality frontier

Optimization is a multi-objective problem. Track the frontier explicitly:

```
            Quality
               ▲
   Expensive   │  ●  large model, full context, best reranking
   & accurate  │
               │      ● cascade + caching + tightened retrieval
               │
   Cheap       │          ● small model, minimal context
   & shallow   │
               └──────────────────────────────────────────────▶ Cost
```

For each workload, pick the acceptable point and **measure quality whenever you move left**. Document the choice in an ADR — cost decisions are architecture decisions.

## Anti-patterns

- Optimizing cost without measuring quality impact
- Cache layers that ignore user permissions
- Cost dashboards with no owner and no action
- Budget alarms nobody defined a behavior for
- Committed spend based on projected, not measured, volume
- Ignoring embedding, storage, and egress costs
- Agent cost discovered by finance rather than monitoring
