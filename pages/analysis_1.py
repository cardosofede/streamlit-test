import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analysis 1")

file = st.file_uploader('Please upload your file')

if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    c1, c2 = st.columns(2)
    with c1:
        min_ss = st.number_input("Min Spending Score", min_value=0, max_value=100)
    with c2:
        max_ss = st.number_input("Max Spending Score", min_value=0, max_value=100)
    fig = px.scatter(df.loc[df["Spending Score (1-100)"].between(min_ss, max_ss),:], x="Annual Income (k$)", y="Spending Score (1-100)")
    st.plotly_chart(fig)
