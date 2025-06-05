import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_low_balance_alert(user_id, balance):
    message = f"🔔 Внимание! У пользователя ID {user_id} низкий баланс: {balance}"
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
    except Exception as e:
        print(f"Ошибка при отправке уведомления: {e}")
