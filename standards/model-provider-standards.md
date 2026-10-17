# Model Provider Standards

**Status:** Proposed · **Last reviewed:** 2026-10-17

Standards for selecting and operating hosted foundation-model providers.

## Selection criteria (in priority order)

1. **Data handling** — no training on our data by default; contractual opt-out; regional data residency; retention limits
2. **Security posture** — SSO/SAML, audit logs, private networking options, SOC 2 / ISO 27001
3. **Capability fit** — benchmarked against our task-specific evaluation sets, not vendor leaderboards
4. **Reliability** — published SLOs, status history, rate-limit headroom, multi-region failover
5. **Cost** — token pricing, committed-use discounts, egress and fine-tuning fees
6. **Portability** — OpenAI-compatible or otherwise standard interfaces; switching cost estimate

## Non-negotiable requirements

- Provider keys live only in the AI gateway or secrets manager — never in application code or client-side
- Zero-data-retention or contracted no-training terms before any production traffic
- Per-provider evaluation report on file (see [research/prototypes/](../research/prototypes/))
- Approved region(s) only; cross-region routing must be explicit and documented

## Multi-provider strategy

- Every production workload names a **primary** and at least one **contingency** provider
- Prompt/model abstraction is required where practical, but not at the cost of lowest-common-denominator capability — abstraction decisions are ADR-worthy
- Provider concentration risk reviewed annually with Enterprise Architecture

## Onboarding a new provider

1. Time-boxed validation prototype (2–4 weeks) per [research process](../research/README.md)
2. Security review with Cybersecurity (contracts, data flow, egress)
3. Scored against [technology-evaluation-criteria.md](../docs/technology-evaluation-criteria.md)
4. Cross-cutting review, then add to [approved-technologies.md](approved-technologies.md)
