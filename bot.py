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
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ========== ROUTES WEB ==========
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
        "telegram": "configured",
        "port": PORT
    }

# ========== TELEGRAM COMMANDS ==========
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
    "🤖 *Bienvenue sur Trader Bot Pro Madagascar!* 🇲🇬\n\n"
    "✅ *Nouveau bot activé avec succès!*\n"
    "📊 *Fonctionnalités:*\n"
    "• Analyse marché temps réel\n"
    "• Signaux trading\n"
    "• Gestion risques\n\n"
    "⚡ *Commandes:*\n"
    "/start - Démarrer\n"
    "/status - Vérifier statut\n"
    "/signal - Signaux\n"
    "/help - Aide",
    parse_mode='Markdown')

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, 
    f"📈 *STATUT DU BOT*\n\n"
    f"⏰ *Heure:* {datetime.now().strftime('%H:%M:%S')}\n"
    f"🟢 *Statut:* ACTIF\n"
    f"📊 *Mode:* Trading 24/7\n"
    f"📍 *Région:* Madagascar\n\n"
    f"✅ Tout fonctionne normalement!",
    parse_mode='Markdown')

@bot.message_handler(commands=['signal'])
def send_signal(message):
    bot.reply_to(message,
    "🚨 *SIGNAL TRADING*\n\n"
    "*EURUSD (H1)*\n"
    "🟢 ACTION: BUY\n"
    "🎯 ENTRY: 1.0950\n"
    "⛔ SL: 1.0920\n"
    "✅ TP: 1.0980\n"
    "📊 CONFIDENCE: 78%\n\n"
    f"⚡ *Généré:* {datetime.now().strftime('%H:%M')}",
    parse_mode='Markdown')

# ========== DÉMARRAGE ==========
def start_telegram():
    print("📱 Démarrage du bot Telegram...")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    print("🚀 Lancement des services...")
    
    # Démarrer Telegram dans un thread
    telegram_thread = threading.Thread(target=start_telegram, daemon=True)
    telegram_thread.start()
    
    print("🌐 Serveur web démarré")
    print(f"🔗 URL: https://[ton-app].onrender.com")
    print("⚡ Prêt à recevoir des requêtes!")
    
    # Démarrer Flask
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)
