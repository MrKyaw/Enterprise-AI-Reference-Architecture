# Domain & Business Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns that connect architecture to business reality — the domain-driven and business-analysis techniques that determine *where* AI capability belongs and *whether* it is worth building. Used in [solution design lifecycle](../docs/solution-design-lifecycle.md) and [product lifecycle](../lifecycles/product-lifecycle.md).

## Domain-driven design (DDD) patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Bounded context** | Explicit boundary where a model and vocabulary are consistent | Complex domains; multiple teams | Boundaries must map to ownership, not org charts |
| **Ubiquitous language** | One shared vocabulary between business and code | Always | Language drifts without enforcement |
| **Context map** | Document relationships between contexts | Several bounded contexts | Stale maps mislead integration planning |
| **Anticorruption layer** | Translate/protect a new domain from legacy models | Integrating legacy/third-party systems | Owned by the new side; must not leak legacy models |
| **Shared kernel** | Deliberately shared model across contexts | Tightly coupled teams | Churn cost; changes affect both |
| **Customer/supplier** | Upstream/downstream with negotiated contract | Service dependencies | Power imbalances need explicit SLAs |
| **Conformist** | Adopt upstream model as-is | Upstream can't change | Loss of domain independence |
| **Partnership** | Two contexts evolve together | Genuine mutual dependence | Coordination cost |
| **Domain event** | Business-significant state change as an event | Event-driven systems, audit needs | Event naming discipline |
| **Aggregate** | Consistency boundary for transactional changes | Write-side modeling | Over-large aggregates hurt throughput |
| **Repository** | Abstract persistence behind domain semantics | Always for domain code | Leaky abstractions into storage specifics |
| **Specification** | Encapsulate business rules as composable predicates | Complex eligibility/rules logic | Can duplicate policy engines |

### DDD applied to AI

| Question | DDD lens |
|---|---|
| Where does the AI capability live? | Inside a **bounded context**, owning its decisions |
| What does the AI decide vs. the domain? | Domain rules are deterministic and owned; AI supplies judgment where rules can't reach |
| How does AI integrate with legacy? | **Anticorruption layer** at the boundary; AI never inherits legacy semantics silently |
| What event signals the AI's action? | **Domain events** for auditability and downstream reactions |
| Who owns the prompt/knowledge? | The **context owner**, not a central team |

## Discovery & modeling techniques

| Technique | Intent | Output | Best for |
|---|---|---|---|
| **Event storming** | Map the real process as a timeline of events, commands, actors, policies | Process map + context candidates | Finding where value/waste and AI decision points live |
| **Domain storytelling** | Narrate concrete business scenarios step by step | Shared understanding + vocabulary | Aligning business and technical stakeholders |
| **Example mapping** | Concrete examples to expose rules and ambiguities | Acceptance criteria | Requirements precision |
| **Impact mapping** | Connect goals → actors → impacts → deliverables | Prioritized scope | Ensuring deliverables serve goals |
| **Process mining** | Derive actual process from system logs | As-is process with metrics | Discovering automation candidates objectively |
| **Value-stream mapping** | Map flow and wait time to find waste | Lead-time breakdown | Deciding *whether* to automate or simplify |
| **Wardley mapping** | Map components by value-chain position and evolution | Strategic build/buy/partner view | Technology strategy and horizon decisions |
| **Capability mapping** | Business capabilities and their maturity | Capability heat map | Portfolio-level AI placement |
| **Customer journey mapping** | Experience across touchpoints | Pain points + moments of truth | Where AI improves experience |
| **Assumption mapping** | Surface and rank risky assumptions | Test plan | Before prototyping |

## Business-analysis patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Problem statement before solution** | Frame the problem and measurable outcome first | The most skipped step; cause of most failed AI initiatives |
| **Cost-of-delay / opportunity sizing** | Quantify what waiting costs | Over-precision creates false confidence |
| **Outcome vs. output metrics** | Measure business change, not activity | Outputs are easier to fake |
| **Baseline capture** | Record the current-state metric before launch | Without it, value claims are unprovable |
| **Kill criteria** | Pre-agree conditions to stop | Set at approval; rarely revisited otherwise |
| **Attribution discipline** | Honest account of what caused the change | AI overselling destroys future credibility |
| **Stakeholder map** | Who decides, who uses, who is affected, who can block | Security/legal are often discovered late |
| **Definition of done (business)** | The business-observable completion condition | "Deployed" is not done |

## Stakeholder & communication patterns

| Pattern | Intent |
|---|---|
| **Two-view design** (stakeholder + engineering) | Same design expressed for executives and for builders ([lifecycle](../docs/solution-design-lifecycle.md)) |
| **Decision log / ADR** | Record why, so the question stays settled |
| **Trade-off framing** | Present options with costs, not one recommendation in disguise |
| **Risk register** | Track business + technical + compliance risks with owners |
| **Enablement package** | Training, docs, champions so adoption survives the launch |
| **Escalation path** | Named route for unresolved disagreement |

## Choosing the right technique

| Situation | Technique |
|---|---|
| "We should use AI for X" with unclear value | Value-stream mapping + Wardley + problem framing |
| Complex integration with legacy | Event storming + context mapping + ACL |
| Ambiguous requirements | Example mapping + domain storytelling |
| Portfolio-level prioritization | Capability mapping + impact mapping + opportunity scoring |
| Risky technical assumption | Assumption mapping → [prototype](../research/prototypes/TEMPLATE.md) |

## Anti-patterns

- Technology-first problem selection
- Bounded contexts drawn to match the org chart
- Discovery workshops with no artifacts or owners afterwards
- Value cases that never capture a baseline
- Expanding scope without re-running proportionate discovery
- "AI will handle it" replacing explicit domain rules that should be deterministic
