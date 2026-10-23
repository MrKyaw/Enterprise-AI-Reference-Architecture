# Blueprints & Starter Kits

**Status:** 17 kits scaffolded · **Last reviewed:** 2026-10-21

Runnable project scaffolds for exploring AI workload designs. Each kit includes a service skeleton, placeholder pipeline, screening examples, infrastructure baseline, smoke tests, and a production checklist. They require implementation and review before real use; copying a kit does not establish compliance or approval.

> **Principle: the compliant path must be the fast path.** Central architecture should review novel and high-risk designs, not re-review the same scaffold for the twentieth time.

---

## What every kit gives you

| Included | Detail |
|---|---|
| **Working service** | FastAPI app with `/health` and `/v1/run`, typed request/response models, local input screening, and PII redaction |
| **Pipeline stub** | `src/pipeline.py` with the exact steps to implement for that workload, so the design is visible in code |
| **Smoke tests** | `pytest` suite wired for CI — health, scaffold response, validation, injection rejection |
| **Infrastructure baseline** | Terraform: encrypted artifact bucket with versioning + lifecycle, KMS key, CloudWatch log group |
| **Container** | Non-root `Dockerfile`, Python 3.12 slim |
| **Configuration contract** | `.env.example` listing every variable the service expects |
| **Production checklist** | `.github/PULL_REQUEST_TEMPLATE.md` covering security, evaluation, rollout, and ownership |
| **Evidence links** | Each README maps to its reference architecture, lifecycles, patterns, and controls |

Every generated service returns `status: "scaffold"` until its pipeline is implemented. Treat that status as a visible boundary, not a deployment safeguard. The skeletons do not authenticate callers; request `tenant_id` values are not trusted identity, and regex screening/redaction is not a complete security or privacy control.

---

## Catalog

### Core reference architectures (8)

| Kit | Status | Reference architecture | Focus | Stack highlights |
|---|---|---|---|---|
| [`inference-starter-kit`](inference-starter-kit/README.md) | ✅ Scaffolded | [Inference](../reference-architectures/inference/README.md) | Gateway-mediated model serving | FastAPI, gateway, Terraform |
| [`rag-starter-kit`](rag-starter-kit/README.md) | ✅ Scaffolded | [RAG](../reference-architectures/rag/README.md) | Retrieval, reranking, citations, ACLs | Hybrid index, reranker, eval gate |
| [`agent-starter-kit`](agent-starter-kit/README.md) | ✅ Scaffolded | [Agentic](../reference-architectures/agentic/README.md) | Tool use, approval gates, trajectory audit | Typed tool registry, HITL, kill switch |
| [`data-agent-starter-kit`](data-agent-starter-kit/README.md) | ✅ Scaffolded | [Data agent](../reference-architectures/data-agent/README.md) | NL analytics on a governed semantic layer | Semantic layer, policy injection, query limits |
| [`copilot-starter-kit`](copilot-starter-kit/README.md) | ✅ Scaffolded | [Copilots](../reference-architectures/copilots/README.md) | In-app assistance, record context, audited writes | Host extension, context assembly, telemetry |
| [`fine-tuning-starter-kit`](fine-tuning-starter-kit/README.md) | ✅ Scaffolded | [Fine-tuning](../reference-architectures/fine-tuning/README.md) | Baseline-first adaptation, LoRA/QLoRA | Dataset curation, registry, model card |
| [`training-starter-kit`](training-starter-kit/README.md) | ✅ Scaffolded | [Training](../reference-architectures/training/README.md) | Reproducible training and registration | Versioned data, experiment tracking, lineage |
| [`intelligent-automation-starter-kit`](intelligent-automation-starter-kit/README.md) | ✅ Scaffolded | [Intelligent automation](../reference-architectures/intelligent-automation/README.md) | Rules → ML → agent, human exceptions | Durable workflow, compensation, approval |

### Specialized domains (5)

| Kit | Status | Lifecycle | Focus | Stack highlights |
|---|---|---|---|---|
| [`edge-ai-starter-kit`](edge-ai-starter-kit/README.md) | ✅ Scaffolded | [Edge AI](../lifecycles/edge-ai-lifecycle.md) | On-device inference, OTA, fleet monitoring | Quantization, target runtime, signed updates |
| [`physical-ai-starter-kit`](physical-ai-starter-kit/README.md) | ✅ Scaffolded | [Physical AI](../lifecycles/physical-ai-lifecycle.md) | Sim-to-real, test bed, safety envelope | Domain randomization, independent e-stop |
| [`embodied-ai-starter-kit`](embodied-ai-starter-kit/README.md) | ✅ Scaffolded | [Embodied AI](../lifecycles/embodied-ai-lifecycle.md) | Perception → world model → policy | Curriculum learning, skill registry |
| [`quantum-starter-kit`](quantum-starter-kit/README.md) | ✅ Scaffolded | [Quantum computing](../lifecycles/quantum-computing-lifecycle.md) | Hybrid classical-quantum experiments | Suitability gate, simulator-first, budget caps |
| [`agent-factory-starter-kit`](agent-factory-starter-kit/README.md) | ✅ Scaffolded | [Agent factory](../lifecycles/agent-factory-lifecycle.md) | Mass-producing governed agents | Scaffold generation, certification, registry |

### Cross-cutting (4)

| Kit | Status | Lifecycle | Focus | Stack highlights |
|---|---|---|---|---|
| [`evaluation-starter-kit`](evaluation-starter-kit/README.md) | ✅ Scaffolded | [Evaluation](../lifecycles/evaluation-lifecycle.md) | Golden/adversarial sets, judge calibration, CI gate | Deterministic scorers first, per-slice reporting |
| [`observability-starter-kit`](observability-starter-kit/README.md) | ✅ Scaffolded | [Operations & incident](../lifecycles/operations-incident-lifecycle.md) | Traces, token/cost metrics, quality sampling, SLOs | OpenTelemetry, collector, burn-rate alerts |
| [`ai-security-starter-kit`](ai-security-starter-kit/README.md) | ✅ Scaffolded | [Model risk](../lifecycles/model-risk-lifecycle.md) | Gateway, guardrails, egress allowlist, red team | Fail-closed, tenant scoping, adversarial suite |
| [`integration-starter-kit`](integration-starter-kit/README.md) | ✅ Scaffolded | [API](../lifecycles/api-lifecycle.md) | Contracts, schema registry, DLQ, replay | OpenAPI/AsyncAPI, idempotency, trace propagation |


---

## Enterprise-first architecture blueprints (design documents)

These are architecture blueprints, not runnable starter kits. Each makes one concern the primary optimization target.

| Blueprint | Primary concern | Closest starter kit |
|---|---|---|
| [Secure Agentic Enterprise](enterprise-first/README.md) | End-to-end secure agent platform | `agent-starter-kit` + `ai-security-starter-kit` |
| [Production-First](../reference-architectures/enterprise-first/production-first.md) | Reliable operation | `inference-starter-kit` |
| [AI-First](../reference-architectures/enterprise-first/ai-first.md) | AI as primary interaction layer | `agent-starter-kit` |
| [Compliance-First](../reference-architectures/enterprise-first/compliance-first.md) | Regulatory and policy obligations | `ai-security-starter-kit` |
| [Quality-First](../reference-architectures/enterprise-first/quality-first.md) | Correctness and usefulness | `evaluation-starter-kit` |
| [Security-First](../reference-architectures/enterprise-first/security-first.md) | Threat modeling and controls | `ai-security-starter-kit` |
| [Data-First](../reference-architectures/enterprise-first/data-first.md) | Governed data foundations | `data-agent-starter-kit` |
| [User-First](../reference-architectures/enterprise-first/user-first.md) | Human outcomes and control | `copilot-starter-kit` |
| [Cost-First](../reference-architectures/enterprise-first/cost-first.md) | Unit economics | `observability-starter-kit` |
| [Resilience-First](../reference-architectures/enterprise-first/resilience-first.md) | Graceful degradation and recovery | `intelligent-automation-starter-kit` |
| [Governance-First](../reference-architectures/enterprise-first/governance-first.md) | Ownership and decision rights | `agent-factory-starter-kit` |
| [Privacy-First](../reference-architectures/enterprise-first/privacy-first.md) | Data minimization and deletion | `rag-starter-kit` |
| [Observability-First](../reference-architectures/enterprise-first/observability-first.md) | Traceability and debuggability | `observability-starter-kit` |
| [Evaluation-First](../reference-architectures/enterprise-first/evaluation-first.md) | Measured quality gates | `evaluation-starter-kit` |
| [Ethics-First](../reference-architectures/enterprise-first/ethics-first.md) | Fairness and societal impact | `evaluation-starter-kit` |
| [Explainability-First](../reference-architectures/enterprise-first/explainability-first.md) | Inspectable decisions | `rag-starter-kit` |
| [Accessibility-First](../reference-architectures/enterprise-first/accessibility-first.md) | Inclusive design | `copilot-starter-kit` |
| [Sustainability-First](../reference-architectures/enterprise-first/sustainability-first.md) | Energy and carbon constraints | `training-starter-kit` |
| [Safety-First](../reference-architectures/enterprise-first/safety-first.md) | Harm prevention | `physical-ai-starter-kit` |
| [Interoperability-First](../reference-architectures/enterprise-first/interoperability-first.md) | Open standards and portability | `integration-starter-kit` |

See [enterprise-first/README.md](enterprise-first/README.md) for the full catalog and adoption steps.

---

## Coverage by area

| Area | Covered by |
|---|---|
| Software / service delivery | `inference`, `evaluation`, `integration` |
| Algorithms / statistics / ML / data science | `training`, `fine-tuning`, `evaluation` |
| Integration | `integration`, `data-agent`, `intelligent-automation` |
| DevOps / platform | every kit (`Dockerfile`, Terraform, CI tests) |
| Data engineering | `rag` (ingestion), `data-agent`, `integration` |
| MLOps / LLMOps | `training`, `fine-tuning`, `evaluation`, `observability` |
| LLM / LLM inference | `inference`, `rag` |
| GenAI / RAG | `rag`, `agent`, `copilot` |
| Agentic AI / multi-agent | `agent`, `agent-factory`, `intelligent-automation` |
| Observability | `observability` (plus baseline in every kit) |
| Evals | `evaluation` (plus gate in every kit) |
| Edge AI | `edge-ai` |
| Quantum computing | `quantum` |
| Cyber security | `ai-security` (plus controls in every kit) |
| Agent factory | `agent-factory` |
| Physical AI | `physical-ai` |
| Embodied AI | `embodied-ai` |

---

## Quickstart (any kit)

```bash
git clone https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture.git
cd Enterprise-AI-Reference-Architecture/blueprints/<kit-name>

cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src uvicorn main:app --reload --port 8080

# verify
curl -s localhost:8080/health
PYTHONPATH=src pytest -q
```

Supporting infrastructure:

```bash
cd infra
terraform init
terraform plan
```

---

## Blueprint quality gates

A kit is only accepted when all of these pass:

| Gate | Requirement |
|---|---|
| **Runs** | `PYTHONPATH=src pytest -q` passes from a clean checkout |
| **Valid IaC** | `terraform validate` passes |
| **No secrets** | No keys or real credentials in code or `.env.example` |
| **Gateway-only model access** | No provider SDK keys in application code (AI kits) |
| **Guardrails visible** | Input screening, redaction, and tenant scoping present |
| **Evaluation hook** | A documented path to run evals in CI with explicit thresholds |
| **Observability** | Correlation ID and stage-level tracing documented |
| **Ownership** | Status, owner, last-reviewed date, and cost note present |
| **Standards mapped** | Links to the reference architecture, lifecycles, and controls |

---

## Using a kit

1. **Pick the closest kit** from the catalog — do not start from a blank repository.
2. **Read its architecture diagram** and confirm the shape matches your problem.
3. **Replace `src/pipeline.py`** with the real pipeline, keeping the request/response contract.
4. **Wire the evaluation harness** and set thresholds before the first deploy.
5. **Fill the PR checklist**; record any deviation as an [ADR](../adr/README.md).
6. **Register the workload** (owner, cost budget, on-call) before production traffic.

## Adding or changing a kit

1. One concern per PR; state the change type (src / infra / guardrails / eval / docs).
2. Update the kit README **and** this catalog in the same PR.
3. If a standard changes, update every affected kit in the same PR.
4. New kits must pass the quality gates above and include a working smoke test.
5. Reviewer routing: 1 engineering reviewer; +1 security reviewer for guardrail,
   tool, permission, or egress changes; +1 architecture reviewer for new kits.

---

## Roadmap

| Item | Status |
|---|---|
| Core reference-architecture kits (8) | ✅ Complete |
| Specialized domain kits (5) | ✅ Complete |
| Cross-cutting kits (4) | ✅ Complete |
| Shared Terraform modules (network, gateway, observability) | Planned |
| Generated kits from the agent factory | Planned |
| Automated conformance checks (policy-as-code) | Planned |
| Kit upgrade tooling when standards change | Planned |

---

## Related

- [Reference architectures](../reference-architectures/README.md)
- [Lifecycles](../lifecycles/README.md)
- [Design patterns](../design-patterns/README.md)
- [Production issues](../production-issues/README.md)
- [AI security controls](../security/ai-security-controls.md)
- [Design review checklist](../docs/design-review-checklist.md)
- [Architect career resources](../resources/README.md)

---

*Blueprint catalog version 2.0.0 · Last updated: 2026-10-21*
