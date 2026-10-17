# Agent Interoperability Standards

**Status:** Proposed · **Last reviewed:** 2026-10-17

Standards for how agents discover and invoke tools and talk to other agents — the contracts that make agent systems integrable, auditable, and portable.

## Principles

1. **Contracts over cleverness** — every tool/exchange has a machine-readable contract with typed inputs and outputs; free-form "call anything" is not an integration
2. **Identity first** — who is calling (workload identity) and on whose behalf (end-user delegation) is explicit in every call
3. **Deny by default** — a tool not in the registry is not callable, regardless of what the model believes

## Tool & context protocols

| Standard style | Use for | Requirements |
|---|---|---|
| **Declarative tool servers** (e.g., Model Context Protocol–style servers) | Exposing enterprise tools and resources to agents via a standard discovery + invocation contract | Contract in version control; server authenticates the agent; per-tool authorization; read/write split |
| **Typed function calling** | Model-native tool invocation inside a single agent loop | Schema validated server-side; never trust model-provided arguments without validation |
| **Agent-to-agent protocols** (e.g., A2A-style exchange) | Multi-agent delegation and task handoff | Explicit delegation chain with the origin user preserved; recipient cannot exceed originator's authority |

> Concrete protocol technologies are approved per [approved-technologies.md](approved-technologies.md). The **requirements above hold regardless of protocol choice**.

## Mandatory requirements for any tool integration

- **Typed contract**: input/output schema, error semantics, idempotency key for writes
- **Side-effect classification**: `read` / `reversible-write` / `irreversible` (drives [HITL approval](../design-patterns/human-in-the-loop-approval.md))
- **Authorization**: least-privilege, short-lived credentials scoped per tool — credentials never enter model context (control AI-4)
- **Validation**: server-side schema and policy validation of everything the model produced
- **Audit**: every invocation logged with run correlation ID (control AI-7)
- **Timeouts & bounds**: rate limits, timeouts, and max-call budgets per run (control AI-8)
- **Versioning**: breaking contract changes require a version bump and consumer notification

## Tool registry

All callable tools live in a per-system registry listing: contract location, owner, credential scope, side-effect class, and authorization policy. The tool router rejects unregistered calls — this registry is the authorization boundary, not the model's prompt.

## Portability stance

Standardize **our contracts** (registry entries, schemas, policies) so the underlying protocol or framework can change. Framework-specific tool definitions that can't leave the framework are a lock-in risk — record such choices as ADRs.

## Review

New agent-to-agent topologies and first-of-kind protocol uses → [T2 central review](../docs/architecture-review-process.md).
