# Experimentation & Feature Release Lifecycle

**Status:** Proposed · **Owner:** Product / engineering · **Last reviewed:** 2026-10-17

How changes are tested against reality — through controlled experiments and progressive feature release — and how the machinery is cleaned up afterwards.

## Part 1 — Experimentation (A/B, online tests)

| Phase | Activities | Artifact |
|---|---|---|
| **1. Hypothesize** | State the change, expected effect, metric, and threshold *before* running | Experiment brief |
| **2. Design** | Unit of randomization, sample size/power, duration, guardrail metrics, stopping rule | Experiment design |
| **3. Instrument** | Exposure logging, metric pipelines, attribution correctness | Instrumentation checklist |
| **4. Run** | Monitor for interference, sample-ratio mismatch, novelty effects; do **not** peek-and-stop | Live dashboard |
| **5. Analyze** | Effect size with confidence intervals; segment analysis; guardrail checks | Analysis report |
| **6. Decide** | Ship, iterate, or kill — with the pre-registered threshold | Decision record; ADR if architectural |

**Rules:** pre-registration is mandatory; guardrail metrics (latency, cost, quality, harm) can halt an experiment; a null result is a result and gets recorded.

## Part 2 — Feature release (progressive rollout)

```
Build behind flag → Internal users → 1% → 5% → 25% → 100% → flag removal
                     (dark launch)     (canary slices, each with exit criteria)
```

| Phase | Activities | Exit criteria |
|---|---|---|
| **1. Flag design** | Flag created with owner, default state (off), expiry date | Flag registered |
| **2. Dark launch** | Code deployed, feature disabled; verify no side effects | No errors; no behavior change |
| **3. Internal** | Employees/testers only | Qualitative feedback; no critical defects |
| **4. Canary slices** | Incremental cohorts with monitoring at each step | Quality + SLO stable at each slice |
| **5. General availability** | Full rollout | Metrics at or above target |
| **6. Flag cleanup** | Remove flag and dead code path | Flag deleted from registry |

**Flag hygiene:** every flag has an owner and an expiry; flags older than 90 days without a cleanup plan are debt — review in the same cadence as dependency updates.

## AI-specific considerations

- **Flag granularity includes autonomy:** capability flags, autonomy-level flags, and model-version flags are separate
- **Experiments must include quality metrics**, not only behavioral/business ones ([evaluation lifecycle](evaluation-lifecycle.md))
- **Guardrails are never part of the experiment arm** — safety behavior is consistent across arms
- **Cost guardrail metrics are mandatory** for experiments touching model/prompt config
- **Novelty effects** are larger for AI features (users explore new capabilities) — extend observation windows or use holdout cohorts

## Anti-patterns

- Peeking until significance appears (in either direction)
- Randomized experiments on populations where the change cannot be isolated (shared caches, shared memory)
- Flags without owners that live for years
- Shipping a model/prompt change without a quality arm
- Cleaning up instrumentation but leaving the flag, or vice versa
