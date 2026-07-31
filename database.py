import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT NOT NULL DEFAULT 'pendiente',
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = get_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()
    return tasks


def get_task(task_id):
    conn = get_connection()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return task


def insert_task(title, description, due_date):
    conn = get_connection()
    conn.execute(
        "INSERT INTO tasks (title, description, due_date, status, created_at) "
        "VALUES (?, ?, ?, 'pendiente', ?)",
        (title, description, due_date, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def update_task(task_id, title, description, due_date, status):
    conn = get_connection()
    conn.execute(
        "UPDATE tasks SET title = ?, description = ?, due_date = ?, status = ? "
        "WHERE id = ?",
        (title, description, due_date, status, task_id),
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()