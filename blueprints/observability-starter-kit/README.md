# Observability Starter Kit

**Status:** Scaffolded · **Reference architecture:** [Cross-cutting](../../reference-architectures/README.md) · **Owner:** platform engineering · **Last reviewed:** 2026-10-21

## What it is

An observability baseline for AI services: OpenTelemetry traces across retrieval and generation, token and cost metrics, quality sampling, SLOs, and alerts that page on user impact.

## When to use it

Use for every AI workload before production; especially where quality decay is invisible to uptime monitoring.

## Architecture

```mermaid
flowchart LR
    APP[AI service] --> OT[OpenTelemetry SDK]
    OT --> COL[Collector]
    COL --> TR[(Traces)]
    COL --> ME[(Metrics)]
    COL --> LO[(Logs)]
    TR --> DASH[Dashboards]
    ME --> DASH
    LO --> DASH
    DASH --> SLI[SLIs + SLOs]
    SLI --> AL[Alerts]
    Q[Quality sampling] --> DASH
    AL --> IR[Incident response]
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
cd blueprints/observability-starter-kit
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

1. Instrument every request with a correlation ID and stage spans.
2. Emit token, cost, and latency metrics per stage.
3. Sample requests for offline quality evaluation.
4. Define SLIs and SLOs, including a quality SLO.
5. Alert on burn rate, not raw thresholds.

## Tech stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Instrumentation | OpenTelemetry traces, metrics, logs | Correlation ID propagated end to end |
| Backend | Collector plus your existing observability stack | Avoid per-vendor SDKs in application code |
| Quality | Sampled evaluation of real traffic | Uptime is not quality |
| SLOs | Latency, error rate, quality, cost | Alerts tied to user impact |
| Delivery | FastAPI + uvicorn | One service shape across every kit; swap the pipeline, keep the contract |
| Observability | OpenTelemetry + structured JSON logs | Correlation ID per request; stage-decomposed traces |
| IaC | Terraform | Artifact bucket, KMS key, and log group with encryption and lifecycle rules |
| Tests | pytest + FastAPI TestClient | Smoke tests run in CI before any deployment |

## Security and guardrails

- Redact PII at the logging boundary.
- No raw prompts or documents in logs by default.
- Access to traces follows least privilege.
- Retention aligned with privacy policy.

Authoritative controls live in [AI security controls](../../security/ai-security-controls.md) and the [secure SDLC](../../security/secure-sdlc.md). The local screen in `src/guardrails.py` is a heuristic only — it is not a security control.

## Evaluation

- Trace completeness across stages.
- Alert precision and time to detect a seeded failure.
- Quality SLO coverage per workload.

Wire the harness into CI using [evaluation in CI](../../design-patterns/evaluation-in-ci.md). A behavior change without an evaluation gate does not ship.

## Operations

- **SLO:** Every request traceable; quality and cost visible alongside latency.
- **Cost:** Observability spend tracked as a platform cost per workload.
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

- Cost attribution by tenant and feature.
- Automated drift detection from sampled quality.
- SLO dashboards published to consuming teams.

## Related

- [Reference architecture: Cross-cutting](../../reference-architectures/README.md)
- Lifecycles: [Operations & incident lifecycle](../../lifecycles/operations-incident-lifecycle.md) · [MLOps lifecycle](../../lifecycles/mlops-lifecycle.md) · [FinOps cost lifecycle](../../lifecycles/finops-cost-lifecycle.md)
- [Blueprints catalog](../README.md)
- [Production issues](../../production-issues/README.md)
- [Design patterns](../../design-patterns/README.md)

---

*Scaffold version 1.0.0 · Generated from the blueprint factory · Update this kit in the same PR as any standard it depends on.*
