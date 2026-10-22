# Training Starter Kit

**Status:** Scaffolded · **Reference architecture:** [Training](../../reference-architectures/training/README.md) · **Owner:** platform engineering · **Last reviewed:** 2026-10-21

## What it is

A reproducible training pipeline: validated inputs, versioned datasets and code, experiment tracking, evaluation gates, and registration of an immutable model artifact.

## When to use it

Use when you are building or retraining a model and need reproducibility, lineage, and a gate before anything reaches serving.

## Architecture

```mermaid
flowchart TB
    D[(Versioned dataset)] --> V[Validate schema + quality + leakage]
    V -->|fail| Q[Quarantine + alert]
    V -->|pass| T[Train with pinned code + config]
    T --> TR[Experiment tracking]
    TR --> E[Evaluate on held-out + out-of-time]
    E -->|fail| I[Iterate]
    E -->|pass| R[Register model + lineage + model card]
    R --> A[Approval gate by risk tier]
    A --> S[Serving handoff]
```

## What's in the box

| Path | Purpose |
|---|---|
| `src/main.py` | FastAPI service: health, input screening, run endpoint |
| `src/pipeline.py` | The pipeline stub — replace this with the real implementation |
| `src/guardrails.py` | Local input screening and PII redaction (defense in depth) |
| `tests/test_smoke.py` | Smoke tests wired for CI |
| `infra/` | Terraform: artifact bucket, KMS key, log group |
| `Dockerfile` | Non-root container image |
| `.github/PULL_REQUEST_TEMPLATE.md` | Pre-filled production checklist |
| `.env.example` | Configuration contract — never commit real values |

## Quickstart

```bash
cd blueprints/training-starter-kit
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src uvicorn main:app --reload --port 8080
```

```bash
curl -s localhost:8080/health
curl -s -X POST localhost:8080/v1/run \
  -H 'content-type: application/json' \
  -d '{"input": "smoke test", "tenant_id": "demo"}'
```

Run the tests:

```bash
PYTHONPATH=src pytest -q
```

Provision the supporting infrastructure:

```bash
cd infra
terraform init
terraform plan
```

> The service returns a `scaffold` status until you replace `run_pipeline()`.

## Pipeline steps to implement

1. Snapshot and validate the dataset; check leakage and label quality.
2. Pin code, config, and environment for the run.
3. Train and log parameters, metrics, and artifacts.
4. Evaluate on held-out and out-of-time data, including subgroups.
5. Register the artifact with lineage and a model card.

## Tech stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Data | Versioned snapshots with point-in-time correctness | No training on drifting live tables |
| Training | Pinned code, config, and environment | Reproducible runs or it did not happen |
| Tracking | Experiment tracker + artifact store | Metrics, params, and data hash per run |
| Registry | Immutable model artifact + lineage | Rollback and audit |
| Delivery | FastAPI + uvicorn | One service shape across every kit; swap the pipeline, keep the contract |
| Observability | OpenTelemetry + structured JSON logs | Correlation ID per request; stage-decomposed traces |
| IaC | Terraform | Artifact bucket, KMS key, and log group with encryption and lifecycle rules |
| Tests | pytest + FastAPI TestClient | Smoke tests run in CI before any deployment |

## Security and guardrails

- Dataset access follows least privilege and retention policy.
- PII and sensitive attributes handled per policy before training.
- No promotion without an evaluation gate and recorded approval.
- Model card documents intended use and limitations.

Authoritative controls live in [AI security controls](../../security/ai-security-controls.md) and the [secure SDLC](../../security/secure-sdlc.md). The local screen in `src/guardrails.py` is a heuristic only — it is not a security control.

## Evaluation

- Task metrics plus calibration and subgroup performance.
- Comparison against the current production baseline.
- Reproducibility check: re-run from the recorded config.

Wire the harness into CI using [evaluation in CI](../../design-patterns/evaluation-in-ci.md). A behavior change without an evaluation gate does not ship.

## Operations

- **SLO:** Reproducible runs; every registered model traceable to data and code.
- **Cost:** Track GPU hours per run and cost per registered model.
- **Traces:** one correlation ID per request, stage spans around every external call.
- **Runbook:** add alert → diagnosis → mitigation before the first production deploy.

## Production checklist

- [ ] Pipeline stub replaced and covered by tests
- [ ] All model calls go through the AI gateway (no provider keys in code)
- [ ] Input screening, PII redaction, and tenant scoping verified
- [ ] Evaluation harness runs in CI with explicit thresholds
- [ ] Dashboards and alerts created; correlation IDs visible end to end
- [ ] Terraform applied to a non-production account; state is remote and locked
- [ ] Rollback and kill switch tested
- [ ] Owner, on-call rotation, and cost budget recorded in the workload registry
- [ ] Design review checklist completed or deviations recorded as an ADR

## Extension points

- Automated retraining triggers from drift and delayed ground truth.
- Feature-store integration for point-in-time correctness.
- Cost-aware hyperparameter search.

## Related

- [Reference architecture: Training](../../reference-architectures/training/README.md)
- Lifecycles: [ML project lifecycle](../../lifecycles/ml-project-lifecycle.md) · [MLOps lifecycle](../../lifecycles/mlops-lifecycle.md) · [Data lifecycle](../../lifecycles/data-lifecycle.md)
- [Blueprints catalog](../README.md)
- [Production issues](../../production-issues/README.md)
- [Design patterns](../../design-patterns/README.md)

---

*Scaffold version 1.0.0 · Generated from the blueprint factory · Update this kit in the same PR as any standard it depends on.*
