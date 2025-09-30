import os
from dotenv import load_dotenv

#Carica le variabili dal file .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_KEY = os.getenv("WEATHER_KEY")

if not TELEGRAM_TOKEN:
    raise ValueError("❌ Errore: TOKEN non trovato in .env")

if not WEATHER_KEY:
    raise ValueError("❌ Errore: KEY mancante per le API meteo in .env")