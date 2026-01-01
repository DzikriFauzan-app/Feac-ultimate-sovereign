import sqlite3
import json
from datetime import datetime
from .settings import Settings

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Settings.DB_PATH, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS agents (name TEXT PRIMARY KEY, status TEXT, capabilities TEXT, last_active TIMESTAMP)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, type TEXT, payload TEXT, status TEXT, result TEXT, created_at TIMESTAMP, completed_at TIMESTAMP)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, level TEXT, message TEXT, timestamp TIMESTAMP)''')
        self.conn.commit()

    def log_agent(self, name, status, capabilities):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO agents (name, status, capabilities, last_active) VALUES (?, ?, ?, ?)', (name, status, json.dumps(capabilities), datetime.now()))
        self.conn.commit()

    def add_task(self, task_id, task_type, payload):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (id, type, payload, status, created_at) VALUES (?, ?, ?, ?, ?)', (task_id, task_type, json.dumps(payload), "PENDING", datetime.now()))
        self.conn.commit()

    def update_task(self, task_id, status, result=None):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE tasks SET status = ?, result = ?, completed_at = ? WHERE id = ?', (status, json.dumps(result) if result else None, datetime.now(), task_id))
        self.conn.commit()
