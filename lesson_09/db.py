# lesson_09/db.py
import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

def get_database_url() -> str:
    """
    Если DATABASE_URL не задан – используем SQLite (файл test.db в корне проекта).
    Для PostgreSQL пример:
    postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase
    """
    return os.getenv("DATABASE_URL", "sqlite:///test.db")

def make_engine(echo: bool = False) -> Engine:
    return create_engine(get_database_url(), echo=echo, future=True)

# DDL под SQLite (INTEGER PRIMARY KEY AUTOINCREMENT; булево как 0/1)
DDL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS test_students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    is_deleted INTEGER NOT NULL DEFAULT 0
);
"""

def ensure_schema(engine: Engine) -> None:
    """Создаёт таблицу, если её нет."""
    with engine.begin() as conn:
        conn.execute(text(DDL_CREATE_TABLE))
