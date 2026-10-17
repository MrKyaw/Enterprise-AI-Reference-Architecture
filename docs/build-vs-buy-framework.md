# Build-vs-Buy Framework

**Status:** Proposed · **Last reviewed:** 2026-10-17

Evidence-based framework for deciding whether to build, buy, or adopt a managed/AI-accelerated solution. Recommendations must cite prototype evidence or production experience — not vendor slideware.

## Decision matrix

| | **Strong strategic differentiation** | **Weak differentiation** |
|---|---|---|
| ** commodity market (many vendors)** | Buy the platform; build the differentiating layer on top | Buy |
| **Nascent market (few/no vendors)** | Build (with a documented exit path) | Build minimal, time-boxed; re-evaluate in 6 months |

"Strategic differentiation" = does this capability materially affect competitive position or is it deeply entangled with proprietary data/processes? For AI/ML: foundation capabilities are almost never differentiating; **your data and workflow integration usually are**.

## Mandatory considerations (override defaults when violated)

1. **Maintenance debt** — building means owning model upgrades, drift, evals, and on-call forever. Staffing cost ≈ 2–3 engineers ongoing for any production AI component. Is that funded?
2. **Data gravity** — does buying lock data into a vendor ecosystem you can't extract from? Document the exit path either way.
3. **Security reviewability** — a buy option that fails [model-provider-standards](../standards/model-provider-standards.md) gates is disqualified regardless of fit.
4. **Time-to-value** — if buy delivers in weeks and build in quarters, the build case must show capability the buy option provably cannot reach (with evidence).
5. **AI-specific flip risk** — managed AI features from vendors (agents, copilots) churn fast and often can't be self-hosted. Weigh vendor roadmap dependence heavily.

## Recommendation template

Every build-vs-buy recommendation produces a one-page ADR containing:

- Decision: **Build** / **Buy** / **Hybrid** (buy platform, build layer)
- Evidence: prototype results, scored against [technology-evaluation-criteria.md](technology-evaluation-criteria.md)
- 3-year TCO comparison with assumptions
- Exit/switching plan
- Maintenance owner and staffing plan
- Re-evaluation trigger and date (e.g., "revisit when vendor X GA's self-hosted option, or 2027-04")

## Review

Build-vs-buy recommendations for high-risk or novel initiatives are presented to the Head of AI Governance and Architecture alongside research findings; material platform choices become cross-cutting standards decisions.
