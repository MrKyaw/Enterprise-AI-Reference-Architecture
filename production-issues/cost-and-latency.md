# Production Issues — Cost & Latency (`C-`)

Failures of economics and responsiveness. These rarely cause an outage, so they go unnoticed until the invoice or the user's patience runs out.

## Index

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| C-01 | Monthly spend 5–20× forecast | Unbounded context, verbose outputs, retries, or long agent runs | Budget shock; project cancellation | Context minimization; output caps; loop/step ceilings; budget alarms |
| C-02 | One workload consumes most of the budget | No per-workload attribution | Cannot prioritize or optimize | Gateway tagging + attribution dashboards |
| C-03 | Cost per request crept up gradually | Prompt/context bloat; larger model by default; more retrieved chunks | Silent margin erosion | Unit-economics monitoring; periodic prompt/context review |
| C-04 | Retry storm doubles spend during provider incidents | Aggressive retries without budget or jitter | Cost spike exactly when value is lowest | Retry budgets; jitter; circuit breakers |
| C-05 | Cache never hits (or hits too much with stale data) | Cache keyed incorrectly; semantic threshold wrong; no invalidation | Wasted spend or wrong answers | Key design; threshold calibration; invalidation on model/prompt change |
| C-06 | p99 latency exceeds SLA under peak | Autoscaling on CPU instead of queue depth; cold starts; unbounded retrieval | Abandoned sessions; SLA breach | Queue-depth scaling; warm pools; retrieval bounds |
| C-07 | Latency spikes unexplained | Serial stage chain; one slow dependency in the middle | Inconsistent UX | Stage-decomposed tracing to find the bottleneck |
| C-08 | Cost spikes with no traffic change | Anomalous client behavior or injection loop driving requests | Unnoticed burn | Spend anomaly detection; rate limits; kill switch |
| C-09 | Embedding/re-index job cost surprises | Full re-embedding triggered by a small change | Large one-time cost | Incremental re-embedding; change-scoped migrations |
| C-10 | Cost optimization degraded quality | Trimming context/model without evaluation | Quality regression hidden by cost win | Quality gates on optimization changes |
| C-11 | Reserved/committed spend wasted | Commitment based on projection, not measured baseline | Paid-for unused capacity | Commit against measured usage; review cadence |
| C-12 | Long-tail requests dominate cost | A few pathological inputs (huge documents, wide queries) | Budget unpredictability | Input size limits; per-request token caps; tiered handling |

---

## C-01 — Monthly spend 5–20× forecast

**Symptom:** Finance reports spend vastly above the business case. Engineering cannot immediately explain which workload caused it.

**Root cause:** Compound of unbounded factors — context assembled at the window limit, outputs uncapped, agent loops without ceilings, retries without budgets, and no per-workload attribution to reveal the culprit.

**Impact:** High. AI budgets are often small relative to the forecast shock, so an incident like this can pause the entire program and damage credibility for future initiatives.

**Fix:** Add attribution first (you cannot fix what you cannot see); then apply ceilings: maximum context tokens, maximum output tokens, step/time/cost budgets per request and per run; enable budget alarms.

**Prevention:** [Cost & FinOps patterns](../design-patterns/cost-finops.md), per-request tagging at the [gateway](../design-patterns/llm-gateway.md), unit economics as a design input in the [inference RA](../reference-architectures/inference/README.md), and budget thresholds with **defined behaviors** ([FinOps lifecycle](../lifecycles/finops-cost-lifecycle.md)).

**Future work:** Automatic cost regression detection in CI (cost is a testable metric); predictive spend forecasting per workload; cost-aware routing that optimizes quality per dollar automatically.

---

## C-04 — Retry storm doubles spend during provider incidents

**Symptom:** A provider has a partial degradation; spend spikes sharply for an hour even though useful output dropped.

**Root cause:** Retries configured per-request with no global budget or jitter, so a degraded provider receives a multiplication of load just as its capacity is lowest. Every retry costs tokens.

**Impact:** Medium–High. Cost increases precisely when value decreases; can also turn a partial degradation into a full outage (thundering herd).

**Fix:** Enable exponential backoff with jitter, cap retry counts, add circuit breakers with half-open probing, and a global retry budget.

**Prevention:** [Reliability patterns](../design-patterns/reliability-resilience.md), provider failover configuration, and cost anomaly alerting that fires on retry amplification.

**Future work:** Adaptive retry budgets that account for provider health signals; brownout-aware routing that shifts load away from degraded providers before retries escalate.

---

## C-06 — p99 latency exceeds SLA under peak

**Symptom:** Median latency looks fine; p99 is several seconds and grows under load. Users abandon sessions.

**Root cause:** Autoscaling keyed on CPU (which stays low for I/O-bound AI calls), cold starts for models/containers, and unbounded retrieval or reranking that grows with corpus size.

**Impact:** High for interactive systems. p99 is what users remember, and abandonment shows up as an adoption failure rather than a latency incident.

**Fix:** Scale on queue depth and latency; add warm capacity; bound retrieval (top-k caps, reranker timeouts) and stream responses to improve perceived latency.

**Prevention:** [Distributed scaling patterns](../design-patterns/distributed-scaling.md), stage-decomposed latency budgets in the [NFRs](../docs/non-functional-requirements.md), and load testing at 2× peak as a release gate.

**Future work:** Predictive warm pools based on traffic patterns; adaptive retrieval depth under load; latency-aware request routing that degrades gracefully to preserve p99.

---

## C-10 — Cost optimization degraded quality

**Symptom:** Spend drops as intended, and within days user complaints rise. The optimization was shipped without an evaluation.

**Root cause:** Cost work (smaller model, trimmed context, fewer retrieved chunks, aggressive caching) was treated as an infrastructure change rather than a behavior change, so it bypassed evaluation gates.

**Impact:** Medium–High. Directly erodes the value the system existed to deliver, and undermines confidence in cost governance ("optimization broke it").

**Fix:** Roll back the optimization to the last evaluated configuration; re-run the evaluation suite; reintroduce changes incrementally with measurement.

**Prevention:** Treat any change affecting model, prompt, context, or retrieval as **behavioral**: evaluation gates apply ([EDD](../approaches/driven-development-approaches.md)). Track the cost-quality frontier explicitly ([cost patterns](../design-patterns/cost-finops.md)).

**Future work:** Automated cost-quality regression testing in CI; per-change frontier reporting; optimization recommendations that include predicted quality impact.
