# Data Agent Starter Kit

**Status:** Scaffolded · **Reference architecture:** [Data agent](../../reference-architectures/data-agent/README.md) · **Owner:** platform engineering · **Last reviewed:** 2026-10-21

> **Implementation boundary:** architecture diagrams and pipeline steps describe intended behavior. The shipped pipeline is a stub; callers are not authenticated, request `tenant_id` is caller-supplied, and regex screening/redaction is illustrative. Implement identity, authorization, workload logic, evaluation, and operational controls before exposing the service. Use synthetic or explicitly authorized data. A copied `.env` file is not loaded automatically.

## What it is

A natural-language analytics service grounded in a governed semantic layer: ambiguity detection, query synthesis against metric definitions, policy injection, and answers that always show the definition used.

## When to use it

Use when business users need numbers from governed data and conflicting metric definitions are the main trust problem.

## Architecture

```mermaid
flowchart TB
    Q[Business question] --> AM{Ambiguous?}
    AM -->|yes| CL[Clarify]
    AM -->|no| SR[Retrieve metrics + schema]
    SL[(Semantic layer)] --> SR
    SR --> QS[Synthesize query]
    QS --> PV[Validate + inject row/column policy]
    PV --> EX[Execute on governed platform]
    EX --> GR[Ground answer in result + definition]
    GR --> ANS[Answer + definition + drill-down]
    ANS --> FB[Feedback -> regression set]
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
cd blueprints/data-agent-starter-kit
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

1. Detect ambiguity and ask a clarifying question when confidence is low.
2. Retrieve only relevant metrics, dimensions, and joins from the semantic layer.
3. Synthesize a query against governed definitions; never invent a metric.
4. Validate and inject the caller's row/column policy before execution.
5. Return the answer with definition, filters, and time window.

## Tech stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Semantic layer | Governed metrics, dimensions, joins as code | The architectural keystone; one definition reused by BI and AI |
| Policy | Identity propagation + row/column security | No agent superuser; negative tests for denial |
| Execution | Governed warehouse with scan/cost limits | Timeouts and query budgets |
| Evaluation | Question to expected result pairs | Two layers: query correctness and answer correctness |
| Delivery | FastAPI + uvicorn | One service shape across every kit; swap the pipeline, keep the contract |
| Observability | OpenTelemetry + structured JSON logs | Correlation ID per request; stage-decomposed traces |
| IaC | Terraform | Artifact bucket, KMS key, and log group with encryption and lifecycle rules |
| Tests | pytest + FastAPI TestClient | Smoke tests run in CI before any deployment |

## Security and guardrails

- Identity propagated end to end; the agent never runs as a superuser.
- Undefined metrics return an explicit not-defined path, not an improvised calculation.
- Query cost and scan ceilings enforced before execution.
- No raw table access for the default path.

Authoritative controls live in [AI security controls](../../security/ai-security-controls.md) and the [secure SDLC](../../security/secure-sdlc.md). The local screen in `src/guardrails.py` is a heuristic only — it is not a security control.

## Evaluation

- Golden question to expected result pairs per domain.
- Unauthorized-access attempts must be denied and logged.
- Definition-change regression: re-run evals when the semantic layer changes.

Wire the harness into CI using [evaluation in CI](../../design-patterns/evaluation-in-ci.md). A behavior change without an evaluation gate does not ship.

## Operations

- **SLO:** Answer latency within the analytics UX budget; zero policy bypasses.
- **Cost:** Cache common metrics; cap scans per query; alert on cost outliers.
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

- Anomaly-aware answers with statistical context.
- Multi-step analysis with human-approved query plans.
- Automated metric onboarding with governance review.

## Related

- [Reference architecture: Data agent](../../reference-architectures/data-agent/README.md)
- Lifecycles: [Data lifecycle](../../lifecycles/data-lifecycle.md) · [Evaluation lifecycle](../../lifecycles/evaluation-lifecycle.md) · [Model risk lifecycle](../../lifecycles/model-risk-lifecycle.md)
- [Blueprints catalog](../README.md)
- [Production issues](../../production-issues/README.md)
- [Design patterns](../../design-patterns/README.md)

---

*Scaffold version 1.0.0 · Generated from the blueprint factory · Update this kit in the same PR as any standard it depends on.*
