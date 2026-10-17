# Reference Architectures

Canonical, end-to-end reference architectures for each supported AI/ML workload type. Each one defines the approved components, integration patterns, security controls, and operational expectations for that workload.

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
