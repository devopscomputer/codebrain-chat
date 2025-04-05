# app/core/chain.py
from app.core.model import query_model
from app.core.prompts import build_prompt
from app.core.filters import apply_filters
from app.utils.logger import log_event


def process_message(message: str, context: dict = {}) -> dict:
    # Detecta o comando, se existir
    command = message.split()[0] if message.startswith("/") else ""
    msg_body = message[len(command):].strip() if command else message

    # Contexto de linguagem e versão
    lang = context.get("language")
    version = context.get("version")

    # Aplica filtros se necessário (ex: idioma e versão)
    filtros = apply_filters(lang, version)

    # Se não houver comando, define o modo hacker como ativo por padrão
    if not command:
        command = "/modo_hacker"
    
    # Cria o prompt final com base no comando
    prompt = build_prompt(msg_body, command=command, context=filtros)

    # Log do prompt final gerado
    log_event("PromptFinal", prompt)

    # Envia o prompt para o modelo (Ollama)
    resposta = query_model(prompt)

    # Retorna a resposta e o comando utilizado
    return {"answer": resposta, "command": command or "default"}
# app/core/chain.py

from app.core.model import query_model
from app.core.prompts import build_prompt
from app.core.filters import apply_filters
from app.utils.logger import log_event


def process_message(message: str, context: dict = {}) -> dict:
    """
    Processa a mensagem vinda do frontend:
    - Detecta comandos (/modo_hacker, etc)
    - Aplica filtros técnicos (linguagem, versão)
    - Gera o prompt com build_prompt()
    - Consulta o modelo via query_model()
    """

    # Detecta o comando, se existir
    command = message.split()[0] if message.startswith("/") else ""
    msg_body = message[len(command):].strip() if command else message

    # Contexto de linguagem e versão
    lang = context.get("language")
    version = context.get("version")

    # Aplica filtros técnicos (ex: linguagem, versão)
    filtros = apply_filters(lang, version)

    # Se não houver comando explícito, ativa modo hacker como default
    if not command:
        command = "/modo_hacker"
    
    # Cria o prompt final baseado no comando
    prompt = build_prompt(msg_body, command=command, context=filtros)

    # Log do prompt final gerado
    log_event("PromptFinal", {
        "command": command,
        "prompt": prompt
    })

    # Envia o prompt para o modelo local via Ollama
    resposta = query_model(prompt)

    # Retorna a resposta e o comando utilizado
    return {
        "answer": resposta,
        "command": command or "default"
    }


def build_streaming_prompt(message: str, context: dict = {}) -> str:
    """
    Gera prompt simples para uso com resposta streaming.
    (Pode evoluir no futuro para interpretar comandos de forma parcial)
    """
    return build_prompt(message, command="/modo_hacker", context=apply_filters(
        context.get("language"), context.get("version")
    ))
