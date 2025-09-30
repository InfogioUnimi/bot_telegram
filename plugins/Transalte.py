from googletrans import Translator
from telegram import Update
from telegram.ext import ContextTypes

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trans_to = context.args[0]
    text_to_translate = " ".join(context.args[1:])
    origin_lang = ""
    async with Translator() as translator:
        result = await translator.detect(text_to_translate)
        origin_lang = result.lang

    async with Translator() as translator:
        result = await translator.translate(text_to_translate, src=origin_lang, dest=trans_to)
        await update.message.reply_text(result.text)

