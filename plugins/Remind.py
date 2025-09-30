from telegram import Update
from telegram.ext import ContextTypes
import time

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    waiting = context.args[0]
    msg = " ".join(context.args[1:])
    waiting_time = 0
    if waiting[-1] == 's':
        waiting_time = int(waiting[0:-1])
    elif waiting[-1] == 'm':
        waiting_time = int(waiting[0:-1]) * 60
    elif waiting[-1] == 'h':
        waiting_time = int(waiting[0:-1]) * 60 * 60
    else:
        await update.message.reply_text("Riprova inserendo una specifica se intendi ore (h), minuti (m) o secondi (s)")
        return

    await update.message.reply_text(f"Perfetto tra {waiting_time} secondi ti ricordererò '{msg}'")

    time.sleep(waiting_time)
    await update.message.reply_text(msg)