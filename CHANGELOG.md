# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
for content releases (`MAJOR` = breaking changes to standards or reference architectures,
`MINOR` = new documents/standards, `PATCH` = corrections and clarifications).

## [Unreleased]

### Added

- Repeatable tracked-Markdown and Mermaid validation with pinned Node dependencies, repaired documentation CI, and publication review guidance.

- Practical architecture leadership guide with 16 Amazon principles mapped to working behaviors and evidence, ten complementary leadership approaches, eight customer stages, an illustrative retail integration, customer relationship habits, and authentic interview guidance.
- Reusable architecture leadership engagement worksheet for baselines, decision rights, experiments, delivery readiness, and business outcome reviews; linked from governance, lifecycle, resource, and root navigation.

- **Architect resource hub** (`resources/README.md`) — full competency framework with embedded diagrams, 12 role paths, 40+ books, 25+ YouTube channels, certifications, official docs/standards, 14 foundational papers, newsletters/podcasts/communities, 60+ tools, 14 labs, and 90-day plans
- **16 new starter kits**, bringing the total to 17:
  - Reference architectures: `rag`, `agent`, `data-agent`, `copilot`, `fine-tuning`, `training`, `intelligent-automation`
  - Specialized domains: `edge-ai`, `physical-ai`, `embodied-ai`, `quantum`, `agent-factory`
  - Cross-cutting: `evaluation`, `observability`, `ai-security`, `integration`
  - Each kit ships a working FastAPI skeleton, pipeline stub, guardrails, smoke tests, Terraform baseline, non-root Dockerfile, and production checklist
- **5 new lifecycle domains** — Edge AI, Quantum Computing, Agent Factory, Physical AI, Embodied AI (all 22 target domains now covered)
- **Issue templates** — `bug_report.yml`, `feature_request.yml`

### Fixed

- Replaced unsupported embedding benchmark/cost findings with explicitly unexecuted evaluation plans.
- Corrected literal-newline and syntax defects in specialized lifecycle diagrams; removed placeholder reviewer teams and unsupported security response promises.

- Broken internal links across use-case index, research briefs, blueprint catalog, starter kit, and new lifecycle references
- Blueprint catalog now reflects what actually exists (previously claimed unbuilt kits as scaffolded)

### Changed

- Reconciled README and About metadata with the actual catalog; clarified proposed standards, illustrative failure scenarios, public-data boundaries, and all 17 unauthenticated starter scaffolds.

- README blueprint section now lists all 17 kits and their groups
- Resources section in README expanded with counts and direct link to the hub
- All 17 starter kits now share the same layout: FastAPI service, pipeline stub, guardrails, smoke tests, Terraform baseline, non-root Dockerfile, and PR checklist
- Lifecycle count corrected to **24** across the README (the previous table showed 19 with duplicate numbering and omitted the 5 specialized lifecycles)
- Lifecycles index now lists all 24 lifecycle files and maps the 5 specialized ones to their starter kits; the solution design lifecycle remains in `docs/`
- Blueprint catalog now shows an explicit status per kit (all ✅ Scaffolded)

## [0.4.0] - 2026-10-17

### Added

**Lifecycles (6 more, now 19 total)** — `api-lifecycle`, `experimentation-lifecycle` (incl. progressive feature release), `finops-cost-lifecycle`, `documentation-knowledge-lifecycle`, `vendor-third-party-lifecycle`, `enablement-adoption-lifecycle`

**Pattern catalogs (3 more, now 13 total)** — `ai-ux-and-interaction`, `distributed-scaling` (incl. multi-tenancy isolation), `cost-finops`

**Approaches** — `delivery-and-practice-approaches`: hypothesis-driven, risk-first, design thinking, dual-track agile, DevOps/CD, trunk-based, GitOps, platform engineering, SRE/error budgets, chaos engineering, data-centric AI, benchmark-driven, simulation-driven, ontology-driven, postmortem-driven, Six Sigma/DMAIC, agent-assisted development

**Use cases (`use-cases/`)** — 8 end-to-end scenarios, each with problem statement, pain points, users, workflow diagram, tech stack, trade-offs table, success metrics, failure modes, and future work:
enterprise knowledge assistant · NL analytics data agent · agentic process automation · enterprise copilot rollout · domain model adaptation · real-time decision scoring · document intelligence pipeline · AI platform foundation

**Production issues (`production-issues/`)** — 79 real failure modes across 6 categories with symptom, root cause, impact, fix, prevention, and future work, plus a five-cause cross-cutting analysis:
quality & hallucination · retrieval & data · cost & latency · security & injection · agents & tools · platform, operations & lifecycle

**Completeness updates** — README collection table, repository map, tree, workflows, documentation catalog; `docs/README.md` related collections; `CODEOWNERS`; `CONTRIBUTING.md` branch prefixes

## [0.3.0] - 2026-10-17

### Added

**Lifecycles (`lifecycles/`)** — 13 end-to-end lifecycles with phase/artifact/exit-gate tables, plus a phase/artifact completeness matrix and nesting diagram:
- `software-development-lifecycle`, `ml-project-lifecycle`, `mlops-lifecycle`
- `genai-llmops-lifecycle`, `rag-lifecycle`, `agent-lifecycle` (AgentOps, autonomy levels L0–L4)
- `data-lifecycle`, `prompt-lifecycle`, `evaluation-lifecycle`
- `product-lifecycle`, `model-risk-lifecycle`, `operations-incident-lifecycle`, `technology-lifecycle`

**Design pattern catalogs (`design-patterns/`)** — 10 category catalogs with intent/applicability/pitfalls:
- `general-architecture`, `data-architecture`, `ml-engineering`, `mlops-deployment`
- `genai-prompting` (incl. guardrail sandwich, cascades, caches), `rag-patterns` (chunking/query/retrieval/generation/adaptive/evaluation)
- `agent-patterns` (core loop, memory, multi-agent, safety/control, orchestration), `reliability-resilience`
- `security-patterns` (incl. attack→pattern mapping), `domain-and-business` (DDD, discovery and business-analysis techniques)
- Rebuilt `design-patterns/README.md` as a category index with a cross-cutting pattern map and a "you need → start with" selector

**Approaches (`approaches/`)**:
- `driven-development-approaches` — TDD, BDD, ATDD, DDD, data-, model-, evaluation-, prompt-, retrieval-, security-, API/contract/spec-, documentation-, outcome/value-driven, and evidence-driven architecture, each with its AI adaptation
- `testing-strategy` — full test-type catalog, AI-specific test/evaluation layers, non-determinism handling, coverage by risk tier, per-workload emphasis, and where tests run

**Cross-cutting**
- Root README: "What's inside" collection table; repository map and directory tree updated for the new collections
- `docs/README.md`: Related collections section
- `CODEOWNERS`: ownership for `lifecycles/` and `approaches/`

## [0.2.0] - 2026-10-17

### Added

**Reference architectures**
- Three new workload types: `data-agent` (natural-language query over governed data), `copilots` (embedded AI in enterprise applications), `intelligent-automation` (workflow + RPA + AI)

**Governance docs**
- `non-functional-requirements.md` — NFR set with numbers, not adjectives
- `poc-to-production.md` — five gated transitions to sustained operation
- `solution-design-lifecycle.md` — discovery → design → diligence → deployment → expansion
- `business-case-and-value.md` — opportunity discovery, ROI, KPIs, kill criteria
- `legacy-modernization.md` — incremental AI on existing systems

**Standards**
- `agent-protocols.md` — typed tool contracts, tool registry as authorization boundary
- `ai-assisted-development.md` — safe use of AI coding assistants

**Patterns**
- `architecture-as-code.md` — versionable, reviewable, executable architecture
- `semantic-layer-grounding.md` — governed business definitions as AI ground truth

**Security**
- `secure-sdlc.md` — security checkpoints per lifecycle phase
- New controls: AI-11 (sandbox isolation & authorization boundaries), AI-12 (secure SDLC gates)

**Repository**
- Professional community docs: `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates
- Upgraded root README: badges, table of contents, repository map, workflows, documentation catalog

### Changed

- Evaluation pattern extended with AI-specific metrics: task success rate, tool-call accuracy, reasoning integrity, ambiguity handling
- HITL approval pattern extended with escalation policies and sandbox dry-runs
- Design review checklist references NFRs, agent-protocol standards, and AI-assisted development rules

## [0.1.0] - 2026-10-17

### Added

- Initial structure: 5 reference architectures (training, inference, RAG, agentic, fine-tuning)
- Standards: approved technologies, model providers, integration patterns
- Governance: architecture review process (T0–T3), design review checklist, technology evaluation criteria, build-vs-buy framework
- Security: 10 AI security controls, red-team integration loop
- Research pipeline: briefs and time-boxed prototype templates
- ADR system with template and index
- Design patterns: LLM gateway, human-in-the-loop approval, evaluation in CI
- Blueprints concept, templates, `.github` PR template and CODEOWNERS
- Repository foundations: README, CONTRIBUTING, MIT license
