# app/router/chat.py
from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.core.chain import process_message
from app.utils.logger import log_event

router = APIRouter()


class ChatInput(BaseModel):
    message: str
    context: dict | None = {}


@router.post("/api/chat")
async def chat_endpoint(payload: ChatInput, request: Request):
    client_ip = request.client.host
    log_event("NewChatRequest", {"ip": client_ip, "msg": payload.message, "ctx": payload.context})

    result = process_message(payload.message, context=payload.context or {})
    log_event("ChatResponse", result)

    return {
        "status": "success",
        "command": result["command"],
        "answer": result["answer"]
    }