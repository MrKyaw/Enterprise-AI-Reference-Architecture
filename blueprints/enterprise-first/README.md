# Enterprise-First Architecture Blueprints

Design blueprints for enterprise AI systems where one concern is the **primary optimization target**. These are architecture documents, not runnable starter kits. Use them to shape a design, record an ADR, and then implement with the closest [starter kit](../README.md).

## Catalog

| Blueprint | Primary concern | Closest starter kit |
|---|---|---|
| [Secure Agentic Enterprise](../../reference-architectures/enterprise-first/secure-agentic-enterprise.md) | End-to-end secure agent platform | `agent-starter-kit` + `ai-security-starter-kit` |
| [Production-First](../../reference-architectures/enterprise-first/production-first.md) | Reliable operation | `inference-starter-kit` |
| [AI-First](../../reference-architectures/enterprise-first/ai-first.md) | AI as primary interaction layer | `agent-starter-kit` |
| [Compliance-First](../../reference-architectures/enterprise-first/compliance-first.md) | Regulatory and policy obligations | `ai-security-starter-kit` |
| [Quality-First](../../reference-architectures/enterprise-first/quality-first.md) | Correctness and usefulness | `evaluation-starter-kit` |
| [Security-First](../../reference-architectures/enterprise-first/security-first.md) | Threat modeling and controls | `ai-security-starter-kit` |
| [Data-First](../../reference-architectures/enterprise-first/data-first.md) | Governed data foundations | `data-agent-starter-kit` |
| [User-First](../../reference-architectures/enterprise-first/user-first.md) | Human outcomes and control | `copilot-starter-kit` |
| [Cost-First](../../reference-architectures/enterprise-first/cost-first.md) | Unit economics | `observability-starter-kit` |
| [Resilience-First](../../reference-architectures/enterprise-first/resilience-first.md) | Graceful degradation and recovery | `intelligent-automation-starter-kit` |
| [Governance-First](../../reference-architectures/enterprise-first/governance-first.md) | Ownership and decision rights | `agent-factory-starter-kit` |
| [Privacy-First](../../reference-architectures/enterprise-first/privacy-first.md) | Data minimization and deletion | `rag-starter-kit` |
| [Observability-First](../../reference-architectures/enterprise-first/observability-first.md) | Traceability and debuggability | `observability-starter-kit` |
| [Evaluation-First](../../reference-architectures/enterprise-first/evaluation-first.md) | Measured quality gates | `evaluation-starter-kit` |
| [Ethics-First](../../reference-architectures/enterprise-first/ethics-first.md) | Fairness and societal impact | `evaluation-starter-kit` |
| [Explainability-First](../../reference-architectures/enterprise-first/explainability-first.md) | Inspectable decisions | `rag-starter-kit` |
| [Accessibility-First](../../reference-architectures/enterprise-first/accessibility-first.md) | Inclusive design | `copilot-starter-kit` |
| [Sustainability-First](../../reference-architectures/enterprise-first/sustainability-first.md) | Energy and carbon constraints | `training-starter-kit` |
| [Safety-First](../../reference-architectures/enterprise-first/safety-first.md) | Harm prevention | `physical-ai-starter-kit` |
| [Interoperability-First](../../reference-architectures/enterprise-first/interoperability-first.md) | Open standards and portability | `integration-starter-kit` |

## How to use

1. Select the blueprint whose primary concern is your dominant risk or differentiator.
2. Record the selection and any deviations in an ADR.
3. Map the blueprint's metrics to SLOs and dashboards before implementation.
4. Implement with the closest starter kit and complete its production checklist.

## Related

- [Enterprise-first reference architectures](../../reference-architectures/enterprise-first/README.md)
- [Reference architectures](../../reference-architectures/README.md)
- [Blueprints catalog](../README.md)
- [Design review checklist](../../docs/design-review-checklist.md)
