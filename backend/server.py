#uvicorn is a command the fastapi runs internally benefit no need to reload manually

from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from  typing import List
from pydantic import BaseModel


app = FastAPI()

class Expense(BaseModel):
    # expense_date : date
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date


class SelectedYearDate(BaseModel):
    # selected_year_date: date
    selected_year : int

class ExpenseDate(BaseModel):
    expense_date : date
    amount: float
    category: str
    notes: str


@app.get("/expenses/{expense_date}", response_model = List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expenses_for_date(expense_date, expense.amount, expense.category, expense.notes)

    return {"message" : "Expenses updated successfully"}


@app.post("/analytics/category/")
def get_analytics_category(date_range: DateRange):
    data = db_helper.fetch_expenses_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to Retrieve Summary from the database")
    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total'] / total) * 100 if total !=0 else 0
        breakdown[row['category']]={
            'Total': row['total'],
            'Percentage': percentage,
        }
    return breakdown


@app.post("/analytics/months/")
def get_analytics_months(date_year: SelectedYearDate):
    data = db_helper.fetch_expenses_summary_of_all_months_in_year( date_year.selected_year )
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to Retrieve Summary from the database")

    return data