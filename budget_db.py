import sqlite3

conn = sqlite3.connect("finance.db")
c = conn.cursor()

# Create budgets table
c.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
        user_id INTEGER,
        category TEXT,
        month TEXT,
        year TEXT,
        amount REAL,
        PRIMARY KEY (user_id, category, month, year)
    )
''')

conn.commit()
conn.close()

print("Budgets table created successfully.")
