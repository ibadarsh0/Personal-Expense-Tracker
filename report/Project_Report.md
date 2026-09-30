# PERSONAL EXPENSE TRACKER
## Python Essentials — Project Report

**Student Name:** Adarsh Bhardwaj  
**Course:** Python Essentials  
**Project Title:** Personal Expense Tracker  
**Project Type:** Command-Line Application

---

## 1. Introduction

Managing daily expenses manually can make it difficult to understand where money is being spent. The Personal Expense Tracker is a command-line Python application designed to provide a simple way to record and analyze personal expenses.

The application stores expense information locally in JSON format and provides options for searching, deleting, summarizing, and exporting records.

---

## 2. Problem Statement

People often record expenses in notebooks or scattered applications, making it difficult to search previous transactions or calculate monthly spending.

The proposed system provides a lightweight terminal-based solution that allows users to:

- Record expenses.
- View saved expenses.
- Search expenses.
- Delete incorrect records.
- Calculate monthly statistics.
- Analyze spending by category.
- Export expense records to CSV.

---

## 3. Objectives

The main objectives are:

1. Develop a practical Python command-line application.
2. Demonstrate core Python programming concepts.
3. Implement persistent file-based data storage.
4. Validate user input.
5. Generate useful expense statistics.
6. Provide CSV export functionality.
7. Create a project that can be executed from a standard terminal without a GUI.

---

## 4. Scope

The application is intended for personal expense tracking.

### Included

- Expense creation
- Expense listing
- Expense searching
- Expense deletion
- Monthly analysis
- Category-wise analysis
- CSV report generation
- JSON persistence

### Not Included

- Online banking integration
- Cloud synchronization
- Multi-user authentication
- Online payment processing

These features are outside the scope of this academic project.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| JSON | Persistent expense storage |
| CSV | Report export |
| datetime | Date validation and monthly processing |
| pathlib | File management |
| uuid | Unique expense IDs |
| collections | Category aggregation |

The project uses Python's standard library and does not require third-party packages.

---

## 6. System Design

### Basic Flow

```text
+----------------------+
|      Start Program   |
+----------+-----------+
           |
           v
+----------------------+
| Load expenses.json   |
+----------+-----------+
           |
           v
+----------------------+
| Display Main Menu    |
+----------+-----------+
           |
           v
+----------------------+
| User selects option |
+----------+-----------+
           |
     +-----+-----+----------------+
     |           |                |
     v           v                v
   Add/View    Search/Delete    Summary
     |           |                |
     +-----------+----------------+
                 |
                 v
        +----------------+
        | Save / Display |
        +-------+--------+
                |
                v
          +-----------+
          | Exit?     |
          +-----+-----+
                |
          No <--+--> Yes
                |       |
                |       v
                |    Program End
                |
                +----> Menu
```

---

## 7. Module Description

### main.py

Responsible for:

- Displaying the menu.
- Receiving user choices.
- Calling the appropriate operations.
- Handling top-level errors.

### expense_manager.py

Contains the `ExpenseManager` class.

Responsibilities:

- Loading JSON data.
- Saving JSON data.
- Adding expenses.
- Returning expenses.
- Searching expenses.
- Deleting expenses.
- Calculating monthly summaries.
- Exporting CSV reports.

### utils.py

Contains reusable functions for:

- Validating amounts.
- Validating dates.
- Checking non-empty input.
- Formatting expense output.

### expenses.json

Stores expense records persistently.

---

## 8. Functionalities

### 8.1 Add Expense

The user enters:

- Amount
- Category
- Description
- Date

The program validates the input, generates a unique ID, and stores the record.

### 8.2 View Expenses

All saved expenses are displayed in a formatted table.

### 8.3 Search Expenses

Users can search by category or description. Matching is case-insensitive.

### 8.4 Delete Expense

An expense can be deleted using its unique ID.

### 8.5 Monthly Summary

The application calculates:

- Number of expenses
- Total spending
- Average expense
- Highest expense
- Category-wise spending

### 8.6 CSV Export

The complete expense list can be exported into a CSV file for further analysis.

---

## 9. Input Validation

The program validates user inputs before processing them.

Examples:

- Amount must be numeric.
- Amount must be greater than zero.
- Category cannot be blank.
- Description cannot be blank.
- Date must follow `DD-MM-YYYY`.
- Menu choices must be between 1 and 7.

This reduces incorrect or inconsistent data.

---

## 10. Testing

| Test Case | Expected Result |
|---|---|
| Add valid expense | Record is saved |
| Enter text instead of amount | Error message displayed |
| Enter negative amount | Input rejected |
| Enter blank category | Input rejected |
| View records | All records displayed |
| Search existing category | Matching records displayed |
| Search unavailable category | No records found |
| Delete valid ID | Record deleted |
| Delete invalid ID | Not-found message |
| Generate monthly summary | Statistics displayed |
| Export report | CSV created |

---

## 11. Sample Output

```text
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
Enter your choice: 5

--- Monthly Summary ---

Month: 09-2026
Number of expenses : 3
Total expenses     : ₹550.00
Average expense    : ₹183.33
Highest expense    : ₹350.00

Category-wise spending:
  Education          ₹350.00
  Food               ₹120.00
  Transport           ₹80.00
```

---

## 12. Advantages

- Simple command-line interface.
- No external database required.
- No third-party dependencies.
- Persistent data storage.
- Input validation.
- Modular code structure.
- Easy to execute and understand.
- CSV export for further processing.

---

## 13. Limitations

- Data is stored locally on one computer.
- No user authentication.
- No graphical interface.
- No automatic cloud backup.
- Currency is represented as Indian Rupees.

---

## 14. Future Enhancements

Possible future improvements include:

- Graphical user interface.
- SQLite database integration.
- User authentication.
- Budget limits and alerts.
- Charts and visual analytics.
- Cloud synchronization.
- Recurring expense support.

---

## 15. Conclusion

The Personal Expense Tracker demonstrates how Python can be used to build a practical command-line application. The project combines functions, classes, collections, file handling, JSON, CSV, validation, exception handling, and date processing into one application.

The project satisfies the requirement of being executable from a terminal while providing useful functionality for recording and analyzing expenses.
