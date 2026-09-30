from expense_manager import ExpenseManager
from utils import print_expenses, get_valid_amount, get_non_empty_input, get_valid_date
from datetime import datetime

DATA_FILE = "expenses.json"


def add_expense(manager):
    print("\n--- Add Expense ---")
    amount = get_valid_amount("Amount (₹): ")
    category = get_non_empty_input("Category: ").title()
    description = get_non_empty_input("Description: ")
    date = get_valid_date("Date (DD-MM-YYYY, press Enter for today): ", allow_blank=True)

    expense = manager.add_expense(amount, category, description, date)
    print(f"\nExpense added successfully. ID: {expense['id']}")


def view_expenses(manager):
    print("\n--- All Expenses ---")
    expenses = manager.get_all()
    print_expenses(expenses)


def search_expenses(manager):
    print("\n--- Search Expenses ---")
    keyword = get_non_empty_input("Enter category or description: ")
    results = manager.search(keyword)
    print_expenses(results)


def delete_expense(manager):
    print("\n--- Delete Expense ---")
    expense_id = get_non_empty_input("Enter expense ID: ")
    if manager.delete_expense(expense_id):
        print("Expense deleted successfully.")
    else:
        print("No expense found with that ID.")


def monthly_summary(manager):
    print("\n--- Monthly Summary ---")
    month = input("Enter month (MM-YYYY, press Enter for current month): ").strip()
    if not month:
        month = datetime.now().strftime("%m-%Y")

    try:
        datetime.strptime(month, "%m-%Y")
    except ValueError:
        print("Invalid month. Use MM-YYYY.")
        return

    summary = manager.monthly_summary(month)
    print(f"\nMonth: {month}")
    print(f"Number of expenses : {summary['count']}")
    print(f"Total expenses     : ₹{summary['total']:.2f}")
    print(f"Average expense    : ₹{summary['average']:.2f}")
    print(f"Highest expense    : ₹{summary['highest']:.2f}")

    if summary["categories"]:
        print("\nCategory-wise spending:")
        for category, amount in summary["categories"].items():
            print(f"  {category:<18} ₹{amount:.2f}")
    else:
        print("No expenses found for this month.")


def export_report(manager):
    print("\n--- Export Report ---")
    filename = manager.export_report()
    print(f"Report exported successfully to: {filename}")


def show_menu():
    print("""
==================================================
              PERSONAL EXPENSE TRACKER
==================================================
1. Add Expense
2. View Expenses
3. Search Expenses
4. Delete Expense
5. Monthly Summary
6. Export Report
7. Exit
==================================================
""")


def main():
    manager = ExpenseManager(DATA_FILE)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_expense(manager)
            elif choice == "2":
                view_expenses(manager)
            elif choice == "3":
                search_expenses(manager)
            elif choice == "4":
                delete_expense(manager)
            elif choice == "5":
                monthly_summary(manager)
            elif choice == "6":
                export_report(manager)
            elif choice == "7":
                print("\nThank you for using Personal Expense Tracker!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
        except (EOFError, KeyboardInterrupt):
            print("\n\nProgram closed safely.")
            break
        except Exception as error:
            print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
