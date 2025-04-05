# app/core/chain.py
from app.core.model import query_model
from app.core.prompts import build_prompt
from app.core.filters import apply_filters
from app.utils.logger import log_event


def process_message(message: str, context: dict = {}) -> dict:
    command = message.split()[0] if message.startswith("/") else ""
    msg_body = message[len(command):].strip() if command else message

    lang = context.get("language")
    version = context.get("version")
    filtros = apply_filters(lang, version)
    
    prompt = build_prompt(msg_body, command=command, context=filtros)
    log_event("PromptFinal", prompt)

    resposta = query_model(prompt)
    return {"answer": resposta, "command": command or "default"}

