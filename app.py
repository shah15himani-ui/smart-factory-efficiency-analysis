
---

import streamlit as st
import pandas as pd

st.title("Smart Factory Efficiency Dashboard")

df = pd.read_csv("processed_factory_data.csv")

# Sidebar filters
machine = st.sidebar.selectbox("Select Machine", df['Machine_ID'].unique())
mode = st.sidebar.selectbox("Operation Mode", df['Operation_Mode'].unique())

filtered = df[(df['Machine_ID'] == machine) & (df['Operation_Mode'] == mode)]

st.subheader("Filtered Data")
st.write(filtered.head())

st.subheader("Efficiency Distribution")
st.bar_chart(df['Efficiency_Status'].value_counts())

st.subheader("Production vs Defect")
st.scatter_chart(df[['Production_Speed_units_per_hr','Quality_Control_Defect_Rate_%']])
