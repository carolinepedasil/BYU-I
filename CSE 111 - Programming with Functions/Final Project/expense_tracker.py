import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from collections import defaultdict

EXPENSE_FILE = "expenses.csv"

def add_expense(category: str, amount: float, date: str, filename: str = "expenses.csv") -> None:
    """Adds an expense entry to the dataset."""
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        datetime.strptime(date, "%Y-%m-%d")
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])
    except ValueError as e:
        print(f"Error: {e}")

def load_expenses_from_file(filename: str = EXPENSE_FILE) -> list:
    """Loads expenses from a CSV file and returns them as a list of dictionaries."""
    expenses = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    date, category, amount = row
                    expenses.append({"date": date, "category": category, "amount": float(amount)})
    except FileNotFoundError:
        print("No expense records found. Starting fresh.")
    return expenses

def view_expenses() -> list:
    """Returns a list of all recorded expenses."""
    return load_expenses_from_file()

def get_category_summary(category: str) -> dict:
    """Returns a summary of expenses for a given category."""
    expenses = load_expenses_from_file()
    total_spent = sum(exp["amount"] for exp in expenses if exp["category"].lower() == category.lower())
    return {"category": category, "total_spent": total_spent}

def generate_monthly_report(month: str) -> dict:
    """Generates a summary report for the given month (YYYY-MM)."""
    expenses = load_expenses_from_file()
    monthly_expenses = [exp for exp in expenses if exp["date"].startswith(month)]
    summary = defaultdict(float)
    for exp in monthly_expenses:
        summary[exp["category"]] += exp["amount"]
    return dict(summary)

def plot_expense_trends() -> None:
    """Plots expense trends over time using matplotlib."""
    expenses = load_expenses_from_file()
    if not expenses:
        print("No expense data available for plotting.")
        return

    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    df.sort_values(by="date", inplace=True)
    df_grouped = df.groupby("date")["amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(df_grouped.index, df_grouped.values, marker="o", linestyle="-", color="b")
    plt.xlabel("Date")
    plt.ylabel("Total Expenses")
    plt.title("Expense Trends Over Time")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    print("Expense Tracker Running...")
