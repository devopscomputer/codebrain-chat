# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import chat
from app.config import settings

app = FastAPI(
    title="CodeBrain Chat API",
    description="API de assistente de programação com IA local (sem censura)",
    version="1.0.0"
)

# CORS para permitir requisições do frontend local ou produção
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(chat.router)

@app.get("/")
def root():
    return {"status": "online", "message": "CodeBrain API rodando com sucesso!"}