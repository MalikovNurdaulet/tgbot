import telebot
from config import TOKEN

from classes.user import User
from classes.course import Course
from classes.telegram_bot import TelegramBot

bot = telebot.TeleBot(TOKEN)
