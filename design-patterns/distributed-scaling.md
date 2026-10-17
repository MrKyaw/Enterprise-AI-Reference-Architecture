# Distributed Systems & Scaling Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns for scaling compute, storage, and inference across nodes, regions, and tenants. Complements [general architecture](general-architecture.md) and [reliability](reliability-resilience.md).

## Scaling patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Horizontal scaling (scale out)** | Add instances | Requires statelessness or externalized state |
| **Vertical scaling (scale up)** | Bigger instances | Ceiling; cost curve; hardware availability for GPUs |
| **Autoscaling on the right signal** | Scale on queue depth/latency, not CPU | Wrong signals cause oscillation ([inference RA](../reference-architectures/inference/README.md)) |
| **Sharding / partitioning** | Split data or load by key | Hot partitions; rebalancing; cross-shard queries |
| **Consistent hashing** | Minimize reshuffling on node changes | Virtual nodes needed for balance |
| **Replication (leader/follower)** | Read scale + availability | Replication lag and read-your-write consistency |
| **Read replicas** | Offload reads | Staleness tolerance required |
| **CQRS + materialized views** | Separate read models | Projection lag; rebuild cost |
| **Cache tiers (local → regional → global)** | Reduce latency and cost | Invalidation; correctness across tiers |
| **Queue-based load leveling** | Absorb bursts | Latency vs. stability |
| **Batching / microbatching** | Amortize per-request overhead (esp. GPU) | Latency increase; fairness across tenants |
| **Geographic distribution** | Latency and residency | Data residency constraints; consistency |
| **Cell-based architecture** | Isolate failures to a cell | Routing and data placement complexity |
| **Warm pools** | Avoid cold-start latency | Idle cost |

## Coordination patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Leader election** | Single writer/coordinator | Split-brain; needs consensus |
| **Consensus (majority quorum)** | Agreement under failure | Latency; operationally complex |
| **Distributed locks** | Mutual exclusion across nodes | Lease expiry; fencing tokens |
| **Idempotency keys** | Safe retries | Key scope and retention |
| **Work distribution / work queue** | Parallel task processing | Poison messages; visibility timeouts |
| **Saga / process manager** | Multi-step distributed transactions | Compensation design |
| **Outbox** | Atomic publish | Relay monitoring |
| **Two-phase commit** | Atomic across participants | Blocking; avoid when sagas fit |
| **Gossip / membership** | Failure detection at scale | Eventual knowledge |
| **Rate limiting & quotas** | Fairness and protection | Distributed counters need accuracy |

## Multi-tenancy & isolation

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Silo (per-tenant resources)** | Maximum isolation | Regulated tenants, noisy-neighbor sensitivity | Cost and operational overhead |
| **Pool (shared resources)** | Efficiency | Many small tenants | Noisy neighbors; blast radius |
| **Bridge/hybrid** | Shared pool + silo for sensitive tenants | Mixed tenant profiles | Complexity of two operational models |
| **Tenant-scoped storage & indexes** | Isolate data and retrieval | Multi-tenant RAG/agents | Must be enforced at query time, not by convention |
| **Per-tenant quotas** | Fairness and cost control | Shared inference capacity | Quota tuning |
| **Tenant-aware caching & memory** | Isolate cached answers and agent memory | Multi-tenant AI | Cross-tenant leakage is a critical defect |
| **Noisy-neighbor protection** | Bulkheads + fair scheduling | Shared GPU inference | Sizing and priority policy |

## Inference-specific scaling

| Pattern | Intent | Watch out |
|---|---|---|
| **Continuous batching** | Raise GPU utilization | Tail latency |
| **Model-aware scheduling** | Route requests to models with capacity | Complexity |
| **GPU sharing / time-slicing** | Reduce idle GPU cost | Interference between workloads |
| **Speculative decoding / quantized serving** | Reduce latency/cost | Quality validation required |
| **Model multiplexing** | Serve many models from shared infrastructure | Cold-start and memory pressure |
| **Edge/pre-compute** | Move work closer to consumers | Staleness and sync |
| **Async/batch offload** | Move non-interactive work off the hot path | Freshness expectations |

## Capacity & planning

| Pattern | Intent |
|---|---|
| **Load shedding with priority tiers** | Protect critical work under overload |
| **Admission control** | Reject early rather than degrade everything |
| **Capacity headroom for provider failover** | Survive losing a primary provider |
| **Peak vs. sustained cost modeling** | Avoid provisioning for the worst minute |
| **Frontier testing (load test at 2× peak)** | Find the breaking point deliberately |

## Anti-patterns

- Autoscaling on CPU for I/O- or GPU-bound AI workloads
- Shared mutable state across instances
- One shard for a hot tenant or hot key
- Global caches with no tenant boundary
- Bulkheads sized from average, not peak, concurrency
- Multi-region without a data-residency or consistency plan
- Distributed locks without lease expiry and fencing
