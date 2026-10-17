# Delivery & Practice Approaches

**Status:** Proposed · **Last reviewed:** 2026-10-17

Approaches that shape *how work is organized and delivered*, complementing the [driven-development approaches](driven-development-approaches.md). Each entry states the idea, the practice, and the AI/ML-specific angle.

---

## Product & discovery approaches

### Hypothesis-Driven Development
**Idea:** Frame work as falsifiable hypotheses; measure; learn from both success and failure.
- **Practice:** "We believe X will produce Y, measured by Z" → cheapest test → decide
- **AI angle:** AI capability claims ("agents will cut handling time") are hypotheses needing measurement, not features to ship.

### Lean Startup / Build-Measure-Learn
**Idea:** Minimize time through the loop; treat early versions as experiments.
- **AI angle:** prototypes are for learning ([research rules](../research/README.md)); production is a separate, deliberate rebuild ([PoC→production](../docs/poc-to-production.md)).

### Design Thinking / Human-Centered Design
**Idea:** Empathize → define → ideate → prototype → test with real users.
- **AI angle:** AI features live or die on trust and workflow fit; observe real workflows, don't infer them.

### Dual-Track Agile (discovery + delivery)
**Idea:** Continuous discovery runs alongside delivery so decisions are informed before commitment.
- **AI angle:** model/data evaluation runs as discovery while the surrounding product is built in delivery.

### Risk-First / Risk-Driven Delivery
**Idea:** Sequence work to retire the biggest risks (technical, data, compliance, adoption) first.
- **AI angle:** typical priority order — data availability → evaluation feasibility → security review → integration → UX polish. "Demo-ability first" is the anti-pattern.

### Jobs-to-be-Done
**Idea:** Frame requirements around the job the user is trying to complete, not the feature.
- **AI angle:** grounds use-case selection ([use cases](../use-cases/README.md)) in real work rather than capability enthusiasm.

---

## Engineering delivery approaches

### DevOps & Continuous Delivery
**Idea:** Small, frequent, automated, reversible changes.
- **AI angle:** prompts, models, indexes, and configs are deployables too — same pipeline, same gates.

### Trunk-Based Development
**Idea:** Short-lived branches, integrate frequently, hide incomplete work behind flags.
- **AI angle:** flag granularity includes model version and autonomy level ([experimentation lifecycle](../lifecycles/experimentation-lifecycle.md)).

### GitOps
**Idea:** Desired state declared in Git; automated reconciliation to that state.
- **AI angle:** serving resources, guardrails, tool registries declared as code ([architecture as code](../design-patterns/architecture-as-code.md)).

### Platform Engineering / Internal Developer Platform
**Idea:** Treat developers as customers; provide self-service golden paths.
- **AI angle:** [blueprints](../blueprints/) and reference architectures are the golden path — the mechanism that lets central architecture scale without reviewing everything.

### SRE / Error Budgets
**Idea:** Reliability targets with explicit budgets; spend budget on change, stop when exhausted.
- **AI angle:** add **quality budgets** — "average faithfulness must stay ≥ threshold; regressions consume the budget."

### Chaos Engineering
**Idea:** Deliberately inject failures to validate resilience.
- **AI angle:** drill the degradation ladder, kill switch, provider failover, and index-outage behavior ([operations lifecycle](../lifecycles/operations-incident-lifecycle.md)).

### Progressive Delivery (canary, blue-green, feature flags)
**Idea:** Expose changes to a growing slice with automated safety checks.
- **AI angle:** compare **quality** metrics between variants, not just error rates.

---

## Data & model approaches

### Data-Centric AI
**Idea:** Improve the data (labels, coverage, consistency) rather than only the model architecture.
- **AI angle:** most production quality gains come from better data and retrieval, not bigger models.

### Benchmark-Driven Development
**Idea:** Define benchmarks early; optimize against them; guard against overfitting.
- **AI angle:** our own task-specific benchmarks, not vendor leaderboards.

### Simulation-Driven Development
**Idea:** Build simulated environments to test behavior safely at scale.
- **AI angle:** agent trajectory testing, synthetic multi-turn scenarios, adversarial user simulation before real side effects.

### Ontology- / Knowledge-Driven Development
**Idea:** Encode domain knowledge explicitly (ontologies, taxonomies, semantic models) and build on it.
- **AI angle:** [semantic-layer grounding](../design-patterns/semantic-layer-grounding.md), Graph RAG, governed entity resolution.

### Human-in-the-Loop Learning (feedback loops)
**Idea:** Systematically convert human corrections into improved data/behavior.
- **AI angle:** feedback→triage→regression set→retrain/re-prompt ([evaluation lifecycle](../lifecycles/evaluation-lifecycle.md)); watch for feedback bias.

---

## Operational & process approaches

### Postmortem-Driven Improvement
**Idea:** Every incident produces system-level learning and tracked actions; blameless.
- **AI angle:** quality/safety failures count as incidents, and production failures become evaluation cases.

### Six Sigma / Lean Process Improvement (DMAIC)
**Idea:** Define → Measure → Analyze → Improve → Control, applied to processes.
- **AI angle:** for [intelligent automation](../reference-architectures/intelligent-automation/README.md) — measure the process before automating it, and simplify waste before adding AI.

### Shift-Left (and Shift-Right) Quality & Security
**Idea:** Move verification earlier (left) and production feedback into development (right).
- **AI angle:** evaluation and threat modeling at design; production quality signals feeding the backlog.

### Agent-Assisted Development
**Idea:** Use AI coding agents to accelerate delivery with human accountability.
- **AI angle:** governed by the [AI-assisted development standard](../standards/ai-assisted-development.md) — stricter review, not weaker, for AI-authored code on AI-critical paths.

### FinOps Practice
**Idea:** Engineering, finance, and product share cost accountability.
- **AI angle:** unit economics per workload as a first-class design constraint ([cost lifecycle](../lifecycles/finops-cost-lifecycle.md)).

---

## Combining approaches by context

| Context | Recommended mix |
|---|---|
| New greenfield AI product | Design thinking → dual-track agile → risk-first → TDD/BDD for logic + evaluation-driven for AI → progressive delivery |
| Adding AI to a legacy system of record | Domain-driven → strangler fig → contract-first → evaluation-driven → security-driven |
| Platform/enablement work | Platform engineering → documentation-driven → GitOps → enablement lifecycle |
| High-risk agentic capability | Risk-first → simulation-driven → security-driven → chaos → postmortem-driven |
| Cost-sensitive scale-out | FinOps → benchmark-driven → data-centric → SRE error budgets |
| Process automation at scale | Lean/Six Sigma → outcome/value-driven → contract-first → experimentation |

## Anti-patterns

- Adopting approaches as identity markers rather than tools
- Ceremonies without artifacts (retrospectives with no actions, discovery with no decisions)
- Optimization work with no measurement discipline
- Choosing a heavyweight approach for a small problem
- Changing approaches mid-flight without an ADR explaining why
