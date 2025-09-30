# plugins/weather.py  — versione migliorata
import time
import aiohttp
import logging
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
import config

API_URL = "https://api.openweathermap.org/data/2.5/weather"
CACHE: dict = {}  # {city_lower: (timestamp, data)}
CACHE_TTL = 600   # secondi (10 minuti)

logger = logging.getLogger(__name__)

def _format_city(name: str) -> str:
    # usa title per gestire nomi multi-parola
    return name.title()

def _format_message(city: str, data: dict) -> str:
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    wind = data.get("wind", {})

    temp = main.get("temp", "—")
    humidity = main.get("humidity", "—")
    desc = weather_list[0].get("description", "—").capitalize() if weather_list else "—"
    wind_speed = wind.get("speed", "—")

    city_display = _format_city(city)

    msg = (
        f"📍 Meteo a <b>{city_display}</b>:\n"
        f"🌡️ Temperatura: {temp}°C\n"
        f"☁️ Condizioni: {desc}\n"
        f"💧 Umidità: {humidity}%\n"
        f"💨 Vento: {wind_speed} m/s"
    )
    return msg

async def _fetch_weather(city: str) -> dict:
    params = {
        "q": city,
        "appid": config.WEATHER_KEY,
        "units": "metric",
        "lang": "it"
    }
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(API_URL, params=params) as resp:
            data = await resp.json()
            if resp.status != 200:
                # Solleva un'eccezione con messaggio leggibile
                msg = data.get("message", f"HTTP {resp.status}")
                raise RuntimeError(msg)
            return data

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Usa il comando così:\n/weather <città>")
        return

    city = " ".join(context.args).strip()
    city_key = city.lower()

    # controllo cache
    cached = CACHE.get(city_key)
    now = time.time()
    if cached and now - cached[0] < CACHE_TTL:
        data = cached[1]
    else:
        try:
            data = await _fetch_weather(city)
            CACHE[city_key] = (now, data)
        except Exception as e:
            logger.exception("Errore fetching weather")
            await update.message.reply_text("⚠️ Non sono riuscito a recuperare il meteo in questo momento. Riprova più tardi.")
            return

    msg = _format_message(city, data)
    await update.message.reply_text(msg, parse_mode=ParseMode.HTML)
