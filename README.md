 
# 🤖 tgbot — Project Telegram Bot

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

An educational Telegram bot developed in **Python** to demonstrate fundamental programming concepts, including functions, modules, exception handling, regular expressions, and user input validation.

## 📌 About the Project

**tgbot** is a practice-oriented Python project that combines programming fundamentals with Telegram Bot API integration.

The project focuses on writing clean, modular, and reusable Python code while implementing practical bot commands.

## ✨ Features


- ⏱️ coming soon ...


## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pyTelegramBotAPI | Telegram Bot API integration |
| Regular Expressions (`re`) | Input validation and text processing |
| Python Modules | Modular code organization |
| Exception Handling | Error management |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
tgbot/
│
├── oop/                     # Object-oriented modules
│   ├── __init__.py
│   ├── user.py              # User class
│   ├── course.py            # Course class
│   ├── syllabus.py          # Syllabus management
│   └── telegram_bot.py      # Telegram bot class
│
├── syllabus/                # Course syllabus files
│   ├── pedagogy.md          # Pedagogy syllabus
│   └── psychology.md        # Psychology syllabus
│
├── bot.py                   # Main Telegram bot
├── config.py                # Bot configuration
├── functions.py             # Helper functions
├── test.py                  # Tests
├── contacts.txt             # List of verified students
│
├── Dockerfile               # Docker image configuration
├── compose.yaml             # Docker Compose configuration
├── .dockerignore            # Docker ignored files
├── .gitignore               # Git ignored files
├── requirements.txt         # Python dependencies
│
├── LICENSE                  # Project license
└── README.md                # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MalikovNurdaulet/tgbot.git
cd tgbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your bot
**Step 1. Create a Telegram Bot**

1. Open Telegram and [@BotFather](https://t.me/BotFather).
2. Send the `/newbot` command.
3. Follow the instructions to create your bot.
4. Copy the API token provided by BotFather.

**Step 2. Configure the Bot Token**

Open `config.py` and add your Telegram Bot API token:

```python
TOKEN = "YOUR_TOKEN"
```
Replace `YOUR_TOKEN` with your actual token from BotFather.

> **Security:** Never share your bot token or commit it to a public GitHub repository. Add `config.py` to `.gitignore` if it contains your token.

**Step 3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**Step 4. Run the Bot**

Run locally:

```bash
python bot.py
```

Or run using Docker:

```bash
docker compose up -d --build
```

**Step 5. Verify the Bot**

Check the Docker container logs:

```bash
docker compose logs -f
```

Expected output:
```text
Telegram bot started...
```

Open your bot in Telegram and send `/start` to verify that it works.


## 💬 Available Commands

| Command | Description |
|---|---|
| `/start` | Start the bot |
| `/courses` | List of subjetcs |
| `/info` | Info about subjects |
| `/logout` | Logout for guests |




## 🔮 Future Improvements plans

- […] Add database integration (PostgreSQL or SQLite)
- […] Implement user registration
- [✅] Add interactive inline keyboards
- […] Introduce logging and monitoring
- [✅] Containerize the application with Docker
- [✅] Deploy the bot to a cloud server

---