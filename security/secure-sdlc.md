# Secure SDLC for AI Systems (SSDLC)

**Status:** Proposed · **Owner:** Cybersecurity (with AI Architecture) · **Last reviewed:** 2026-10-17

Security activity embedded into the AI delivery lifecycle — not bolted on before go-live. Every phase below has a security checkpoint; [design reviews](../docs/architecture-review-process.md) verify these activities are scheduled and later verified.

## Phases

### 1. Concept & architecture
- Threat model started: assets, trust boundaries, attacker goals, abuse cases
- [AI security controls](ai-security-controls.md) mapped to the design (checklist section 4)
- Data classification and lawful basis established
- **Gate:** design review outcome (T1–T3 as applicable)

### 2. Design
- Data-flow diagrams with trust boundaries reviewed by Cybersecurity
- Third-party/model-provider terms reviewed per [model-provider-standards](../standards/model-provider-standards.md)
- Abuse cases defined: prompt injection vectors, tool abuse, data exfiltration, cost abuse
- **Gate:** security sign-off on design

### 3. Build
- Secure coding standards + [AI-assisted development](../standards/ai-assisted-development.md) review rules
- SAST, dependency, and secrets scanning in CI — unchanged by AI-generated code
- Tool contracts validated against the [agent registry requirements](../standards/agent-protocols.md)
- No production credentials in development environments
- **Gate:** CI green including security checks

### 4. Test
- [Red-team exercise](red-team-integration.md) for agentic and user-facing systems
- Abuse-case tests automated where possible (injection suites in the evaluation pipeline)
- Access-control negative tests (retrieval-time authorization, row-level policy)
- **Gate:** red-team findings triaged with remediation plan

### 5. Deploy
- Infrastructure via IaC with [policy-as-code](../design-patterns/architecture-as-code.md) checks
- Artifact scanning (control AI-9) before promotion
- Logging, alerting, and kill switch verified in production configuration
- **Gate:** readiness review includes security items

### 6. Operate
- Incident runbook includes AI-specific scenarios: jailbreak waves, tool-abuse runs, provider compromise, data leakage via prompts
- Vulnerability and dependency management cadence for AI stack (frameworks, model runtimes, tool servers)
- Quarterly control attestation for high-risk systems

### 7. Change & retire
- Model, prompt, guardrail, and tool changes follow [evaluation-in-ci](../design-patterns/evaluation-in-ci.md); material capability changes re-trigger red-teaming
- Retirement: data deletion propagates to indexes, caches, logs, and fine-tuning datasets; credentials revoked; tool registry entries removed

## Roles

| Activity | Responsible |
|---|---|
| Threat model, red team, security sign-off | Cybersecurity |
| Control mapping, design conformance | AI Architecture |
| Remediation, scanning, runbooks | Delivery team |

## Verification

The [design review checklist](../docs/design-review-checklist.md) links each applicable SSDLC artifact; T2/T3 reviews confirm phase gates before deployment approval.
