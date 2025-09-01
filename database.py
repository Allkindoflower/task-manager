import sqlite3
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_FILE = os.path.join(BASE_DIR, "tasks.db")



def get_connection():
    # Enable type detection for converters
    conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            deadline DATE,               -- Changed from TEXT to DATE
            status INTEGER DEFAULT 0,
            user_id TEXT,
            priority INTEGER DEFAULT 2  
        )
    ''')
    conn.commit()
    conn.close()

def get_tasks_db(user_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, deadline, status, priority FROM tasks WHERE user_id = ?', (user_id,))
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        task = dict(row)
        tasks.append(task)

    return tasks

def add_task_db(name, deadline, user_id, priority=2):
    if hasattr(priority, 'value'):  # Enum
        priority_int = priority.value
    else:
        priority_int = priority

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
    'INSERT INTO tasks (name, deadline, user_id, priority) VALUES (?, ?, ?, ?)',
    (name, deadline if deadline else None, user_id, priority_int)
)

    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id

def delete_task_db(task_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, user_id))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount > 0

def toggle_task_status_db(task_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT status FROM tasks WHERE id = ? AND user_id = ?', (task_id, user_id))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return False

    new_status = 0 if row['status'] else 1
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ? AND user_id = ?', (new_status, task_id, user_id))
    conn.commit()
    conn.close()
    return True

create_table()
