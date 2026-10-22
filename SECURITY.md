# Security Policy

## Reporting a vulnerability

**Do not open a public issue for security vulnerabilities.**

Use GitHub's **private vulnerability reporting** for this repository:

`Security` tab → *Report a vulnerability* → describe the issue

If private reporting is unavailable, use an explicitly offered private contact option on the maintainer's GitHub profile. If no private route is available, request a private contact method without posting vulnerability details or secrets in a public issue. No response-time SLA is promised.

### What to include

- Affected document, pattern, control, or blueprint
- The risk: what could be enabled or exposed if the weakness is followed or exploited
- A concrete scenario or reproduction (e.g., a design that passes the checklist but violates a control)
- Suggested remediation, if you have one

### What to expect

- **Confirmed** → remediation committed, credit offered if desired, coordinated disclosure date agreed
- **Not confirmed** → explanation of the triage reasoning
- Reports that identify *gaps in our published security controls* are treated as first-class findings — this repository's whole purpose is to prevent those gaps in systems built from it

## Scope

In scope:

- [AI security controls](security/ai-security-controls.md) that are incorrect, incomplete, or self-contradictory
- Reference architectures and patterns that would lead an implementing team to a vulnerable system
- Blueprints/starter kits containing insecure defaults, secrets, or unsafe infrastructure configuration
- Injection, authorization, or data-leakage flaws in example code or templates

Out of scope:

- Third-party products, model providers, or platforms referenced by name in standards (report those upstream)
- Reports without a demonstrable impact on designs or artifacts in this repository

## Supported versions

This repository is a living document set. Security-relevant content is supported on the latest commit of `main`; older revisions should not be used for production designs. Material security fixes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Disclosure process

1. Report received and triaged privately
2. Fix prepared and reviewed (per [CONTRIBUTING.md](CONTRIBUTING.md) security routing)
3. Fix merged; affected documents updated with status and review dates
4. CHANGELOG entry published; coordinated disclosure if appropriate

## Relationship to red-teaming

Red-team findings from operational systems feed back through [security/red-team-integration.md](security/red-team-integration.md). Vulnerability reports against *this repository* feed the same loop: generalized findings become control or reference-architecture updates here.

## Public examples and confidentiality

This repository is public guidance and scaffolding. Never submit live credentials, customer transcripts, private topology, cloud state, or restricted benchmark data. Synthetic fixtures, regex redaction, and a passing secret scan do not establish that an artifact is safe to publish. Review the [publication checklist and evidence](docs/publication-review.md), including historical Git metadata and copies outside the repository. A suspected exposure requires credential rotation and an incident assessment; deleting the current file alone is insufficient.
