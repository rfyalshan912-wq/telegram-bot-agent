import os
import telebot
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
AGENT_URL = os.getenv("AGENT_URL")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً! أرسل لي أي رسالة وأنا أوصلها للوكيل.")

@bot.message_handler(func=lambda m: True)
def forward(message):
    try:
        r = requests.post(AGENT_URL, json={"text": message.text}, timeout=30)
        reply = r.json().get("reply", "ما جاني رد من الوكيل")
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"صار خطأ: {e}")

bot.infinity_polling()
