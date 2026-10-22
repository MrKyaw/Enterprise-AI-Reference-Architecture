# inference-starter-kit

> Scaffolded inference deployment with AI gateway, guardrails, and eval-in-CI.

## Quickstart

```bash
git clone https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture.git
cd Enterprise-AI-Reference-Architecture/blueprints/inference-starter-kit
terraform init
terraform apply
cd src
pip install -r requirements.txt
uvicorn main:app --reload
```

## Directory Structure

```
inference-starter-kit/
├── infra/          # Terraform baseline deployment
│   ├── main.tf
│   ├── vpc.tf
│   ├── gateway.tf
│   └── outputs.tf
├── src/            # Sample FastAPI service
│   ├── __init__.py
│   ├── main.py
│   ├── guardrails.py
│   └── requirements.txt
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── .env.example
├── README.md
└── .gitignore
```

## Architecture

This blueprint implements the [inference reference architecture](../../reference-architectures/inference/README.md):

- AI Gateway with egress allowlists
- Guardrails for input/output filtering
- Least-privilege credentials via vault
- Observability with correlation IDs
- Canary deployment via feature flags

## Cost Estimate

| Component | Monthly (~1M requests) |
|---|---|
| Gateway overhead | $150 |
| Model inference (mix of cheap/strong) | $800 |
| Guardrails processing | $50 |
| **Total** | **~$1,000** |

## Security

- All model traffic transits the AI gateway (control AI-1)
- No provider keys in application code
- PII redaction before prompt assembly
- See [ai-security-controls.md](../../security/ai-security-controls.md)

## Evaluation

Eval-in-CI configured with [evaluation-in-ci pattern](../../design-patterns/evaluation-in-ci.md):

```bash
pytest tests/ -k "inference"
```

## Quickstart Script

```bash
./scripts/quickstart.sh
```

## Troubleshooting

Common issues:
- ` gateway unreachable` — check VPC endpoint and security groups
- `guardrails blocking` — review PII patterns in `guardrails.py`
- `authentication failed` — verify `.env.example` variables