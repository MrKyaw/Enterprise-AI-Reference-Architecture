# Use Cases

Concrete, end-to-end scenarios: the **problem statement**, the **pain points**, the **workflow**, the **tech stack**, the **trade-offs**, the success metrics, and the failure modes — each mapped to the reference architectures, lifecycles, and patterns that implement it.

Use cases are how the abstract collections connect to real work. Each one is written to be readable by both business and engineering audiences ([solution design lifecycle](../docs/solution-design-lifecycle.md)).

## Index

| Use case | Problem | Primary pattern/RA |
|---|---|---|
| [enterprise-knowledge-assistant.md](enterprise-knowledge-assistant.md) | Employees can't find answers across scattered, permissioned content | [RAG RA](../reference-architectures/rag/README.md) |
| [nl-analytics-data-agent.md](nl-analytics-data-agent.md) | Business users wait on analysts for routine data questions | [Data agent RA](../reference-architectures/data-agent/README.md) |
| [agentic-process-automation.md](agentic-process-automation.md) | High-volume operational processes need judgment at every step | [Agentic RA](../reference-architectures/agentic/README.md) + [Automation RA](../reference-architectures/intelligent-automation/README.md) |
| [enterprise-copilot-rollout.md](enterprise-copilot-rollout.md) | Work happens inside business apps; context switching kills productivity | [Copilots RA](../reference-architectures/copilots/README.md) |
| [domain-model-adaptation.md](domain-model-adaptation.md) | Generic models underperform on specialized, terminology-heavy tasks | [Fine-tuning RA](../reference-architectures/fine-tuning/README.md) |
| [realtime-decision-scoring.md](realtime-decision-scoring.md) | Decisions must be made in milliseconds at high volume | [Inference RA](../reference-architectures/inference/README.md) |
| [document-intelligence-pipeline.md](document-intelligence-pipeline.md) | Unstructured documents gate downstream processes | [Inference RA](../reference-architectures/inference/README.md) + [Data lifecycle](../lifecycles/data-lifecycle.md) |
| [ai-platform-foundation.md](ai-platform-foundation.md) | Every team builds its own provider access, guardrails, and evals | [Inference RA](../reference-architectures/inference/README.md) gateway |

## How to use a use case

1. **Confirm the problem statement is yours** — if it isn't, don't copy the design
2. **Walk the workflow** — identify which steps your reality changes
3. **Read the trade-offs** — they are the actual design decisions, not the tech list
4. **Start from the mapped reference architecture**, and record deviations as [ADRs](../adr/README.md)
5. **Check the failure modes** — they are drawn from real production problems ([production issues](../production-issues/README.md))

## Common structure

Every use case contains: problem statement · pain points · users & stakeholders · workflow (diagram) · tech stack (generic layers) · trade-offs · success metrics · failure modes & mitigations · related artifacts · future work.

## Choosing between overlapping use cases

| If the need is… | Prefer |
|---|---|
| Answer questions from documents | [Knowledge assistant](enterprise-knowledge-assistant.md) |
| Answer questions from structured data/metrics | [Data agent](nl-analytics-data-agent.md) |
| Both | Data agent for metrics; RAG for narrative docs — one interface, two governed sources |
| Assist inside an existing app | [Copilot](enterprise-copilot-rollout.md) |
| Take actions across systems | [Agentic automation](agentic-process-automation.md) + [human approval](../design-patterns/human-in-the-loop-approval.md) |
| Improve a specific narrow task | [Domain adaptation](domain-model-adaptation.md) or a focused prompt/retrieval solution first |
| Predict a number/class at scale | [Real-time scoring](realtime-decision-scoring.md) |
| Extract structure from documents | [Document intelligence](document-intelligence-pipeline.md) |
