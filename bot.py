import telebot
from config import TOKEN

from oop.user import User
from oop.course import Course
from oop.telegram_bot import TelegramBot

def main():
    bot = TelegramBot(TOKEN)
    bot.run()

if __name__ == "__main__":
    main()