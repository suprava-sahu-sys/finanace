import sqlite3

conn = sqlite3.connect('finance_app.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Show transactions table content
cursor.execute("SELECT * FROM transactions;")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
