import sqlite3

import sqlite3

DB_NAME = "finance.db"

def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print("✅ Registration successful.")
        return True
    except sqlite3.IntegrityError:
        print("❌ Username already exists. Try a different one.")
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    conn.close()
    if result:
        return result[0]  # return user_id
    else:
        print("❌ Invalid username or password.")
        return None
