# From Prototype to Production

**Status:** Proposed · **Last reviewed:** 2026-10-17

Isolated proofs of concept do not create business value — production systems do. This document defines the deliberate path an AI capability travels from exploratory prototype to a supported, observable, secure production service.

> Prototypes answer questions ([research/prototypes](../research/prototypes/TEMPLATE.md)). Products serve users. They are different artifacts with different rules — a prototype that "graduates" without rebuilding against the reference architecture is future production debt.

## The five gates

```
Prototype → Production candidate → Limited release → General availability → Sustained operation
 (research)      (build phase)       (controlled)      (ramped)             (run & improve)
```

### Gate 1 — Prototype → Production candidate
- Question answered; decision recorded in a [research brief](../research/briefs/TEMPLATE.md)
- Rebuilt against the applicable [reference architecture](../reference-architectures/) — not patched into shape
- [Design review](architecture-review-process.md) completed at the correct tier

### Gate 2 — Production candidate → Limited release
- [NFRs](non-functional-requirements.md) met with evidence (load test, failure drills)
- [Evaluation suite in CI](../design-patterns/evaluation-in-ci.md) with explicit thresholds
- All applicable [AI security controls](../security/ai-security-controls.md) verified; [SSDLC](../security/secure-sdlc.md) activities complete
- Runbook, on-call owner, and budget alarm in place

### Gate 3 — Limited release → General availability
- Canary/shadow rollout completed with measured quality vs baseline
- Observability dashboards reviewed for a full business cycle
- [Red-teaming](../security/red-team-integration.md) complete for agentic/user-facing systems
- Support model defined (who answers, who fixes, what SLA)

### Gate 4 — GA → Sustained operation
- Drift monitoring active with review cadence
- Cost-per-unit tracked against forecast
- Scheduled re-evaluation date set (model upgrades, provider changes)
- Sunset plan documented: graceful shutdown, data deletion, fallback

## What "done" includes

| Capability | Artifact |
|---|---|
| Quality | Evaluation datasets + thresholds in CI |
| Reliability | SLOs, alerting, runbook, degradation path |
| Security | Controls checklist, threat model, red-team results |
| Cost | Unit economics + budget alarms |
| Ownership | Named team, on-call rotation, lifecycle dates |
| Knowledge | Design doc, architecture diagram, ADRs |

## Common failure modes

- **Forever-PoC:** prototype runs in front of real users with no SLOs or owner — treat as an incident risk
- **Skip-the-rebuild:** bolting guardrails onto prototype code instead of re-architecting
- **Evaluation theater:** metrics exist but don't gate deployment
- **Vendor-driven pacing:** going GA because the provider shipped a feature, not because Gate 2 evidence exists
