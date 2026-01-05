# rag-backend-starter

Minimal FastAPI backend starter (Stage One - Week 1).

## Run locally

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install fastapi uvicorn
uvicorn app.main:app

## Architecture (Week 1)
FastAPI app with a single health endpoint. Next step is adding ingestion → embedding → retrieval → QA.
