# Testing Strategy

**Status:** Proposed · **Last reviewed:** 2026-10-17

Test types, where they apply, and how AI systems extend the classical pyramid. Complements [evaluation lifecycle](../lifecycles/evaluation-lifecycle.md) — **tests verify determinism, evaluation measures quality**; AI systems need both.

## Test pyramid (classical software)

```
        /\        Few, slow, expensive
       /  \       E2E / UI / journey tests
      /----\      Integration & contract tests
     /------\     Unit tests (many, fast, cheap)
    /--------\    Static analysis, lint, type checks
```

| Level | Verifies | Notes |
|---|---|---|
| Static analysis / lint / types | Correctness-adjacent defects, style, security smells | Cheapest gate; run on every commit |
| Unit tests | Single unit behavior in isolation | Fast; mock external boundaries |
| Integration tests | Component wiring with real dependencies | Use containers/emulators over mocks where feasible |
| Contract tests | Provider/consumer agreement (APIs, tool contracts) | Consumer-driven; critical for agent tools and AI gateway |
| End-to-end tests | Full user journey | Few; highest signal per run, highest cost |

## Test types catalog

| Type | Purpose |
|---|---|
| **Unit** | Logic correctness in isolation |
| **Integration** | Components work together |
| **Contract** | Interface agreement honored by both sides |
| **Component** | A service tested in isolation with real I/O boundaries |
| **End-to-end** | Business journey works across the whole system |
| **Smoke** | Deployed system is minimally functional |
| **Regression** | Previously fixed issues stay fixed |
| **Acceptance / BDD** | Business scenarios satisfied |
| **Property-based** | Invariants hold for generated inputs |
| **Mutation** | Test suite actually detects injected faults |
| **Fuzz** | Robustness against malformed input |
| **Performance / load** | Latency and throughput under expected/peak load |
| **Soak / endurance** | Stability over long runs (memory leaks, index growth) |
| **Chaos / fault injection** | Behavior under dependency failure |
| **Security (SAST/DAST/SCA/secrets)** | Vulnerabilities in code, deps, and runtime |
| **Penetration / red-team** | Adversarial human-driven attack testing |
| **Accessibility** | Usability for assistive technology users |
| **Data quality tests** | Freshness, completeness, schema, distribution |
| **Visual/UI regression** | Rendering stability (human-facing apps) |
| **Compatibility** | Host-app/version matrix (copilots, embedded AI) |
| **Migration/upgrade** | State survives version transitions |

## AI-specific test & evaluation layers

| Layer | What it verifies | Type |
|---|---|---|
| **Model evaluation** | Quality against golden/adversarial sets | Evaluation ([lifecycle](../lifecycles/evaluation-lifecycle.md)) |
| **Prompt regression** | Prompt version doesn't degrade behavior | Evaluation in CI |
| **Retrieval evaluation** | Hit rate, recall@k, MRR, filter correctness | Evaluation |
| **Grounding/faithfulness** | Answers supported by evidence; citations valid | Evaluation + human review |
| **Tool-call tests** | Right tool, right args, unauthorized rejected | Deterministic (mock the model) + evaluation |
| **Guardrail tests** | Filters perform as specified | Deterministic per rule + adversarial set |
| **Injection suites** | Resistance to known injection patterns | Adversarial evaluation |
| **Trajectory tests** | Agent reached the goal without unsafe steps | Evaluation over traces |
| **Bounded-autonomy tests** | Step/cost/time ceilings enforced | Deterministic |
| **Approval-gate tests** | Write/irreversible actions cannot bypass HITL | Deterministic + negative tests |
| **Permission/ACL tests** | Unauthorized retrieval or action denied | Negative tests (prove denial) |
| **Drift tests** | Monitoring fires on synthetic drift | Monitoring verification |
| **Cost tests** | Budget ceilings and attribution work | Deterministic + instrumentation |
| **Fallback tests** | Degradation ladder rungs function | Chaos/game-day |
| **Non-determinism handling** | Same input acceptable-output ranges | Sampled runs with tolerances |

## Making non-deterministic tests trustworthy

| Technique | Use |
|---|---|
| Mock the model at unit level | Test your logic deterministically; don't test the provider |
| Fixed seeds & pinned model versions | Reduce variance in evaluation |
| Property/range assertions | Assert acceptable bounds instead of exact text |
| N-sample consensus thresholds | e.g., "≥ 9/10 runs pass criteria" |
| Frozen recordings (cassettes) | Deterministic replay for integration tests |
| Judge calibration | Validate automated judging against humans |
| Flake quarantine policy | Time-boxed; flaky tests get fixed or deleted, never ignored |

## Coverage expectations

| System tier | Requirement |
|---|---|
| Low risk | Unit + integration + evaluation; contract tests for interfaces |
| Medium risk | Above + E2E for key journeys, performance test, security scan, drift test |
| High risk | Above + negative access tests, adversarial suite, chaos/game-day, red-team, human review sample |

Treat coverage as a signal, not a target — mutation testing reveals whether tests actually assert anything.

## Test strategy per workload

| Workload | Emphasis |
|---|---|
| Training / ML | Data quality, leakage tests, reproducibility, evaluation, backtesting |
| Inference | Contract, latency, fallback, canary comparison, cost bounds |
| RAG | Retrieval evaluation, ACL negative tests, injection-via-document suites, freshness |
| Data agent | Query correctness, semantic-definition adherence, unauthorized data tests |
| Agentic | Trajectory evaluation, tool authorization, bounds, approval gates, chaos, red-team |
| Copilots | Host-app compatibility, acceptance/trust metrics, permission tests |
| Automation | End-to-end process tests, exception paths, idempotency, breakage detection |

## Where tests run

| Stage | Runs |
|---|---|
| Pre-commit | Lint, type check, secrets scan, fast unit tests |
| PR gate | Unit, integration, contract, fast evaluation slice, SAST/SCA |
| Nightly | Full evaluation, performance, soak, mutation, drift, chaos (scheduled) |
| Pre-release | Acceptance/E2E, security scan, red-team (for in-scope systems), human review sample |
| Post-deploy | Smoke, canary comparison, monitoring verification |

## Anti-patterns

- Testing the model provider instead of your system
- Flaky "AI tests" that assert exact strings
- Access-control "happy path" tests only (denial must be proven)
- Coverage percentage as the goal
- Skipping negative and adversarial tests because they're negative
- Evaluation datasets that never receive production failures
