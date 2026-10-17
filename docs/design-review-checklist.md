# Design Review Checklist

**Status:** Proposed · Used by T0 self-certification through T3 central review. Items marked **[SEC]** require Cybersecurity sign-off; **[EA]** require Enterprise Architecture alignment.

## 1. Scope & alignment

- [ ] The design names which [reference architecture](../reference-architectures/) it follows
- [ ] Deviations are listed explicitly, each with an ADR and justification
- [ ] Workload type(s) identified: training / inference / RAG / agentic / fine-tuning
- [ ] **[EA]** Data, cloud platform, and enterprise architecture teams' standards are respected (networking, identity, data platform)

## 2. Technology

- [ ] All frameworks, providers, and platforms are on the [approved list](../standards/approved-technologies.md)
- [ ] New/unapproved technologies include a completed [evaluation](technology-evaluation-criteria.md) and a build-vs-buy note if applicable
- [ ] Model provider data-handling terms reviewed per [model-provider-standards.md](../standards/model-provider-standards.md)

## 3. Data

- [ ] Data classification identified; only permitted classes touch the system
- [ ] Retention and deletion requirements implemented end-to-end (including indexes, logs, caches)
- [ ] For RAG: retrieval-time access control verified against a negative test case
- [ ] For fine-tuning: lawful basis and consent for training data documented

## 4. Security **[SEC]**

- [ ] All model traffic goes through the AI gateway; no direct provider keys in code
- [ ] Guardrails configured for user-facing inputs and outputs
- [ ] Prompt-injection threat modeled; untrusted content treated as untrusted everywhere
- [ ] Least-privilege credentials per component; no shared long-lived keys
- [ ] Agentic: side-effect classification complete; approval gate enforced outside the model; egress allowlisted; kill switch present
- [ ] Findings from [red-team exercises](../security/red-team-integration.md) addressed or scheduled

## 5. Reliability & operations

- [ ] SLOs defined (availability, latency, quality) with monitoring in place
- [ ] Degradation path defined (fallback model / non-AI path) for user-facing systems
- [ ] Cost model estimated; budgets and alerting configured; per-project attribution enabled
- [ ] Change management: canary/shadow rollout for model or prompt changes
- [ ] Incident runbook exists and names an on-call owner

## 6. Quality & evaluation

- [ ] Evaluation dataset exists with golden examples and adversarial cases
- [ ] [Evaluation in CI](../design-patterns/evaluation-in-ci.md) configured with explicit thresholds
- [ ] Baseline metrics recorded before changes; comparison on every model/prompt update

## 7. Records

- [ ] ADRs filed for every deviation and significant choice
- [ ] Checklist (this document, completed) archived with the design
