import logging
import config
from plugins import Weather, Remind, Transalte
from telegram import Update
from telegram.constants import ParseMode # questo permette la formattazione del testo nelle risposte
from telegram.ext import (
    Application,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Benvenuto {update.message.from_user.first_name}, sono il tuo Bot Assistente Personale.\n"
        "Per conoscere le mie funzionalità digita il comando /help"
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Comandi disponibili\n"
        "/start - Messaggio di benvenuto\n"
        "/help - Mostra le funzionalità e i comandi disponibili\n"
        "/wheather [city] - Mostra il meteo attuale della città richiesta 🌦️\n"
        "/translate <lang> <text> - Traduce il testo nella lingua selezionata 🔤\n"
        "/remind <time> <msg> - Ogni intervallo di tempo selezionato invia il msg fornito⏰\n"
    )

def main():
    
    #Crea l'applicazione con il TOKEN fornito attraverso config.py
    app = Application.builder().token(config.TELEGRAM_TOKEN).build()
    
    #Creazione degli handler per ogni comando
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", Weather.weather))
    app.add_handler(CommandHandler("remind", Remind.remind))
    app.add_handler(CommandHandler("translate", Transalte.translate))


    #Avvia il bot
    print("🤖 Bot in ascolto...")
    app.run_polling()

if __name__ == "__main__":
    main()