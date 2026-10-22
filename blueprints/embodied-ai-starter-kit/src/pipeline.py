"""Pipeline implementation for Embodied AI Starter Kit.

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
    """Run the embodied-ai-starter-kit pipeline.

    Implement these steps:
      1. Define the task and embodiment constraints.
      2. Build the perception and state-estimation path.
      3. Choose a learning paradigm based on available demonstrations.
      4. Train in simulation with a curriculum; transfer with measured gap.
      5. Deploy with a safety envelope and monitor skill quality.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[embodied-ai-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
