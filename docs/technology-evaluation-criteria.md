# Technology Evaluation Criteria

**Status:** Proposed · **Last reviewed:** 2026-10-17

Scoring rubric for candidate AI/ML technologies (frameworks, platforms, providers, tooling). Used by time-boxed validation prototypes and for build-vs-buy evidence.

## Scoring

Each criterion is scored 1–5 with written evidence. Total score is necessary but not sufficient — **security and data-handling criteria are pass/fail gates**.

| # | Criterion | Weight | What "5" looks like |
|---|---|---|---|
| 1 | **Fit with reference architecture** | 15% | Drops into an existing RA component slot with no topology change |
| 2 | **Security & compliance** *(gate)* | Pass/fail | SOC 2/ISO 27001, SSO, audit logs, private networking, no-training/data-residency terms |
| 3 | **Data handling** *(gate)* | Pass/fail | Regional residency, contractual retention limits, deletion guarantees |
| 4 | **Capability, measured by us** | 20% | Wins on our own evaluation sets and prototypes, not vendor benchmarks |
| 5 | **Operability** | 15% | IaC support, observability, upgrade path, no exotic operational skills needed |
| 6 | **Reliability & vendor health** | 10% | Published SLOs, healthy track record, sustainable business |
| 7 | **Cost (TCO, 3-year)** | 15% | Predictable; includes egress, fine-tuning, and hidden fees |
| 8 | **Portability & exit** | 10% | Standard interfaces; switching cost documented and acceptable |
| 9 | **Ecosystem & skills** | 10% | Teams can hire/train for it; active ecosystem; good docs |

## Evidence requirements

A score without evidence is not a score. The evaluation report must include:

- Time-boxed prototype results (see [research/prototypes/](../research/prototypes/TEMPLATE.md))
- Our own benchmark or golden-set numbers where capability is claimed
- Cost model with assumptions
- Security review outcome

## Decision path

1. Score → present to architecture team
2. If adopted: add to [approved-technologies.md](../standards/approved-technologies.md) and publish a research brief
3. If rejected: record why in the research log so the question isn't re-litigated in 6 months
4. Standards-level changes go through cross-cutting review (EA, Cloud, Data, Cybersecurity) per [CONTRIBUTING.md](../CONTRIBUTING.md)
