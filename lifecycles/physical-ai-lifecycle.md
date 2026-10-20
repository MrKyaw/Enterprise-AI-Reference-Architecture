# Physical AI Lifecycle

**Status:** Draft · **Primary RA:** [Intelligent automation](../reference-architectures/intelligent-automation/README.md) · **Lifecycle position:** Simulation → real-world deployment → monitoring → retirement

## Problem statement

Bridging the gap between AI systems that reason in simulation and their deployment to physical systems (robotics, autonomous vehicles, drones, industrial automation) where actions have real-world consequences. The core challenge is the sim-to-real gap: models that perform well in simulation may fail unpredictably when deployed on physical hardware due to unmodeled dynamics, sensor noise, and safety constraints.

**Outcome wanted:** a repeatable process for developing, validating, and deploying AI controllers to physical systems with quantified sim-to-real transfer, safety guarantees, and systematic retirement when the system is decommissioned.

## Pain points

| Pain | Consequence |
|---|---|
| Sim-to-real gap unquantified | System works in simulation, fails in production; safety incidents |
| No structured validation before deployment | Deploy too early; costly rework; potential harm |
| Sensor/actuator fidelity limits | Model assumes ideal hardware; real‑world performance degrades |
| Safety envelope undefined | No clear boundaries for acceptable behavior; accident risk |
| Model drift in physical environment | Wear, degradation, environment changes not captured in simulation |
| Retirement / decommissioning hard | Physical system modifications; ecological/environmental cleanup |
| Real‑world data collection expensive | Limited labeled data from physical interactions; sample inefficiency |

## Users & stakeholders

| Role | Interest |
|---|---|
| Robotics engineers | Hardware integration, sim-to-real transfer |
| Safety/compliance | Defined safety envelopes; regulatory adherence |
| Product team | Time-to-deployment; feature delivery pace |
| Operations | System maintenance, fault handling, retirement |
| Risk/governance | Physical harm liability; audit trail |

## Workflow

```mermaid
flowchart TB
    subgraph Simulate [Simulation design & training phase]\n    SD[System definition: dynamics, actuators, sensors]\n    SD --> MT[Model training in simulation]\n    MT --> SV[Simulation validation]\n    SV -->|pass| QS[Quantify sim-to-real gap]\n    SV -->|fail| IT[Iterate: model or simulation]\n    MT --> REG[(Model registry)]\n    end\n    subgraph Validate [Physical validation phase]\n    QS --> PT[Physical test bed: reduced‑scale / lab environment]\n    PT --> PV[Physical validation: safety + quality metrics]\n    PV -->|pass| SC[Scale‑up to full system]\n    PV -->|fail| IT2[Iterate: model, simulation, or hardware]\n    end\n    subgraph Deploy [Real‑world deployment phase]\n    SC --> DD[Device deployment: robot, vehicle, system]\n    DD --> CO[Commissioning + calibration]\n    CO --> MON[Monitoring: safety, drift, performance]\n    MON -->|within bounds| OP[Operational mode]\n    MON -->|violation| EM[Emergency mitigation / stop]\n    end\n    EM --> RF[Retire or redesign]\n    OP --> RET[Scheduled retirement / decommission]\n    RET --> CD[Component cleanup + data retention]\n```

**Human decision points:** sim-to-real gap acceptance; physical test‑bed clearance; emergency mitigation triggers; retirement scheduling.

## Tech stack (layers, not products)

| Layer | Capability | Notes |
|---|---|---|
| Simulation engine | Physics‑based (MuJoCO, PyBullet, Isaac SIM) | Must match real‑world dynamics within acceptance envelope |
| Model architecture | Policy network / dynamics model | Architecture chosen to match observation/actuation bandwidth |
| Sim‑to‑real transfer | Domain randomization, randomized dynamics, CAD‑to‑sim | Critical for closing the gap; measure gap quantitatively |
| Real‑world test bed | Reduced‑scale replica or instrumented lab | Not full production; used for validation before deployment |
| Sensor simulation | Camera, lidar, IMU models with noise profiles | Essential for sim‑to‑real; model generalizes across noise |
| Actuator model | Idealized + friction + wear models | Affects policy real‑world performance |
| Safety envelope | Hard limits on velocity, force, proximity | Programmed into policy; violations trigger emergency stop |
| Simulation‑real logging | Correlated observation‑action trajectories | Required for drift analysis and retraining triggers |

## Trade-offs

| Decision | Option A | Option B | Guidance |
|---|---|---|---|
| Simulation fidelity | Low‑fiction (fast, coarse) | High‑fiction (slow, detailed) | Start low‑fiction for rapid iteration; increase fidelity when gap stalls progress |
| Sim‑to‑real method | Domain randomization only | Domain random + fine‑tuning on real data | Domain randomization first; add real‑world fine‑tuning if gap remains |
| Safety envelope | Soft limits (performance warning) | Hard limits (emergency stop) | Hard limits for any safety‑critical system; soft only for research prototypes |
| Real‑world data collection | Random exploration | Guided exploration (curriculum) | Guided is more sample‑efficient; random only when environment is safe |
| Simulation‑real cycle time | Long (weeks per iteration) | Short (hours per iteration with cloud sim) | Invest in fast simulation first; real‑world cycles are expensive by design |
| Retirement form | Complete disassembly | Partial reuse (re‑purpose hardware) | Plan for reuse where possible; document cleanup requirements |

## Success metrics

| Metric | Target | Measurement |
|---|---|---|
| Sim‑to‑real gap (quality loss) | ≤ 5% accuracy drop | Hold‑out real‑world test set |
| Safety violations | → 0 during validation | Emergency stop triggers |
| Time from simulation start to deployment | Within project timeline | Milestone tracking |
| Sample efficiency (real‑world interactions needed) | Within budget | Number of physical trials |
| Commissioning time (calibration + validation) | ≤ 1 day per deployment | Operational efficiency |
| Retirement clean‑up completeness | 100% documented + executed | Decommission audit |

## Failure modes & mitigations

| Failure | Mitigation |
|---|---|
| Sim‑to‑real gap too large | Increase domain randomization; add real‑world fine‑tuning; revisit model architecture |
| Unmodeled dynamics cause crash | Instrumented test bed early; model-based RL that learns dynamics; safety envelope with emergency stop |
| Safety envelope breached | Hard limits in policy; real‑time monitoring with automated stop; never deploy without safety validation |
| Real‑world data too expensive | Sim2real techniques that minimize real‑world trials; transfer learning from prior systems |
| Retirement creates environmental hazard | Planned decommissioning ADR; component recycling policy; data retention compliance |
| Model drift in field (wear, environment) | Periodic re‑validation on test bed; scheduled retraining with new real‑world data |

## Related artifacts

[Intelligent automation reference architecture](../reference-architectures/intelligent-automation/README.md) · [Simulation‑to‑real transfer patterns](../design-patterns/sim-to-real.md) · [Safety envelope design](../design-patterns/safety-envelope.md) · [Agent lifecycle](../lifecycles/agent-lifecycle.md)

## Physical AI checklist

- [ ] System dynamics and hardware limits documented
- [ ] Simulation engine selected and validated against real hardware specs
- [ ] Model trained in simulation with quantifiable gap target
- [ ] Domain randomization configured and tested
- [ ] Physical test‑bed validation passed (safety + quality)
- [ ] Safety envelope defined and baked into policy
- [ ] Sensor/actuator models configured with realistic noise/wear
- [ ] Commissioning + calibration plan documented
- [ ] Monitoring + alerting configured for safety violations
- [ ] Retirement / decommissioning ADR documented

--- 

*Physical AI lifecycle version 0.1 — Last updated: 2026-10-19*