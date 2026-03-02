# 🦊 nanobot-telegram-assistant

Ultra-Lightweight Telegram AI Assistant powered by Nanobot + OpenRouter.

A minimal, production-ready Telegram bot that connects to LLM models using OpenRouter and runs as a clean AI agent.

---

## ✨ Features

- ⚡ Ultra-lightweight architecture
- 🤖 AI-powered Telegram responses
- 🔐 Secure environment variable setup
- 🧠 OpenRouter LLM support
- 🧩 Clean modular structure
- 🚀 Easy deployment

---

## 🏗 Architecture


## 🏗 Architecture

The Nanobot Telegram Assistant follows a clean and lightweight AI agent flow.

### 🔄 System Flow

```mermaid
flowchart LR
    A[Telegram User] --> B[Telegram Bot API]
    B --> C[telegram_nanobot.py]
    C --> D[OpenRouter API]
    D --> E[LLM Model (GPT / Claude / etc.)]
    E --> C
    C --> B
    B --> A


---

## 📦 Project Structure


nanobot-telegram-assistant/
│
├── telegram_nanobot.py # Main bot logic
├── requirements.txt # Python dependencies
├── .env.example # Environment variable template
├── .gitignore # Ignored files
└── README.md # Project documentation


---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/nanobot-telegram-assistant.git
cd nanobot-telegram-assistant
