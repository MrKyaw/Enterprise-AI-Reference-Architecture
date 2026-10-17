# Software Development Lifecycle (SDLC)

**Status:** Proposed · **Owner:** Engineering · **Last reviewed:** 2026-10-17

The base lifecycle every other lifecycle extends. Applies to applications, services, libraries, data pipelines, and AI components alike.

## Phases

| Phase | Activities | Artifacts | Exit gate |
|---|---|---|---|
| **1. Requirements** | Elicit functional + non-functional needs | Requirements list, [NFRs](../docs/non-functional-requirements.md) | Requirement reviewed and accepted |
| **2. Design** | Architecture, interfaces, data model, threat model | Design doc, diagrams, [ADRs](../adr/README.md) | [Design review](../docs/architecture-review-process.md) outcome |
| **3. Implementation** | Coding, config, IaC | Source, IaC, tests | CI green |
| **4. Verification** | Unit → integration → contract → system → acceptance | Test suites, coverage report, eval results | Quality gates passed |
| **5. Release** | Versioning, changelog, packaging, deploy automation | Release notes, deploy pipeline | Release readiness checklist |
| **6. Deployment** | Rollout (canary/blue-green/shadow), migration | Deployment record | Smoke tests pass |
| **7. Operations** | Monitor, alert, incident response, tuning | Dashboards, runbook | SLOs met over a full cycle |
| **8. Maintenance** | Bug fixes, dependency updates, refactors | Patch releases | Backlog cadence |
| **9. Retirement** | Deprecate, migrate consumers, decommission | Deprecation notice, decommission record | Consumers migrated, resources removed |

## Methodologies

| Methodology | Shape | Fits when |
|---|---|---|
| Waterfall | Sequential, gated | Regulated, fixed-scope, low-change domains |
| Agile / Scrum | Iterative sprints | Product development with evolving requirements |
| Kanban | Continuous flow | Operations, support, steady-state work |
| SAFe / scaled agile | Portfolio of agile teams | Multi-team enterprise programs |
| Continuous delivery | Always-releasable trunk | Mature engineering with strong test automation |
| Contract-first / API-first | Interfaces before implementation | Cross-team and partner integration |

Choose per project; document the choice in an ADR if it deviates from the organization default.

## Engineering practices (required baseline)

- Trunk-based development or short-lived branches; PR review for all changes
- Automated tests in CI; no merge with failing tests
- Everything as code: infrastructure, config, policy ([architecture as code](../design-patterns/architecture-as-code.md))
- Trunk must always be releasable (CI/CD, feature flags for incomplete work)
- Security scanning in pipeline ([secure SDLC](../security/secure-sdlc.md))
- Observability built with the feature, not after ([NFRs](../docs/non-functional-requirements.md#observability))

## AI-specific extensions

AI systems add these to the standard SDLC:

- **Data/provenance requirements** at phase 1
- **Evaluation datasets and thresholds** as test artifacts at phase 4
- **Prompt/model versioning** as release artifacts at phase 5
- **Quality and drift monitoring** at phase 7
- **Guardrail and tool-registry changes** treated as code, with review

Full details: [GenAI/LLMOps lifecycle](genai-llmops-lifecycle.md).

## Anti-patterns

- Testing only in production ("we'll monitor it")
- Manual deployments that can't be reproduced
- Architecture decisions living only in slide decks
- Feature work without corresponding test/eval updates
- Retiring code but keeping its data and credentials alive
