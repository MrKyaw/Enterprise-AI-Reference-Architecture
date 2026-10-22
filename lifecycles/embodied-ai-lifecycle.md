# Embodied AI Lifecycle

**Status:** Draft · **Primary RA:** [Agentic](../reference-architectures/agentic/README.md) · **Lifecycle position:** Perception‑action loop → sensorimotor learning → environment interaction → retirement

## Problem statement

Embodied AI focuses on agents that live inside a body (robot, agent, organism) and must learn to perceive, act, and survive in a continuous environment. Unlike classical AI that processes static data, embodied AI must deal with real‑time sensorimotor contingencies, credit assignment across long time horizons, and the reality of physical interaction. The lifecycle must connect perception pipelines, motor control, and relational understanding of the world.

**Outcome wanted:** a repeatable process for developing embodied agents that learn sensorimotor skills, maintain stable world models, and can be evaluated, transferred, and retired in a governed way.

## Pain points

| Pain | Consequence |
|---|---|
| Credit assignment across long horizons | Learning stalls; rewards too sparse; agent gives up |
| Sim-to-real gap for sensorimotor skills | Policy works in simulator, fails on real robot |
| Perception‑action latency | Agent reacts too slowly; collision or missed opportunity |
| World model fragmentation | No consistent understanding of environment state |
| Sample inefficiency | Collecting real‑world trajectories is slow and expensive |
| Safety during learning | Agent explores dangerously while learning |
| Evaluation stagnation | Agent appears to learn but plateaus at sub‑optimal skill |
| Retirement / reuse hard | No standardized body‑model or skill inventory |

## Users & stakeholders

| Role | Interest |
|---|---|
| Robotics/embedded engineers | Sensor/actuator integration, real‑time constraints |
| Reinforcement learning researchers | Learning algorithms, sample efficiency |
| Safety/compliance | Safe exploration; bounded physical behavior |
| Product team | Time-to‑functional‑behavior; deployment timeline |
| Operations | System maintenance, fault handling, skill retirement |

## Workflow

```mermaid
flowchart TB
    subgraph Design [Embodied agent design phase]\n    IA[Identify task + embodiment constraints]\n    IA --> SW[Select learning paradigm: RL, imitation, neuros‑ymbolic]\n    SW --> MM[Design sensorimotor module: perception → decision → action]\n    MM --> WW[Design world model + state representation]\n    WW --> REG[(Artifact registry: policy + model + config)]\n    end\n    subgraph Train [Training phase]\n    RL[Reinforcement learning / imitation]\n    RL --> EV[Evaluation in simulation]\n    EV -->|pass| PT[Physical test bed: reduced‑scale / safe environment]\n    EV -->|fail| IT[Iterate: reward, model, representation]\n    RL -->|real‑world| RW[Real‑world data collection (curriculum)]\n    RW --> RL\n    PT -->|pass| DEP[Deploy to full embodiment]\n    PT -->|fail| IT2[Iterate: perception, model, or safety]\n    end\n    subgraph Operate [Operational phase]\n    DEP --> MON[Monitoring: skill quality, safety, sample efficiency]\n    MON -->|drift/violation| RT[Retraining or skill retirement]\n    MON -->|stable| KEEP[Keep skill in repertoire]\n    end\n    RT --> REG\n    KEEP --> AUD[Audit log + skill version bump]\n    AUD --> RET[Retire skill; optionally preserve model]\n    RET --> CD[Component cleanup + data retention policy]\n```

**Human decision points:** learning paradigm selection; simulation‑to‑real gap acceptance; physical test‑bed clearance; skill retirement triggers.

## Tech stack (layers, not products)

| Layer | Capability | Notes |
|---|---|---|
| Perception pipeline | Camera, lidar, tactile, proprioception stacks | Must output compact, robust state representation |
| Decision module | Policy network (RL / imitation / neuros‑ymbolic) | Architecture matches observation‑action bandwidth |
| World model | State estimator (occupancy grid, belief state, latent dynamics) | Essential for credit assignment across timesteps |
| Learning algorithm | RL (PPO, SAC, TD3), imitation, offline RL | Choice depends on data availability and credit‑assignment needs |
| Simulation engine | Physics‑based with stochastic dynamics | Must include sensor noise, actuator delay; key for sim‑to‑real |
| Sim‑to‑real transfer | Domain randomization, randomized dynamics, real‑world fine‑tuning | Critical; measure gap before deployment |
| Real‑world data collection | Curriculum-driven exploration, human teleop, expert demonstrations | Sample efficiency is key; avoid random exploration when possible |
| Safety envelope | Hard limits on velocity, force, joint positions | Programmed into policy; violations trigger emergency stop |
| Observation‑action tracing | Correlated trajectories for credit analysis | Required for debugging and improvement |

## Trade-offs

| Decision | Option A | Option B | Guidance |
|---|---|---|---|
| Learning paradigm | RL (exploration‑heavy) | Imitation (demonstration‑heavy) | Imitation when expert demos available; RL when no demonstrations |
| Sim‑to‑real method | Domain randomization only | Domain randomization + real‑world fine‑tuning | Start with randomization; add real‑world fine‑tuning if gap persists |
| Exploration strategy | Random + uniform | Curriculum (harden → progressively harder) | Curriculum is more sample‑efficient and safer |
| World model complexity | Simple (hand‑crafted features) | Complex (learned latent dynamics) | Start simple; increase only if credit assignment fails |
| Safety envelope | Soft limits (performance warning) | Hard limits (emergency stop) | Hard limits for any physical interaction; soft only for indoor/controlled |
| Real‑world data cost | Collect new data per task | Transfer from related embodiment | Transfer whenever possible; collect only when necessary |

## Success metrics

| Metric | Target | Measurement |
|---|---|---|
| Sample efficiency (real‑world timesteps to skill) | Within budget for task | Number of physical trials |
| Sim‑to‑real gap (quality loss) | ≤ 10% accuracy drop on real robot | Hold‑out real‑world evaluation |
| Credit assignment success | Learning curve improves, no stagnation | Learning curve + success rate |
| Safety violations | → 0 during training and deployment | Emergency stop triggers |
| Skill transferability (to new embodiment) | Within task‑specific threshold | Cross‑robot evaluation |
| Retirement clean‑up completeness | 100% documented + executed | Decommission audit |

## Failure modes & mitigations

| Failure | Mitigation |
|---|---|
| Learning stalls (sparse rewards) | Shaped rewards; curriculum learning; hierarchical abstraction |
| Sim‑to‑real gap too large | Increase domain randomization; add real‑world fine‑tuning; reconsider physics model |
| Safety violations during learning | Sim‑only early phases; safety envelope in policy; human‑in‑the‑loop override |
| Credit assignment fails (long horizons) | Hierarchical RL; option-critic; temporally‑extended actions |
| Sample inefficiency (too many real‑world trials) | Sim-to-real transfer first; offline RL from prior datasets; imitation from demos |
| World model fragmentation | Consistent state representation; curriculum that gradually increases complexity |
| Retirement unclear (orphan skills) | Skill registry with versioning; retirement ADR when skill is superseded |

## Related artifacts

[Physical AI lifecycle](../lifecycles/physical-ai-lifecycle.md) · [Simulation‑to‑real transfer patterns](../design-patterns/ml-engineering.md) · [Safety envelope design](../design-patterns/reliability-resilience.md) · [Agent patterns](../design-patterns/agent-patterns.md) · [Artifact registry](../standards/README.md)

## Embodied AI checklist

- [ ] Task and embodiment constraints identified
- [ ] Learning paradigm selected (RL / imitation / neuros‑ymbolic)
- [ ] Sensorimotor module designed (perception → decision → action)
- [ ] World model + state representation defined
- [ ] Artifact registry entry created (policy + model + config)
- [ ] Training configured with evaluation checkpoints
- [ ] Physical test‑bed validation passed (safety + quality)
- [ ] Sim‑to‑real transfer configured and gap measured
- [ ] Safety envelope defined and baked into policy
- [ ] Monitoring + alerting configured for skill quality + safety
- [ ] Skill retirement criteria documented
- [ ] Retirement / decommissioning ADR prepared

--- 

*Embodied AI lifecycle version 0.1 — Last updated: 2026-10-19*