# app/models/schemas.py
from __future__ import annotations

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from datetime import datetime, timezone


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class ChunkMetadata(BaseModel):
    # Traceability / auditability
    source: str = Field(..., description="Original source identifier, e.g. file path")
    source_type: str = Field(..., description="e.g. markdown, pdf")
    doc_id: str = Field(..., description="Stable document id, e.g. hash(source)")
    chunk_index: int = Field(..., ge=0)
    char_start: int = Field(..., ge=0)
    char_end: int = Field(..., gt=0)

    # Optional future-proof fields (not required in Week 2)
    title: Optional[str] = None
    heading_path: Optional[str] = None

    # room for extra metadata without breaking schema
    extra: Dict[str, Any] = Field(default_factory=dict)


class Chunk(BaseModel):
    id: str = Field(..., description="Chunk UUID")
    text: str = Field(..., min_length=1)
    metadata: ChunkMetadata
    created_at: str = Field(default_factory=utc_now_iso)
    chunk_version: str = Field(default="v1")


class IngestionManifest(BaseModel):
    doc_id: str
    source: str
    source_type: str
    created_at: str = Field(default_factory=utc_now_iso)

    # pipeline config snapshot (even if Week 2 hasn't implemented chunking yet)
    chunk_version: str = "v1"
    chunk_size: Optional[int] = None
    overlap: Optional[int] = None

    # output stats
    num_chunks: int = 0

    # optional integrity fields
    sha256_source_text: Optional[str] = None
