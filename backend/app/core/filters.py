
# app/core/filters.py
def apply_filters(language: str = None, version: str = None) -> str:
    filters = []
    if language:
        filters.append(f"[Linguagem: {language}]")
    if version:
        filters.append(f"[Versao: {version}]")
    return " ".join(filters)
