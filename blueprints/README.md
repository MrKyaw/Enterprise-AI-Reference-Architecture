# Blueprints & Starter Kits

**Status:** Developer Preview · **Last reviewed:** 2026-10-19

Ready-to-scaffold project templates that let engineering teams start a compliant AI workload **without central involvement**, per the matching reference architecture.

## Philosophy

**Blueprints are not just documentation — they are runnable scaffolds.** Each blueprint provides:
- **Scaffolded project structure** — working skeleton code with the approved stack wired up
- **Infrastructure-as-code** — baseline deployment for the reference architecture's component view
- **Guardrails pre-wired** — gateway client, logging with PII redaction, eval-in-CI setup
- **Checklist** — the [design review checklist](../docs/design-review-checklist.md) pre-filled where the blueprint already satisfies the item; the team fills the rest
- **README quickstart** — from clone to first working deployment in under an hour

## Philosophy: "The compliant path must be the fast path"

Central architecture should not be a bottleneck. Blueprints make the compliant path the **fast path** by providing:
- Pre-approved technology stacks from [`standards/approved-technologies.md`](standards/approved-technologies.md)
- Pre-configured guardrails from [`security/ai-security-controls.md`](security/ai-security-controls.md)
- Pre-configured evaluation harnesses from [`evaluation-in-ci](../design-patterns/evaluation-in-ci.md)`
- Pre-configured guardrail sandwich from [`genai-prompting](../design-patterns/genai-prompting.md)`

## Available Blueprints

| Blueprint | Target RA | Status | Tech Stack |
|---|---|---|---|
| `inference-starter-kit` | [Inference](../reference-architectures/inference/README.md) | ✅ Scaffolded | FastAPI + Terraform + gateway |
| `rag-starter-kit` | [RAG](../reference-architectures/rag/README.md) | ✅ Scaffolded | LangChain + Pinecone/Weaviate + evaluation |
| `agent-starter-kit` | [Agentic](../reference-architectures/agentic/README.md) | ⚠️ In progress | AutoGen + tool registry + sandbox |
| `data-agent-starter-kit` | [Data agent](../reference-architectures/data-agent/README.md) | ⚠️ In progress | Semantic layer + query synthesis |
| `copilot-starter-kit` | [Copilots](../reference-architectures/copilots/README.md) | ⚠️ In progress | Host-embedded extension + context assembly |

## Blueprint: inference-starter-kit

### Quickstart

```bash
git clone https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture.git
cd Enterprise-AI-Reference-Architecture/blueprints/inference-starter-kit
terraform init
terraform apply
cd src
pip install -r requirements.txt
uvicorn main:app --reload
```

### Directory Structure

```
inference-starter-kit/
├── infra/              # Terraform baseline deployment
│   ├── main.tf         # Provider + workspace config
│   ├── vpc.tf          # Network with gateway endpoint
│   ├── gateway.tf      # AI gateway deployment (private ALB)
│   └── outputs.tf      # Connection details
├── src/                # Sample FastAPI service
│   ├── __init__.py
│   ├── main.py         # Main app with gateway client + guardrails
│   ├── guardrails.py   # Input/output filtering
│   └── requirements.txt
├── .github/            # PR template auto-filling checklist
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example        # Placeholder variables (never commit)
├── README.md           # Quickstart guide
└── .gitignore
```

### Architecture

This blueprint implements the [inference reference architecture](../reference-architectures/inference/README.md):

```mermaid
flowchart TB
    subgraph Client [Client Apps]
        U[User / Front-end]
    end
    subgraph Gateway [AI Gateway]
        GW[Auth + Rate Limits]
        GR[Guardrails (input/output)]
        RW[Router + Routing]
    end
    subgraph infra [Deployed Infrastructure]
        direction TB
        VPC[VPC / Network]
        GW_endp[AI Gateway Endpoint]
        M[Model Provider]
        FW[Firewall / DLP]
    end
    U -->|HTTPS| GW_endp
    GW_endp --> GR
    GR --> RW
    RW --> M
    M -->|response| GR
    GR --> GW_endp
    GW_endp -->|decision| VPC
```

### Tech Stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Ingestion | N/A (gateway-mediated) | No direct provider SDK in application code |
| Serving | AI Gateway + model provider | Gateway mediates all traffic |
| Safety | Guardrails service | Fail-closed; input/output filtering |
| Delivery | FastAPI + uvicorn | Standard Python web framework |
| Observability | Correlation IDs + stage-decomposed tracing | Every request traced through gateway |
| Cost | Per-request tagging + budget alarms | Attribution via gateway |

### Security

- All model traffic transits the AI gateway (control AI-1)
- No provider keys in application code
- PII redaction before prompt assembly
- See [ai-security-controls.md](../security/ai-security-controls.md)

### Evaluation

Eval-in-CI configured with [evaluation-in-CI pattern](../design-patterns/evaluation-in-ci.md):

```bash
pytest tests/ -k "inference"
```

### Cost Estimate

| Component | Monthly (~1M requests) |
|---|---|
| Gateway overhead | $150 |
| Model inference (mix of cheap/strong) | $800 |
| Guardrails processing | $50 |
| **Total** | **~$1,000** |

### Troubleshooting

Common issues:
- `gateway unreachable` — check VPC endpoint and security groups
- `guardrails blocking` — review PII patterns in `guardrails.py`
- `authentication failed` — verify `.env.example` variables

### Pull Request Checklist

- [ ] One concern per PR; title states the change type (infra / src / guardrails / eval)
- [ ] Blueprint changes linked from blueprints/README.md
- [ ] Naming conventions followed (kebab-case; env vars UPPERCASE)
- [ ] Blueprint satisfies applicable items in [design-review-checklist.md](../docs/design-review-checklist.md); remaining items filled
- [ ] Evaluation in CI configured with explicit thresholds

## Reviewer routing (see CONTRIBUTING.md for required reviewers)

- [ ] Infrastructure changes — 1 infrastructure reviewer
- [ ] Code/guardrails changes — 1 engineering reviewer + 1 security reviewer
- [ ] New blueprint — blueprint maintainer + 1 architecture team reviewer

## Evidence (required for blueprint changes)

- [ ] Terraform plan output linked
- [ ] Evaluation harness results linked
- [ ] No secrets in .env or code

---

## Adding a new blueprint

1. Copy the appropriate scaffold template into `blueprints/{workload}-starter-kit/`
2. Fill in the `README.md` with project-specific quickstart steps
3. Replace placeholder infrastructure with your platform's IaC
4. Ensure the embedded checklist in `.github/PULL_REQUEST_TEMPLATE.md` reflects the applicable [design review checklist](../docs/design-review-checklist.md)
5. Open a PR — the blueprint maintainer owns the template, but teams own their scaffolded project after generation

## Blueprint design principles

- **Opinionated but extensible** — pre-approved stack, but customization points exist
- **Guardrails by default** — removing guardrails requires explicit approval
- **IaC first** — all infrastructure is code; no click-ops in production
- **Team-owned after generation** — blueprint maintainers own the template; teams own their scaffolded project
- **Standards-aligned** — when a standard changes, the blueprint changes in the same PR

---

## Blueprint Roadmap

| Blueprint | Target RA | ETA |
|---|---|---|
| inference-starter-kit | [Inference](../reference-architectures/inference/README.md) | ✅ Complete |
| rag-starter-kit | [RAG](../reference-architectures/rag/README.md) | Q1 2027 |
| agent-starter-kit | [Agentic](../reference-architectures/agentic/README.md) | Q2 2027 |
| data-agent-starter-kit | [Data agent](../reference-architectures/data-agent/README.md) | Q2 2027 |
| copilot-starter-kit | [Copilots](../reference-architectures/copilots/README.md) | Q3 2027 |

## Blueprint examples (diagrams)

### inference-starter-kit architecture diagram

```mermaid
flowchart TB
    subgraph Client [Client Apps]
        U[User / Front-end]
    end
    subgraph Gateway [AI Gateway (managed)]
        GW[Auth + Rate Limits]
        GR[Guardrails (input/output)]
        RW[Router + Routing]
    end
    subgraph infra [Deployed Infrastructure]
        direction TB
        VPC[VPC / Network]
        GW_endp[AI Gateway Endpoint (private ALB)]
        M[Model Provider (e.g., OpenAI, Anthropic, Cohere)]
        FW[Firewall / DLP]
    end
    U -->|HTTPS| GW_endp
    GW_endp --> GR
    GR --> RW
    RW --> M
    M -->|token-cost| GR
    GR --> GW_endp
    GW_endp -->|decision| VPC
```

### RAG starter kit architecture diagram

```mermaid
flowchart TB
    subgraph Ingest [Scheduled Ingest]
        S[(Sources: docs, wiki, tickets)] --> EX[Extract & clean]
        EX --> CH[Chunk per content type]
        CH --> MD[Attach metadata: source, date, ACL tags]
        MD --> EM[Embed (versioned model)]
        EM --> IX[(Hybrid index: vector + keyword)]
    end
    subgraph Serve [Query pipeline - per request]
        U[User question] --> QP[Query rewrite + filters]
        QP --> RT[Hybrid retrieval + ACL filter]
        IX --> RT
        RT --> RR[Rerank top-k]
        RR --> AS[Prompt assembly with citations]
        AS --> MDL[Model via gateway + guardrails]
        MDL --> ANS[Answer with citations]
    end
```

### Agent starter kit architecture diagram

```mermaid
flowchart LR
    subgraph Agent [Agent Runtime]
        A[Agent Loop]
        A --> T[Tool Registry]
        T -->|authorize| C[Tool Calls]
        C --> E[Execute (API / DB / UI)]
        E -->|result| A
    end
    subgraph Controls [Safety Controls]
        SC[Side-effect classification]
        AK[Authorization Boundary]
        KS[Kill Switch]
    end
    A -->|classify| SC
    A -->|boundary check| AK
    A -->|exceeds limits| KS
    subgraph Memory [Memory Layer]
        M[Turn-scoped / Session-scoped]
    end
    A --> M
```

---

## Blueprint Quality Gates

Every blueprint must pass these gates before acceptance:

| Gate | Requirement | Artifact |
|---|---|---|
| **Security** | All model traffic via gateway; no provider keys in code | `security/ai-security-controls.md` mapping |
| **Evaluation** | Eval-in-CI passes with thresholds | [evaluation-in-CI](../design-patterns/evaluation-in-ci.md) |
| **Observability** | Correlation IDs, cost attribution, quality sampling | Trace configuration |
| **Compliance** | Status, owner, last-reviewed date set | Metadata in blueprint README |
| **Standards** | Uses only approved technologies | [`standards/approved-technologies.md`](../standards/approved-technologies.md) |

---

## Community blueprints (external, not maintained)

| Name | Description | Link |
|---|---|---|
| `community/rag-experiment` | Community experiment with LlamaIndex + Pinecone | (external) |
| `community/agent-demo` | Demo of AutoGen agent workflow | (external) |

*External blueprints are not maintained by the architecture team. Use at your own risk and evaluate against [standards](../standards/approved-technologies.md).*

---

## migrating between blueprints

If your needs change, you can migrate between blueprints by:

1. **Importing data** from the old blueprint's data store
2. **Re-running the evaluation harness** to compare quality
3. **Updating the tech stack** via the [tech migration guide](../standards/tech-migration.md) (work in progress)
4. **Updating ADRs** to reflect the new architecture decision

---

## migrating from a blueprint to a custom build

As your team matures, you may want to move from a blueprint to a fully custom build. The transition path is:

1. **Fork the blueprint** and remove opinionated components
2. **Replace IaC** with your platform's native tools
3. **Migrate guardrails** to your existing security pipeline
4. **Update evaluation harness** to your custom metrics
5. **Document the migration** as an [ADR](../adr/README.md) for future reference

---

## Code of Conduct

All blueprint contributors and users are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md). Violations should be reported via the GitHub Security Advisory channel.

---
*Blueprint version: 2.0.0 — Last updated: 2026-10-19*