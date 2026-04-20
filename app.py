import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

# Title
st.title("🏭 Smart Factory Efficiency Dashboard")

# Load data
df = pd.read_csv("processed_factory_data.csv")

# Sidebar filters
st.sidebar.header("Filters")

machine = st.sidebar.selectbox("Select Machine", df['Machine_ID'].unique())
mode = st.sidebar.selectbox("Select Operation Mode", df['Operation_Mode'].unique())

filtered_df = df[(df['Machine_ID'] == machine) & (df['Operation_Mode'] == mode)]

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("📊 Data Preview")
st.write(filtered_df.head())

# -------------------------------
# EFFICIENCY DISTRIBUTION
# -------------------------------
st.subheader("📉 Efficiency Distribution")
st.bar_chart(df['Efficiency_Status'].value_counts())

# -------------------------------
# CORRELATION HEATMAP
# -------------------------------
st.subheader("🔥 Correlation Heatmap")

plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
st.pyplot(plt)
plt.clf()

# -------------------------------
# TEMPERATURE VS DEFECT
# -------------------------------
st.subheader("🌡️ Temperature vs Defect Rate")

plt.figure()
sns.scatterplot(data=df, x='Temperature_C', y='Quality_Control_Defect_Rate_%')
st.pyplot(plt)
plt.clf()

# -------------------------------
# VIBRATION VS ERROR
# -------------------------------
st.subheader("⚙️ Vibration vs Error Rate")

plt.figure()
sns.scatterplot(data=df, x='Vibration_Hz', y='Error_Rate_%')
st.pyplot(plt)
plt.clf()

# -------------------------------
# POWER VS EFFICIENCY
# -------------------------------
st.subheader("⚡ Power Consumption vs Efficiency")

plt.figure()
sns.boxplot(data=df, x='Efficiency_Status', y='Power_Consumption_kW')
st.pyplot(plt)
plt.clf()

# -------------------------------
# PRODUCTION VS DEFECT
# -------------------------------
st.subheader("📦 Production Speed vs Defect Rate")

plt.figure()
sns.scatterplot(data=df, x='Production_Speed_units_per_hr', y='Quality_Control_Defect_Rate_%')
st.pyplot(plt)
plt.clf()

# -------------------------------
# MACHINE SUMMARY
# -------------------------------
st.subheader("📌 Machine Summary")

summary = df.groupby('Machine_ID').agg({
    'Health_Index':'mean',
    'Production_Speed_units_per_hr':'mean',
    'Quality_Control_Defect_Rate_%':'mean',
    'Error_Rate_%':'mean'
}).sort_values(by='Health_Index')

st.write(summary)
