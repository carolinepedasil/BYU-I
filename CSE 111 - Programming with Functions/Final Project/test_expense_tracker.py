import pytest
import os
from expense_tracker import add_expense, get_category_summary, generate_monthly_report, load_expenses_from_file, view_expenses

TEST_FILE = "test_expenses.csv"

@pytest.fixture(autouse=True)
def setup_test_file():
    """Creates a temporary test CSV file before each test."""
    with open(TEST_FILE, mode="w", newline="") as file:
        file.write("2025-02-01,Food,15.00\n")
        file.write("2025-02-02,Transport,5.50\n")
        file.write("2025-02-02,Food,10.00\n")
        file.write("2025-02-03,Entertainment,20.00\n")

@pytest.mark.parametrize("category, expected", [
    ("Food", 25.00),
    ("Transport", 5.50),
    ("Entertainment", 20.00)
])
def test_get_category_summary(category, expected):
    """Tests the get_category_summary function."""
    result = get_category_summary(category)
    assert result["total_spent"] == expected

def test_generate_monthly_report():
    """Tests the generate_monthly_report function."""
    result = generate_monthly_report("2025-02")
    assert result["Food"] == 25.00
    assert result["Transport"] == 5.50
    assert result["Entertainment"] == 20.00

def test_add_expense():
    """Tests that add_expense correctly writes to the test file and reloads data."""
    
    add_expense("Utilities", 30.00, "2025-02-04")

    expenses = load_expenses_from_file()

    print("Expenses Loaded:", expenses)

    assert any(exp["category"] == "Utilities" and exp["amount"] == 30.00 for exp in expenses)

def test_view_expenses():
    """Tests that view_expenses returns a list."""
    expenses = view_expenses()
    assert isinstance(expenses, list)
    assert len(expenses) > 0

@pytest.fixture(scope="session", autouse=True)
def cleanup():
    """Removes the test file after tests finish."""
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
