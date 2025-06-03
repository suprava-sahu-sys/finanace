import sqlite3

conn = sqlite3.connect("finance.db")
c = conn.cursor()

# Replace this query if you want to try others
c.execute("SELECT id, user_id, type, category, amount, description, date FROM transactions")

rows = c.fetchall()

print("\n--- Transactions Table ---")
for row in rows:
    print(row)

conn.close()
