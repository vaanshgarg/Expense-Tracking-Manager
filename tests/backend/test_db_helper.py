from backend import db_helper


def test_fetch_expenses_for_date_aug_02():
    expenses = db_helper.fetch_expenses_for_date("2024-08-02")

    assert len(expenses)  == 6
    assert expenses[0]['amount'] == 50
    assert expenses[0]['category'] == "Entertainment"
    assert expenses[0]['notes'] == "Movie tickets"

def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-01")
    assert len(expenses) == 0


def test_fetch_expenses_summary_invalid_range():
    expenses = db_helper.fetch_expenses_summary("9999-08-01","8888-02-01")
    assert len(expenses) == 0
