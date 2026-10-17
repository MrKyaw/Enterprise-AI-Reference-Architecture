# Security Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Security-by-design patterns for AI systems. Control requirements live in [AI security controls](../security/ai-security-controls.md); these are the *implementation shapes* that satisfy them.

## Foundational patterns

| Pattern | Intent | Maps to |
|---|---|---|
| **Defense in depth** | Multiple independent layers so one bypass isn't a breach | All controls |
| **Zero trust** | Authenticate and authorize every call; no implicit network trust | AI-1, AI-4 |
| **Least privilege** | Minimum scope, minimum duration, per component/tool | AI-4 |
| **Separation of duties** | Builder cannot self-approve high-risk capability | Model risk lifecycle |
| **Fail closed** | Safety checks deny/abstain when unavailable | AI-2, AI-5 |
| **Trust boundaries explicit** | Diagram where trust changes; validate at each crossing | AI-3, AI-6 |
| **Immutable audit log** | Write-once record of decisions and actions | AI-7 |

## Identity & secret patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Secret vaulting + short-lived credentials** | No long-lived keys in code/config | Rotation automation |
| **Workload identity (no static keys)** | Platform-issued identity per service | Requires platform support |
| **User delegation** | Agent acts *as the user*, never above them | Must preserve origin identity through chains |
| **Per-tool service accounts** | Isolate blast radius per tool | Management overhead |
| **Just-in-time elevation** | Grant elevated access only for a bounded task | Needs logging and time bounds |
| **No secrets in prompts/context** | Credentials never enter model context | Enforce via assembly, not instructions |
| **Key rotation & revocation runbook** | Recover from compromise | Tested before needed |

## Prompt-injection & untrusted-content patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Instruction/data separation** | Delimit untrusted content clearly | Prompt-only defense is insufficient alone |
| **Authority from the system, not content** | Tool availability/permissions decided by the router, not the text | Requires external enforcement |
| **Input screening** | Detect known injection signatures | Signature drift; false positives |
| **Content provenance tagging** | Track where each context element came from | Enables policy by source |
| **Untrusted tool output handling** | Treat tool/API responses as untrusted input | Includes retrieved docs and emails |
| **Capability-scoped context** | Only expose tools relevant to the task | Reduces attack surface |
| **Canary/spotlighting techniques** | Mark and monitor injected-content influence | Evolving area; test empirically |
| **Sandbox execution** | Contain the effect of a successful injection | Control AI-11 |

## Data-protection patterns

| Pattern | Intent |
|---|---|
| **Classification at the boundary** | Apply handling rules when data crosses into AI |
| **Redaction/pseudonymization before prompt** | Minimize personal data sent to models |
| **Retrieval-time authorization** | Enforce permissions before results return |
| **Tenant isolation** | Separate memory, caches, indexes per tenant |
| **Egress allowlist + DLP** | Prevent exfiltration via model calls |
| **Output filtering** | Remove secrets/PII/policy-violating content |
| **Deletion propagation** | Derived copies (embeddings, caches, logs) deleted with source |
| **Encryption in transit + at rest** | Baseline hygiene, including vector stores |

## Application & platform patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **API gateway enforcement** | Central auth, rate limit, audit ([llm-gateway](llm-gateway.md)) | Single point of failure — make it highly available |
| **Policy as code** | Enforceable controls checked automatically | Keep checks fast and precise |
| **Supply-chain verification** | Pin and scan dependencies and model artifacts (AI-9) | Model artifact scanning is newer — still required |
| **Signed artifacts & provenance** | Verify what's deployed | Signing infrastructure |
| **Secrets scanning in CI** | Prevent credential commits | Even for AI-generated code |
| **Network segmentation for AI planes** | Bounded blast radius (control AI-11) | Operational complexity |
| **Break-glass procedure** | Emergency access with audit | Post-incident review mandatory |

## Verification patterns

| Pattern | Intent |
|---|---|
| **Negative testing** | Prove access control denies unauthorized retrievals/actions |
| **Adversarial/red-team suites** | Continuous injection and abuse testing ([red team](../security/red-team-integration.md)) |
| **Abuse-case-driven tests in CI** | Automate known attack classes |
| **Permission diffing** | Detect privilege creep in tool credentials |
| **Tool-call authorization tests** | Prove unregistered tools and unauthorized args are rejected |
| **Kill-switch drills** | Prove containment works |

## Pattern selection by attack

| Attack | Primary patterns |
|---|---|
| Indirect prompt injection via documents | Instruction/data separation, authority from system, sandbox, output filtering |
| Data exfiltration through model calls | Egress allowlist, DLP, minimization, retrieval-time ACLs |
| Unauthorized agent action | Tool registry allowlist, per-tool identity, HITL gate, authorization boundary |
| Credential theft | Vaulting, short-lived tokens, workload identity, rotation |
| Cross-tenant leakage | Tenant isolation, scoped memory, cache separation |
| Poisoned knowledge base | Ingestion screening, provenance, anomaly detection, versioned rollback |
| Cost abuse / DoS | Rate limits, budgets, loop detection, quotas |

## Anti-patterns

- Prompt instructions as the only injection defense
- Safety filters configured fail-open
- One shared credential for all tools and agents
- Retrieved content able to change tool availability
- Audit logs mutable or missing correlation IDs
- Permissions granted "temporarily" and never reviewed
