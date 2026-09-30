import json
import csv
import uuid
from collections import defaultdict
from datetime import datetime
from pathlib import Path


class ExpenseManager:
    """Handles expense storage, retrieval, searching and reporting."""

    def __init__(self, filename="expenses.json"):
        self.filename = Path(filename)
        self.expenses = self._load()

    def _load(self):
        if not self.filename.exists():
            return []

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def _save(self):
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description, date):
        expense = {
            "id": uuid.uuid4().hex[:8].upper(),
            "amount": round(float(amount), 2),
            "category": category,
            "description": description,
            "date": date,
        }
        self.expenses.append(expense)
        self._save()
        return expense

    def get_all(self):
        return sorted(
            self.expenses,
            key=lambda item: datetime.strptime(item["date"], "%d-%m-%Y"),
            reverse=True,
        )

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            expense for expense in self.get_all()
            if keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
        ]

    def delete_expense(self, expense_id):
        original_count = len(self.expenses)
        self.expenses = [
            expense for expense in self.expenses
            if expense["id"].upper() != expense_id.upper()
        ]

        if len(self.expenses) < original_count:
            self._save()
            return True
        return False

    def monthly_summary(self, month):
        selected = [
            expense for expense in self.expenses
            if expense["date"][3:] == month
        ]

        total = sum(item["amount"] for item in selected)
        categories = defaultdict(float)

        for item in selected:
            categories[item["category"]] += item["amount"]

        highest = max((item["amount"] for item in selected), default=0)

        return {
            "count": len(selected),
            "total": total,
            "average": total / len(selected) if selected else 0,
            "highest": highest,
            "categories": dict(
                sorted(categories.items(), key=lambda pair: pair[1], reverse=True)
            ),
        }

    def export_report(self, filename="expense_report.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Amount", "Category", "Description", "Date"])

            for expense in self.get_all():
                writer.writerow([
                    expense["id"],
                    f"{expense['amount']:.2f}",
                    expense["category"],
                    expense["description"],
                    expense["date"],
                ])

        return filename
