import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7612508935:AAGBw93LBf7WLjfAlthptH9umFoC8clon_0"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Merhaba! TradingView alarm botu aktif.')

async def notify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = 'TradingView alarmı: Koşullar gerçekleşti!'
    await update.message.reply_text(message)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("notify", notify))

    print("Bot çalışıyor...")
    app.run_polling()
