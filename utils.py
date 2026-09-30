from datetime import datetime


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt).strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid numeric amount.")


def get_valid_date(prompt, allow_blank=False):
    while True:
        value = input(prompt).strip()

        if allow_blank and not value:
            return datetime.now().strftime("%d-%m-%Y")

        try:
            datetime.strptime(value, "%d-%m-%Y")
            return value
        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY.")


def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print(
        f"\n{'ID':<10} {'Date':<12} {'Category':<18} "
        f"{'Amount':>12}  Description"
    )
    print("-" * 80)

    for expense in expenses:
        print(
            f"{expense['id']:<10} "
            f"{expense['date']:<12} "
            f"{expense['category']:<18} "
            f"₹{expense['amount']:>10.2f}  "
            f"{expense['description']}"
        )
