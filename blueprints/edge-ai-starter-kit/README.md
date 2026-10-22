# Edge AI Starter Kit

**Status:** Scaffolded · **Reference architecture:** [Inference (edge profile)](../../reference-architectures/inference/README.md) · **Owner:** platform engineering · **Last reviewed:** 2026-10-21

> **Implementation boundary:** architecture diagrams and pipeline steps describe intended behavior. The shipped pipeline is a stub; callers are not authenticated, request `tenant_id` is caller-supplied, and regex screening/redaction is illustrative. Implement identity, authorization, workload logic, evaluation, and operational controls before exposing the service. Use synthetic or explicitly authorized data. A copied `.env` file is not loaded automatically.

## What it is

A conversion and deployment scaffold for on-device inference: quantize, validate the quality drop, benchmark on target hardware, ship over the air, and monitor the fleet.

## When to use it

Use when latency, bandwidth, privacy, or offline operation require inference on the device rather than in the cloud.

## Architecture

```mermaid
flowchart LR
    T[Train / select model] --> Q[Quantize + prune]
    Q --> C[Convert to target runtime]
    C --> V[Validate quality drop]
    V -->|too large| R[Redesign or retrain]
    V -->|accepted| B[Benchmark on device]
    B --> D[Sign + package]
    D --> O[OTA canary rollout]
    O --> M[Fleet telemetry]
    M -->|drift or faults| U[Rollback or retrain]
    U --> T
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
cd blueprints/edge-ai-starter-kit
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

1. Export and quantize the model; measure the quality delta on a held-out set.
2. Convert to the target runtime and load it on reference hardware.
3. Benchmark latency and power on the slowest supported device.
4. Package and sign; roll out to a canary cohort.
5. Monitor fleet quality and roll back on regression.

## Tech stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Compression | int8 first; int4 only with evidence | Quantization-aware training when needed |
| Runtime | Target-device SDK | TensorFlow Lite, ONNX Runtime, CoreML, OpenVINO |
| Update | Signed OTA with canary and rollback | Immutable device identity |
| Monitoring | Fleet latency, quality, power, faults | Per-device telemetry, aggregated dashboards |
| Delivery | FastAPI + uvicorn | One service shape across every kit; swap the pipeline, keep the contract |
| Observability | OpenTelemetry + structured JSON logs | Correlation ID per request; stage-decomposed traces |
| IaC | Terraform | Artifact bucket, KMS key, and log group with encryption and lifecycle rules |
| Tests | pytest + FastAPI TestClient | Smoke tests run in CI before any deployment |

## Security and guardrails

- Signed updates and verified boot; rollback must be tested.
- No raw user data leaves the device without explicit policy.
- Model and firmware versions pinned and inventoried.
- Hard resource limits so inference cannot starve the host function.

Authoritative controls live in [AI security controls](../../security/ai-security-controls.md) and the [secure SDLC](../../security/secure-sdlc.md). The local screen in `src/guardrails.py` is a heuristic only — it is not a security control.

## Evaluation

- Quality retention versus the cloud baseline on device.
- Latency and power on the target device, not a workstation.
- Canary versus fleet quality comparison.

Wire the harness into CI using [evaluation in CI](../../design-patterns/evaluation-in-ci.md). A behavior change without an evaluation gate does not ship.

## Operations

- **SLO:** p95 on-device latency within budget; OTA success rate within target.
- **Cost:** Cost per device update and per inference, including power.
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

- Hybrid edge-cloud fallback for hard inputs.
- Fleet learning with privacy-preserving aggregation.
- Automated device-matrix regression testing.

## Related

- [Reference architecture: Inference (edge profile)](../../reference-architectures/inference/README.md)
- Lifecycles: [Edge AI lifecycle](../../lifecycles/edge-ai-lifecycle.md) · [MLOps lifecycle](../../lifecycles/mlops-lifecycle.md) · [Technology lifecycle](../../lifecycles/technology-lifecycle.md)
- [Blueprints catalog](../README.md)
- [Production issues](../../production-issues/README.md)
- [Design patterns](../../design-patterns/README.md)

---

*Scaffold version 1.0.0 · Generated from the blueprint factory · Update this kit in the same PR as any standard it depends on.*
