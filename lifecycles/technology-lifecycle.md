# Technology Lifecycle

**Status:** Proposed · **Owner:** Architecture · **Last reviewed:** 2026-10-17

How technologies enter, stay in, and leave the approved landscape. This lifecycle keeps [standards](../standards/approved-technologies.md) current as the AI field churns — without churn for its own sake.

## Radar states

| State | Meaning | Use |
|---|---|---|
| **Watching** | Horizon-scan interest; no decision yet | Research/prototype only |
| **Trial** | Approved for time-boxed, non-production evaluation | Prototypes with cleared data |
| **Adopt** | Approved for production within stated scope | Standard, listed as approved |
| **Hold** | No new adoption; existing use continues | Deprecated-in-waiting; migrate when practical |
| **Deprecate** | Actively migrate away; 12-month retention | Needs migration plan |
| **Remove** | Not permitted | Direct review required for exception |

Movement is deliberate: **Watching → Trial → Adopt**, or exit to Hold/Deprecate. Nothing is adopted without a prototype and an evaluation score.

## Lifecycle

### 1. Horizon scanning
- Continuous: publications, upstream releases, peer practice, vendor announcements, community signals
- Watch list of candidate technologies with the question each would answer
- Trigger conditions that would make evaluation urgent (e.g., incumbent deprecation, security advisory)

### 2. Trial
- Time-boxed [prototype](../research/prototypes/TEMPLATE.md) (2–4 weeks) against a decision question
- Scored with [technology evaluation criteria](../docs/technology-evaluation-criteria.md)
- Evaluated on **our** workloads and data, not vendor benchmarks

### 3. Research brief
- Findings, recommendation, adoption path, falsification conditions ([template](../research/briefs/TEMPLATE.md))
- Negative results published too — closed questions stay closed

### 4. Adoption review
- Cross-cutting review: Enterprise Architecture, Cloud Platform, Data, Cybersecurity
- Security gates are pass/fail regardless of capability score
- Approved scope defined: which workloads may use it

### 5. Adopt & standardize
- Added to [approved technologies](../standards/approved-technologies.md) with scope and conditions
- [Blueprints](../blueprints/) updated to embody it; checklists updated
- Enablement: documentation, examples, guidance for teams

### 6. Maintain
- Track upstream health: releases, security advisories, community activity, license changes, vendor stability
- Re-review cadence (per standard, plus event-driven)
- Usage census: which systems depend on it (informs migration cost)

### 7. Deprecate
- Trigger: better standard, unmaintained upstream, security/legal concern, concentration risk
- Publish migration path and sunset date (≥ 12 months for widely used tech)
- Support existing users; block new adoption immediately

### 8. Remove
- After migrations complete: remove from approved list, archive guidance, delete blueprints
- Exceptions require direct architecture review

## Review triggers

| Trigger | Action |
|---|---|
| Security advisory or CVE | Immediate assessment; possible emergency deprecation |
| Upstream abandonment | Migration planning begins |
| License change | Legal + architecture review |
| Provider concentration risk | Portfolio review |
| Leap in capability (new technique/architecture) | Trial candidate |
| Provider model deprecation | Replacement evaluated before forced migration |

## Anti-patterns

- Adopting on announcement day (no prototype, no evidence)
- Never removing anything (the list rots into a menu of dead options)
- Migrating for novelty when the incumbent is healthy
- Standards that lag reality, so every team needs an exception
- One-way adoption with no dependency census, so nothing can ever be retired
