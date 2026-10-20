# Production Issues

Real failure modes observed in production AI/ML systems — with symptom, root cause, impact, fix, prevention, and future work. Every entry maps back to a pattern, control, or lifecycle so the fix is structural, not tribal.

## Why this exists

Most AI incidents are **not novel**. They are recurring, well-understood failure modes that teams rediscover one at a time. This library is the memory of the organization: read it before designing, and add to it after every incident.

**Every production incident becomes an entry here** ([operations lifecycle](../lifecycles/operations-incident-lifecycle.md)), and every entry links to the controlling artifact that prevents recurrence.

## Severity guide

| Severity | Definition | Response |
|---|---|---|
| **Critical** | Harm to people/customers, data breach, unauthorized action, regulatory exposure | Immediate containment; incident declared |
| **High** | Silent quality collapse, cost runaway, availability loss on a critical path | Mitigate within the day; root-cause within a week |
| **Medium** | Degraded quality, elevated cost, user-visible inconsistency | Planned fix in the next cycle |
| **Low** | Friction, minor inaccuracy, cosmetic trust erosion | Backlog |

## Cross-cutting causes (the "why" behind 80% of issues)

Across all catalogued issues, five causes recur:

1. **Unmeasured change** — something changed (prompt, model, index, data) without evaluation ([evaluation-driven development](../approaches/driven-development-approaches.md))
2. **Controls in the model instead of around it** — prompt instructions used as security/safety controls ([controls](../security/ai-security-controls.md))
3. **No attribution or visibility** — cost, quality, or permission failures invisible until they hurt ([FinOps](../lifecycles/finops-cost-lifecycle.md))
4. **Silent divergence** — train/serve, definition drift, index staleness, provider version changes ([MLOps](../lifecycles/mlops-lifecycle.md))
5. **Unbounded behavior** — loops, context, retries, autonomy without ceilings ([agent lifecycle](../lifecycles/agent-lifecycle.md))

Fix the cause pattern, not just the instance.

## Category: Quality & Hallucination (`Q-`)

Failures where the system gives a wrong, unsupported, or confidently bad answer.

| ID | Symptom | Root cause | Impact | Fix | Prevention |
|---|---|---|---|---|---|
| **Q-01** | Confident fabrication presented as fact | No grounding requirement; model asked to answer without evidence | Misinformed decisions; trust collapse | Require grounding + abstention; cite evidence | [Grounding instruction](../design-patterns/rag-patterns.md), refusal behavior ([prompt lifecycle](../lifecycles/prompt-lifecycle.md)), faithfulness metrics as hard gate ([evaluation-in-CI](../design-patterns/evaluation-in-ci.md)) |
| **Q-02** | Answer contradicts an authoritative source | Retrieval returned stale/wrong chunk; no verification | Policy/legal errors | Freshness SLO; answer verification pass; source precedence | [Corpus charter](../lifecycles/rag-lifecycle.md) with source precedence, freshness SLOs, source-owner accountability |
| **Q-06** | Inconsistent answers to the same question | Model non-determinism + unstable inputs (context ordering, sampling) | User distrust ("it said otherwise yesterday") | Lower sampling temperature; stable context ordering; caching; log assembled context | [Deterministic configuration defaults for factual workloads](../approaches/driven-development-approaches.md); prompt/context versioning |
| **Q-06** | Judge says "good" but humans disagree | Uncalibrated LLM-as-judge; judge version not pinned | False confidence in quality dashboards | Calibrate judge vs human labels; pin judge version; blind judge; report agreement | [LLM-as-judge discipline](../lifecycles/evaluation-lifecycle.md): human review sampling, judge upgrades treated as evaluation-system changes |
| **Q-12** | Quality varies by time of day / load | Provider throttling or model-version routing under load | Inconsistent experience; SLA breaches | Capacity planning; consistent routing; degradation ladder | [Capacity planning with headroom](../design-patterns/distributed-scaling.md); provider failover config |

## Category: Retrieval & Data (`R-`)

Failures in ingestion, indexing, retrieval, permissions, and data quality. **Rule:** when answer quality drops, investigate retrieval first.

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| **R-01** | Relevant document exists but is never retrieved | Chunking destroyed context, embedding mismatch, or query/document vocabulary gap | Wrong or missing answers | Re-chunk; hybrid search (dense + sparse); query rewriting; rerank |
| **R-03** | Unauthorized content appears in an answer | ACLs enforced after retrieval or not at all | **Critical** data leak, compliance breach | Retrieval-time ACL filtering + negative tests (prove denial) |
| **R-05** | Deleted source still answerable | Deletion not propagated to index/cache | **Privacy/compliance violation** | Deletion propagation pipeline + verification; treat embeddings/caches as derived personal data |
| **R-08** | Tables/figures mangled or empty in answers | Naive text extraction destroyed structure | Misread numbers | Per-type parsers; table-aware chunking; end-to-end validation |
| **R-13** | Train/serve skew produces worse production results | Feature logic duplicated between training and serving | **Silent quality loss** that monitoring misses | Single transformation definition (feature store or shared library); distribution comparison between training and serving features as monitor |

## Category: Cost & Latency (`C-`)

Failures of economics and responsiveness. These rarely cause an outage, so they go unnoticed until the invoice or the user's patience runs out.

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| **C-01** | Monthly spend 5–20× forecast | Unbounded context, verbose outputs, retries, or long agent runs | Budget shock; project cancellation | Context minimization; output caps; loop/step ceilings; budget alarms; per-workload attribution |
| **C-04** | Retry storm doubles spend during provider incidents | Aggressive retries without budget or jitter | Cost spike exactly when value is lowest | Exponential backoff with jitter; cap retry counts; circuit breakers; global retry budget |
| **C-06** | p99 latency exceeds SLA under peak | Autoscaling on CPU instead of queue depth; cold starts; unbounded retrieval | Abandoned sessions; SLA breach | Queue-depth scaling; warm capacity; bound retrieval (top-k caps, reranker timeouts); stage-decomposed latency budgets |
| **C-10** | Cost optimization degraded quality | Optimization shipped without evaluation | Quality regression hidden by cost win | Treat any change affecting model/prompt/context/regression as behavioral: evaluation gates apply ([EDD](../approaches/driven-development-approaches.md)); track cost-quality frontier |

## Category: Security & Injection (`S-`)

Security failures specific to AI systems. **The core insight:** the model processes attacker-influenced input by design, so controls must live outside it.

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| **S-01** | Agent/assistant follows instructions hidden in retrieved content | Indirect prompt injection; content treated as instructions | **Critical**: unauthorized actions, data exfiltration | Instruction/data separation; authority from system; sandbox ([control AI-11]); input screening; egress allowlist |
| **S-04** | Data exfiltration via generated links | Model-induced exfiltration to attacker-controlled endpoints | **Critical**: data theft | Egress allowlist + DLP on model egress; render-time link scrutiny; no auto-fetch, no external image rendering |
| **S-06** | Cross-tenant data leakage in memory/index | Shared caches/indexes/memory without tenant scoping | **Critical** multi-tenant breach | Tenant-scoped stores/caches; per-tenant quotas; isolation tests; every key/query filter must include tenant dimension |
| **S-08** | Safety filter failed open during dependency outage | Guardrail calls failed; default "proceed" | Unfiltered content reaches users | **Fail-closed** principle ([security patterns](../design-patterns/security-patterns.md)); explicit degradation ladder; chaos drills that kill the guardrail dependency |

## Category: Agents & Tools (`A-`)

Failures specific to systems that take actions. These carry the highest blast radius.

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| **A-02** | Agent performs an action nobody approved | Autonomy level higher than intended; approval gate bypassable | **Critical**: unauthorized change | Enforce approval outside the model; verify gate; declare authorization boundary; red-team specifically attempts to bypass the gate |
| **A-04** | Agent reports success without doing the work | Fabricated tool results; swallowed errors | Silent failure; downstream chaos | Verify outcomes by querying target system after action; treat tool responses as evidence, not truth; fix error-swallowing retry wrapper |
| **A-05** | Partial failure leaves inconsistent state | No compensation/rollback; non-idempotent steps | Broken records; manual cleanup | Saga/compensation pattern; idempotency keys for writes ([reliability patterns](../design-patterns/reliability-resilience.md)); dry-run/staged commit |
| **A-13** | Trajectory unreconstructable during incident | Missing step-level logging/correlation | Cannot diagnose or prove behavior; audit/exposure risk | **Immutable trajectory logging** with correlation IDs end-to-end ([control AI-7]); redaction at logging boundary; operations lifecycle requirements for postmortems |

## Category: Platform, Operations & Lifecycle (`O-`)

Failures in MLOps, drift management, scaling, incident response, vendor dependence, and governance.

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| **O-01** | Silently decaying quality | No drift monitoring; no delayed-ground-truth measurement | High: value erodes without triggering event | Quality SLOs alongside availability ([NFRs](../docs/non-functional-requirements.md)); drift + delayed-ground-truth monitoring ([MLOps](../lifecycles/mlops-lifecycle.md)); retraining triggers wired to those signals |
| **O-03** | Provider silently changed the model | Unpinned version; no change-detection mechanism | High: behavior shift at scale | Pin versions; scheduled evaluation runs that detect behavioral drift; provider deprecation watch ([technology lifecycle](../lifecycles/technology-lifecycle.md)) |
| **O-07** | Rollback impossible because only code was versioned | Behavioral change lives in prompts, index, model version, config | High: extended outage | Treat every behavior-affecting artifact as a versioned deployable ([GenAI lifecycle](../lifecycles/genai-llmops-lifecycle.md)); maintain rollback target for each; test rollback as part of release readiness |
| **O-10** | "What model made this decision?" unanswerable | No model inventory, no per-decision provenance, no approval records | **High to Critical** regulatory exposure | Model inventory and approval records ([model risk lifecycle](../lifecycles/model-risk-lifecycle.md)); decision lineage ([MLOps patterns](../design-patterns/mlops-deployment.md)); immutable audit logging (control AI-7) |
| **O-12** | Platform becomes a bottleneck for delivery | Central review of everything; no review tiers, no golden path | High: slow delivery, shadow AI, inconsistent controls | Review tiers with published checklists ([architecture review process](../docs/architecture-review-process.md)); ship [blueprints](../blueprints/README.md) so compliant path is fast path; move routine approvals to engineering leads; measure delegation (review requests trending down, exception counts trending down) |

## How to use this library

1. **Before designing** — scan the relevant category for known failure modes and their prevention controls
2. **During design** — ensure each gap identified is addressed by an existing control or an new ADR
3. **After an incident** — add a new entry with all fields; link it from the category table; if the issue generalizes, update the controlling artifact in the same PR
4. **Contributing** — after any incident, add an entry with all fields; open a PR. If the issue generalizes to a control or pattern, update that artifact in the same PR

## Contributing an issue

After any incident, add an entry with all five fields (symptom, root cause, impact, fix, prevention) and link it from the appropriate category. If the issue generalizes to a control or pattern, update that artifact in the same PR ([red-team loop](../security/red-team-integration.md)).

---
*This library is a living document. New failure modes are added continuously; old entries are never removed, only superseded by more specific guidance.*
*Last updated: 2026-10-19*