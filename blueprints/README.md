# Blueprint Starter Kits

> Each blueprint provides a scaffolded project structure with working code, IaC, guardrails pre-wired, and a pre-filled design review checklist — so engineering teams can start a compliant AI workload without central involvement.

## Available Blueprints

| Blueprint | Target RA | Status |
|---|---|---|
| inference-starter-kit | [Inference](../reference-architectures/inference/README.md) | Scaffolded |
| rag-starter-kit | [RAG](../reference-architectures/rag/README.md) | Scaffolded |
| agent-starter-kit | [Agentic](../reference-architectures/agentic/README.md) | Scaffolded |
| data-agent-starter-kit | [Data agent](../reference-architectures/data-agent/README.md) | Scaffolded |
| copilot-starter-kit | [Copilots](../reference-architectures/copilots/README.md) | Scaffolded |

## Blueprint Structure

Each blueprint (`blueprints/{workload}-starter-kit/`) provides:

1. **Scaffolded project structure** — working skeleton code with the approved stack wired up
2. **Infrastructure-as-code** — baseline deployment for the reference architecture's component view
3. **Guardrails pre-wired** — gateway client, logging with PII redaction, eval-in-CI setup
4. **Checklist** — the [design review checklist](../docs/design-review-checklist.md) pre-filled where the blueprint already satisfies the item; the team fills the rest
5. **README quickstart** — from clone to first working deployment in under an hour

## Blueprint: inference-starter-kit

```text
blueprints/inference-starter-kit/
├── README.md          # Quickstart: clone → deploy in < 30 min
├── infra/             # Terraform for baseline deployment
│   ├── main.tf        # Provider + workspace config
│   ├── vpc.tf         # Network with gateway endpoint
│   ├── gateway.tf     # AI gateway deployment
│   └── outputs.tf     # Connection details
├── src/               # Sample inference service
│   ├── __init__.py
│   ├── main.py        # FastAPI app with gateway client
│   ├── guardrails.py  # Input/output filtering
│   └── requirements.txt
├── .github/           # PR template auto-filling checklist
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example       # Placeholder variables (never commit secrets)
├── README.md          # Quickstart guide
└── .gitignore
```

## Blueprint: rag-starter-kit

```text
blueprints/rag-starter-kit/
├── README.md
├── infra/ # Terraform for RAG deployment
│   ├── main.tf
│   ├── data.tf      # Source registry + ingestion pipeline
│   ├── index.tf     # Vector index deployment
│   └── output.tf
├── src/ # Sample RAG service
│   ├── __init__.py
│   ├── ingest.py      # Scheduled ingestion pipeline
│   ├── retrieve.py    # Hybrid retrieval
│   ├── generate.py    # Prompt assembly + guardrails
│   └── requirements.txt
├── evaluation/ # CI evaluation config
│   ├── golden_set.json
│   └── test_rag.py
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example
├── README.md
└── .gitignore
```

## Blueprint: agent-starter-kit

```text
blueprints/agent-starter-kit/
├── README.md
├── infra/ # Terraform for agent deployment
│   ├── main.tf
│   ├── agent.tf     # Agent runtime + tool registry
│   ├── memory.tf    # Scoped memory config
│   └── output.tf
├── src/ # Sample agent
│   ├── __init__.py
│   ├── agent.py       # Core loop with tool use
│   ├── tools.py       # Registered tool definitions
│   ├── memory.py      # Turn/session/semantic memory
│   └── requirements.txt
├── evaluation/ # Agent eval harness
│   ├── task_success.py
│   ├── tool_call_acc.py
│   └── trajectory.py
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example
├── README.md
└── .gitignore
```

## Blueprint: data-agent-starter-kit

```text
blueprints/data-agent-starter-kit/
├── README.md
├── infra/ # Terraform for data agent deployment
│   ├── main.tf
│   ├── semantic.tf  # Semantic layer deployment
│   ├── index.tf     # Metric/definition catalog
│   └── output.tf
├── src/ # Sample data agent
│   ├── __init__.py
│   ├── agent.py       # NL query over governed data
│   ├── metric.py      # Metric resolution + query synthesis
│   ├── eval.py        # CI evaluation harness
│   └── requirements.txt
├── evaluation/ # Golden question set
│   ├── questions.json
│   └── expected.json
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example
├── README.md
└── .gitignore
```

## Blueprint: copilot-starter-kit

```text
blueprints/copilot-starter-kit/
├── README.md
├── infra/ # Terraform for copilot deployment
│   ├── main.tf
│   ├── extension.tf # Host-app extension points
│   ├── guardrails.tf
│   └── output.tf
├── src/ # Sample copilot
│   ├── __init__.py
│   ├── chat.py        # Chat interface + context assembly
│   ├── retrieval.py   # Governed metric retrieval
│   └── requirements.txt
├── evaluation/ # Acceptance + quality metrics
│   ├── acceptance.py
│   └── quality.py
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example
├── README.md
└── .gitignore
```

## Adding a new blueprint

1. Copy the appropriate scaffold template above into `blueprints/{workload}-starter-kit/`
2. Fill in the `README.md` with project-specific quickstart steps
3. Replace placeholder infrastructure with your platform's IaC
4. Ensure the embedded checklist in `.github/PULL_REQUEST_TEMPLATE.md` reflects the applicable [design review checklist](../docs/design-review-checklist.md)
5. Open a PR — the blueprint maintainer owns the template, but teams own their scaffolded project after generation

## Rules

- Blueprints use **only** [approved technologies](../standards/approved-technologies.md); when a standard changes, the blueprint changes in the same PR
- Blueprints are opinionated: customization is fine, but removing guardrails is not
- Teams own their forked/scaffolded project after generation; blueprint maintainers own the template