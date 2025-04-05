# 🧠 CodeBrain Chat — AI Dev Assistant Sem Filtro

CodeBrain é um projeto de chat inteligente **voltado exclusivamente para programadores**, alimentado por **modelos de IA open-source locais** (como Mistral, Deepseek ou Code Llama), com dados filtrados de alto valor técnico (Stack Overflow, GitHub, RFCs, MDN).

---

## 🚀 Visão Geral

- 💻 **IA especialista para devs**
- 🔍 **Respostas técnicas profundas** com contexto
- ❌ **Sem censura**: comandos avançados como `/modo_hacker`, `/refactor`, `/doc`
- 📚 **Big Data técnico filtrado** indexado com LangChain + FAISS
- 🧠 **LLMs locais** via Ollama ou Llama.cpp (offline-ready)
- 📦 API FastAPI robusta, modular, pronta para produção
- ⚙️ Pipeline RAG com suporte a **filtros por linguagem, versão, stack**

---

## 🗂 Estrutura do Projeto

### 📁 Frontend (`/codebrain-chat`)

| Arquivo           | Descrição                                |
|-------------------|-------------------------------------------|
| `index.html`      | Interface inicial responsiva e leve       |
| `style.css`       | Dark mode dev-friendly, layout terminal   |
| `script.js`       | Envia mensagem, processa mock/resposta    |
| `mock-responses`  | Simula IA antes da conexão real           |

### 📁 Backend (`/codebrain-backend`)

| Diretório         | Descrição                                                       |
|-------------------|-----------------------------------------------------------------|
| `app/main.py`     | Entrypoint FastAPI                                              |
| `router/chat.py`  | Endpoint `/api/chat` para receber mensagens                     |
| `core/model.py`   | Conecta com Ollama ou Llama.cpp                                 |
| `core/chain.py`   | Pipeline LangChain + contexto técnico via embeddings            |
| `core/prompts.py` | Interpreta comandos (`/modo_hacker`, etc.)                      |
| `utils/logger.py` | Logs organizados no estilo DevSecOps                            |
| `data/`           | Dumps técnicos (StackOverflow, MDN, GitHub)                     |
| `embeddings/`     | Índice vetorial FAISS para busca semântica                     |

---

## ⚙️ Instalação Rápida (modo dev)

```bash
cd codebrain-backend
python -m venv venv
.\venv\Scripts\activate     # ou source venv/bin/activate no Linux
pip install -r requirements.txt
uvicorn app.main:app --reload
🔗 Endpoint de API
POST /api/chat

json
Copiar
Editar
{
  "message": "Como usar OAuth2 com Node.js?",
  "context": {
    "language": "Node",
    "version": "18.0.0"
  }
}
✨ Comandos Especiais
Comando	Função
/modo_hacker	Ativa respostas voltadas à engenharia reversa
/refactor	IA melhora e reestrutura códigos enviados
/doc	Busca documentos técnicos por linguagem/tag
/explain	Explicações passo a passo
/snippet	Responde só com código direto, sem explicação
💥 Diferenciais Técnicos (para recrutadores)
✅ Backend desacoplado, modular, escalável

✅ API RESTful documentada e limpa

✅ Prompt engineering contextualizado

✅ LLMs open-source com controle total

✅ Suporte à RAG com FAISS (custom retrieval)

✅ Pronto para deploy com Docker / CI/CD / monitoramento

✅ Segurança: sem dependência externa de OpenAI ou Anthropic

🧱 Stack Utilizada
🧠 FastAPI + Uvicorn

🧠 LLama.cpp / Ollama (modelo local)

🧠 LangChain + FAISS

📡 Requests/HTTPX para integração com LLM

📦 Python 3.10+, venv, .env, dotenv, requirements.txt

📊 Dumps reais técnicos de Stack Overflow, MDN, GitHub

📍 Roadmap (v1.0 → v2.0)
 Estrutura completa backend + frontend

 API conectada à IA local via Ollama

 Prompt e filtros por linguagem

 Chat UI com streaming real-time

 Modo mobile (React Native)

 Painel de usuários (devs)

 Histórico, favoritos, pastas

 CI/CD via GitHub Actions

 Dockerfile com IA embutida

📜 Licença
MIT — projeto educacional/open-source.

🤝 Contato / Parcerias
Desenvolvido por Paulo Silas
Tech Lead | Especialista em automação, IA, backend e segurança
🔗 GitHub: @devopscomputer

