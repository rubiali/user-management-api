from fastapi import FastAPI
from app.database import engine

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        return {"db": "connected"}
