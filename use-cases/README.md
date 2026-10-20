# Use Cases

Concrete, end-to-end scenarios: the **problem statement**, the **pain points**, the **workflow**, the **tech stack**, the **trade-offs**, the **success metrics**, the **failure modes & mitigations**, and the **future work**. Each use case is mapped to the reference architectures, lifecycles, and patterns that implement it.

Use cases are how the abstract collections connect to real work. Each one is written to be readable by both business and engineering audiences ([solution design lifecycle](../docs/solution-design-lifecycle.md)).

## How to use a use case

1. **Confirm the problem statement is yours** — if it isn't, don't copy the design
2. **Walk the workflow** — identify which steps your reality changes
3. **Read the trade-offs** — they are the actual design decisions, not the tech list
4. **Start from the mapped reference architecture**, and record deviations as [ADRs](../adr/README.md)
5. **Check the failure modes** — they are drawn from real production problems ([production-issues](../production-issues/README.md))

## Common structure

Every use case contains: problem statement · pain points · users & stakeholders · workflow (diagram) · tech stack (generic layers) · trade-offs · success metrics · failure modes & mitigations · related artifacts · future work.

## Choosing between overlapping use cases

| If the need is… | Prefer |
|---|---|
| Answer questions from documents | [Knowledge assistant](use-cases/enterprise-knowledge-assistant.md) |
| Answer questions from structured data/metrics | [Data agent](use-cases/nl-analytics-data-agent.md) |
| Both | Data agent for metrics; [RAG](use-cases/enterprise-knowledge-assistant.md) for narrative docs — one interface, two governed sources |
| Assist inside an existing app | [Copilot](use-cases/enterprise-copilot-rollout.md) |
| Take actions across systems | [Agentic process automation](use-cases/agentic-process-automation.md) + [human approval](../design-patterns/human-in-the-loop-approval.md) |
| Improve a specific narrow task | [Domain adaptation](use-cases/domain-model-adaptation.md) or a focused prompt/retrieval solution first |
| Predict a number/class at scale | [Real-time decision scoring](use-cases/realtime-decision-scoring.md) |
| Extract structure from documents | [Document intelligence](use-cases/document-intelligence-pipeline.md) |

---

## [1] Enterprise Knowledge Assistant

*See [use-cases/enterprise-knowledge-assistant.md](../use-cases/enterprise-knowledge-assistant.md)*

## [2] Natural-Language Analytics (Data Agent)

*See [use-cases/nl-analytics-data-agent.md](../use-cases/nl-analytics-data-agent.md)*

## [3] Agentic Process Automation

*See [use-cases/agentic-process-automation.md](../use-cases/agentic-process-automation.md)*

## [4] Enterprise Copilot Rollout

*See [use-cases/enterprise-copilot-rollout.md](../use-cases/enterprise-copilot-rollout.md)*

## [5] Domain Model Adaptation (Fine-tuning)

*See [use-cases/domain-model-adaptation.md](../use-cases/domain-model-adaptation.md)*

## [5] Real-Time Decision Scoring

*See [use-cases/realtime-decision-scoring.md](../use-cases/realtime-decision-scoring.md)*

## [6] Document Intelligence Pipeline

*See [use-cases/document-intelligence-pipeline.md](../use-cases/document-intelligence-pipeline.md)*

## [7] AI Platform Foundation (Enablement Platform)

*See [use-cases/ai-platform-foundation.md](../use-cases/ai-platform-foundation.md)*