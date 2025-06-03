import sqlite3
from datetime import datetime

DB_NAME = "finance.db"

def get_monthly_summary(user_id, month, year):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT LOWER(type), SUM(amount) FROM transactions
        WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY LOWER(type)
    ''', (user_id, f"{int(month):02d}", str(year)))
    results = c.fetchall()
    conn.close()

    income = 0
    expense = 0
    for row in results:
        if row[0] == 'income':
            income = row[1]
        elif row[0] == 'expense':
            expense = row[1]

    savings = income - expense
    return income, expense, savings

def get_yearly_summary(user_id, year):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT LOWER(type), SUM(amount) FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY LOWER(type)
    ''', (user_id, str(year)))
    results = c.fetchall()
    conn.close()

    income = 0
    expense = 0
    for row in results:
        if row[0] == 'income':
            income = row[1]
        elif row[0] == 'expense':
            expense = row[1]

    savings = income - expense
    return income, expense, savings
