import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

# API_URL = "http://localhost:8000"
https://project-expense-tracking.onrender.com/

def analytics_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 30))

    if st.button("Get Analytics"):

        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/category", json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["Total"] for category in response],
            "Percentage": [response[category]['Percentage'] for category in response]
       }

        # df = pd.DataFrame.from_dict(response, orient="index")
        # df.index.name = "Category"

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense BreakDown By Category")

        # st.bar_chart(data= df_sorted.set_index("Category")['Percentage'], use_container_width=True)

        fig = px.bar(
            df,
            x="Category",
            y="Percentage",
            color="Percentage",
            color_continuous_scale=[
                "#FFE5B4",
                "#FFD08A",
                "#FFB347",
                "#FB923C",
                "#F97316",
                "#EA580C"
            ]
        )

        st.plotly_chart(fig, use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.dataframe(df_sorted)







