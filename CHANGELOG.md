# Changelog

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
for content releases (`MAJOR` = breaking changes to standards or reference architectures,
`MINOR` = new documents/standards, `PATCH` = corrections and clarifications).

## [Unreleased]

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
