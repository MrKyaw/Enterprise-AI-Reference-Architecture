# Embodied AI Starter Kit

**Status:** Scaffolded · **Reference architecture:** [Agentic (embodied profile)](../../reference-architectures/agentic/README.md) · **Owner:** platform engineering · **Last reviewed:** 2026-10-21

> **Implementation boundary:** architecture diagrams and pipeline steps describe intended behavior. The shipped pipeline is a stub; callers are not authenticated, request `tenant_id` is caller-supplied, and regex screening/redaction is illustrative. Implement identity, authorization, workload logic, evaluation, and operational controls before exposing the service. Use synthetic or explicitly authorized data. A copied `.env` file is not loaded automatically.

## What it is

A sensorimotor learning scaffold: perception to world model to policy to action, with curriculum-driven data collection, safety-bounded exploration, and skill versioning.

## When to use it

Use when an agent must learn skills through interaction in a continuous environment rather than answer a single request.

## Architecture

```mermaid
flowchart LR
    P[Perception: vision, proprioception] --> WM[World model / state estimate]
    WM --> PL[Policy / skill selection]
    PL --> AC[Action]
    AC --> ENV[(Environment)]
    ENV --> P
    AC --> SF{Safety envelope}
    SF -->|violation| ES[Emergency stop / human takeover]
    ENV --> DATA[Trajectory buffer]
    DATA --> L[Learning update]
    L --> PL
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
cd blueprints/embodied-ai-starter-kit
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

1. Define the task and embodiment constraints.
2. Build the perception and state-estimation path.
3. Choose a learning paradigm based on available demonstrations.
4. Train in simulation with a curriculum; transfer with measured gap.
5. Deploy with a safety envelope and monitor skill quality.

## Tech stack (layers, not products)

| Layer | Choice | Notes |
|---|---|---|
| Perception | Compact, robust state representation | Fuse vision, proprioception, tactile |
| World model | Belief state or latent dynamics | Needed for credit assignment over time |
| Learning | RL, imitation, or hybrid | Curriculum-driven, sample-efficient |
| Safety | Hard envelope plus human takeover | Exploration must be bounded |
| Delivery | FastAPI + uvicorn | One service shape across every kit; swap the pipeline, keep the contract |
| Observability | OpenTelemetry + structured JSON logs | Correlation ID per request; stage-decomposed traces |
| IaC | Terraform | Artifact bucket, KMS key, and log group with encryption and lifecycle rules |
| Tests | pytest + FastAPI TestClient | Smoke tests run in CI before any deployment |

## Security and guardrails

- Exploration only inside a validated safe set.
- Independent emergency stop and human takeover.
- Skill registry with versions and retirement records.
- No deployment without test-bed validation.

Authoritative controls live in [AI security controls](../../security/ai-security-controls.md) and the [secure SDLC](../../security/secure-sdlc.md). The local screen in `src/guardrails.py` is a heuristic only — it is not a security control.

## Evaluation

- Skill success rate and sample efficiency.
- Cross-embodiment transfer where applicable.
- Safety violations during training and operation.

Wire the harness into CI using [evaluation in CI](../../design-patterns/evaluation-in-ci.md). A behavior change without an evaluation gate does not ship.

## Operations

- **SLO:** Bounded safety violations; skill performance above the task threshold.
- **Cost:** Cost per real-world timestep and per skill retrain.
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

- Hierarchical skills for long-horizon tasks.
- Offline RL from prior trajectories.
- Sim-to-real with learned dynamics.

## Related

- [Reference architecture: Agentic (embodied profile)](../../reference-architectures/agentic/README.md)
- Lifecycles: [Embodied AI lifecycle](../../lifecycles/embodied-ai-lifecycle.md) · [Physical AI lifecycle](../../lifecycles/physical-ai-lifecycle.md) · [Agent lifecycle](../../lifecycles/agent-lifecycle.md)
- [Blueprints catalog](../README.md)
- [Production issues](../../production-issues/README.md)
- [Design patterns](../../design-patterns/README.md)

---

*Scaffold version 1.0.0 · Generated from the blueprint factory · Update this kit in the same PR as any standard it depends on.*
