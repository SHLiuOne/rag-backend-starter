from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello"}

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello"}

@app.get("/files")
def list_files():
    return []

@app.get("/files/{file_id}")
def get_file(file_id: int):
    raise HTTPException(status_code=404, detail="File not found")