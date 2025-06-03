import sqlite3
from datetime import datetime

DB_NAME = "finance.db"

def set_budget(user_id, category, amount, month=None, year=None):
    if not month or not year:
        now = datetime.now()
        month = now.strftime("%m")
        year = now.strftime("%Y")
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Insert or update the budget
    c.execute('''
        INSERT INTO budgets (user_id, category, month, year, amount)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id, category, month, year)
        DO UPDATE SET amount=excluded.amount
    ''', (user_id, category, month, year, amount))

    conn.commit()
    conn.close()
    print(f"Budget of ₹{amount} set for '{category}' in {month}/{year}.")

def check_budget_status(user_id, category, month=None, year=None):
    if not month or not year:
        now = datetime.now()
        month = now.strftime("%m")
        year = now.strftime("%Y")

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Get the budget
    c.execute('''
        SELECT amount FROM budgets
        WHERE user_id = ? AND category = ? AND month = ? AND year = ?
    ''', (user_id, category, month, year))
    budget_row = c.fetchone()

    if not budget_row:
        conn.close()
        message = f"No budget set for '{category}' in {month}/{year}."
        print(message)  # optional print, remove if you want only return
        return False, message

    budget_amount = budget_row[0]

    # Calculate total expense for that category
    c.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND category = ? AND type = 'Expense'
        AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
    ''', (user_id, category, month, year))
    total_expense_row = c.fetchone()
    total_expense = total_expense_row[0] or 0

    conn.close()

    message = f"[{category} Budget] Limit: ₹{budget_amount} | Used: ₹{total_expense}"
    print(message)  # optional print, remove if needed

    if total_expense > budget_amount:
        alert_msg = f"⚠️ ALERT: Budget exceeded by ₹{total_expense - budget_amount}"
        print(alert_msg)  # optional print
        return True, alert_msg
    else:
        ok_msg = f"✅ Budget is under control. ₹{budget_amount - total_expense} left."
        print(ok_msg)  # optional print
        return True, ok_msg
