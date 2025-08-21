# backend/database.py
import sqlite3
from typing import List
from models.course_model import Course

DB_FILE = "gpa_calculator.db"

class Database:
    def __init__(self, db_file=DB_FILE):
        self.conn = sqlite3.connect(db_file)
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            name TEXT,
            credits REAL,
            grade TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_course(self, code: str, name: str, credits: float, grade: str):
        query = "INSERT INTO courses (code, name, credits, grade) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (code, name, credits, grade))
        self.conn.commit()

    def get_all_courses(self) -> List[Course]:
        query = "SELECT id, code, name, credits, grade FROM courses"
        rows = self.conn.execute(query).fetchall()
        return [
            Course(
                id=r[0],
                code=r[1],
                name=r[2],
                credits=r[3],
                grade=r[4]
            )
            for r in rows
        ]

    def clear_courses(self):
        query = "DELETE FROM courses"
        self.conn.execute(query)
        self.conn.commit()
