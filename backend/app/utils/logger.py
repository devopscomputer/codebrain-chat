# app/utils/logger.py
import datetime
import json
import os


def log_event(tag: str, data, ip: str = None):
    """
    Registra eventos em JSON estruturado, com suporte a IP e logs por data.

    Args:
        tag (str): Rótulo do tipo de evento (ex: 'ChatRequest', 'PromptFinal')
        data (any): Dados relacionados ao evento
        ip (str, opcional): IP do cliente, se disponível
    """

    timestamp = datetime.datetime.now()
    log_dir = "logs/" + timestamp.strftime("%Y-%m-%d")
    os.makedirs(log_dir, exist_ok=True)

    log = {
        "timestamp": timestamp.isoformat(),
        "tag": tag,
        "ip": ip,
        "data": data
    }

    filename = f"{log_dir}/codebrain_log.json"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")
