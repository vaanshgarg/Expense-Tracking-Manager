import streamlit as st

st.title("Expense Management System")

expense_dt = st.date_input("Expense date: ")
if expense_dt:
    st.write(f"Fetching expenses for {expense_dt}")

