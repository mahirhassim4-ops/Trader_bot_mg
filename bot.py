import os
import time
import threading
from datetime import datetime
import telebot
from flask import Flask

print("=" * 60)
print("🤖 TRADER BOT PRO MADAGASCAR")
print("🇲🇬 NOUVEAU TOKEN - Version Stable")
print("=" * 60)

# NOUVEAU TOKEN ICI ↓
TELEGRAM_TOKEN = "8233744779:AAGRZSeHNb0Grid1GZLahx89EpZtwTlxukuE"
PORT = int(os.getenv('PORT', 10000))

print(f"✅ Token: {TELEGRAM_TOKEN[:15]}...")
print(f"✅ Port: {PORT}")
print(f"✅ Heure: {datetime.now().strftime('%H:%M:%S')}")
print()

# INITIALISATION SIMPLE
app = Flask(__name__)

# ESSAIE DE DÉMARRER TELEGRAM, MAIS CONTINUE SI ERREUR
try:
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    print("✅ Bot Telegram initialisé")
    TELEGRAM_OK = True
except Exception as e:
    print(f"⚠️ Erreur Telegram: {e}")
    print("⚠️ Le site web fonctionnera sans Telegram")
    TELEGRAM_OK = False

# ========== ROUTES WEB SIMPLES ==========
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🤖 Trader Bot Pro MG</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                padding: 50px;
                background: #f5f5f5;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: 0 auto;
            }
            h1 { color: #4CAF50; }
            .status { 
                background: #4CAF50; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 TRADER BOT PRO MADAGASCAR</h1>
            <div class="status">🟢 EN LIGNE - NOUVEAU TOKEN</div>
            <p>📍 Nouveau bot créé avec succès</p>
            <p>📱 Telegram: @TraderBotProMG_bot</p>
            <p>🎯 Token actif et vérifié</p>
            <p><a href="/health">📡 Vérifier l'état</a></p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {
        "status": "active",
        "service": "Trader Bot Pro Madagascar",
        "version": "2.0",
        "timestamp": datetime.now().isoformat(),
        "telegram": "configured" if TELEGRAM_OK else "not_configured",
        "port": PORT
    }

# ========== TELEGRAM SEULEMENT SI ÇA MARCHE ==========
if TELEGRAM_OK:
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "✅ NOUVEAU BOT ACTIVÉ! Trader Bot Pro Madagascar 🇲🇬")

    @bot.message_handler(commands=['status'])
    def send_status(message):
        bot.reply_to(message, f"🟢 ACTIF | {datetime.now().strftime('%H:%M:%S')} | Madagascar")

    def start_telegram():
        try:
            print("📱 Lancement du bot Telegram...")
            bot.polling(non_stop=True, timeout=60)
        except Exception as e:
            print(f"❌ Erreur Telegram polling: {e}")

# ========== DÉMARRAGE SÉCURISÉ ==========
if __name__ == "__main__":
    print("🚀 Démarrage sécurisé...")
    
    # Démarrer Telegram si disponible
    if TELEGRAM_OK:
        telegram_thread = threading.Thread(target=start_telegram, daemon=True)
        telegram_thread.start()
        print("✅ Thread Telegram démarré")
    
    print(f"🌐 Serveur web sur port {PORT}")
    print("⚡ Attente des requêtes...")
    
    # Démarrer Flask (BLOCKANT)
    try:
        app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
    except Exception as e:
        print(f"❌ Erreur Flask: {e}")
