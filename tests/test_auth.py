import unittest
import sqlite3
from auth import register_user, login_user

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()
        self.test_username = "testuser_{int(time.time())}"

    def tearDown(self):
        self.conn.close()

    def test_register_and_login(self):
        result = register_user(self.test_username, "password123")
        self.assertTrue(result, "Registration failed")

        login_result = login_user(self.test_username, "password123")
        self.assertTrue(login_result, "Login failed")

if __name__ == "__main__":
    unittest.main()
