from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}

app = FastAPI(title="rag-backend-starter", version="0.1.0")
