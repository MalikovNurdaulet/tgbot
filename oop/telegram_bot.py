import telebot

class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def start_command(self, message):
        pass
