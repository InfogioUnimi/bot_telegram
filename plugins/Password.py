import random
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

def new_password(length: int) -> str:
    caratteri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%&(?=)[]{/}.,;:-_@#+*"
    password = ""
    i = 0

    while i < length:
        c = random.choice(caratteri)
        if c in "(?=)[]{/}.,;:-_@#+*":
            c = "\\" + c
        password = password + c
        i+=1
        
    return password


async def password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 1:
        try:
            int_length = int(context.args[0])
            if int_length <= 16 and int_length >= 6:
                length = int_length
                pwd = new_password(length)
                await update.message.reply_text(f"La password è stata generata ed è: ||{pwd}||", parse_mode="MarkdownV2")
            else:
                await update.message.reply_text("Inserisci un numero compreso tra 6 e 16")
        except ValueError:
            await update.message.reply_text("Inserisci un intero come valore di <lenght>")
        
    else:
        await update.message.reply_text(
                "Il corretto utilizzo del comando è il seguente:\n/password <length>\nDove <length> è un numero intero minore o uguale a 16 che indica la lunghezza desiderata per la password."
            )
        return
    
    