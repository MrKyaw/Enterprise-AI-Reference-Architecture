## What changed

<!-- One concern per PR. State the change type: src / infra / guardrails / eval / docs. -->

## Evidence

- [ ] `PYTHONPATH=src pytest -q` passes
- [ ] Evaluation harness run (link results) — required for any behavior change
- [ ] `terraform plan` output reviewed (for infra changes)
- [ ] No secrets, keys, or real PII added

## Production readiness

- [ ] All model traffic goes through the AI gateway
- [ ] Input screening, PII redaction, and tenant scoping verified
- [ ] Dashboards and alerts updated
- [ ] Rollback and kill switch tested
- [ ] Owner and cost budget recorded in the workload registry
- [ ] Design review checklist completed or deviations recorded as an ADR

## Reviewer routing

- [ ] 1 engineering reviewer
- [ ] 1 security reviewer (guardrails, tools, permissions, or egress changes)
- [ ] 1 architecture reviewer (new kit or reference-architecture deviation)
