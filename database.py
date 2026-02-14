import sqlite3
import os
from models import Contact

class ContactRepository:

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, "contacts.db")
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def get_all(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()

        conn.close()

        return [Contact(*row) for row in rows]

    def add(self, contact: Contact):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO contacts (name, phone, address) VALUES (?, ?, ?)",
            (contact.name, contact.phone, contact.address)
        )

        conn.commit()
        conn.close()

    def update(self, contact: Contact):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE contacts SET name=?, phone=?, address=? WHERE id=?",
            (contact.name, contact.phone, contact.address, contact.id)
        )

        conn.commit()
        conn.close()

    def delete(self, contact_id: int):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        conn.close()
