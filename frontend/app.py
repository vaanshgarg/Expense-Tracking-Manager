import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_tab
from analytics_by_months import analytics_month_tab


API_URL = "https://project-expense-tracking.onrender.com/"

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
)

st.title("💰 Expense Analytics Dashboard")
st.caption("Track and visualize your spending habits")

tab1, tab2, tab3 = st.tabs(["Add/update", "Analytics (CategoryWise)","Analytics (MonthsWise/Year)"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_month_tab()