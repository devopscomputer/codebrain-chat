# client_cli.py
import requests

API_URL = "http://127.0.0.1:8000/api/chat-stream"

def main():
    print("\n🤖 Bem-vindo ao CodeBrain CLI!\nDigite sua mensagem (ou 'sair' para encerrar):\n")

    while True:
        user_input = input("Você > ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando CodeBrain Chat.")
            break

        payload = {
            "message": user_input,
            "context": {
                "language": "Python",
                "version": "3.10"
            }
        }

        try:
            with requests.post(API_URL, json=payload, stream=True) as res:
                if res.status_code != 200:
                    print(f"❌ Erro HTTP {res.status_code}: {res.text}")
                    continue

                print("CodeBrain > ", end="", flush=True)
                for chunk in res.iter_content(chunk_size=None):
                    try:
                        token = chunk.decode("utf-8")
                        print(token, end="", flush=True)
                    except Exception as e:
                        print(f"\n❌ Erro ao decodificar chunk: {e}")
                print()  # quebra de linha final
        except Exception as e:
            print(f"❌ Erro de conexão: {e}")

if __name__ == "__main__":
    main()
