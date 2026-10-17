# Approaches

Development and delivery **approaches** — the "X-driven" method families and the testing strategy that supports them. Approaches are how work is done; [lifecycles](../lifecycles/README.md) are the phases work flows through; [patterns](../design-patterns/README.md) are the solutions applied inside them.

## Index

| Document | Covers |
|---|---|
| [driven-development-approaches.md](driven-development-approaches.md) | Test-, behavior-, domain-, data-, model-, evaluation-, security-, API/contract/spec-, outcome- and evidence-driven approaches |
| [delivery-and-practice-approaches.md](delivery-and-practice-approaches.md) | Hypothesis-, risk-, design-thinking, Lean/Dual-track, DevOps/CD, trunk-based, GitOps, platform engineering, SRE/error budgets, chaos, data-centric, benchmark-, simulation-, ontology-driven, postmortem-driven, Six Sigma, agent-assisted |
| [testing-strategy.md](testing-strategy.md) | Test types across the pyramid, AI-specific test layers, and the test strategy per workload |

## How to combine them

Approaches are complementary, not exclusive. A typical AI system uses:

```
Domain-driven  → decide where the capability belongs and its boundaries
API/contract   → define interfaces before implementation
Test/BDD       → drive logic and behavior at build time
Evaluation     → drive AI quality (the AI analogue of tests)
Data-driven    → make decisions from measurement, not opinion
Security-driven→ embed controls throughout, not at the end
Outcome/value  → keep the business result in view; retire what doesn't deliver
```

## Selection matrix

| Approach | Primary artifact | Strongest when | Weakest when |
|---|---|---|---|
| Test-driven development | Failing test → code | Deterministic logic, contracts | Spec is unknown; prototyping to learn |
| Behavior-driven development | Executable scenarios | Multi-stakeholder requirements | Over-formalized for internal tooling |
| Domain-driven design | Bounded contexts + model | Complex, long-lived domains | Simple CRUD or throwaway tools |
| Data-driven development | Metrics + experiments | Measurable objectives | Metrics gameable or absent |
| Model-driven development | Models as source of truth | Well-specified, repetitive domains | Novel domains with unstable semantics |
| Evaluation-driven development | Golden sets + thresholds | Every AI/LLM feature | High-judgment tasks with no ground truth (then: human review cadence) |
| Specification/contract-first | Interface specs | Cross-team and partner integration | Rapid internal iteration |
| Security-driven (DevSecOps) | Controls in pipeline | Always | Never skip |
| Outcome/value-driven | KPI + baseline | Funding and prioritization | Not a substitute for engineering rigor |
| Evidence-driven architecture | Prototype + brief | Build/buy and tech adoption | Trivial decisions |

## Core principle

Each approach answers a different question:

| Question | Approach |
|---|---|
| Does the code work? | Test-driven |
| Does it do what the business asked? | Behavior-driven |
| Is the model right? | Domain-driven |
| Is the AI answer good? | Evaluation-driven |
| Is it secure? | Security-driven |
| Is it worth it? | Outcome/value-driven |
| Is it true? | Evidence-driven |
| Is it measurable? | Data-driven |

**"Done" requires answers to all of them.** A system can be fully unit-tested, BDD-verified, and still produce harmful or valueless AI output — that is why the AI-specific approaches exist.
