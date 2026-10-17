# Enablement & Adoption Lifecycle

**Status:** Proposed · **Owner:** Leadership / enablement · **Last reviewed:** 2026-10-17

How the organization builds AI capability in its people and drives durable adoption. Architecture standards only scale through **enabled teams** — this lifecycle closes that loop.

## Phases

### 1. Assess capability
- Skills inventory: architecture, ML/AI engineering, data engineering, security, product, domain
- Map gaps against the capability needs of the roadmap (not a generic curriculum)
- Identify roles: architects, tech leads, AI engineers, data stewards, reviewers
- **Artifact:** capability heat map with gaps prioritized

### 2. Build capability
| Mechanism | Best for | Notes |
|---|---|---|
| Reference architectures + checklists | Making good design the easy path | Scales without central involvement |
| Blueprints / starter kits | Hands-on learning by doing | Learn on a real skeleton |
| Architect/lead training | Applying standards independently | Enables delegated reviews |
| Pairing and review shadowing | Deep skill transfer | Highest cost, highest yield |
| Internal community of practice | Cross-team knowledge flow | Needs cadence and ownership |
| External training/certification | Baseline and credentials | Follow up with internal application |
| Research briefs and demos | Horizon awareness | Ties to [research](../research/README.md) |
**Artifact:** enablement plan per role with milestones

### 3. Enable in-flight work
- Project architects and tech leads run design reviews using published checklists (**delegation**, not escalation)
- Office hours and review clinics for edge cases
- Standards evolve from field feedback — friction reported by teams becomes a standards backlog item (this is the architectural feedback loop)
- **Artifact:** review coverage metrics; escalation rate

### 4. Sustain adoption
| Signal | Meaning |
|---|---|
| Decreasing central review requests | Delegation working |
| Rising blueprint usage | Standards being adopted by default |
| Shrinking exception counts | Standards fit reality |
| Internal contributions to standards/patterns | Community is engaged, not just consuming |
| Fewer repeated findings in reviews | Learning is landing |

- Rotate researchers/architects through delivery teams to keep knowledge bidirectional
- Recognize internal contributions (patterns, briefs, blueprints) as real work

### 5. Refresh
- Re-assess skills each cycle against evolving technology ([technology lifecycle](technology-lifecycle.md))
- Retire enablement content that no longer matches standards

## Enablement for AI specifically

- **Trust and judgment training** — users and reviewers need to know what AI systems fail at, not just what they can do
- **Evaluation literacy** — reading an evaluation report and challenging thresholds
- **Security awareness** — prompt injection and data handling for everyone touching AI builds
- **Data literacy** — classification, purpose limitation, and what can go into a prompt
- **Decision-making with AI** — calibration, when to override, how to escalate

## Anti-patterns

- Central architecture as bottleneck instead of platform (the failure this lifecycle exists to prevent)
- Training without practice (knowledge decays without application)
- Enablement disconnected from the roadmap's actual capability needs
- Ignoring field feedback so standards diverge from reality
- Measuring adoption by training attendance rather than behavior change
