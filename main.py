from auth import register_user, login_user
from transactions import add_transaction, view_transactions, delete_transaction
from budget import set_budget, check_budget_status
import sqlite3
import reports
import backup_restore

def user_dashboard(user_id):
    while True:
        print("\n1. Add Transaction")
        print("2. Delete Transaction")
        print("3. View Transactions")
        print("4. View Reports")
        print("5. Set Budget")          # New option for budgeting
        print("6. Check Budget Status") # New option for checking budgets
        print("7. Backup Database")
        print("8. Restore Database")
        print("9. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\nAdd Transaction")
            t_type = input("Enter type (Income/Expense): ").strip().capitalize()
            if t_type not in ["Income", "Expense"]:
                print("❌ Invalid type. Please enter 'Income' or 'Expense'.")
                continue

            category = input("Enter category (e.g., Food, Salary, Rent): ").strip()
            try:
                amount = float(input("Enter amount: ₹"))
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
                continue
            description = input("Enter description (optional): ").strip()

            add_transaction(user_id, t_type, category, amount, description)
            print("✅ Transaction added successfully!")

        elif choice == '2':
            try:
                trans_id = int(input("Enter transaction ID to delete: "))
                delete_transaction(user_id, trans_id)
            except ValueError:
                print("❌ Invalid ID. Must be a number.")

        elif choice == '3':
            view_transactions(user_id)

        elif choice == '4':
            print("\n1. Monthly Report")
            print("2. Yearly Report")
            report_choice = input("Enter your choice: ").strip()

            if report_choice == '1':
                month = input("Enter month (1-12): ").strip()
                year = input("Enter year (e.g., 2025): ").strip()
                income, expense, savings = reports.get_monthly_summary(user_id, month, year)
                print(f"\n📅 Monthly Summary for {month}/{year}")
                print(f"Income: ₹{income}")
                print(f"Expenses: ₹{expense}")
                print(f"Savings: ₹{savings}")

            elif report_choice == '2':
                year = input("Enter year (e.g., 2025): ").strip()
                income, expense, savings = reports.get_yearly_summary(user_id, year)
                print(f"\n📆 Yearly Summary for {year}")
                print(f"Income: ₹{income}")
                print(f"Expenses: ₹{expense}")
                print(f"Savings: ₹{savings}")

            else:
                print("❌ Invalid choice.")

        elif choice == '5':  # Set Budget
            category = input("Enter category to set budget for (e.g., Food, Rent): ").strip()
            try:
                amount = float(input("Enter monthly budget amount: ₹"))
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
                continue
            set_budget(user_id, category, amount)
            print(f"✅ Budget set for category '{category}' as ₹{amount}")

        elif choice == '6':  # Check Budget Status
            category = input("Enter category to check budget status (e.g., Food, Rent): ").strip()
            check_budget_status(user_id, category)

        # Add these in the input handler
        elif choice == '7':
            backup_restore.backup_database()

        elif choice == '8':
            backup_file = input("Enter backup filename to restore: ").strip()
            backup_restore.restore_database(backup_file)

        elif choice == '9':
            print("Logged out successfully!")
            break

        else:
            print("❌ Invalid choice. Try again.")

def main():
    while True:
        print("\n==== Personal Finance Manager ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            register_user(username, password)

        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            user_id = login_user(username, password)
            if user_id:
                user_dashboard(user_id)

        elif choice == "3":
            print("✅ Exiting the application. Bye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
