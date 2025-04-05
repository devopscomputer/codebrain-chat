# app/core/model.py
import requests
from app.config import settings
from app.utils.logger import log_event


def query_model(prompt: str, model: str = None) -> str:
    url = settings.MODEL_API_URL
    model = model or settings.DEFAULT_MODEL

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        log_event("LLM Response", result)
        return result.get("response", "[❌ Erro: resposta vazia da IA]")
    except Exception as e:
        log_event("LLM Error", str(e))
        return f"[❌ Erro ao consultar o modelo: {str(e)}]"
