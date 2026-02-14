import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "contacts.db")


def init_db():
    conn = sqlite3.connect(DB_NAME)
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

def get_all_contacts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    conn.close()
    return rows

def add_contact(name, phone, address):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, phone, address) VALUES (?, ?, ?)",
        (name, phone, address)
    )

    conn.commit()
    conn.close()

def update_contact(contact_id, name, phone, address):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE contacts SET name=?, phone=?, address=? WHERE id=?",
        (name, phone, address, contact_id)
    )

    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()