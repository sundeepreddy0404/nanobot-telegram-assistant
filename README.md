## 🏗 Architecture

### 🔄 System Flow

```mermaid
flowchart LR
    A[Telegram User] --> B[Telegram Bot API]
    B --> C[telegram_nanobot.py]
    C --> D[OpenRouter API]
    D --> E[LLM Model - GPT or Claude]
    E --> C
    C --> B
    B --> A
🧠 How It Works

A user sends a message in Telegram

Telegram Bot API forwards the request to the bot

telegram_nanobot.py processes and prepares the prompt

The request is sent to OpenRouter

OpenRouter routes it to the configured LLM model

The model generates a response

The response is returned to the user via Telegram

🧩 Architecture Layers
📱 Chat Layer

Telegram User Interface

Telegram Bot API

🧠 Bot Layer

telegram_nanobot.py

Handles message parsing

Sends prompts to OpenRouter

Returns formatted responses

🌐 AI Layer

OpenRouter API

Configured LLM model (GPT / Claude / etc.)

🔁 Response Layer

AI response sent back to Telegram user

🚀 Design Principles

⚡ Ultra-lightweight architecture

🧩 Modular and extendable

🔐 Secure environment variable configuration

🔄 Model flexibility via OpenRouter

🛠 Easy to extend with memory or tools

🔮 Future Extensions

Persistent conversation memory

Tool integrations (search, APIs, automation)

Multi-model routing

Deployment containerization (Docker)

Logging & monitoring layer
