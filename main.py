import telebot
from web3 import Web3

# --- اطلاعات خصوصی ---
TOKEN = "7988601127:AAFXcCLC94rdXTMNQ_YudTL0VqPBjuhdQ1w"
CHAT_ID = "256764836"
PRIVATE_KEY = "b2038d5efe463048a9d44ea612c6e3d36d493437ae242a00813e16f892c69e65"
WALLET_ADDRESS = "0xD15fBdba08e12C865c37751F57D3F936d56fd2d8"

# --- اتصال به تلگرام ---
bot = telebot.TeleBot(TOKEN)

# --- اتصال به شبکه بلاک‌چین (مثلاً BSC) ---
RPC_URL = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "✅ ربات فعال شد و آماده دریافت دستورات است!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() in ["سلام", "hi", "hello"]:
        bot.reply_to(message, "سلام! من ربات شکارچی توکن هستم، آماده‌ام!")
    elif "کیف پول" in message.text:
        bot.send_message(message.chat.id, f"🏦 آدرس کیف پول: `{WALLET_ADDRESS}`", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "پیامت دریافت شد! ✌️")

bot.send_message(CHAT_ID, "🤖 ربات راه‌اندازی شد!")

bot.polling()
