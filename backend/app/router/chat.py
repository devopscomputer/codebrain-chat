from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.core.chain import process_message, build_streaming_prompt
from app.core.model import query_model
from app.utils.logger import log_event

router = APIRouter()

# Modelo de entrada
class ChatInput(BaseModel):
    message: str
    context: dict | None = {}

# 📦 Endpoint tradicional com resposta completa
@router.post("/api/chat")
async def chat_endpoint(payload: ChatInput, request: Request):
    client_ip = request.client.host
    log_event("NewChatRequest", {
        "ip": client_ip,
        "msg": payload.message,
        "ctx": payload.context
    })

    result = process_message(payload.message, context=payload.context or {})
    log_event("ChatResponse", result)

    return {
        "status": "success",
        "command": result["command"],
        "answer": result["answer"]
    }

# ⚡ Endpoint de streaming
@router.post("/api/chat-stream")
async def chat_stream(payload: ChatInput):
    def generate():
        try:
            prompt = build_streaming_prompt(payload.message, context=payload.context or {})
            log_event("PromptStreaming", {"prompt": prompt})

            for token in query_model(prompt, stream=True):
                print("🔹 Token:", token["response"])  # Debug
                yield token["response"]  # ✅ Corrigido aqui!

        except Exception as e:
            error_msg = f"[❌ Erro: {str(e)}]"
            log_event("StreamError", error_msg)
            yield error_msg

    return StreamingResponse(generate(), media_type="text/plain")
