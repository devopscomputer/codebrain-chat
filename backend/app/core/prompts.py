

# app/core/prompts.py
def build_prompt(user_message: str, command: str = "", context: str = "") -> str:
    base = """
Você é um assistente de programação chamado CodeBrain. Responda com precisão, objetividade e foco em código.
Utilize Markdown para formatar blocos de código.
    """

    if command == "/modo_hacker":
        base += "\nModo Hacker ativado: inclua técnicas de engenharia reversa, análise de binários, etc."
    elif command == "/refactor":
        base += "\nRefatore o código enviado com boas práticas e comentários."
    elif command == "/snippet":
        base += "\nResponda apenas com um snippet funcional, sem explicação."
    elif command == "/doc":
        base += "\nExplique usando documentação oficial se possível."
    elif command == "/explain":
        base += "\nExplique linha por linha o que o código faz."

    final_prompt = f"{base}\n\nContexto:\n{context}\n\nPergunta:\n{user_message}"
    return final_prompt

