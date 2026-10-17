# Production Issues — Platform, Operations & Lifecycle (`O-`)

Failures in MLOps, drift management, scaling, incident response, vendor dependence, and governance — the operational layer beneath every AI workload.

## Index

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| O-01 | Model quality decays over months | Data/behavior/concept drift; no monitoring | Silent value loss | Drift + delayed-ground-truth monitoring; retraining triggers |
| O-02 | Retraining ran but made things worse and was promoted | Auto-promotion without evaluation gates | Production regression | Evaluation gates; champion/challenger; rollback |
| O-03 | Provider silently changed the model | Unpinned version; change not detected | Behavior shift at scale | Pin versions; scheduled re-eval; change detection |
| O-04 | Provider deprecation forces emergency migration | No lifecycle watch | Scramble; possible outage | Deprecation watch; pre-evaluated replacement |
| O-05 | Cannot reproduce a past result | No reproducibility manifest; data/version lost | Audit failure; cannot debug | Manifest per run (code/data/deps/seeds/config) |
| O-06 | Prompt/config edited directly in production, then broke | Config not under version control | Untraceable regression | Config-as-code; UI edits disabled in prod |
| O-07 | Rollback impossible because only code was versioned | Index/prompt/data changes not reversible | Extended outage | Version and roll back all changeable artifacts |
| O-08 | Cost/quality incident detected by a user, not monitoring | No quality SLO or sampling | Slow detection; trust damage | Quality SLOs; sampled judging; anomaly alerts |
| O-09 | Evaluation datasets rot and lose signal | No curator; no refresh; overfitting to the set | False confidence | Named curator; cadence; held-out sets |
| O-10 | Compliance can't answer "what model made this decision?" | No model inventory or decision provenance | Regulatory exposure | Model inventory; decision lineage; approval records |
| O-11 | Capacity exhausted during a traffic spike or provider failover | No headroom; single-provider dependence | Outage | Headroom planning; contingency provider; load shedding |
| O-12 | Platform became a bottleneck for delivery | Central review of everything | Slow delivery; shadow bypass | Delegated review tiers; blueprints; self-service |
| O-13 | Blueprints and standards drifted apart | Updated separately | Teams follow stale guidance | Update in the same PR |
| O-14 | Multiple teams built the same capability | No reusable catalog | Duplicated spend and divergence | Platform capability catalog; reuse incentives |
| O-15 | Governance treated as a launch checkbox | No ongoing obligation | Late-discovered harm | Risk-tiered monitoring; revalidation cadence |

---

## O-01 — Silently decaying quality

**Symptom:** No error, no alarm, no incident — but six months later users say the system "used to be good." Metrics that exist show normal latency and cost.

**Root cause:** Drift in three forms (input distribution, model behavior, real-world concept) with no monitoring for any of them, and no delayed-ground-truth measurement. Quality simply isn't an observed signal.

**Impact:** High. Value erodes without a triggering event, so it is discovered only through anecdote or an audit. Rebuilding trust is far harder than fixing the model.

**Fix:** Instrument quality immediately — sampled automated judging plus delayed ground truth where labels arrive; compare current quality against the launch baseline to quantify the decay.

**Prevention:** Quality SLOs alongside availability ([NFRs](../docs/non-functional-requirements.md)); drift and delayed-ground-truth monitoring ([MLOps patterns](../design-patterns/mlops-deployment.md)); retraining triggers wired to those signals ([MLOps lifecycle](../lifecycles/mlops-lifecycle.md)).

**Future work:** Automated drift-response with bounded autonomy; quality forecasting from leading indicators; segment-level drift detection that catches subgroup decay before the aggregate moves.

---

## O-03 — Provider silently changed the model

**Symptom:** Behavior shifts noticeably on a specific date with no deployment on our side. Cost or refusal rates change; previously working prompts underperform.

**Root cause:** The provider updated or replaced the model behind an unpinned alias, or routing changed between model variants. No change-detection mechanism exists because the version was never pinned.

**Impact:** High and organization-wide — every workload using that alias is affected simultaneously, and the cause is invisible in our own deployment history.

**Fix:** Identify the change window via evaluation deltas; pin to a specific version going forward; re-run full evaluations; adjust prompts/config if needed or move to the pinned version until migration is evaluated.

**Prevention:** Version pinning ([model-provider standards](../standards/model-provider-standards.md)); scheduled evaluation runs that detect behavioral drift; provider deprecation/change watch in the [technology lifecycle](../lifecycles/technology-lifecycle.md).

**Future work:** Automated daily behavioral fingerprinting per model version; contractual change-notice guarantees; evaluation-diff reports that attribute quality changes to provider events automatically.

---

## O-07 — Rollback impossible

**Symptom:** A bad change must be reverted, but reverting the code doesn't restore correct behavior because the prompt, index, model version, or config also changed.

**Root cause:** Rollback planning covered code only. Behavioral change lives in prompts, retrieval configuration, embeddings, guardrails, tool definitions, and provider model versions — none of which were versioned as deployables.

**Impact:** High. Short incidents become long ones, and teams resort to disabling functionality entirely.

**Fix:** Reconstruct prior state from whatever history exists; rebuild the index/prompt/config to the previous known-good version; then fix the versioning gap.

**Prevention:** Treat every behavior-affecting artifact as a versioned deployable ([GenAI lifecycle](../lifecycles/genai-llmops-lifecycle.md)); maintain a rollback target for each; test rollback as part of release readiness ([PoC→production](../docs/poc-to-production.md)).

**Future work:** Coordinated atomic rollback across code+prompt+index+config; rollback drills as a standard release gate; automatic rollback triggered by quality SLO breach rather than human decision.

---

## O-10 — "What model made this decision?" unanswerable

**Symptom:** An auditor or regulator asks how a specific decision was reached and which model version, prompt, or data was involved. The team cannot answer with evidence.

**Root cause:** No model inventory, no per-decision provenance, and no approval records tying a model version to its intended use and limitations.

**Impact:** **High to Critical** depending on regulation. Direct compliance exposure and potential inability to defend a decision.

**Fix:** Reconstruct from logs where possible; document current state going forward; establish inventory and lineage retroactively for the systems in scope.

**Prevention:** [Model risk lifecycle](../lifecycles/model-risk-lifecycle.md) inventory and approval records; decision lineage ([MLOps patterns](../design-patterns/mlops-deployment.md)); immutable audit logging (control AI-7).

**Future work:** Automated decision-provenance capture as a platform feature rather than per-team work; standardized model cards propagated to decision records; explainability surfaces usable by non-technical reviewers.

---

## O-12 — Platform becomes the bottleneck

**Symptom:** Delivery slows; teams route around the platform or the standards. The central function reviews everything and becomes the constraint it was meant to remove.

**Root cause:** Standards published without enablement, reviews centralized at every tier, and no golden path — so "ask the architecture team" is the only known route, and exceptions become the norm when standards lag reality.

**Impact:** High for the organization (slow delivery, shadow AI, inconsistent controls) though invisible in any single workload's metrics.

**Fix:** Introduce review tiers with published checklists ([review process](../docs/architecture-review-process.md)); ship [blueprints](../blueprints/) so the compliant path is the fast path; move routine approvals to engineering leads.

**Prevention:** [Enablement lifecycle](../lifecycles/enablement-adoption-lifecycle.md) — measure delegation (review requests and exception counts trending down) as the success signal rather than review throughput.

**Future work:** Self-service conformance checks in CI that replace routine review entirely; automated standards-drift detection; internal capability catalog with quality ratings so teams reuse instead of rebuild.
