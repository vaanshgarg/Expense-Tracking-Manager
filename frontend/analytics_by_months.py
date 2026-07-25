import streamlit as st
import requests
import pandas as pd
import calendar
import  plotly.express as px
from config import API_URL


# API_URL = "http://localhost:8000"


def analytics_month_tab():

    year = list(range(2005,2100))
    year = st.selectbox("Select Year", year,index=21)

    payload = {
        "selected_year": int(year)
    }

    response  = requests.post(f"{API_URL}/analytics/months/",json=payload)
    response = response.json()
    df = pd.DataFrame(response)

    if st.button("Get Analytics ") :
        if df.empty:
            st.warning("No data found for the selected year.")
        else:
            df.rename(columns={
                "Month": "Months",
                "Total_Expenses": "Total Expenditure",
            }, inplace=True)

            df['Months'] = df["Months"].apply(lambda x: calendar.month_name[x])

            # st.bar_chart(data = df , x ="Months", y="Total Expenditure")

            fig = px.bar(
                df,
                x="Months",
                y="Total Expenditure",
                text="Total Expenditure",
                color="Total Expenditure",
                color_continuous_scale=[
                    "#FFE0B2",
                    "#FFCC80",
                    "#FFB74D",
                    "#FB923C",
                    "#F97316",
                    "#EA580C"
                ]
            )

            fig.update_layout(
                paper_bgcolor="#FAF7F2",
                plot_bgcolor="#FAF7F2",
                font=dict(color="#2C2C2C"),
                coloraxis_showscale=False,
                title="Monthly Expenditure",
                title_x=0.5
            )

            fig.update_traces(
                marker_line_width=0,
                textposition="outside"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(df)







