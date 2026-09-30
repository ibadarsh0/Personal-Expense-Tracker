# Testing Guide

Run the application:

```bash
python main.py
```

## Test 1: View Initial Data

Select:

```text
2
```

Expected: the three demo records from `expenses.json` appear.

## Test 2: Add Expense

Select:

```text
1
```

Enter:

```text
Amount: 500
Category: Food
Description: Dinner
Date: 30-09-2026
```

Expected: a new unique ID is displayed and the record is saved.

## Test 3: Invalid Amount

Enter:

```text
abc
```

Expected:

```text
Please enter a valid numeric amount.
```

## Test 4: Negative Amount

Enter:

```text
-100
```

Expected:

```text
Amount must be greater than zero.
```

## Test 5: Search

Select `3` and search for:

```text
Food
```

Expected: all Food records are displayed.

## Test 6: Delete

Select `4` and provide an existing expense ID.

Expected: the expense is deleted.

## Test 7: Monthly Summary

Select `5` and enter:

```text
09-2026
```

Expected: count, total, average, highest expense, and category totals are displayed.

## Test 8: Export

Select `6`.

Expected:

```text
expense_report.csv
```

is created in the project directory.
