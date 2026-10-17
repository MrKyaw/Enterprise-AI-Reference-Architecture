# Driven Development Approaches

**Status:** Proposed · **Last reviewed:** 2026-10-17

Catalog of the "X-driven" approaches and how each applies to AI/ML delivery. Each entry: what it means, its practice, its artifacts, and its AI-specific adaptation.

---

## Test-Driven Development (TDD)

**Idea:** Write a failing test, make it pass, refactor. Design emerges from tests.

- **Practice:** red → green → refactor; small steps; tests as executable specification
- **Artifacts:** test suites, coverage reports, CI gate
- **AI adaptation:** deterministic code around the model is TDD-able (gateways, parsers, filters, policy engines, tool adapters). Non-deterministic model output is **not** TDD-able in the classic sense — use [evaluation-driven](#evaluation-driven-development-edd) for that layer.
- **Boundary rule:** test the *system* with TDD; measure the *model* with evaluation.

## Behavior-Driven Development (BDD)

**Idea:** Executable scenarios in business language (Given/When/Then) agreed before implementation.

- **Practice:** three-amigos conversations; scenario files live with code; automatable acceptance tests
- **Artifacts:** feature scenarios, acceptance suite
- **AI adaptation:** scenarios assert *properties and acceptable ranges* rather than exact strings — e.g., "Given a refund request over the limit, When the agent evaluates it, Then it escalates for approval and does not issue the refund." Safety behavior is BDD-friendly because it's deterministic.

## Acceptance-Test-Driven Development (ATDD)

**Idea:** Acceptance criteria written collaboratively *before* coding; the acceptance test drives implementation.

- **Artifacts:** acceptance criteria, end-to-end acceptance tests
- **AI adaptation:** include acceptance criteria for refusal behavior, citation presence, and escalation — these are testable conditions.

## Domain-Driven Design (DDD)

**Idea:** Model the business domain explicitly; language, boundaries, and context come first.

- **Practice:** bounded contexts, ubiquitous language, context mapping, anticorruption layers ([patterns](../design-patterns/domain-and-business.md))
- **AI adaptation:** the AI capability belongs inside a bounded context with an owning team; AI supplies judgment where deterministic rules can't reach; domain rules stay deterministic and owned.

## Data-Driven Development

**Idea:** Decisions come from measurement, not opinion.

- **Practice:** define metrics and baselines before change; instrument; compare; iterate
- **Artifacts:** metric definitions, dashboards, experiment results
- **AI adaptation:** applies to *everything* — model choice, prompt changes, retrieval settings, rollout. Every claim ("this is better") needs a number and a baseline.

## Model-Driven Development (MDD)

**Idea:** A model is the source of truth from which implementation is generated.

- **Practice:** domain models, schemas, and interface definitions drive code, docs, and IaC generation
- **Artifacts:** models, generators, generated code
- **AI adaptation:** overlaps with **architecture-as-code** ([pattern](../design-patterns/architecture-as-code.md)). Useful where structure is repetitive (schemas, tool contracts, pipeline definitions); keep abstract models close to the domain, not to tooling.

## Evaluation-Driven Development (EDD)

**Idea:** The AI analogue of TDD — no AI behavior change ships without an evaluation that proves it improved or held.

- **Practice:** golden + adversarial + regression sets; thresholds agreed up front; evaluation in CI; promotion blocked on regression ([pattern](../design-patterns/evaluation-in-ci.md))
- **Artifacts:** evaluation datasets, harness, thresholds, eval reports
- **Applies to:** prompts, models, retrieval configs, chunking, tools, guardrails, agent loops
- **The core AI discipline:** if it changes AI behavior and isn't evaluated, it's a guess in production.

## Prompt-Driven Development

**Idea:** Iterate primarily through prompt/context design, with evaluation measuring each iteration.

- **Practice:** version prompts, evaluate each change, treat prompts as production config ([lifecycle](../lifecycles/prompt-lifecycle.md))
- **Caution:** prompt-only iteration hits a ceiling — when quality stalls, the answer is usually retrieval, data, or task decomposition, not a cleverer prompt.

## Retrieval-Driven Development

**Idea:** For knowledge tasks, drive improvement through retrieval quality before generation tweaks.

- **Practice:** evaluate retrieval independently (hit rate, recall@k, MRR); then generation ([RAG patterns](../design-patterns/rag-patterns.md))
- **Rule:** fix retrieval before prompting.

## Security-Driven Development / DevSecOps

**Idea:** Security activities are embedded in every phase, automated where possible.

- **Practice:** threat modeling at design, SAST/dependency/secrets scanning in CI, red-teaming before launch, policy-as-code ([secure SDLC](../security/secure-sdlc.md))
- **AI adaptation:** assume the model can be manipulated; controls live outside the model; safety filters fail closed.

## API-First / Contract-First / Spec-First Development

**Idea:** Define the interface before implementing either side.

- **Practice:** OpenAPI/schema definitions reviewed before code; consumer-driven contract tests; typed tool contracts ([agent protocols](../standards/agent-protocols.md))
- **AI adaptation:** every agent tool and every AI-to-system integration has a typed contract; model-provided arguments are validated server-side.

## Documentation-Driven Development

**Idea:** Write the docs (and ADRs) as part of the change, not after.

- **Practice:** doc-as-code in the same PR; README quickstarts tested; ADRs for decisions
- **AI adaptation:** prompts, tool contracts, and evaluation criteria are documented artifacts — undocumented AI behavior is unmaintainable behavior.

## Outcome-Driven / Value-Driven Development

**Idea:** Optimize for the business outcome, not the deliverable.

- **Practice:** problem statement + measurable outcome first; baseline captured; value reported post-launch; kill criteria ([business case](../docs/business-case-and-value.md))
- **AI adaptation:** the primary defense against "AI solution looking for a problem."

## Evidence-Driven Architecture

**Idea:** Major technical decisions are justified by prototype results and scored evaluation, not preference.

- **Practice:** time-boxed prototype → research brief → scored evaluation → decision ADR ([technology evaluation](../docs/technology-evaluation-criteria.md))
- **Applies to:** build-vs-buy, platform selection, framework adoption, reference-architecture deviations.

---

## Mapping to lifecycle phases

| Phase | Approaches that apply |
|---|---|
| Discovery & requirements | Domain-driven, behavior-driven, outcome/value-driven |
| Design | Domain-driven, API/contract-first, evidence-driven, security-driven |
| Build | Test-driven, documentation-driven, model-driven |
| AI build & tuning | Evaluation-driven, prompt-driven, retrieval-driven, data-driven |
| Verification | BDD/ATDD, evaluation-driven, security-driven, testing strategy |
| Release | Contract-first, security-driven, documentation-driven |
| Operations | Data-driven, evaluation-driven, outcome-driven |
| Evolution & retirement | Evidence-driven, outcome/value-driven, data-driven |

## Anti-patterns across all approaches

- Applying an approach as ritual (tests that assert nothing, BDD scenarios nobody reads)
- Using TDD expectations for non-deterministic output (flaky tests) instead of evaluation
- Choosing an approach for identity rather than fit
- Adopting "AI-driven" as a synonym for "unmeasured"
