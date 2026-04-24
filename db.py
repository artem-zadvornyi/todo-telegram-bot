import sqlite3


conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    text TEXT NOT NULL
)
""")

conn.commit()


def add_task_db(user_id: int, text: str) -> None:
    cursor.execute(
        "INSERT INTO tasks (user_id, text) VALUES (?, ?)",
        (user_id, text)
    )
    conn.commit()


def get_tasks_db(user_id: int):
    cursor.execute(
        "SELECT id, text FROM tasks WHERE user_id = ? ORDER BY id",
        (user_id,)
    )
    return cursor.fetchall()


def delete_task_db(user_id: int, task_id: int) -> bool:
    cursor.execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?",
        (task_id, user_id)
    )
    conn.commit()
    return cursor.rowcount > 0