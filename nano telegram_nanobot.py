import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from nanobot import Agent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Telegram token from environment
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN not found in environment variables")

# Initialize Nanobot agent
agent = Agent()

# Handle incoming Telegram messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = agent.run(user_message)
    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🚀 Telegram Nanobot running...")
app.run_polling()
