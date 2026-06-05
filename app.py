import streamlit as st

import pandas as pd

import plotly.express as px

@st.cache_data

def load_data():

    return pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Sales":[1000, 1500, 1200]})


st.write("Sales Prototype")

df = load_data()

fig = px.bar(df, x="Month", y="Sales")

st.plotly_chart(fig)



