"""Pipeline implementation for Copilot Starter Kit.

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
    """Run the copilot-starter-kit pipeline.

    Implement these steps:
      1. Read the current record and user role through host APIs.
      2. Assemble minimal context; apply user-inherited permissions.
      3. Generate a suggestion through the gateway with guardrails.
      4. Let the user accept as draft or commit an explicit, audited write.
      5. Emit adoption and quality events keyed to feature version.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[copilot-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
