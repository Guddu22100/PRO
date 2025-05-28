import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# --- Developer Introduction ---
DEVELOPER_INFO = """
🤖 Welcome to the AI-Powered Creative Prompt Bot!

👨‍💻 Developed by: Divyanshu Kharat
😪 Instagram   : https://www.instagram.com/guddu_2008o

This bot provides unique and creative writing prompts powered by AI.
"""

# --- Bot Configuration ---
BOT_TOKEN = "6863996484:AAExAC9IlBrNiczmjHPZ51W3nmeQkzu5SHo"  # Replace with your bot's token
ADMIN_ID = 6182507613  # Replace with your Telegram user ID

# --- Enable Logging ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Command Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Start Bot", callback_data='start_bot')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to begin:", reply_markup=reply_markup)

async def start_bot_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Hello {query.from_user.first_name}\n\n" + DEVELOPER_INFO)

async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sample_prompts = [
        "Write a story where time travel is banned.",
        "Describe a world where emotions are traded like currency.",
        "Create a dialogue between a robot and a tree."
    ]
    from random import choice
    await update.message.reply_text(choice(sample_prompts))

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# --- Main Function ---
def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(start_bot_callback, pattern='^start_bot$'))
    application.add_handler(CommandHandler("prompt", prompt))

    application.add_error_handler(error_handler)

    application.run_polling()

if __name__ == "__main__":
    main()
