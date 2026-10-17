# Vendor & Third-Party Lifecycle

**Status:** Proposed · **Owner:** Procurement / architecture · **Last reviewed:** 2026-10-17

How external products and services (model providers, AI platforms, vector stores, evaluation tools, automation platforms) are assessed, integrated, managed, and exited. Applies the [technology lifecycle](technology-lifecycle.md) to commercial relationships.

## Phases

| Phase | Activities | Artifacts | Exit gate |
|---|---|---|---|
| **1. Need assessment** | Capability gap vs build; requirements; volume/scale estimate | Requirement brief | Build-vs-buy decision → [framework](../docs/build-vs-buy-framework.md) |
| **2. Market scan** | 2–4 credible options; capability comparison on **our** evaluation sets | Shortlist with evidence | Shortlist approved |
| **3. Technical validation** | Time-boxed prototype; integration test; performance/cost validation | [Prototype report](../research/prototypes/TEMPLATE.md) | Evaluation score → [criteria](../docs/technology-evaluation-criteria.md) |
| **4. Security & compliance review** | Data handling, residency, retention, subprocessors, certifications, contract terms | Security review outcome | **Pass/fail gate** ([provider standards](../standards/model-provider-standards.md)) |
| **5. Commercial negotiation** | Pricing model, commitments, SLAs, exit clauses, data-deletion terms, audit rights | Executed agreement | Terms reviewed by legal + architecture |
| **6. Integration** | Adapter at the boundary ([llm-gateway](../design-patterns/llm-gateway.md)); no vendor SDK sprawl in application code | Integration design + tests | Design review for material integration |
| **7. Manage** | SLA monitoring, incident contacts, usage vs commitments, contract renewals, security re-attestation | Vendor scorecard | Annual review |
| **8. Exit** | Data extraction/deletion, credential revocation, replacement migration, contract termination | Exit record | Data deletion verified |

## Vendor risk register

| Risk | Question to answer before adoption |
|---|---|
| Data handling | Is our data used for training? Where is it stored? Retention? Deletion guarantees? |
| Concentration | How many workloads depend on this vendor? What is the exit cost? |
| Model lifecycle | How are provider-side model changes communicated? Deprecation windows? |
| Commercial | Price-change exposure? Minimum commitments? Overage pricing? |
| Operational | SLA, status transparency, support escalation path, regional availability |
| Security | Certifications, incident history, breach notification terms, audit rights |
| Legal/regulatory | Subprocessors, jurisdiction, sector-specific constraints |
| Longevity | Funding/stability, roadmap dependence, lock-in mechanism |

## Required contract terms (AI providers)

- No training on our data by default; documented opt-out
- Data residency and retention limits stated explicitly
- Breach notification timelines and incident cooperation
- Model deprecation notice periods sufficient to migrate
- Data deletion on termination with verification
- Audit rights or equivalent attestation
- Exit assistance and data-portability commitments

## Integration rules

1. **Adapter boundary** — vendor specifics isolated so replacement is localized
2. **Gateway mediation** — one egress path, one policy surface ([LLM gateway](../design-patterns/llm-gateway.md))
3. **No vendor SDK directly in domain code**
4. **Contingency always identified** — for production workloads, a named alternate provider
5. **Usage metered and attributed** ([FinOps lifecycle](finops-cost-lifecycle.md))

## Anti-patterns

- Adopting on a sales demonstration with no prototype on our data
- Vendor SDKs spread across the codebase, making exit a rewrite
- No data-deletion clause, then trying to delete at exit
- Single provider for all workloads with no contingency plan
- Renewals auto-signed without a scorecard review
- Prototypes with production data before security review completes
