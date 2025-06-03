import unittest
import sqlite3
from transactions import add_transaction, delete_transaction

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                user TEXT,
                date TEXT,
                category TEXT,
                amount REAL,
                type TEXT
            )
        """)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_add_transaction(self):
        result = add_transaction("testuser", "2025-05-18", "Food", 100, "Expense")
        self.assertTrue(result, "Failed to add transaction")

    def test_delete_transaction(self):
        # Add transaction first
        add_result = add_transaction("testuser", "2025-05-18", "Food", 100.0, "expense")
        self.assertTrue(add_result, "Failed to add transaction")

        # Get the last inserted transaction ID
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM transactions WHERE user_id = ? ORDER BY id DESC LIMIT 1", ("testuser",))
        row = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(row, "No transaction found")
        transaction_id = row[0]

        # Now delete it
        delete_result = delete_transaction("testuser", transaction_id)
        self.assertTrue(delete_result, "Failed to delete transaction")


if __name__ == "__main__":
    unittest.main()
