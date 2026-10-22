# Quantum Computing Starter Kit

**Status:** Scaffolded · **Reference architecture:** [Inference (quantum-accelerated profile)](../../reference-architectures/inference/README.md) · **Owner:** platform engineering · **Last reviewed:** 2026-10-21

## What it is

A hybrid classical-quantum scaffold: suitability screening, circuit construction, simulation, hardware execution, and a strict classical-baseline comparison.

## When to use it

Use only for a bounded sub-problem where a classical baseline exists and quantum advantage is a testable hypothesis.

## Architecture

```mermaid
flowchart TB
    ID[Identify sub-problem] --> FS{Quantum suitable?}
    FS -->|no| CL[Document classical-only]
    FS -->|yes| AL[Select algorithm + circuit]
    AL --> SIM[Simulate]
    SIM --> BM[Benchmark vs classical baseline]
    BM -->|no advantage| CL
    BM -->|advantage| HY[Hybrid workflow]
    HY --> PRE[Classical pre-processing]
    PRE --> QC[Quantum execution]
    QC --> POST[Classical post-processing]
    POST --> EV[Evaluate quality + cost]
    EV -->|pass| PR[Operational pipeline]
    EV -->|fail| IT[Iterate or sunset]
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
cd blueprints/quantum-starter-kit
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

1. Screen the sub-problem for quantum suitability.
2. Implement the algorithm and validate on a simulator.
3. Benchmark against the strongest classical baseline.
4. Run on hardware only after simulator evidence.
5. Measure end-to-end hybrid latency and cost before adoption.

## Tech stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Screening | Explicit suitability gate | Optimization, sampling, or linear algebra only |
| SDK | Provider SDK (Qiskit, Cirq, Braket) | Circuit portability where possible |
| Execution | Simulator first, hardware second | Multiple shots; report confidence intervals |
| Baseline | Best classical implementation | No claim without a measured comparison |
| Delivery | FastAPI + uvicorn | One service shape across every kit; swap the pipeline, keep the contract |
| Observability | OpenTelemetry + structured JSON logs | Correlation ID per request; stage-decomposed traces |
| IaC | Terraform | Artifact bucket, KMS key, and log group with encryption and lifecycle rules |
| Tests | pytest + FastAPI TestClient | Smoke tests run in CI before any deployment |

## Security and guardrails

- Hard budget cap on hardware time and shots.
- No production dependency on unproven quantum advantage.
- Classical fallback always available.
- Document negative results; they are valuable.

Authoritative controls live in [AI security controls](../../security/ai-security-controls.md) and the [secure SDLC](../../security/secure-sdlc.md). The local screen in `src/guardrails.py` is a heuristic only — it is not a security control.

## Evaluation

- Statistical significance of any claimed advantage.
- Simulator-to-hardware consistency.
- Total hybrid latency and cost versus classical.

Wire the harness into CI using [evaluation in CI](../../design-patterns/evaluation-in-ci.md). A behavior change without an evaluation gate does not ship.

## Operations

- **SLO:** Research-grade: bounded spend, reproducible experiments.
- **Cost:** Track hardware time, queue latency, and engineering cost per experiment.
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

- Problem-specific encodings and error mitigation.
- Hardware-aware circuit optimization.
- Classical-quantum workload orchestration.

## Related

- [Reference architecture: Inference (quantum-accelerated profile)](../../reference-architectures/inference/README.md)
- Lifecycles: [Quantum computing lifecycle](../../lifecycles/quantum-computing-lifecycle.md) · [Technology lifecycle](../../lifecycles/technology-lifecycle.md) · [Evaluation lifecycle](../../lifecycles/evaluation-lifecycle.md)
- [Blueprints catalog](../README.md)
- [Production issues](../../production-issues/README.md)
- [Design patterns](../../design-patterns/README.md)

---

*Scaffold version 1.0.0 · Generated from the blueprint factory · Update this kit in the same PR as any standard it depends on.*
