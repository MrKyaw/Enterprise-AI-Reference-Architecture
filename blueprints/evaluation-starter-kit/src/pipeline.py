"""Pipeline implementation for Evaluation Starter Kit.

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
    """Run the evaluation-starter-kit pipeline.

    Implement these steps:
      1. Define success criteria and the slices that matter.
      2. Curate golden, adversarial, and production-sample datasets.
      3. Implement deterministic scorers; add a judge only where needed.
      4. Calibrate the judge against human labels and pin its version.
      5. Gate CI on explicit thresholds and report per-slice results.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[evaluation-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
