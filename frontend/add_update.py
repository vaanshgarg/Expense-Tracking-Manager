import streamlit as st
from datetime import datetime
import requests

# API_URL = "http://localhost:8000"
API_URL = "https://project-expense-tracking.onrender.com/"


def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("Request failed")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    with st.form(key="expense_form"):
        # Display columns headers
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Amount")
        with col2:
            st.header("Category")
        with col3:
            st.header("Notes")

        expenses = []
        for i in range(5):

            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            # st.session_state[f"amount_{i}"] = amount
            # st.session_state[f"category_{i}"] = category
            # st.session_state[f"notes_{i}"] = notes

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount,
                                               key=f"amount_{selected_date}_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{selected_date}_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", key=f"notes_{selected_date}_{i}", value=notes,
                                            label_visibility="collapsed")

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            # st.write(filtered_expenses)
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)

            if response.status_code == 200:
                st.success("Expense Updated Successfully!!!")
            else:
                st.error("Failed to update expenses.")







