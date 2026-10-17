# Architecture Review Process

**Status:** Proposed · **Last reviewed:** 2026-10-17

## Who reviews what

| Tier | Design profile | Reviewer | Target turnaround |
|---|---|---|---|
| **T0 — Self-certify** | Conforms fully to a reference architecture; no new tech; no sensitive data beyond the RA's scope | Project tech lead completes [design-review-checklist.md](design-review-checklist.md); no central involvement | Immediate |
| **T1 — Delegated** | Minor deviations, standard new technology already approved, or new use of sensitive data | Engineering/architecture lead in the business unit, using published checklists | 3 business days |
| **T2 — Central** | High-risk or novel: agentic with side effects, deviation from a reference architecture, new model provider, regulated data | Central architecture team + Cybersecurity | 10 business days |
| **T3 — Governance** | Cross-cutting: new standard, new reference architecture, major platform shift | Head of AI Governance and Architecture + EA/Cloud/Data/Cybersecurity leads | Scheduled forum; 2–4 weeks |

## Process

1. **Intake** — open an issue from the [design review request template](../templates/design-review-request.md) in this repo (or your project's repo for T0/T1).
2. **Tiering** — central team triages within 2 business days (intake is only for T2/T3; T0/T1 are self- or business-unit-run).
3. **Review** — reviewers use [design-review-checklist.md](design-review-checklist.md) and record findings as inline comments.
4. **Outcome** — one of:
   - **Approved** — proceed; checklist archived with the design
   - **Approved with conditions** — conditions tracked as ADRs with owners and dates
   - **Changes required** — re-review (fast-tracked)
   - **Rejected** — with written rationale and suggested alternatives
5. **Recording** — decisions that create precedent are published as ADRs or updates to reference architectures/standards.

## Escalation & disagreement

Disagreements between reviewers escalate to the Head of AI Governance and Architecture, who decides and (optionally) publishes the decision rationale as an ADR so the precedent is reusable.

## Design review is not security review

Cybersecurity red-teaming and threat modeling run in parallel per [security/red-team-integration.md](../security/red-team-integration.md); architecture review incorporates their findings but does not replace them.
