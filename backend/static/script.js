let controller = null;

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  appendMessage("user", message);
  input.value = "";

  const loading = appendMessage("bot", "⏳ Pensando...");
  controller = new AbortController();
  document.getElementById("stop-btn").disabled = false;

  try {
    const res = await fetch("http://localhost:8000/api/chat-stream", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: message,
        context: {
          language: "Python",
          version: "3.10"
        }
      }),
      signal: controller.signal
    });

    const reader = res.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let buffer = "";
    let result = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });

      // Divide por linhas no buffer
      let lines = buffer.split("\n");
      buffer = lines.pop(); // guarda a última linha incompleta para o próximo chunk

      for (let line of lines) {
        if (!line.trim()) continue;

        try {
          const json = JSON.parse(line);
          const token = json.response || "";
          result += token;
          loading.textContent = result;
        } catch (err) {
          console.warn("⚠️ Linha inválida de JSON:", line);
        }
      }
    }

  } catch (err) {
    if (err.name === "AbortError") {
      loading.textContent = "❌ Resposta interrompida pelo usuário.";
    } else {
      loading.textContent = "❌ Erro ao se conectar com a IA.";
      console.error("❌ Erro:", err);
    }
  } finally {
    controller = null;
    document.getElementById("stop-btn").disabled = true;
  }
}

function appendMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
  return msg;
}

function abortMessage() {
  if (controller) {
    controller.abort();
    document.getElementById("stop-btn").disabled = true;
    console.log("🔴 Streaming interrompido");
  }
}
