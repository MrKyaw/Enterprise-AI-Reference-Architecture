# Reference Architectures

Proposed end-to-end reference designs for eight AI/ML workload types. They describe candidate components, integration patterns, security controls, and operational expectations. An adopting organization must validate the design and record its own approvals; these documents do not certify a running system.

## Workload types

| Workload | Reference architecture | Status |
|---|---|---|
| Training | [training/README.md](training/README.md) | Proposed |
| Inference | [inference/README.md](inference/README.md) | Proposed |
| RAG | [rag/README.md](rag/README.md) | Proposed |
| Agentic | [agentic/README.md](agentic/README.md) | Proposed |
| Fine-tuning | [fine-tuning/README.md](fine-tuning/README.md) | Proposed |
| Data agent (NL query over governed data) | [data-agent/README.md](data-agent/README.md) | Proposed |
| Enterprise copilots & embedded AI | [copilots/README.md](copilots/README.md) | Proposed |
| Intelligent automation (workflow + RPA + AI) | [intelligent-automation/README.md](intelligent-automation/README.md) | Proposed |

## Enterprise-first architecture blueprints

Architecture blueprints that make one concern the primary optimization target. They are design documents, not runnable starter kits.

| Blueprint family | Documents | Use when |
|---|---|---|
| [Enterprise-first](enterprise-first/README.md) | 20 blueprints: secure agentic enterprise plus production-first, AI-first, compliance-first, quality-first, security-first, data-first, user-first, cost-first, resilience-first, governance-first, privacy-first, observability-first, evaluation-first, ethics-first, explainability-first, accessibility-first, sustainability-first, safety-first, interoperability-first | A single concern must be the tie-breaker in an enterprise AI design |

## When central review is required

A design needs direct architecture review when **any** of the following is true (otherwise, conforming designs are self-certified via the checklist):

- It deviates from a published reference architecture (deviations must be recorded as ADRs and justified)
- It introduces a technology not on the [approved list](../standards/approved-technologies.md)
- It handles regulated, highly confidential, or customer PII data
- It is a novel or high-risk initiative (new agentic capability with side effects, first-of-kind model usage, etc.)

## Anatomy of a reference architecture document

Every reference architecture follows the same structure:

1. **Scope & non-goals** — what this architecture covers and explicitly does not
2. **Context diagram** — actors, systems, trust boundaries (Mermaid)
3. **Component view** — approved building blocks and where they sit
4. **Data flow** — how data moves, where it is persisted, retention
5. **Technology mapping** — each component mapped to approved technologies
6. **Security controls** — mapped to [`security/ai-security-controls.md`](../security/ai-security-controls.md)
7. **Operational requirements** — SLOs, observability, capacity, cost guardrails
8. **Deviation process** — how to get an exception

## Change control

Reference architecture changes require cross-cutting review with Enterprise Architecture, Cloud Platform, Data, and Cybersecurity, and sign-off from the Head of AI Governance and Architecture. See [CONTRIBUTING.md](../CONTRIBUTING.md).
