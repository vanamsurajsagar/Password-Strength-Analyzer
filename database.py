import sqlite3
from pathlib import Path
import bcrypt

DB_PATH = Path(__file__).with_name("password_history.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS password_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password_hash BLOB NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def hash_password(password: str):
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO password_history (password_hash) VALUES (?)",
            (password_hash,)
        )
        conn.commit()


def password_was_used(password: str) -> bool:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT password_hash FROM password_history"
        ).fetchall()

    password_bytes = password.encode("utf-8")
    return any(
        bcrypt.checkpw(password_bytes, stored_hash)
        for (stored_hash,) in rows
    )
