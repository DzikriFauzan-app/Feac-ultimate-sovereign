import sqlite3
import json
from datetime import datetime
from core.settings import Settings

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Settings.DB_PATH, check_same_thread=False)
        self._ensure_tables()

    def _ensure_tables(self):
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS agents (
                name TEXT PRIMARY KEY,
                status TEXT,
                capabilities TEXT,
                last_active TIMESTAMP
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                agent TEXT,
                command TEXT,
                payload TEXT,
                status TEXT,
                result TEXT,
                created_at TIMESTAMP,
                completed_at TIMESTAMP
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                level TEXT,
                message TEXT,
                timestamp TIMESTAMP
            )
        ''')
        self.conn.commit()

    def log_agent(self, name, status, capabilities):
        cur = self.conn.cursor()
        cur.execute('''
            INSERT OR REPLACE INTO agents (name, status, capabilities, last_active)
            VALUES (?, ?, ?, ?)
        ''', (name, status, json.dumps(capabilities), datetime.utcnow()))
        self.conn.commit()

    def add_task(self, task_id, agent, command, payload):
        cur = self.conn.cursor()
        cur.execute('''
            INSERT INTO tasks (id, agent, command, payload, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (task_id, agent, command, json.dumps(payload), "PENDING", datetime.utcnow()))
        self.conn.commit()

    def update_task(self, task_id, status, result=None):
        cur = self.conn.cursor()
        cur.execute('''
            UPDATE tasks SET status = ?, result = ?, completed_at = ? WHERE id = ?
        ''', (status, json.dumps(result) if result is not None else None, datetime.utcnow(), task_id))
        self.conn.commit()

    def add_log(self, source, level, message):
        cur = self.conn.cursor()
        cur.execute('''
            INSERT INTO logs (source, level, message, timestamp) VALUES (?, ?, ?, ?)
        ''', (source, level, message, datetime.utcnow()))
        self.conn.commit()
