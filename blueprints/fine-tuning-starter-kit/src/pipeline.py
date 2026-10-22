"""Pipeline implementation for Fine-tuning Starter Kit.

This is a scaffold. Replace run_pipeline() with the real implementation.
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field


@dataclass
class PipelineInput:
    text: str
    tenant_id: str


@dataclass
class PipelineResult:
    output: str
    citations: list[str] = field(default_factory=list)
    request_id: str = ""
    status: str = "scaffold"


def run_pipeline(payload: PipelineInput) -> PipelineResult:
    """Run the fine-tuning-starter-kit pipeline.

    Implement these steps:
      1. Record the prompting/RAG baseline on the target task.
      2. Curate a dataset with provenance, consent, and a labeling guide.
      3. Validate quality, bias, PII, and leakage before training.
      4. Train with a parameter-efficient method; keep the base model pinned.
      5. Evaluate against baseline and register only if the gate passes.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[fine-tuning-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
