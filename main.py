import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from db import add_task_db, get_tasks_db, delete_task_db


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Todo Bot 🤖\n\n"
        "Команды:\n"
        "/add текст задачи\n"
        "/list\n"
        "/delete номер"
    )


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    task = " ".join(context.args).strip()

    if not task:
        await update.message.reply_text("Пример:\n/add купить хлеб")
        return

    add_task_db(user_id, task)
    await update.message.reply_text(f"✅ Добавлено:\n{task}")


async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tasks = get_tasks_db(user_id)

    if not tasks:
        await update.message.reply_text("📭 Список задач пуст")
        return

    text = "📋 Твои задачи:\n\n"

    for task_id, task_text in tasks:
        text += f"{task_id}. {task_text}\n"

    await update.message.reply_text(text)


async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text("Пример:\n/delete 1")
        return

    try:
        task_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("Нужно написать число. Например:\n/delete 1")
        return

    deleted = delete_task_db(user_id, task_id)

    if deleted:
        await update.message.reply_text("🗑 Задача удалена")
    else:
        await update.message.reply_text("Такой задачи нет")


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found. Create .env file with BOT_TOKEN=your_token")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add_task))
    app.add_handler(CommandHandler("list", list_tasks))
    app.add_handler(CommandHandler("delete", delete_task))

    print("Todo Telegram Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
