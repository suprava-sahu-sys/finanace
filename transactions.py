import sqlite3

def add_transaction(user_id, type, category, amount, description):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (user_id, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, type, category, amount, description))

    conn.commit()
    conn.close()
    print("✅ Transaction added successfully.")
    return True

def view_transactions(user_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, type, category, amount, description, date FROM transactions WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 No transactions found.")
    else:
        print("\n📄 Your Transactions:")
        for row in rows:
            print(f"ID: {row[0]}, Type: {row[1]}, Category: {row[2]}, Amount: ₹{row[3]}, Desc: {row[4]}, Date: {row[5]}")

def delete_transaction(user_id, transaction_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (transaction_id, user_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("❌ Transaction not found or not yours.")
        return False
    else:
        print("✅ Transaction deleted.")
        return True
    conn.close()
