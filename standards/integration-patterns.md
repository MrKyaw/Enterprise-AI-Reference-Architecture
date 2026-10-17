# Integration Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Standard ways AI capabilities integrate with the broader enterprise technology landscape. New integrations should copy one of these patterns rather than inventing a new topology.

## Pattern 1 — Gateway-mediated AI calls

Applications call the **AI Gateway** (see [inference reference architecture](../reference-architectures/inference/README.md)); the gateway owns provider selection, guardrails, auth, and cost attribution.

- ✅ Default for all application-to-model traffic
- ✅ Central observability and spend control

## Pattern 2 — Retrieval over governed data

RAG pipelines read from the **data platform**, never directly from source-of-record systems, so classification, retention, and lineage are inherited.

- ✅ Default for grounding on enterprise content
- ✅ Retrieval-time ACLs mirror source-system permissions

## Pattern 3 — Event-driven inference

Upstream systems publish events; an inference consumer scores/enriches and publishes results downstream. Decouples producers from model latency and lifecycle.

- ✅ Batch enrichment, scoring, classification of streams
- ⚠️ Requires idempotent consumers and dead-letter handling

## Pattern 4 — Human-in-the-loop action

Agents propose; policy gates; humans approve; systems act. Approval state is stored outside the model and enforced by the workflow engine.

- ✅ Required for any write or irreversible action by agentic systems
- ✅ Maps to the approval gate in the [agentic reference architecture](../reference-architectures/agentic/README.md)

## Anti-patterns (banned)

- ❌ Provider SDK calls embedded directly in application code (bypasses gateway/guardrails)
- ❌ Model providers called from client-side/browser code
- ❌ AI output written directly to systems of record without validation or approval
- ❌ Shared long-lived API keys across teams
- ❌ Vector indexes that bypass source-system access control

## Choosing a pattern

Unsure which applies? Ask: *who initiates* (app, event, human), *what side effects* (read-only vs write), and *where data lives* (governed platform vs external). When still ambiguous, bring it to [architecture review](../docs/architecture-review-process.md).
