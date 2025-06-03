import unittest
from budget import set_budget, check_budget_status
from auth import register_user, login_user
from transactions import add_transaction
import sqlite3

DB_NAME = "finance.db"

class TestBudget(unittest.TestCase):
    def setUp(self):
        register_user("testuser", "password")
        self.user_id = login_user("testuser", "password")
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DELETE FROM budgets WHERE user_id = ?", (self.user_id,))
        c.execute("DELETE FROM transactions WHERE user_id = ?", (self.user_id,))
        conn.commit()
        conn.close()

    def test_set_and_check_budget(self):
        set_budget(self.user_id, "Food", 1000)
        # Add transactions to Food category
        add_transaction(self.user_id, "Expense", "Food", 400, "Groceries")
        add_transaction(self.user_id, "Expense", "Food", 700, "Dinner")

        # Should exceed budget (1100 > 1000)
        status, message = check_budget_status(self.user_id, "Food")
        self.assertTrue(status)
        self.assertIn("exceeded", message.lower())

        # For a category without budget
        status2, message2 = check_budget_status(self.user_id, "Rent")
        self.assertFalse(status2)
        self.assertIn("no budget set", message2.lower())

if __name__ == "__main__":
    unittest.main()
