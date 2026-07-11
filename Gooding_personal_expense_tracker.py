"""
Author: Omario Gooding
Date: July 10, 2026
Program: Personal Expense Tracker
Description:
This program saves personal expenses to a text file and displays
all expenses in a simple table.

"""

import os
import datetime


def build_record(description, amount, category):
    """Create one expense record as a comma-separated string."""
    today = str(datetime.date.today())

    # Keep descriptions at 30 characters or fewer.
    short_description = description[:30]

    # The amount is saved with exactly two decimal places.
    amount_text = f"{amount:.2f}"

    fields = [today, short_description, amount_text, category]
    record = ",".join(fields)

    return record


def load_records(filename):
    """Read saved expense records from the file."""
    records = []

    try:
        with open(filename, "r") as expense_file:
            for line in expense_file:
                clean_line = line.strip()

                if clean_line != "":
                    fields = clean_line.split(",")
                    records.append(fields)

    except FileNotFoundError:
        return []

    return records


def save_record(filename, record):
    """Add one expense record to the end of the file."""
    with open(filename, "a") as expense_file:
        expense_file.write(record + "\n")


def display_records(records):
    """Display all expense records in aligned columns."""
    if len(records) == 0:
        print("No expenses on record yet.")
        return

    print(f'{"Date":<12}{"Description":<32}{"Amount":>12}  {"Category":<20}')
    print("-" * 80)

    for record in records:
        date = record[0]
        description = record[1]
        amount = "$" + record[2]
        category = record[3]

        print(f"{date:<12}{description:<32}{amount:>12}  {category:<20}")


# The expense file will be stored in the folder where the program is run.
filename = os.path.join(os.getcwd(), "expenses.txt")

print("===== Your Expense Records =====")
saved_records = load_records(filename)
display_records(saved_records)

print()
number_of_expenses = int(input("How many expenses do you want to add? "))

for expense_number in range(1, number_of_expenses + 1):
    print()
    print(f"--- Expense {expense_number} ---")

    description = input("Description: ").strip()
    amount = float(input("Amount: "))
    category = input("Category: ").strip()

    new_record = build_record(description, amount, category)
    save_record(filename, new_record)

print()
print("===== Updated Expense Records =====")
updated_records = load_records(filename)
display_records(updated_records)