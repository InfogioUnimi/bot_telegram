# 🤖 Assistente personale bot Telegram

Un semplice **Telegram Bot modulare** sviluppato in Python, pensato come progetto didattico.  
Il bot include diversi comandi:
- `/weather <city>` che mostra le condizioni meteo di una città usando l'API di [OpenWeatherMap](https://openweathermap.org/api).
- `/remind <time> <text>` che ricorda dopo un intervallo di tempo `<time>` il testo `<text>`
- `/translate <lang> <text>` che traduce il testo `<text>` nella lingua selezionata in `<lang>`

---

## ✨ Funzionalità
- `/start` → messaggio di benvenuto  
- `/help` → elenco dei comandi disponibili  
- `/weather <città>` → mostra il meteo attuale 🌦️  
- `/remind <time> <text>` → ricorda il messagio dopo un intervallo di tempo selezionato
- `/translate <lang> <text>` → traduce nella lingua selezionata il testo inserito

---

## 📂 Struttura del progetto
```
BOT_TELEGRAM/
│── bot.py              # entrypoint principale del bot
│── config.py           # gestione configurazioni e variabili d'ambiente
│── requirements.txt    # dipendenze Python
│── .env.example        # esempio variabili da impostare
│── plugins/            # cartella plugin modulari
│     └── Weather.py    # comando meteo
│     └── Remind.py     # comando remind
│     └── Translate.py  # comando translate
│     └── __init__.py


```

---

## 🚀 Come eseguire il bot

1. **Clona la repo**  
   ```bash
   git clone https://github.com/tuo-username/smart-telegram-bot.git
   cd smart-telegram-bot
   ```

2. **Crea un virtualenv ed installa le dipendenze**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. **Configura le variabili d'ambiente**  
   - Copia il file `.env.example` in `.env`
   - Inserisci i tuoi token:
     ```bash
     TELEGRAM_TOKEN=INSERISCI_IL_TUO_TOKEN
     OPENWEATHER_KEY=INSERISCI_LA_TUA_KEY_OPENWEATHER
     ```

4. **Avvia il bot**  
   ```bash
   python bot.py
   ```

---

## 🛠️ Tecnologie usate
- [python-telegram-bot](https://python-telegram-bot.org/) – libreria ufficiale per bot Telegram  
- [requests](https://docs.python-requests.org/) – chiamate HTTP  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – gestione file `.env`

---

## 📜 Licenza
Progetto rilasciato sotto licenza **MIT**. Sentiti libero di usarlo e modificarlo.
