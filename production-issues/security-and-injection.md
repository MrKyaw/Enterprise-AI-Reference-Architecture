# Production Issues — Security & Injection (`S-`)

Security failures specific to AI systems. The category is dominated by one insight: **the model processes attacker-influenced input by design, so controls must live outside it.**

## Index

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| S-01 | Agent/assistant follows instructions hidden in retrieved content | Indirect prompt injection; content treated as instructions | Critical: unauthorized actions, data exfil | Instruction/data separation; authority from system; sandbox; input screening |
| S-02 | System prompt or internal instructions leaked | Prompt extraction attack | Exposure of logic/config; enables further attacks | Don't put secrets in prompts; treat prompt as discoverable; output filtering |
| S-03 | Sensitive data sent to a model provider inadvertently | No classification check at the context boundary | Regulatory breach | Classification-aware minimization; redaction before prompt |
| S-04 | Data exfiltration via markdown links or tool arguments | Model-induced exfiltration to attacker-controlled endpoints | Critical: data theft | Egress allowlists; render-time link scrutiny; DLP on model egress |
| S-05 | Provider key discovered in a repository | Keys in code/config rather than a vault | Account takeover; spend abuse | Rotate immediately; vault + short-lived credentials; secret scanning |
| S-06 | Cross-tenant data visible in answers or memory | Shared caches/indexes/memory without tenant scoping | Critical: multi-tenant breach | Tenant-scoped stores/caches; per-tenant quotas; isolation tests |
| S-07 | Guardrails bypassed by encoding or paraphrase | Signature-based filters only | Safety/policy violation | Layered defenses; semantic screening; adversarial test evolution |
| S-08 | Safety filter failed open during a dependency outage | Guardrail service unavailable; fail-open default | Unfiltered content reaches users | Fail-closed configuration; degrade to blocking |
| S-09 | Malicious content poisoned the knowledge base | Unvetted ingestion or compromised source | Persistent, hard-to-detect misinformation | Ingestion screening; provenance; anomaly detection; versioned rollback |
| S-10 | Over-broad service account used by an agent | Convenience credential shared across tools | Large blast radius on compromise | Per-tool least privilege; short-lived tokens |
| S-11 | PII appears in logs, traces, or evaluation datasets | No redaction at the logging boundary | Compliance exposure | Redaction pipeline; classification-aware retention |
| S-12 | Model artifact or dependency supply-chain compromise | Unverified artifacts/dependencies | Critical: code execution, data exposure | Pin + verify + scan artifacts and dependencies |
| S-13 | Unauthorized action allowed because the tool registry wasn't the authority | Tool availability influenced by model output | Unauthorized writes | Registry as the authorization boundary; router-side enforcement |

---

## S-01 — Indirect prompt injection via retrieved content

**Symptom:** After ingesting a document, page, ticket, or email containing hidden instructions, the assistant takes an unintended action or reveals information. The user did nothing wrong.

**Root cause:** Untrusted content is concatenated into the same channel as system instructions, and the model cannot reliably distinguish them. Any system where retrieved/ingested content can influence tool availability or permissions is exploitable.

**Impact:** **Critical** for agentic systems — this is the primary path from a data problem to unauthorized action. For read-only assistants the impact is data disclosure or reputational.

**Fix:** Contain first: disable the affected capability or narrow tool availability. Then add instruction/data separation and verify with an injection test suite that includes the payload that succeeded.

**Prevention:** [Prompt-injection defense patterns](../design-patterns/security-patterns.md) — instruction/data separation, authority derived from the system rather than content, tool registry allowlist, sandbox isolation (control AI-11), egress allowlists, and mandatory [red-teaming](../security/red-team-integration.md) before launch.

**Future work:** Robust provenance-aware context handling; model-assisted injection detection; standard adversarial corpora for indirect injection; capability-scoped context that reduces the attack surface per task.

---

## S-04 — Data exfiltration via generated links

**Symptom:** A generated response includes a link or a tool argument containing sensitive data from the user's context, pointing to an external endpoint.

**Root cause:** The model composes markdown/URLs from context; nothing inspects outbound content or tool arguments for encoded sensitive data. Rendering or a subsequent fetch completes the leak.

**Impact:** **Critical.** Silent data theft that leaves no obvious trace in application logs if egress isn't inspected.

**Fix:** Block the egress path; add outbound DLP inspection for model egress and tool arguments; sanitize rendered links (no auto-fetch, no external image loading).

**Prevention:** [Egress allowlist + DLP patterns](../design-patterns/security-patterns.md), render-time link scrutiny in [AI UX patterns](../design-patterns/ai-ux-and-interaction.md), and controls AI-1/AI-6.

**Future work:** Semantic exfiltration detection for unusual encodings; provenance tagging so the UI can mark context-derived content in links; tool-argument policy engines with data-classification awareness.

---

## S-08 — Safety filter failed open

**Symptom:** During a dependency outage, unfiltered or policy-violating content reached users.

**Root cause:** Guardrail calls failed (timeout, error), and the calling code defaulted to "proceed" because failure handling was written as "don't block the user." This is the most dangerous default in AI systems.

**Impact:** **Critical** when filters enforce legal, safety, or policy requirements.

**Fix:** Change the default to fail-closed; add a cached/static conservative filter as an intermediate degradation step; verify with a failure drill.

**Prevention:** Fail-closed principle ([security patterns](../design-patterns/security-patterns.md)), explicit degradation ladder for guardrails ([reliability](../design-patterns/reliability-resilience.md)), and chaos drills that kill the guardrail dependency ([operations lifecycle](../lifecycles/operations-incident-lifecycle.md)).

**Future work:** In-process lightweight guardrails as a last line when central services are unavailable; standardized fail-closed templates for AI components; automated verification that degradation paths deny by default.

---

## S-06 — Cross-tenant data leakage

**Symptom:** A user in one tenant sees content or memory from another tenant, often in a shared cache or shared semantic index.

**Root cause:** Shared infrastructure without a tenant dimension in the cache key, index filter, or memory scope. Frequently introduced by an optimization ("let's share the cache to save money") that didn't account for isolation.

**Impact:** **Critical.** Multi-tenant breach with contractual and regulatory consequences.

**Fix:** Purge shared caches and memory; add the tenant dimension to every key and every query filter; audit for other shared-state paths.

**Prevention:** [Multi-tenancy isolation patterns](../design-patterns/distributed-scaling.md), tenant-aware caching and memory in the [agent lifecycle](../lifecycles/agent-lifecycle.md), and isolation tests in the [testing strategy](../approaches/testing-strategy.md).

**Future work:** Automated isolation verification in CI for every shared component; tenant-boundary policy enforcement at the platform layer; isolation test suites generated from the data model rather than hand-written.
