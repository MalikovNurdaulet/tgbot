import telebot
from telebot import types
from config import GUEST_PASSWORD
from oop.user import User
from functions import today

class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.contacts_path = "contacts.txt"

        self.authorized_users = {}
        self.guest_users = set()
        self.waiting_password = set()

        self.register_handlers()

        # Очищаем общий список команд
        self.bot.delete_my_commands()
        self.bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())

    def register_handlers(self):

        @self.bot.message_handler(commands=["start"],chat_types=["private"])
        def start(message):
            user_id = message.from_user.id
            self.waiting_password.discard(user_id)
            if user_id in self.authorized_users:
                self.bot.send_message(
                    message.chat.id,
                    "✅ Вы уже вошли как студент."
                )
                return

            if user_id in self.guest_users:
                self.bot.send_message(
                    message.chat.id,
                    "✅ Вы уже вошли как гость."
                )
                return

            self.bot.delete_my_commands(scope=types.BotCommandScopeChat(chat_id=message.chat.id))
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

            keyboard.add(types.KeyboardButton("📱 Поделиться номером",request_contact=True))

            self.bot.send_message(
                message.chat.id,
                "Добро пожаловать!\n\n"
                "Поделитесь своим номером телефона.",
                reply_markup=keyboard
            )

        @self.bot.message_handler(commands=["logout"],chat_types=["private"])
        def logout(message):
            user_id = message.from_user.id
            if user_id in self.guest_users:
                self.guest_users.discard(user_id)
                self.waiting_password.discard(user_id)
                self.bot.delete_my_commands(scope=types.BotCommandScopeChat(chat_id=message.chat.id))
                self.bot.send_message(
                    message.chat.id,
                    "✅ Вы вышли из гостевого режима.\n"
                    "Для повторного входа нажмите /start."
                )
            else:
                self.bot.send_message(
                    message.chat.id,
                    "Вы не авторизованы как гость."
                )

        @self.bot.message_handler(commands=["today"],chat_types=["private"])
        def today_handler(message):
            user_id = message.from_user.id
            if user_id not in self.authorized_users:
                self.bot.send_message(
                    message.chat.id,
                    "❌ Команда доступна только студентам."
                )
                return
            self.bot.send_message(
                message.chat.id,
                today()
            )

        @self.bot.message_handler(content_types=["contact"],chat_types=["private"])
        def check_contact(message):
            contact = message.contact
            user_id = message.from_user.id
            if contact.user_id != user_id:
                self.bot.send_message(
                    message.chat.id,
                    "Пожалуйста, отправьте свой номер "
                    "через кнопку Telegram."
                )
                return
            user = User(
                user_id,
                message.from_user.username,
                message.from_user.first_name
            )
            student = user.find_by_phone(
                contact.phone_number,
                self.contacts_path
            )
            if student:
                self.authorized_users[user_id] = student
                self.guest_users.discard(user_id)
                self.waiting_password.discard(user_id)
                self.bot.set_my_commands(
                    [
                        types.BotCommand(
                            "today",
                            "Учебная неделя и дата"
                        )
                    ],
                    scope=types.BotCommandScopeChat(
                        chat_id=message.chat.id
                    )
                )

                self.bot.send_message(
                    message.chat.id,
                    "✅ Проверка пройдена!\n\n"
                    f"Имя: {student['first_name']}\n"
                    f"Фамилия: {student['last_name']}\n"
                    f"Факультет: {student['faculty']}\n\n"
                    "Роль: Студент",
                    reply_markup=types.ReplyKeyboardRemove()
                )

            else:
                self.waiting_password.discard(user_id)
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(
                    types.InlineKeyboardButton(
                        "📝 Зарегистрироваться",
                        callback_data="register"
                    )
                )
                keyboard.add(
                    types.InlineKeyboardButton(
                        "🔑 Войти как гость",
                        callback_data="guest"
                    )
                )
                self.bot.send_message(
                    message.chat.id,
                    "❌ Ваш номер не найден в списке студентов.\n"
                    "Выберите способ входа:",
                    reply_markup=keyboard
                )
                self.bot.send_message(
                    message.chat.id,
                    "Выберите вариант выше.",
                    reply_markup=types.ReplyKeyboardRemove()
                )

        @self.bot.callback_query_handler(func=lambda call: call.data in ("register", "guest"))
        def handle_choice(call):
            self.bot.answer_callback_query(call.id)
            user_id = call.from_user.id
            chat_id = call.message.chat.id
            if call.message.chat.type != "private":
                return
            if user_id in self.authorized_users:
                self.bot.send_message(
                    chat_id,
                    "Вы уже вошли как студент."
                )
                return
            if user_id in self.guest_users:
                self.bot.send_message(
                    chat_id,
                    "Вы уже вошли как гость."
                )
                return
            if call.data == "register":
                self.bot.send_message(
                    chat_id,
                    "📝 Регистрация студентов пока не реализована."
                )
            elif call.data == "guest":
                self.waiting_password.add(user_id)
                self.bot.send_message(
                    chat_id,
                    "🔐 Введите гостевой пароль:"
                )
        @self.bot.message_handler(func=lambda message: (message.from_user.id in self.waiting_password),content_types=["text"],chat_types=["private"])
        def check_guest_password(message):
            user_id = message.from_user.id
            if message.text == GUEST_PASSWORD:
                self.guest_users.add(user_id)
                self.waiting_password.discard(user_id)
                self.bot.set_my_commands(
                    [
                        types.BotCommand(
                            "logout",
                            "Выйти из гостевого режима"
                        )
                    ],
                    scope=types.BotCommandScopeChat(
                        chat_id=message.chat.id
                    )
                )
                self.bot.send_message(
                    message.chat.id,
                    "✅ Пароль верный!\n\n"
                    "Добро пожаловать в гостевой режим.\n"
                    "Ваша роль: Гость",
                    reply_markup=types.ReplyKeyboardRemove()
                )
            else:
                self.bot.send_message(
                    message.chat.id,
                    "❌ Неверный пароль!\n"
                    "Попробуйте ещё раз или нажмите /start."
                )

        @self.bot.message_handler(content_types=["text"],chat_types=["private"])
        def handle_text(message):
            user_id = message.from_user.id
            if user_id in self.authorized_users:
                return
            if user_id in self.guest_users:
                return
            if user_id in self.waiting_password:
                return
            self.bot.delete_my_commands(scope=types.BotCommandScopeChat(chat_id=message.chat.id))
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
            keyboard.add(
                types.KeyboardButton(
                    "📱 Поделиться номером",
                    request_contact=True
                )
            )
            self.bot.send_message(
                message.chat.id,
                "Для подтверждения номера необходимо "
                "нажать кнопку «📱 Поделиться номером».\n\n"
                "Номер телефона, введённый вручную, "
                "не подходит для подтверждения личности.",
                reply_markup=keyboard
            )

    def run(self):
        print("Telegram bot started...")
        self.bot.infinity_polling()
