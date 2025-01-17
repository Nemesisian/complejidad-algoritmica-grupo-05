import sqlite3

conn = sqlite3.connect("social_media.db")
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth DATE,
        country TEXT,
        phone_number TEXT UNIQUE,
        joined_date DATE DEFAULT CURRENT_TIMESTAMP
    )
"""
)

# Crear tabla de relaciones
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS user_followers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        user_followed TEXT NOT NULL,
        CONSTRAINT unique_relationship UNIQUE (user, user_followed)
    )
"""
)

conn.commit()
conn.close()
