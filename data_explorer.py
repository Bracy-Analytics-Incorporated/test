
import streamlit as st

import pandas as pd

import plotly.express as px

@st.cache_data

def load_data():

    return pd.read_csv(r"..\..\..\..\Navitas\ADPC_42203_20240826.csv")  # csv file


st.title("Data Exploration Tool")

df = load_data()

column = st.selectbox("Select Column", df.columns)

fig = px.histogram(df, x=column, title=f"Distribution of {column}")

st.plotly_chart(fig)
