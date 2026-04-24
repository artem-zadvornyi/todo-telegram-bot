# 📝 Todo Telegram Bot

Simple Telegram bot for managing tasks using Python, SQLite, and python-telegram-bot.

## 🚀 Features

- Add tasks
- View task list
- Delete tasks
- Persistent storage (SQLite)
- Separate tasks per user

## 🛠 Tech Stack

- Python 3
- python-telegram-bot
- SQLite
- dotenv

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/todo-telegram-bot.git
cd todo-telegram-bot

2. Install dependencies:

pip install -r requirements.txt

3. Create .env file:

BOT_TOKEN=your_telegram_bot_token

▶️ Run the bot

python bot.py

💬 Commands

/start        - show help
/add <text>   - add new task
/list         - show all tasks
/delete <id>  - delete task

📁 Project Structure

todo-telegram-bot/
│── bot.py          # main bot logic
│── db.py           # database logic
│── requirements.txt
│── .gitignore

📌 Notes

Tasks are stored in SQLite database (tasks.db)
Each user has their own task list
.env and database file are excluded from Git

👤 Author

Artem Zadvornyi
