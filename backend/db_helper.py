import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper","server.log")

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password= "1234",
        database = "expense_manager"
    )

    cursor  = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date: called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date: called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s", (expense_date,))


def insert_expenses_for_date(expense_date, amount, category, notes):
    logger.info(f"insert_expenses for date: called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)", (expense_date, amount, category, notes))

def fetch_expenses_summary(start_date, end_date):
    logger.info(f"fetch_expenses_summary: called with start_date {start_date}, end_date {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            ''' 
            SELECT category, Sum(amount) as total 
            FROM expenses 
            WHERE expense_date
            BETWEEN %s and %s
            GROUP BY category ; 
            ''',(start_date, end_date))

        data = cursor.fetchall()
        return data

def fetch_expenses_summary_of_all_months_in_year(year):
    logger.info(f"fetch_expenses_summary_of_all_months_in_year: {year}")
    with get_db_cursor() as cursor:
        cursor.execute("""
            SELECT 
                MONTH(expense_date) AS Month,
                sum(amount) AS Total_Expenses
            FROM expenses 
            WHERE YEAR(expense_date) = %s 
            GROUP BY MONTH(expense_date)
        """, (year,))

        data = cursor.fetchall()
        return data


if __name__ == '__main__':
    expense_date = fetch_expenses_for_date("2024-09-30")
    # for data in expense_date:
    #     print(data)

    # insert_expenses_for_date("2025-01-02", 20000, "Clothes", "Zara")
    delete_expenses_for_date("2025-01-01")

    # summary = fetch_expenses_summary('2024-08-02','2024-09-03')
    # for record in summary:
    #     print(record)





# print(__file__)