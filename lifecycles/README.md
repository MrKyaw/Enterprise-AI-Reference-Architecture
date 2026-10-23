# Lifecycles

End-to-end lifecycles that govern how AI/ML work is conceived, built, deployed, operated, and retired. They **nest** rather than compete: a software lifecycle contains a data lifecycle, an ML lifecycle contains MLOps, a GenAI system contains a RAG and prompt lifecycle, and everything sits inside a product lifecycle.

## Index

> The [solution design lifecycle](../docs/solution-design-lifecycle.md) is maintained in `docs/` because it spans discovery, solutioning, and delivery. It is part of the lifecycle family but is not counted among the 24 lifecycle files in this folder.

| Lifecycle | Covers | Owner |
|---|---|---|
| [software-development-lifecycle.md](software-development-lifecycle.md) | Requirements → design → build → test → release → operate | Engineering |
| [ml-project-lifecycle.md](ml-project-lifecycle.md) | Problem framing → data → modeling → evaluation → deployment | Data science / ML |
| [mlops-lifecycle.md](mlops-lifecycle.md) | CI/CD/CT automation, registry, monitoring, retraining | ML platform |
| [genai-llmops-lifecycle.md](genai-llmops-lifecycle.md) | Prompt → model → eval → deploy → observe for LLM apps | AI engineering |
| [rag-lifecycle.md](rag-lifecycle.md) | Corpus → ingest → embed → retrieve → generate → evaluate | AI engineering |
| [agent-lifecycle.md](agent-lifecycle.md) | Design → tools → memory → safety → operate → retire (AgentOps) | AI engineering |
| [data-lifecycle.md](data-lifecycle.md) | Acquire → store → transform → serve → archive → delete | Data |
| [prompt-lifecycle.md](prompt-lifecycle.md) | Author → version → evaluate → deploy → observe → retire | AI engineering |
| [evaluation-lifecycle.md](evaluation-lifecycle.md) | Dataset curation → metrics → harness → gates → drift review | AI quality |
| [product-lifecycle.md](product-lifecycle.md) | Idea → discovery → business case → delivery → value → sunset | Product |
| [model-risk-lifecycle.md](model-risk-lifecycle.md) | Intake → assess → approve → monitor → revalidate → retire | Governance / risk |
| [operations-incident-lifecycle.md](operations-incident-lifecycle.md) | Monitor → detect → triage → mitigate → resolve → postmortem | Operations |
| [technology-lifecycle.md](technology-lifecycle.md) | Horizon scan → trial → adopt → hold → deprecate → remove | Architecture |
| [api-lifecycle.md](api-lifecycle.md) | Design → publish → version → observe → deprecate | Platform / API |
| [experimentation-lifecycle.md](experimentation-lifecycle.md) | Hypothesis → design → run → analyze → decide; progressive feature release | Product / data |
| [finops-cost-lifecycle.md](finops-cost-lifecycle.md) | Forecast → attribute → optimize → govern | Finance / platform |
| [documentation-knowledge-lifecycle.md](documentation-knowledge-lifecycle.md) | Author → review → publish → maintain → retire | Architecture |
| [vendor-third-party-lifecycle.md](vendor-third-party-lifecycle.md) | Assess → contract → integrate → manage → exit | Procurement / architecture |
| [enablement-adoption-lifecycle.md](enablement-adoption-lifecycle.md) | Assess skills → build capability → enable → sustain | Leadership / enablement |
| [edge-ai-lifecycle.md](edge-ai-lifecycle.md) | Train → compress → convert → deploy → fleet monitor → retire | Embedded / AI |
| [quantum-computing-lifecycle.md](quantum-computing-lifecycle.md) | Screen → simulate → benchmark → hybrid integrate → evaluate | Research / architecture |
| [agent-factory-lifecycle.md](agent-factory-lifecycle.md) | Incubate → certify → deploy → monitor → retire agents at scale | AI platform |
| [physical-ai-lifecycle.md](physical-ai-lifecycle.md) | Simulate → validate on test bed → deploy → monitor → decommission | Robotics / AI |
| [embodied-ai-lifecycle.md](embodied-ai-lifecycle.md) | Design → train sensorimotor skills → operate → monitor → retire | Research / robotics |

### Specialized tracks and starter kits

| Lifecycle | Starter kit | Domain focus |
|---|---|---|
| [edge-ai-lifecycle.md](edge-ai-lifecycle.md) | [edge-ai-starter-kit](../blueprints/edge-ai-starter-kit/README.md) | On-device inference, quantization, OTA, fleet telemetry |
| [quantum-computing-lifecycle.md](quantum-computing-lifecycle.md) | [quantum-starter-kit](../blueprints/quantum-starter-kit/README.md) | Hybrid classical-quantum experiments |
| [agent-factory-lifecycle.md](agent-factory-lifecycle.md) | [agent-factory-starter-kit](../blueprints/agent-factory-starter-kit/README.md) | Factory scaffold, certification, registry, retirement |
| [physical-ai-lifecycle.md](physical-ai-lifecycle.md) | [physical-ai-starter-kit](../blueprints/physical-ai-starter-kit/README.md) | Sim-to-real transfer and safety envelopes |
| [embodied-ai-lifecycle.md](embodied-ai-lifecycle.md) | [embodied-ai-starter-kit](../blueprints/embodied-ai-starter-kit/README.md) | Sensorimotor learning and world models |

Lifecycles without a dedicated kit are instantiated through the closest core kit — for example, the [evaluation kit](../blueprints/evaluation-starter-kit/README.md), [observability kit](../blueprints/observability-starter-kit/README.md), and [AI security kit](../blueprints/ai-security-starter-kit/README.md) are cross-cutting and apply to every workload.

### Blueprint coverage by lifecycle

| Lifecycle | Closest starter kit | Coverage note |
|---|---|---|
| [software-development-lifecycle.md](software-development-lifecycle.md) | [inference-starter-kit](../blueprints/inference-starter-kit/README.md) | Service delivery and release mechanics |
| [ml-project-lifecycle.md](ml-project-lifecycle.md) | [training-starter-kit](../blueprints/training-starter-kit/README.md) | Problem framing, data, modeling, evaluation |
| [mlops-lifecycle.md](mlops-lifecycle.md) | [training-starter-kit](../blueprints/training-starter-kit/README.md) | CI/CD/CT, registry, monitoring |
| [genai-llmops-lifecycle.md](genai-llmops-lifecycle.md) | [rag-starter-kit](../blueprints/rag-starter-kit/README.md) | Prompt-to-production for LLM apps |
| [rag-lifecycle.md](rag-lifecycle.md) | [rag-starter-kit](../blueprints/rag-starter-kit/README.md) | Corpus, retrieval, generation, evaluation |
| [agent-lifecycle.md](agent-lifecycle.md) | [agent-starter-kit](../blueprints/agent-starter-kit/README.md) | Tools, memory, safety, operations |
| [data-lifecycle.md](data-lifecycle.md) | [data-agent-starter-kit](../blueprints/data-agent-starter-kit/README.md) | Acquisition, governance, serving |
| [prompt-lifecycle.md](prompt-lifecycle.md) | [rag-starter-kit](../blueprints/rag-starter-kit/README.md) | Authoring, versioning, evaluation |
| [evaluation-lifecycle.md](evaluation-lifecycle.md) | [evaluation-starter-kit](../blueprints/evaluation-starter-kit/README.md) | Datasets, metrics, gates, monitoring |
| [product-lifecycle.md](product-lifecycle.md) | [copilot-starter-kit](../blueprints/copilot-starter-kit/README.md) | Discovery, delivery, value, sunset |
| [model-risk-lifecycle.md](model-risk-lifecycle.md) | [ai-security-starter-kit](../blueprints/ai-security-starter-kit/README.md) | Risk tiering, assessment, approval |
| [operations-incident-lifecycle.md](operations-incident-lifecycle.md) | [observability-starter-kit](../blueprints/observability-starter-kit/README.md) | Detection, triage, mitigation, postmortem |
| [technology-lifecycle.md](technology-lifecycle.md) | [inference-starter-kit](../blueprints/inference-starter-kit/README.md) | Horizon scan, trial, adopt, retire |
| [api-lifecycle.md](api-lifecycle.md) | [integration-starter-kit](../blueprints/integration-starter-kit/README.md) | Design, publish, version, deprecate |
| [experimentation-lifecycle.md](experimentation-lifecycle.md) | [evaluation-starter-kit](../blueprints/evaluation-starter-kit/README.md) | Hypothesis, run, analyze, decide |
| [finops-cost-lifecycle.md](finops-cost-lifecycle.md) | [observability-starter-kit](../blueprints/observability-starter-kit/README.md) | Forecast, attribute, optimize, govern |
| [documentation-knowledge-lifecycle.md](documentation-knowledge-lifecycle.md) | [evaluation-starter-kit](../blueprints/evaluation-starter-kit/README.md) | Author, review, publish, maintain, retire |
| [vendor-third-party-lifecycle.md](vendor-third-party-lifecycle.md) | [integration-starter-kit](../blueprints/integration-starter-kit/README.md) | Assess, contract, integrate, exit |
| [enablement-adoption-lifecycle.md](enablement-adoption-lifecycle.md) | [copilot-starter-kit](../blueprints/copilot-starter-kit/README.md) | Assess, build, enable, sustain |
| [edge-ai-lifecycle.md](edge-ai-lifecycle.md) | [edge-ai-starter-kit](../blueprints/edge-ai-starter-kit/README.md) | Train, compress, deploy, monitor |
| [quantum-computing-lifecycle.md](quantum-computing-lifecycle.md) | [quantum-starter-kit](../blueprints/quantum-starter-kit/README.md) | Screen, simulate, benchmark, integrate |
| [agent-factory-lifecycle.md](agent-factory-lifecycle.md) | [agent-factory-starter-kit](../blueprints/agent-factory-starter-kit/README.md) | Incubate, certify, deploy, retire |
| [physical-ai-lifecycle.md](physical-ai-lifecycle.md) | [physical-ai-starter-kit](../blueprints/physical-ai-starter-kit/README.md) | Simulate, validate, deploy, decommission |
| [embodied-ai-lifecycle.md](embodied-ai-lifecycle.md) | [embodied-ai-starter-kit](../blueprints/embodied-ai-starter-kit/README.md) | Design, train, operate, retire |

Lifecycles without a dedicated kit are implemented through the closest workload or cross-cutting kit; the [secure agentic enterprise starter kit](../blueprints/secure-agentic-enterprise-starter-kit/README.md) combines agent, security, evaluation, and observability patterns for integrated platforms.


## How they relate

```mermaid
flowchart TB
    P[Product lifecycle<br/>idea → value → sunset]
    P --> S[Software development lifecycle]
    P --> M[ML project lifecycle]
    P --> MR[Model risk lifecycle]
    S --> O[Operations & incident lifecycle]
    M --> MLO[MLOps lifecycle]
    M --> D[Data lifecycle]
    MLO --> GEN[GenAI / LLMOps lifecycle]
    GEN --> R[RAG lifecycle]
    GEN --> A[Agent lifecycle]
    GEN --> PR[Prompt lifecycle]
    R --> E[Evaluation lifecycle]
    A --> E
    PR --> E
    MLO --> E
    SP[Specialized lifecycles<br/>edge · quantum · agent factory · physical · embodied]
    SP -.specializes.-> P
    T[Technology lifecycle] -.adopt/retire.-> S
    T -.adopt/retire.-> M
    V[Vendor lifecycle] -.supplies.-> MLO
    F[FinOps lifecycle] -.governs cost of.-> GEN
    EN[Enablement lifecycle] -.builds capability for.-> P
    D2[Documentation lifecycle] -.records.-> S
    A2[API lifecycle] -.contracts for.-> GEN
    X[Experimentation lifecycle] -.validates.-> P
```

## Universal lifecycle rules

Every lifecycle in this directory obeys the same five rules:

1. **Every phase has an artifact** — a lifecycle without artifacts is a vibe
2. **Every phase has an exit gate** — see [design review](../docs/architecture-review-process.md) and [PoC-to-production](../docs/poc-to-production.md)
3. **Changes are versioned** — code, data, prompts, models, definitions, and documents alike
4. **Evaluation is continuous** — quality is measured at every phase, not once before launch ([evaluation lifecycle](evaluation-lifecycle.md))
5. **Retirement is designed in** — every lifecycle ends with data deletion, credential revocation, and decommission criteria

## Phase/artifact matrix (completeness check)

| Lifecycle | Entry artifact | Mid artifact | Exit artifact |
|---|---|---|---|
| Software | Requirement | Design + tests | Release + runbook |
| ML project | Framed problem + baseline | Trained model + eval report | Registered artifact + monitoring |
| MLOps | Pipeline definition | Auto retrain + CT pipeline | SLO dashboard |
| GenAI/LLMOps | Prompt spec + eval set | Deployed prompt/model config | Drift report |
| RAG | Corpus + ACL model | Index + retrieval eval | Grounding metrics |
| Agent | Capability + side-effect map | Tool registry + traces | Autonomy authorization record |
| Data | Source registration | Curated dataset + lineage | Retention/deletion record |
| Prompt | Prompt template | Versioned prompt + eval score | Deprecation note |
| Evaluation | Golden set | Harness + thresholds | Trend history |
| Product | Opportunity + KPI | Business case | Value report / sunset decision |
| Model risk | Intake request | Assessment | Revalidation schedule |
| Operations | SLO + alerting | Runbook | Postmortem + action items |
| Technology | Horizon-scan trigger | Prototype + brief | Standard status change |
| API | Consumer need | Contract + tests | Deprecation/retirement record |
| Experimentation | Hypothesis | Running experiment | Decision record |
| FinOps | Cost model | Attribution dashboard | Optimization report |
| Documentation | Documentation gap | Draft + review | Current, indexed doc |
| Vendor | Capability gap | Security review + prototype | Contract + exit plan |
| Enablement | Capability heat map | Training/blueprint adoption | Sustained adoption metrics |

## Governance tie-in

Lifecycle phase gates map to the [secure SDLC](../security/secure-sdlc.md) checkpoints and the [design review checklist](../docs/design-review-checklist.md). If a lifecycle phase has no security checkpoint, treat that as a gap to report via [SECURITY.md](../SECURITY.md).
