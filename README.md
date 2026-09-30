# Personal Expense Tracker

A command-line Personal Expense Tracker built using Python. The project allows users to record, view, search, delete, and analyze personal expenses. Data is stored locally in a JSON file and reports can be exported as CSV.

## Features

- Add a new expense
- View all saved expenses
- Search by category or description
- Delete an expense using its ID
- Generate monthly spending summaries
- Calculate total, average, and highest expense
- View category-wise spending
- Export expenses to CSV
- Persistent local storage using JSON
- Input validation and error handling
- Fully executable from a terminal

## Technologies Used

- Python 3
- JSON
- CSV
- `datetime`
- `pathlib`
- `uuid`
- `collections`

No third-party Python packages are required.

## Project Structure

```text
personal-expense-tracker/
│
├── main.py
├── expense_manager.py
├── utils.py
├── expenses.json
├── expense_report.csv       # created after exporting a report
├── requirements.txt
├── .gitignore
├── README.md
└── report/
    └── Project_Report.pdf
```

## Requirements

- Python 3.9 or newer
- A terminal/command prompt
- Git (only required for uploading the project to GitHub)

Check your Python version:

```bash
python --version
```

If `python` is not recognized on Windows, try:

```bash
py --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/personal-expense-tracker.git
cd personal-expense-tracker
```

### 2. Optional virtual environment

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

There are no external dependencies, but the following command can be used to verify the project setup:

```bash
pip install -r requirements.txt
```

## How to Run

From the project root:

```bash
python main.py
```

Windows alternative:

```bash
py main.py
```

## Menu

```text
1. Add Expense
2. View Expenses
3. Search Expenses
4. Delete Expense
5. Monthly Summary
6. Export Report
7. Exit
```

## Example

When adding an expense:

```text
Amount (₹): 450
Category: Food
Description: Dinner
Date (DD-MM-YYYY, press Enter for today): 30-09-2026
```

The application generates a unique expense ID and saves the record to `expenses.json`.

## Data Storage

The project uses JSON for persistent storage. This keeps the application simple and makes it possible to run without installing a database server.

Example record:

```json
{
    "id": "AB12CD34",
    "amount": 450.0,
    "category": "Food",
    "description": "Dinner",
    "date": "30-09-2026"
}
```

## CSV Export

Selecting **Export Report** creates:

```text
expense_report.csv
```

The CSV contains:

- Expense ID
- Amount
- Category
- Description
- Date

## Error Handling

The application validates:

- Empty text input
- Invalid amount
- Zero or negative amount
- Invalid date format
- Invalid menu choices
- Missing/corrupted JSON data

## Testing

Suggested test cases:

| Test | Input | Expected Result |
|---|---|---|
| Add expense | Valid amount/details | Expense is saved |
| Invalid amount | `abc` | Validation message |
| Negative amount | `-100` | Rejected |
| Empty category | Blank | Rejected |
| View expenses | Menu 2 | Saved records displayed |
| Search | `Food` | Matching records displayed |
| Delete | Existing ID | Record removed |
| Delete | Invalid ID | Not-found message |
| Summary | `09-2026` | Monthly statistics displayed |
| Export | Menu 6 | CSV file created |

## Learning Outcomes

This project demonstrates practical use of:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Object-oriented programming
- File handling
- JSON and CSV processing
- Exception handling
- Date and time processing
- Searching and sorting
- Modular programming

## Author

**Adarsh Bhardwaj**  
Python Essentials — Evaluated Course Project
