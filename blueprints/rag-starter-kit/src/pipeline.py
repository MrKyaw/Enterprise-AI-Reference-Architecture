"""Pipeline implementation for RAG Starter Kit.

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
    """Run the rag-starter-kit pipeline.

    Implement these steps:
      1. Extract and normalize each source type; attach source, date, and ACL tags.
      2. Chunk per content type, preserving tables and headings.
      3. Embed with a pinned, versioned model and write to the hybrid index.
      4. Retrieve with ACL pre-filters, rerank top-k, and assemble a cited prompt.
      5. Refuse or qualify when evidence is insufficient; log the assembled context.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[rag-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
