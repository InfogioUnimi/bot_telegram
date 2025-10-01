from telegram import Update
from telegram.ext import ContextTypes
import asyncio
import re

def format_delay(delay_str: str) -> int:
    '''questa funzione permette di ottenere un intero che rappresenta i secondi che il bot dovrà aspettare'''
    try:
        match = re.match(r"(\d+)([smhd])", delay_str.lower())

        if not match:
            return None
        
        delay, unit = match.group()

        multipliers = {
            "s": 1,
            "m": 60,
            "h": 3600,
            "d": 86400
        }

        return delay * multipliers[unit]

    except Exception:
        return None



async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 2:
        await update.message.reply_text(
            "⚠️ Uso corretto:\n/remind <tempo> <messaggio>\n\n"
            "Esempi:\n"
            "/remind 30s Bevi acqua 💧\n"
            "/remind 5m Fai una pausa ☕\n"
            "/remind 2h Vai a correre 🏃"
        )


    waiting_str = context.args[0]
    msg = " ".join(context.args[1:])
    waiting_time = format_delay(waiting_str)

    if waiting_time is None:
        await update.message.reply_text(
            "❌ Formato tempo non valido.\n"
            "Usa numeri con unità: s (secondi), m (minuti), h (ore), d (giorni).\n"
            "Esempio: /remind 10m Studia 📚"
        )
        return
    
    #Messaggio di conferma
    await update.message.reply_text(
        f"⏳ Promemoria impostato tra {waiting_str}:\n➡️ {msg}"
    )

    #Task in background per permettere la continua attività del bot
    async def send_reminder():
        try:
            await asyncio.sleep(waiting_time)
            await update.message.reply_text(
                f"🔔 Promemoria!\n➡️ {msg}"
            )
        
        except Exception as e:
            #Non facciamo crushare il bot ma facciamo un log se serve
            print(f"[ERRORE remind] {e}")

    context.application.create_task(send_reminder)
