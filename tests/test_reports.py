import unittest
from reports import get_monthly_summary, get_yearly_summary
from auth import register_user, login_user
from transactions import add_transaction
import sqlite3

DB_NAME = "finance.db"

class TestReports(unittest.TestCase):
    def setUp(self):
        register_user("testuser", "password")
        self.user_id = login_user("testuser", "password")
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DELETE FROM transactions WHERE user_id = ?", (self.user_id,))
        conn.commit()
        conn.close()

        # Add sample transactions for May 2025
        add_transaction(self.user_id, 'Income', 'Salary', 3000, 'May Salary')
        add_transaction(self.user_id, 'Expense', 'Food', 500, 'Groceries')
        add_transaction(self.user_id, 'Expense', 'Rent', 1000, 'May Rent')

    def test_monthly_summary(self):
        income, expense, savings = get_monthly_summary(self.user_id, '5', '2025')
        self.assertEqual(income, 3000)
        self.assertEqual(expense, 1500)
        self.assertEqual(savings, 1500)

    def test_yearly_summary(self):
        income, expense, savings = get_yearly_summary(self.user_id, '2025')
        self.assertEqual(income, 3000)
        self.assertEqual(expense, 1500)
        self.assertEqual(savings, 1500)

if __name__ == "__main__":
    unittest.main()
