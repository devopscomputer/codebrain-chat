import requests
from app.config import settings
from app.utils.logger import log_event

def query_model(prompt: str, model: str = None, stream: bool = False):
    url = settings.MODEL_API_URL
    model = model or settings.DEFAULT_MODEL

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    try:
        if stream:
            with requests.post(url, json=payload, stream=True) as response:
                for line in response.iter_lines():
                    if line:
                        token = line.decode("utf-8")
                        log_event("🧪 Streaming", token)
                        yield token
        else:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            log_event("LLM Response", result)
            return result.get("response", "[❌ Erro: resposta vazia da IA]")

    except Exception as e:
        log_event("LLM Error", str(e))
        if stream:
            yield f"[❌ Erro ao consultar modelo: {str(e)}]"
        else:
            return f"[❌ Erro: {str(e)}]"
