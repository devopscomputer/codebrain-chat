# app/utils/logger.py
import datetime
import json


def log_event(tag: str, data):
    timestamp = datetime.datetime.now().isoformat()
    log = {
        "timestamp": timestamp,
        "tag": tag,
        "data": data
    }
    with open("codebrain_logs.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")
