# Model Risk Lifecycle

**Status:** Proposed · **Owner:** Governance / risk · **Last reviewed:** 2026-10-17

Governance lifecycle for AI models and AI-driven decisions — the "model risk management" discipline. Applies to any model whose output influences a decision about a person, a customer, money, safety, or a regulated process.

## Risk tiers

| Tier | Examples | Requirements |
|---|---|---|
| **Low** | Internal summarization, drafting, search ranking | Standard SDLC + evaluation |
| **Medium** | Content classification, prioritization, recommendations | Above + documented validation, monitoring, owner |
| **High** | Decisions affecting customers, credit, pricing, eligibility, safety | Above + independent validation, approval records, fairness analysis, human review path |
| **Prohibited** | Uses banned by policy/regulation | Not permitted |

Tier is assigned at intake and can only be **lowered** with documented evidence, never by assertion.

## Lifecycle

### 1. Intake & registration
- Register the model/AI use case: purpose, owner, data, decision influenced, tier
- **Artifact:** model inventory entry

### 2. Assessment
- Purpose & suitability: is a model appropriate for this decision at all?
- Data appropriateness: representative, lawful, quality-verified
- Methodology review: reasonable approach, honest evaluation, documented limitations
- Fairness & bias analysis: subgroup performance, disparate impact where applicable
- Interpretability: can we explain the decision to an affected party or regulator?
- **Artifact:** assessment report

### 3. Approval
- Risk-appropriate sign-off (tier-dependent): owner + reviewer + governance (+ independent validation for high tier)
- Conditions and limitations recorded explicitly (what the model must not be used for)
- **Artifact:** approval record with conditions

### 4. Deployment controls
- Human review path for adverse decisions where required
- Appeal/contest mechanism where decisions affect individuals
- Explainability surfaced to the humans operating it
- Monitoring thresholds tied to risk tier (stricter for higher tiers)

### 5. Ongoing monitoring
- Performance, drift, fairness metrics, and incident history per tier cadence
- Deterioration triggers remediation; breaches trigger suspension

### 6. Revalidation
- Periodic (tier-based cadence) and event-based (model change, data change, significant incident, regulatory change)
- Re-approval required after material change; changes to a high-tier model are never silent

### 7. Suspension & remediation
- Authority to suspend a model immediately when harm or unresolvable degradation appears
- Remediation path: retrain, constrain, add human review, or retire

### 8. Retirement
- Decommission, notify consumers, delete data per policy, archive documentation

## Principles

1. **Proportionality** — controls scale with potential harm, not with engineering elegance
2. **Accountability** — every model has a named owner accountable for its outcomes
3. **Human dignity** — decisions affecting people keep a human path to contest
4. **Documentation** — if it isn't written down, it didn't happen
5. **Independence** — high-risk models are validated by someone who didn't build them
6. **Reversibility** — suspension and rollback are always available and tested

## Relationship to other lifecycles

- Technical build: [ML project](ml-project-lifecycle.md) · [MLOps](mlops-lifecycle.md)
- Quality evidence: [evaluation lifecycle](evaluation-lifecycle.md)
- Operational failures: [operations & incident](operations-incident-lifecycle.md)
- Architecture controls: [security controls](../security/ai-security-controls.md), [review process](../docs/architecture-review-process.md)

## Anti-patterns

- Governance as a launch checkbox with no ongoing obligation
- Self-assessment of a high-risk model
- No appeal path for affected individuals
- Tier quietly lowered to reduce paperwork
- Monitoring performance but not fairness or subgroup impact
