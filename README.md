🦊 nanobot-telegram-assistant

Ultra-lightweight Telegram AI Assistant powered by Nanobot + OpenRouter.

A minimal, production-ready Telegram bot that connects to LLM models (GPT / Claude / etc.) using OpenRouter and runs as a clean AI agent.

✨ Features

⚡ Ultra-lightweight architecture

🤖 AI-powered Telegram responses

🔐 Secure environment variable setup

🧠 OpenRouter LLM support

🧩 Clean modular structure

🚀 Easy deployment

🏗 Architecture
🔄 System Flow
Telegram User
      │
      ▼
Telegram Bot API
      │
      ▼
telegram_nanobot.py (Bot Core)
      │
      ▼
OpenRouter API
      │
      ▼
LLM Model (GPT / Claude / etc.)
      │
      ▼
Response back to Telegram
🧠 How It Works

User sends a message in Telegram

Telegram Bot API forwards the request to the bot

telegram_nanobot.py processes the message

Request is sent to OpenRouter

OpenRouter routes it to the configured LLM

The model generates a response

The response is sent back to the user

🧩 Architecture Layers
🗨 Chat Layer

Telegram User Interface

Telegram Bot API

⚙ Bot Layer

telegram_nanobot.py

Message handling

Prompt processing

🤖 Intelligence Layer

OpenRouter API

GPT / Claude models

📦 Project Structure
nanobot-telegram-assistant/
│
├── telegram_nanobot.py   # Main bot logic
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
├── .gitignore            # Ignored files
├── LICENSE               # MIT License
└── README.md             # Project documentation
🔑 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/nanobot-telegram-assistant.git
cd nanobot-telegram-assistant
2️⃣ Create Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate   # Mac/Linux

Windows:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Copy the example file:

cp .env.example .env

Edit .env and add:

TELEGRAM_BOT_TOKEN=your_telegram_token_here
OPENROUTER_API_KEY=your_openrouter_key_here
MODEL=openai/gpt-4o-mini

⚠ Never commit your real .env file.

5️⃣ Run the Bot
python telegram_nanobot.py

Your bot is now live 🚀

🔒 Environment Variables
Variable	Description
TELEGRAM_BOT_TOKEN	Token from @BotFather
OPENROUTER_API_KEY	API key from OpenRouter
MODEL	LLM model name (GPT / Claude / etc.)
🌍 Supported Models

Through OpenRouter, you can use:

OpenAI GPT models

Anthropic Claude

Other supported LLM providers

Just change the MODEL value in .env.

🚀 Deployment Options

You can deploy this bot on:

VPS (DigitalOcean / AWS / etc.)

Railway

Render

Docker container

Local server

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Built with ❤️ by Sundeep Reddy
