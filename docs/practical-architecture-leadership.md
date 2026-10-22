# Practical Leadership Principles for Enterprise, Solution, and AI Architects

**Status:** Proposed · **Owner:** Architecture practice · **Last reviewed:** 2026-10-22

**Customer obsession · Technical credibility · Ownership · Trust · Delivery · Business impact**

A senior solution architect, principal architect, enterprise architect, or customer-facing AI architect earns confidence by understanding the business problem, making feasible technical decisions, helping teams deliver, and staying accountable for operational and customer outcomes. Technical depth supports that responsibility throughout the engagement.

Use this guide during discovery, design reviews, delivery, incidents, and customer-success conversations. Use the [engagement worksheet](../templates/architecture-leadership-engagement.md) to record decisions and evidence. This is a proposed operating practice: teams should agree their own decision rights, risk thresholds, and acceptance criteria.

## 1. Start with a repeatable thought process

**Understand → Design → Validate → Deliver → Operate → Expand**

| Step | Questions to answer | Evidence to leave behind |
|---|---|---|
| Understand | Who experiences the problem? What happens today? What does failure cost? What cannot change? | Observed workflow, stakeholder map, measured baseline, constraints, business owner |
| Design | What are the simplest viable options? What can we reuse? Which trade-offs matter to each stakeholder? | Current/future-state views, options including doing nothing, ADR, costs and dependencies |
| Validate | Which assumption could invalidate the design? How can we test it safely? What result would change our mind? | Timeboxed experiment, approved test data, reproducible results, limitations, proceed/change/stop decision |
| Deliver | Who owns each dependency? What must pass before users depend on this? How do we recover? | API/data contracts, acceptance tests, cutover and rollback plans, readiness decision |
| Operate | Can the receiving team detect and recover from failure? Are users getting the intended result? | SLOs, dashboards, runbooks, incident exercise, named operational owner, adoption review |
| Expand | Has value materialized? What changes with another domain, tenant, region, or data source? | Outcome scorecard, expansion delta, refreshed risks, updated cost model and approvals |

Separate **observed facts**, **assumptions**, **proposals**, and **measured results** in every review. Give unknowns an owner and a validation date. A slide, a prototype, and a production measurement carry different evidence; label each accurately.

### Make the next decision concrete

1. State the customer outcome and the baseline in the customer's language.
2. List constraints: data access, security, integration capabilities, operational capacity, budget, and deadline.
3. Compare viable options, including an existing process or a simpler deterministic solution.
4. Identify the highest-impact uncertainty; build or inspect enough of the implementation to test it.
5. Record the decision, dissent, accepted residual risk, owner, rollback condition, and review date.
6. Follow the result into production and revisit the decision when evidence changes.

For example: “The dashboard is slow” is an observation to investigate. Check query plans, source freshness, joins, concurrency, network timing, and the user's actual task before proposing a new data platform or an AI interface. Record what was measured and what remains unexplained.

## 2. The 16 Amazon Leadership Principles applied to architecture

The principle names below come from [Amazon's official Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles), checked on 2026-10-22. The behaviors, evidence, and failure signals are architecture-specific adaptations of the supplied framework; they are not an official Amazon architecture framework or an endorsement.

| Leadership principle | Practical architect behavior | Working evidence / warning signal |
|---|---|---|
| 1. Customer Obsession | Observe the customer's workflow and agree success criteria before selecting technology. Include users affected by failure. | Baseline and customer-approved acceptance criteria; warning: a technology demo with no named problem owner |
| 2. Ownership | Coordinate discovery through stabilization, assign accountable owners, and make handovers explicit. | Dependency log and accepted handover; warning: assuming another team will operate the design |
| 3. Invent and Simplify | Reduce interfaces and manual steps; prove a reusable pattern on one real integration before generalizing. | Before/after dependency map and working reference; warning: another abstraction with no reduction in effort |
| 4. Are Right, A Lot | Seek contrary evidence, involve domain experts, and update the recommendation when assumptions fail. | Options ADR and disconfirming tests; warning: defending an initial design despite failed validation |
| 5. Learn and Be Curious | Read contracts, inspect schemas, and learn unfamiliar customer systems with their owners. | System walkthrough and answered discovery questions; warning: designing from product names alone |
| 6. Hire and Develop the Best | Coach engineers, share design rationale, give constructive reviews, and build succession into ownership. | Paired implementation and another engineer completing the task; warning: the architect is the only person who can change it |
| 7. Insist on the Highest Standards | Agree testable security, quality, reliability, accessibility, performance, and operational acceptance criteria. | Review evidence and recorded exceptions; warning: “production ready” without acceptance tests |
| 8. Think Big | Show a credible future direction while delivering a bounded first increment. Revalidate expansion assumptions. | Roadmap with adoption gates; warning: speculative platform work ahead of a proven use case |
| 9. Bias for Action | Timebox uncertainty and move quickly on reversible decisions within agreed data and risk boundaries. | Small experiment and explicit rollback; warning: urgency used to bypass authorization or safety controls |
| 10. Frugality | Reuse sound existing investments and evaluate total build, run, support, and change costs. | Cost per completed business task and operating estimate; warning: cheap inference hiding expensive review or support |
| 11. Earn Trust | State limitations early, distinguish commitments from forecasts, and correct mistakes promptly. | Decision/commitment log and consistent updates; warning: silently changing scope or overstating capabilities |
| 12. Dive Deep | Inspect traces, API failures, query plans, lineage, evaluation samples, and incidents with the responsible engineers. | Reproduction and linked corrective action; warning: relying on aggregate dashboards when users report failures |
| 13. Have Backbone; Disagree and Commit | Challenge unsafe or infeasible plans respectfully, record the trade-off, and support the authorized decision. | Dissent and decision owner in the ADR; warning: treating commitment as permission to ignore unresolved mandatory controls |
| 14. Deliver Results | Connect shipping to reliability, adoption, and the agreed business result. Report missed targets with corrective action. | Outcome scorecard against baseline; warning: counting documents or deployments as customer value |
| 15. Strive to Be Earth's Best Employer | Support inclusive reviews, coaching, sustainable workloads, and a credible on-call arrangement. | Capacity plan, supported ownership, and team feedback; warning: success dependent on repeated heroics |
| 16. Success and Scale Bring Broad Responsibility | Review downstream effects on privacy, security, accessibility, people, and resource consumption as scope grows. | Updated impact/risk review for expansion; warning: assuming pilot controls cover every market or user group |

Customer Obsession, Ownership, Earn Trust, Dive Deep, Bias for Action, Have Backbone, and Deliver Results are useful anchors for customer-facing work. They complement the other principles rather than replacing them. Decision speed never removes the need for a properly authorized risk owner.

## 3. Leadership behaviors to adapt to the situation

Consultative solution architecture, servant leadership, and situational leadership complement this operating model. The following labels organize practical behaviors; this table does not claim that adopting a style guarantees an outcome.

| Approach | How to practice it | Customer/team benefit to check |
|---|---|---|
| Consultative | Ask diagnostic questions; replay the problem and constraints before recommending an option. | Stakeholders confirm that the proposed work addresses their actual workflow |
| Servant | Remove an access, dependency, environment, or ownership blocker with the people doing the work. | A previously blocked task progresses without bypassing controls |
| Situational | Coach an unfamiliar team through a new risk; delegate a familiar implementation with clear boundaries. | Engineers can make appropriate decisions without continual escalation |
| Transformational | Explain the future state through business capabilities and an achievable migration sequence. | Sponsors and delivery teams understand both direction and the next increment |
| Technical thought leadership | Publish a reproducible example, explain trade-offs, and invite a critical design review. | Another team can reproduce the result and explain when the pattern does not fit |
| Adaptive | Reassess the recommendation when data quality, costs, requirements, or constraints change. | The plan changes in response to evidence rather than calendar pressure |
| Collaborative | Involve product, engineering, security, data, operations, and customer owners before committing dependencies. | Decisions have accountable owners and fewer late surprises |
| Outcome-based | Agree measures and review them against the pre-change baseline with the business owner. | Adoption and value are assessed independently of deployment activity |
| Ethical | Minimize data exposure, make automated decision boundaries visible, and provide an escalation path. | Affected users can understand, challenge, or recover from an incorrect outcome |
| Coaching | Pair on diagnosis, reviews, and recovery exercises; then let the receiving team lead. | The customer or delivery team can operate and change the system independently |

Change the behavior to fit urgency and team capability while keeping decision rights and acceptance standards consistent. During an incident, establish clear coordination; during learning, create space for questions and controlled experiments.

## 4. Customer lifecycle: actions, deliverables, and exit evidence

This expands the working behaviors within the existing [solution design lifecycle](solution-design-lifecycle.md). Proof of value sits inside design/diligence; onboarding, release, and stabilization refine deployment. Apply the gates proportionally rather than creating another approval chain.

| Customer stage | Architect's leadership actions | Tangible deliverables | Evidence before moving on |
|---|---|---|---|
| 1. Discovery / pre-sales | Meet sponsors, process owners, users, and technical owners; confirm pain points and constraints. | Discovery summary, stakeholder map, business KPI baseline | Customer validates the problem; a sponsor owns the outcome; unknowns are visible |
| 2. Solution design | Map systems of record, workflows, identities, data contracts, and operational responsibilities. Compare feasible options. | Context/component/data-flow diagrams, option assessment, ADR | Technical owners confirm feasibility; business owner understands costs and trade-offs |
| 3. Technical diligence | Bring security, data governance, operations, architecture, and commercial reviewers into the decision. | Threat/data-flow assessment, risk register, controls evidence | Required controls pass or an authorized exception is recorded; unresolved blockers remain blockers |
| 4. Proof of value | Test the riskiest assumption using approved representative or synthetic data in a bounded environment. | Runnable prototype, evaluation set, benchmark method, feasibility report | Agreed success/stop criteria evaluated; limitations recorded; proceed/change/stop decision made |
| 5. Customer onboarding | Coordinate environments, access, contracts, dependency owners, and support arrangements. | Onboarding plan, contract tests, deployment checklist, training plan | Integration works against the intended interface; receiving teams accept responsibilities |
| 6. Production deployment | Rehearse cutover, rollback, detection, and incident communications with the operating team. | Runbooks, SLOs, acceptance tests, rollback record, readiness sign-off | Designated authority approves release; operations demonstrates recovery; business owner accepts residual risk |
| 7. Customer success | Review adoption, reliability, business outcomes, complaints, and outstanding issues after stabilization. | KPI scorecard, customer review, corrective-action backlog | Outcomes compared with baseline; customer feedback recorded with consent; support is sustainable |
| 8. Expansion | Test demand and reassess new sources, regions, users, and business processes before scaling. | Expansion roadmap, delta design, updated controls and cost model | Existing value is evidenced; added scope has owners, capacity, funding, and required approvals |

### Roles and accountability

The architect coordinates technical decisions and evidence. The business sponsor owns the business outcome and funding; engineering owns implementation; data owners authorize data use; security/control owners determine required assurance; operations accepts service ownership. Record the actual decision-maker for release and risk acceptance. Avoid assigning every responsibility to the architect or an unnamed “team.”

## 5. Hands-on example: a retail integration

**Illustrative proposed pattern.** This is a teaching scenario, not a customer case study, a prescribed stack, or evidence of any company's internal architecture.

```text
ERP / POS / Inventory / Merchandising / Order management
              |
     Authorized APIs, batch extracts, or CDC
     Versioned contracts, source timestamps, identifiers
              |
     Ingestion and orchestration
              |
     Validation -> quarantine / repair -> transformation
              |
     Governed analytical store and operational services
              |
     Business workflows / reporting / bounded AI assistance
              |
     Reliability + user adoption + measured business outcome
```

An optional implementation might use GCP, Airflow, Snowflake, PostgreSQL, and Kotlin services if the customer's existing estate and requirements justify them. Each product remains a candidate; a batch pipeline or an existing database may be sufficient. Technology selection follows the [evaluation criteria](technology-evaluation-criteria.md) and [integration patterns](../standards/integration-patterns.md).

### Work through the architecture decision

**Situation:** store planners report stock discrepancies and spend time reconciling orders manually. Source update behavior, data rights, reconciliation effort, and the business impact are initially unknown.

1. **Observe and baseline.** Walk through a reconciliation task with a planner and source owner. Define how discrepancy rate and reconciliation time will be measured. Agree the observation period before setting improvement targets.
2. **Inspect the interfaces.** Read a real contract or approved extract. Check stable identifiers, timestamp semantics, late arrivals, deletion behavior, API limits, and whether CDC is available and authorized.
3. **Compare options.** Compare scheduled reconciliation, incremental ingestion, and event/CDC processing. Record freshness needs and the cost/operational consequences. Keep AI assistance outside the critical correction path until its value and controls are demonstrated.
4. **Build a thin slice.** In an approved non-production environment, ingest one bounded source, validate it, quarantine an invalid record, replay a duplicate, and reconcile a corrected record. Keep production writes disabled.
5. **Test failure recovery.** Inject an upstream timeout and a delayed/out-of-order update. Verify detection, idempotency, replay, recovery, and the operator's ability to distinguish stale from current data.
6. **Make the decision.** Present results and unresolved constraints to the business and technical owners. If source freshness cannot meet the needed workflow, revise the design or expectation before proceeding.
7. **Deliver and measure.** Rehearse rollback, agree who responds to broken feeds, and compare outcomes with the original baseline after an agreed stabilization period.

No latency, cost, accuracy, or customer-satisfaction improvement is claimed here. Populate the [worksheet](../templates/architecture-leadership-engagement.md) with measured results from your own authorized experiment.

### Evidence that makes a prototype credible

Record the code revision, input/schema version, data authorization, environment/hardware, workload size, concurrency, warm/cold conditions, test duration, errors, correctness checks, and cost assumptions. Report distributions when relevant, not one favorable latency sample. Document what was mocked and rerun critical tests against intended interfaces before release.

## 6. Ten habits that protect customer relationships

| Habit | Real working practice |
|---|---|
| Listen before prescribing | Ask why a feature is needed and observe the affected task before proposing implementation. |
| Speak the customer's language | Discuss business outcomes with sponsors, contracts and failure semantics with engineers, and control evidence with security owners. |
| Never overpromise | Label proven behavior, feasible extensions, and unvalidated ideas; confirm commitments with delivery owners. |
| Make commitments visible | Keep an owner, due date, dependency, acceptance condition, and next update for each commitment. |
| Surface risks early | State the consequence, available alternatives, decision needed, and latest responsible decision date. |
| Respect existing investments | Check whether the current platform can meet the need before proposing a replacement. |
| Show working evidence | Walk through runnable examples, traces, contracts, benchmark methods, and failure recovery. |
| Treat incidents as relationship moments | Communicate verified facts and next-update times, coordinate recovery, then track root-cause actions to completion. |
| Enable independence | Provide usable documentation, paired training, access procedures, and an operational recovery exercise. |
| Stay accountable after go-live | Review adoption, reliability, customer feedback, and the business result; act when the result falls short. |

## 7. A practical working cadence

| When | Architect's action | Result to record |
|---|---|---|
| At engagement start | Agree scope, baseline, decision rights, data access, risks, and success/stop criteria. | Completed engagement worksheet with named owners |
| During delivery | Review blocked work with engineers; inspect the artifact behind each material risk. | Updated dependency log, evidence, and next decisions |
| At an agreed weekly review | Give sponsors and customer owners a concise outcome/risk/decision update. | Commitments, changed assumptions, cost/capacity changes, decisions needed |
| Before release | Run operational acceptance and failure-recovery exercises with the receiving team. | Readiness record, remaining exceptions, decision, rollback owner |
| At agreed post-launch checkpoints | Compare reliability, adoption, and business outcomes with baseline. | Continue/change/retire recommendation and corrective actions |
| Before expansion | Reassess additional data, permissions, regions, scale, and operating capacity. | Reviewed delta design and renewed acceptance criteria |

A useful status update: “The approved extract passed schema validation. Duplicate replay is working in the test environment. Source deletion behavior remains unverified; the source owner will confirm it by the agreed review date. Release depends on that test and the recovery exercise.” Replace these illustrative statements with actual evidence, owners, and dates.

## 8. Demonstrate leadership authentically in interviews and reviews

Prepare STAR stories from work you actually performed. Explain the team's contribution and your own decision-making separately. Use employer/customer names, data, and artifacts only where disclosure is authorized; anonymize confidential context.

| Principle | Story to prepare from your own work | Evidence to substantiate |
|---|---|---|
| Customer Obsession | A requirement changed after observing users or consulting a business owner. | Original problem, changed requirement, acceptance criteria, authorized customer feedback |
| Ownership | You coordinated a cross-team delivery through stabilization. | Decisions you owned, dependencies resolved, handover and operational outcomes |
| Bias for Action | A timeboxed experiment resolved a specific uncertainty. | Timebox, scope, result, what it did not prove, resulting decision |
| Invent and Simplify | You removed an unnecessary integration step or operational dependency. | Before/after design, measured maintenance or task impact |
| Dive Deep | You reproduced a performance or correctness failure and changed the design. | Traces, test conditions, root cause, repeated benchmark or regression test |
| Think Big | A proven solution became a reusable capability across another use case. | Adoption evidence, limits of reuse, incremental cost and controls |
| Earn Trust | You disclosed a limitation or missed commitment and helped recover the engagement. | Communication, corrective action, subsequent customer/team feedback |
| Deliver Results | A deployed change improved an agreed outcome. | Baseline, measurement period, observed result, attribution limits, remaining issues |

Do not turn an experiment into a production claim. A latency reduction does not establish customer satisfaction; a successful demo does not establish adoption; a team result does not mean you personally implemented every component. If evidence is unavailable or confidential, explain the method and limitation rather than inventing a number.

### Adaptable leadership statement

> My approach starts with the customer's business goal, existing environment, and operating constraints. I translate those into options, test the assumptions most likely to invalidate the design, and make decisions visible to the people who must build and operate the solution. I contribute hands-on where evidence is needed, help teams remove blockers, and stay accountable through adoption and operational review. I aim to earn trust through clear trade-offs, reliable commitments, and outcomes we can substantiate.

Use this as a draft in your own voice. Pair each claim with an example you can explain and defend.

## 9. Review the practice against evidence

- [ ] The customer and affected users validate the problem and baseline.
- [ ] The business outcome, decision-maker, and technical/operational owners are named.
- [ ] Options, assumptions, trade-offs, dissent, and the chosen decision are recorded.
- [ ] Critical uncertainties have a bounded test and a proceed/change/stop criterion.
- [ ] Data access is authorized; examples and artifacts are appropriate to share.
- [ ] Security, quality, cost, reliability, and accessibility criteria have evidence.
- [ ] The receiving team can detect failures and demonstrate recovery.
- [ ] Commitments and remaining risks have owners and review dates.
- [ ] Post-launch adoption and business results are measured against baseline.
- [ ] Expansion follows verified value and a refreshed risk/capacity review.

Use missing items to identify specific follow-up actions and evidence gaps. Make release or expansion decisions through the established governance process.

## Related guidance and attribution

- [Solution design lifecycle](solution-design-lifecycle.md): phases and architecture artifacts.
- [Business case and value](business-case-and-value.md): baseline, attribution, costs, and kill criteria.
- [Architecture review process](architecture-review-process.md): decision and review routing.
- [POC to production](poc-to-production.md): operational and assurance gates.
- [Enablement and adoption lifecycle](../lifecycles/enablement-adoption-lifecycle.md): team capability and sustainable ownership.
- [Architect competency resources](../resources/README.md): technical and leadership development.
- [Amazon Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles): primary source for the 16 named principles. All architect-specific tables, lifecycle practices, examples, and the worksheet here are adaptations, not official Amazon material.
