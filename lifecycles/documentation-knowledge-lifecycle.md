# Documentation & Knowledge Lifecycle

**Status:** Proposed · **Owner:** Architecture · **Last reviewed:** 2026-10-17

How architectural and operational knowledge is written, kept true, and retired. Undocumented architecture is unmaintainable architecture — and stale documentation is worse than none.

## Phases

| Phase | Activities | Exit criteria |
|---|---|---|
| **1. Identify** | Decide what must be documented: decisions, interfaces, runbooks, diagrams, onboarding paths | Owner assigned |
| **2. Author** | Write for the audience (executive vs engineer); use templates; diagrams as code | Reviewed by a peer |
| **3. Review** | Technical accuracy + audience fit; security review for sensitive content | Approved |
| **4. Publish** | Indexed and discoverable; linked from the relevant index; versioned | Findable in ≤ 2 clicks |
| **5. Maintain** | Reviewed on cadence; updated **in the same PR** as the change it describes | Review date within cadence |
| **6. Measure** | Staleness checks, broken-link checks, search analytics, support-ticket themes | No unowned stale docs |
| **7. Retire** | Mark obsolete, redirect, archive | Removed from active indexes |

## Document types and cadence

| Type | Content | Review cadence |
|---|---|---|
| ADR | Decisions and rationale | Immutable; superseded, never edited |
| Reference architecture | Canonical designs | 6 months or on significant change |
| Standard | Approved technologies and rules | 6 months or event-driven |
| Runbook | Operational procedure | Quarterly + after any incident touching it |
| Diagram | Current/target state | On change (diagrams-as-code in PR) |
| Onboarding guide | How to start contributing | 6 months |
| Research brief | Findings and recommendations | Immutable once published |
| Use case / playbook | Problem, workflow, trade-offs | 6 months |
| Glossary | Shared vocabulary | On demand |

## Principles

1. **Docs live with code** — same repository, same PR, same review
2. **Diagrams as code** — reviewable diffs, not screenshots ([architecture as code](../design-patterns/architecture-as-code.md))
3. **Concise over complete** — a page someone reads beats a book nobody does
4. **Two audiences, two views** — executive framing and engineering detail for the same design ([solution design lifecycle](../docs/solution-design-lifecycle.md))
5. **Automate staleness detection** — link checking in CI, review-date linting, ownership in CODEOWNERS
6. **Delete or mark, never leave ambiguous** — deprecated content states its successor

## Knowledge for AI systems specifically

- **Prompts, tool contracts, and evaluation criteria are documented artifacts** ([prompt lifecycle](prompt-lifecycle.md))
- **Model cards / dataset cards** describe intended use, limitations, and evaluation results ([model risk lifecycle](model-risk-lifecycle.md))
- **Runbooks include AI-specific scenarios** ([operations lifecycle](operations-incident-lifecycle.md))
- **RAG corpora need their own documentation**: sources, refresh cadence, ACL model, known gaps

## Anti-patterns

- Changes merged without updating the docs that describe them
- Diagrams maintained as exported images nobody can edit
- "We'll document it after go-live" (never happens)
- Duplicated truth in multiple pages that drift apart
- Documentation with no owner and no review date
