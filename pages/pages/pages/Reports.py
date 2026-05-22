import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Milk Production Reports")

data = {
    "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Milk (L)":[12,15,18,16,20,22,19]
}

df = pd.DataFrame(data)

st.subheader("Weekly Milk Production")

fig = px.bar(
    df,
    x="Day",
    y="Milk (L)",
    color="Milk (L)",
    title="Milk Collection Report"
)

st.plotly_chart(fig)

total = df["Milk (L)"].sum()

st.metric(
    label="Total Milk Collected",
    value=f"{total} L"
)
