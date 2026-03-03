# app/core/storage.py
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable, Union

from app.models.schemas import Chunk, IngestionManifest


def ensure_parent_dir(path: Union[str, Path]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_jsonl(chunks: Iterable[Chunk], out_path: Union[str, Path]) -> None:
    """
    Writes chunks as JSON Lines: one JSON object per line.
    This format is append-friendly and good for large outputs.
    """
    ensure_parent_dir(out_path)
    out_path = Path(out_path)

    with out_path.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(c.model_dump_json(ensure_ascii=False))
            f.write("\n")


def write_manifest(manifest: IngestionManifest, out_path: Union[str, Path]) -> None:
    ensure_parent_dir(out_path)
    out_path = Path(out_path)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(manifest.model_dump(), f, ensure_ascii=False, indent=2)


def safe_join(*parts: str) -> str:
    return str(Path(*parts))


def default_ingest_dir(doc_id: str, base_dir: str = "data/ingested") -> str:
    return safe_join(base_dir, doc_id)
