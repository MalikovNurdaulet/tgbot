import telebot
from telebot import types
from oop.user import User

class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.contacts_path = "contacts.txt"
        self.authorized_users = {}
        self.register_handlers()

    def register_handlers(self):
        @self.bot.message_handler(commands=["start"],chat_types=["private"])
        def start(message):
            keyboard = types.ReplyKeyboardMarkup(
                resize_keyboard=True,
                one_time_keyboard=True
            )
            button = types.KeyboardButton(
                text="📱 Поделиться номером",
                request_contact=True
            )
            keyboard.add(button)
            self.bot.send_message(
                message.chat.id,
                "Добро пожаловать!\n\n"
                "Для входа в образовательный бот "
                "поделитесь своим номером телефона.",
                reply_markup=keyboard
            )

        @self.bot.message_handler(
            content_types=["contact"],
            chat_types=["private"]
        )
        def check_contact(message):

            if message.contact.user_id != message.from_user.id:
                self.bot.send_message(
                    message.chat.id,
                    "Пожалуйста, отправьте свой контакт "
                    "через кнопку Telegram."
                )
                return
            user = User(
                message.from_user.id,
                message.from_user.username,
                message.from_user.first_name
            )
            student = user.find_by_phone(
                message.contact.phone_number,
                self.contacts_path
            )
            if student:
                self.authorized_users[user.user_id] = student
                self.bot.send_message(
                    message.chat.id,
                    f"✅ Верификация пройдена!\n\n"
                    f"Имя: {student['first_name']}\n"
                    f"Фамилия: {student['last_name']}\n"
                    f"Факультет: {student['faculty']}",
                    reply_markup=types.ReplyKeyboardRemove()
                )
            else:
                self.authorized_users.pop(user.user_id, None)
                self.bot.send_message(
                    message.chat.id,
                    "❌ Вы не найдены в списке студентов.\n\n"
                    "Выберите один из вариантов:\n"
                    "1. Зарегистрироваться\n"
                    "2. Войти как гость",
                    reply_markup=types.ReplyKeyboardRemove()
                )
    def run(self):
        print("Telegram bot started...")
        self.bot.infinity_polling()
