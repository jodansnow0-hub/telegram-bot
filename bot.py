import telebot
import time

TOKEN = "8206754774:AAHXcrSPZgqQQ_Gzvk4RkNBqjMUABvhq_5s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running 24/7 🚀")

while True:
    try:
        print("Bot running...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)