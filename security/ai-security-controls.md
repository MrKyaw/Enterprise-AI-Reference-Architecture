# AI Security Controls

**Status:** Proposed · **Owner:** Cybersecurity (with AI Architecture) · **Last reviewed:** 2026-10-17

Mandatory control set for AI/ML workloads. Controls are referenced by every [reference architecture](../reference-architectures/) and by [design review checklist](../docs/design-review-checklist.md) section 4.

## AI-1 — Gateway enforcement

All model traffic transits the AI gateway. No direct provider endpoints or embedded provider keys in applications. Egress allowlists at network layer as defense in depth.

## AI-2 — Input/output guardrails

User-facing inputs and model outputs pass filtering for prompt-injection signatures, PII, secrets, and topic policy. Filters are updated from red-team findings ([red-team-integration.md](red-team-integration.md)).

## AI-3 — Prompt-injection resilience

All external content (web pages, emails, retrieved documents, tool outputs) is treated as untrusted input:

- Never concatenate untrusted content into privileged instructions
- Retrieved content cannot modify the system's permissions or policy
- Tool selection cannot be influenced by content alone — enforced in the tool router

## AI-4 — Least-privilege credentials

- Per-component, per-tool credentials scoped to the minimum resources
- Short-lived tokens with automatic rotation; no shared service accounts across agents
- Agent credentials are never exposed to model context

## AI-5 — Human approval for side effects

Write and irreversible actions pass an external approval gate per [human-in-the-loop-approval](../design-patterns/human-in-the-loop-approval.md). Approvals expire to deny.

## AI-6 — Data protection

- Classification enforced at ingestion, retrieval, and logging paths
- PII redaction before any prompt/log leaves the trust boundary
- Zero-data-retention contractual terms with model providers
- Deletion requests propagate to indexes, caches, logs, and fine-tuning datasets

## AI-7 — Immutable audit logging

Every step, tool call, approval, and output correlated by run ID and retained per regulatory schedule. Logs are write-once.

## AI-8 — Bounded autonomy & kill switch

Max steps, max cost, max wall-clock per agent run. Central kill switch per agent/system, tested quarterly.

## AI-9 — Artifact scanning

Training and fine-tuned artifacts scanned (malware, secrets, provenance) before promotion to the registry or serving.

## AI-10 — Adversarial testing before production

Agentic and user-facing systems complete a red-team exercise per [red-team-integration.md](red-team-integration.md) before go-live, and after major capability changes.

## AI-11 — Sandbox isolation & authorization boundaries

- Agent and automation execution happens in an isolated environment (network segment or container boundary) with least-privilege access — blast radius of a manipulated agent is bounded by infrastructure, not by prompt text
- Every autonomous decision path declares an explicit **authorization boundary**: the maximum authority a run can exercise without human approval
- Irreversible/high-impact actions remain behind the AI-5 approval gate regardless of autonomy level

## AI-12 — Secure SDLC integration

Security checkpoints from [secure-sdlc.md](secure-sdlc.md) are phase gates in delivery: threat model at design, scanning in CI, red-team at test, control verification at deploy. Skipped gates block release — see [PoC-to-production Gate 2](../docs/poc-to-production.md).

## Mapping

| Control | Training | Inference | RAG | Agentic | Fine-tuning |
|---|---|---|---|---|---|
| AI-1 Gateway | | ✅ | ✅ | ✅ | |
| AI-2 Guardrails | | ✅ | ✅ | ✅ | |
| AI-3 Injection resilience | | | ✅ | ✅ | |
| AI-4 Least privilege | ✅ | ✅ | ✅ | ✅ | ✅ |
| AI-5 Approval gate | | | | ✅ | |
| AI-6 Data protection | ✅ | ✅ | ✅ | ✅ | ✅ |
| AI-7 Audit logging | ✅ | ✅ | ✅ | ✅ | ✅ |
| AI-8 Bounded autonomy | | | | ✅ | |
| AI-9 Artifact scanning | ✅ | | | | ✅ |
| AI-10 Red teaming | | ✅ | ✅ | ✅ | |
| AI-11 Sandbox & authorization boundaries | ✅ | | | ✅ | ✅ |
| AI-12 Secure SDLC gates | ✅ | ✅ | ✅ | ✅ | ✅ |

## Related processes

- [Secure SDLC](secure-sdlc.md) — phase-by-phase security checkpoints
- [Red-team integration](red-team-integration.md) — adversarial findings feed control updates
- [Agent protocols](../standards/agent-protocols.md) — tool registry as the authorization boundary
