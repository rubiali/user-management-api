from fastapi import FastAPI
from app.database import engine
from app import models

app = FastAPI(
    title="User Management API",
    description="API REST para gerenciamento de usuários com autenticação JWT",
    version="1.0.0"
)

models.Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        return {"db": "connected"}
