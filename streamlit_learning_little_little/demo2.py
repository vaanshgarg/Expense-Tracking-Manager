import streamlit as st

# Text elements
st.header("Streamlit Core Features")
st.subheader("Text Elements")
st.text("This is a simple text element")


#Data Display
st.subheader("Data Display")
st.write("Here is a simple table")
st.table({"Column1": [1,2,3], "Column2": [4,5,6]}, hide_index=False)

import pandas as pd
df = pd.DataFrame({
    "ColumnA": [1,2,3],
    "ColumnB": [4,5,6],
})
st.table(df,hide_index=False)

#Charts
st.subheader("Charts")
st.line_chart([1,2,3,4])


# User Input
st.subheader("User Input")
value = st.slider("Select a value",0,100)
st.write(f"Selected Value: {value}")


st.title("Interactive Widgets Example")

# Checkbox
if st.checkbox("Show/Hide"):
    st.write("checkbox is checked")

# Selectbox
option = st.selectbox("Select a number",[1,2,3,4])
st.write(f"Selected Option: {option}")

#Selectbox
option = st.selectbox("category", ['food','shopping'], label_visibility="collapsed")
st.write(f"Selected Option: {option}")

# Multiselect
options = st.multiselect("Select a number", [1,2,3,4])
st.write(f"Selected Option: {options}")





