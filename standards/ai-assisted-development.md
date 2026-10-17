# AI-Assisted Development Standards

**Status:** Proposed · **Last reviewed:** 2026-10-17

Standards for using AI coding assistants (IDE copilots, agentic coding tools, code review assistants) in the development of our systems — including the AI systems themselves.

## Approved usage

- AI-assisted completion, refactoring, test generation, and documentation are **encouraged** for productivity
- Agentic coding tools (autonomous multi-file edits, terminal access) are **allowed with review discipline** below
- Tool selection from the [approved list](approved-technologies.md); enterprise tier with no-training-on-our-code terms required

## Non-negotiable rules

1. **Humans own every line.** The author is accountable for code they commit, AI-generated or not — "the tool wrote it" is not a defense in incident review
2. **No secrets in prompts.** Source code, credentials, and regulated data do not go into unapproved tools; only approved enterprise tiers may process our code
3. **Stronger review for generated code**, not weaker: complexity, error handling, and security implications reviewed with extra care — generated code is fluent before it is correct
4. **Security scanning unchanged.** [SSDLC](../security/secure-sdlc.md) gates (SAST, dependency scanning, secrets detection) apply identically — AI does not earn exemptions
5. **No direct AI output into production.** AI-generated changes to critical paths (auth, data access, agent tools, guardrails) get human pairing, not rubber-stamping

## Tool tiers

| Tier | Examples of use | Requirements |
|---|---|---|
| **Assistive** | Completion, chat, doc generation | Approved tool; no secrets in content |
| **Agentic (workspace)** | Multi-file refactors, scaffolding, test authoring | All changes reviewed in PR; author read every diff |
| **Agentic (environment)** | Terminal access, running commands, dependency changes | Sandbox/branch only; no prod credentials; output reviewed before merge |

## Special rules for AI-system code

AI-generated code that touches **prompts, guardrails, tool definitions, evaluation thresholds, or agent policies** requires two human reviewers from the architecture/security circle — this is exactly where plausible-looking-but-wrong output is most dangerous.

## Measurement

Track adoption (suggest acceptance rate, PR throughput) against [business-case-and-value](../docs/business-case-and-value.md) practices — productivity claims get measured, not assumed. Watch for regressions in defect escape rate as the counter-metric.
