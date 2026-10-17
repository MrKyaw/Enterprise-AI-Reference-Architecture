# Design Patterns

Reusable, cross-cutting implementation patterns that appear across multiple reference architectures. Patterns are **recommended**; reference architectures decide which are **required**.

## Index

| Pattern | Problem it solves | Used by |
|---|---|---|
| [llm-gateway.md](llm-gateway.md) | Centralize provider access, guardrails, auth, and cost attribution | Inference, Agentic |
| [human-in-the-loop-approval.md](human-in-the-loop-approval.md) | Keep humans in control of side-effecting AI actions | Agentic |
| [evaluation-in-ci.md](evaluation-in-ci.md) | Catch quality regressions before deployment, not after | RAG, Fine-tuning |

## Adding a pattern

1. The pattern must be proven in at least one production or prototype system.
2. Document: context, forces, solution, consequences, and how it maps to reference architectures.
3. Two architecture-team reviewers required (see [CONTRIBUTING.md](../CONTRIBUTING.md)).
