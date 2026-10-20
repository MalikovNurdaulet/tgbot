import telebot
from config import TOKEN

from classes.user import User
from classes.course import Course
from classes.telegram_bot import TelegramBot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Telegram-бот.")


if __name__ == "__main__":
    print("Telegram bot is running...")
    bot.infinity_polling()