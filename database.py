import sqlite3

DB_FILE = 'tasks.db'

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            deadline TEXT,
            status INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def get_tasks_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, deadline, status FROM tasks')
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_task_db(name, deadline=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, deadline) VALUES (?, ?)', (name, deadline))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def delete_task_db(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def toggle_task_status_db(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return False
    
    if row['status'] == 0:
        new_status = 1
    else:
        new_status = 0

    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()
    return True


create_table()
