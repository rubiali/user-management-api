from fastapi import FastAPI

app = FastAPI(
    title="User Management API",
    description="API REST para gerenciamento de usuários com autenticação JWT",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
