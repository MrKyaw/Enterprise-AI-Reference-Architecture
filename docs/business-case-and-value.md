# Business Cases & Value Measurement for AI

**Status:** Proposed · **Last reviewed:** 2026-10-17

AI initiatives compete for investment with everything else the organization builds. Every initiative above a threshold of effort needs a business case with quantified value — and a post-launch measurement of whether the value materialized.

## Building the case

### 1. Find and prioritize opportunities
- **Discovery workshops:** facilitated sessions that translate business problems into candidate AI opportunities (participants: process owners + technologists)
- **Opportunity register:** maintained backlog of candidates, each scored on:

| Factor | Question |
|---|---|
| Value | What measurable outcome improves? (hours saved, revenue protected, error rate, cycle time) |
| Feasibility | Data availability, integration complexity, risk class |
| Risk | Data sensitivity, side-effect class, regulatory exposure |
| Strategic fit | Alignment to [reference architectures](../reference-architectures/) and platform direction |

- Prioritization review cadence (quarterly) independent of any formal project pipeline — good ideas outside the project system still get evaluated

### 2. Quantify (one page, honest numbers)

- **Benefit:** annualized, with baseline measurement and the method of attribution
- **Cost:** build + **sustained run cost** — for AI this means ongoing evaluation, model upgrades, retraining, and on-call, not just initial delivery
- **Time to value:** when does the benefit curve start?
- **Risk-adjusted:** apply a discount for adoption uncertainty; over-forecasting AI savings destroys the credibility of the next proposal

### 3. Decide and record
- Present recommendation (build / buy / hybrid / defer / decline) with evidence per [build-vs-buy-framework](build-vs-buy-framework.md)
- Material platform choices become standards decisions with cross-cutting review
- Record as an ADR ([template](../adr/0000-template.md))

## Measuring after launch

- **Define KPIs before build**, with baseline captured pre-launch
- **Leading indicators:** adoption rate, task completion, user trust/satisfaction
- **Lagging indicators:** the business outcome the case promised
- **Review at 30/90/180 days:** report against the original business case — including honest attribution when other changes contributed
- **Kill criteria:** pre-agreed conditions under which the capability is retired (stated at approval time)

## Guardrails against common distortions

- ❌ AI solution looking for a problem (start from the workshop, not the technology)
- ❌ Counting "time saved" that isn't converted to capacity or cost reduction
- ❌ Excluding maintenance and evaluation costs from the TCO
- ❌ Double-counting benefits across multiple initiatives
