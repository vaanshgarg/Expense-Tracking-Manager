import streamlit as st
import requests
import pandas as pd
import calendar

API_URL = "http://localhost:8000"

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

            st.bar_chart(df, x="Months", y="Total Expenditure")

            st.dataframe(df)






