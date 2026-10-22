# Architecture Leadership Engagement Worksheet

**Status:** Template · **Owner:** Assigned per engagement · **Last reviewed:** 2026-10-22

Use with the [practical leadership guide](../docs/practical-architecture-leadership.md). Copy into an approved engagement workspace. Keep confidential customer details and restricted evidence out of this public repository. Replace placeholders; unverified entries remain assumptions.

## Engagement and accountability

| Field | Entry |
|---|---|
| Engagement / decision date | `<name, date>` |
| Business sponsor / outcome owner | `<named owner>` |
| Architect / engineering / operations owners | `<named owners and responsibilities>` |
| Customer and affected users | `<authorized roles or anonymized groups>` |
| Data owner / security reviewer | `<named owners>` |
| Release decision / residual-risk authority | `<named authorized decision-makers>` |
| Scope / exclusions / constraints | `<bounded first increment>` |
| Approved evidence location / classification | `<restricted link if necessary; never paste secrets>` |

## Problem, baseline, and success

- **Observed customer workflow:** `<what happens today; who validated it>`
- **Problem and consequence:** `<business effect, frequency, affected users>`
- **Baseline:** `<metric, value, definition, observation period, source>`
- **Success criterion:** `<target, measurement method, review date, business owner>`
- **Stop or redesign criterion:** `<condition and authorized decision-maker>`
- **Adoption/customer feedback measure:** `<method and consent/access arrangements>`

## Facts and uncertainties

| Statement | Fact / assumption / proposal / measured result | Evidence and limitations | Owner / validation date |
|---|---|---|---|
| `<statement>` | `<type>` | `<approved evidence reference>` | `<owner, date>` |

## Options and decision

Include the existing process or doing nothing where viable.

| Option | Value / feasibility | Build + run + support cost | Risks / reversibility | Decision rationale |
|---|---|---|---|---|
| `<option>` | `<assessment>` | `<estimate with assumptions>` | `<assessment>` | `<accept/reject/defer>` |

- **Chosen option and ADR:** `<link and decision owner>`
- **Dissent / alternatives considered:** `<concern, disposition, decision-maker>`
- **Accepted residual risks:** `<scope, authorized owner, review/expiry date>`
- **Conditions that reopen the decision:** `<new evidence or changed constraints>`

## Thin-slice validation

- **Critical assumption:** `<what could invalidate the design>`
- **Experiment and timebox:** `<bounded test with no unauthorized side effects>`
- **Inputs and authorization:** `<dataset/schema version, classification, approval>`
- **Reproduction details:** `<code revision, environment, hardware, workload, concurrency, duration>`
- **Failure tests:** `<timeout, duplicate, late record, denied access, bad output, rollback as applicable>`
- **Expected criterion / measured result:** `<report both; include errors and distributions where relevant>`
- **Mocks, exclusions, and limitations:** `<what has not been demonstrated>`
- **Decision:** `<proceed/change/stop; owner; date; evidence link>`

## Commitments and delivery readiness

| Commitment / dependency / risk | Accountable owner | Due / next update | Acceptance evidence | Status |
|---|---|---|---|---|
| `<item>` | `<person>` | `<date>` | `<test, contract, review, or artifact>` | `<status>` |

- **Required controls and NFRs:** `<criteria and linked evidence>`
- **Deployment / cutover owner:** `<owner and approved plan>`
- **Rollback trigger / execution owner:** `<condition, method, rehearsal result>`
- **SLOs, alerts, dashboards, and runbooks:** `<links and receiving owner>`
- **Incident communication:** `<coordinator, customer contact, next-update cadence>`
- **Operational handover / training:** `<receiving team's demonstrated task and recovery exercise>`
- **Release decision:** `<approve/defer; decision-maker; date; unresolved conditions>`

## Outcomes and expansion

| Review date / owner | Reliability and adoption | Business result vs baseline | Attribution / limitations | Continue / change / retire |
|---|---|---|---|---|
| `<date, owner>` | `<measured evidence>` | `<measured outcome>` | `<other contributing changes>` | `<decision and action>` |

Before expansion, record the new source/region/process, delta design, data permissions, operational capacity, updated costs, control review, and renewed acceptance criteria. Link to the original decision and any superseding ADR.

## Leadership reflection

- What did users or engineers teach us that changed the design?
- What did I personally own, and what did the team deliver?
- Which commitment, risk, or limitation did we communicate too late?
- Can the receiving team operate and change this without the architect?
- What result can we substantiate and, if authorized, share publicly?
