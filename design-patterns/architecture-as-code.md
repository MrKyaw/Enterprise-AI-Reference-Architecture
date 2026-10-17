# Pattern — Architecture as Code

**Status:** Proposed · **Type:** structural/practice

## Context

Architecture artifacts (diagrams, standards, decisions) drift from reality because they live in documents nobody executes. Meanwhile infrastructure is already code — but the *architecture* between the infrastructure and the application remains prose.

## Forces

- Diagrams in wikis rot within months
- Design reviews verify intent, not deployed state
- Reviewers cannot diff a picture
- Environments diverge because provisioning is manual

## Solution

Encode architecture so it can be **versioned, reviewed, tested, and executed**:

1. **Infrastructure as Code** — every environment provisioned through reviewed IaC; no click-ops in production
2. **Policy as Code** — the enforceable subset of [AI security controls](../security/ai-security-controls.md) and [standards](../standards/) expressed as automated checks (allowed egress endpoints, required logging, region restrictions, secret handling)
3. **Architecture models as code** — component views maintained in a machine-readable form (e.g., Mermaid in-repo, or model files) *in the same PR as* the code they describe
4. **Drift detection** — periodic comparison of deployed state against declared state; drift opens a ticket, not a surprise
5. **Blueprints as templates** — [starter kits](../blueprints/) generate IaC + policy checks + eval config together, so conformance is the default output

## Consequences

- ✅ Architecture conformance becomes a CI check rather than a review meeting talking point
- ✅ Reviewers review diffs; environment parity is a byproduct
- ⚠️ Requires discipline: the as-code artifact and the system must change in the same PR
- ⚠️ Over-modeling risk — encode the decisions that matter (controls, boundaries, topology), not every box in every diagram

## Known uses

- Required for [blueprints](../blueprints/) and referenced by [PoC-to-production](../docs/poc-to-production.md) Gate 1
- Infrastructure provisions the component views of all [reference architectures](../reference-architectures/)
