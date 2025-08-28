# dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from forecasting import forecast
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import subprocess
import report_generator  # Import the module you created


# Load Data
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\sadiq\intellirev\data\company_data.csv")

df = load_data()
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

st.title("📊 IntelliRev - Company Performance Dashboard")

# Sidebar filters
company = st.sidebar.multiselect("Select Company", df["Company"].unique(), default=df["Company"].unique())
year = st.sidebar.multiselect("Select Year", df["Year"].unique(), default=df["Year"].unique())

filtered = df[df["Company"].isin(company) & df["Year"].isin(year)]

# KPI metrics
st.subheader("🔹 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered['Revenue'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered['Profit'].sum():,.0f}")
col3.metric("Lost Contracts", int(filtered["Lost_Contracts"].sum()))

# Charts
st.subheader("📈 Revenue by Company")
fig1 = plt.figure()
sns.barplot(data=filtered, x="Company", y="Revenue", estimator=sum)
st.pyplot(fig1)

st.subheader("📊 Revenue Trend Over Time")
fig1 = plt.figure(figsize=(8, 5))
sns.lineplot(data=filtered, x="Year", y="Revenue", hue="Company", marker="o")
plt.title("Revenue Trend")
plt.ylabel("Revenue")
plt.xticks(sorted(filtered["Year"].unique()))
st.pyplot(fig1)

st.subheader("💰 Profit Margin by Year")
fig2 = plt.figure()
sns.lineplot(data=filtered, x="Year", y="Profit_Margin", hue="Company", marker="o")
st.pyplot(fig2)

st.subheader("💸 Profit Margin Distribution")
filtered["Profit_Margin"] = (filtered["Profit"] / filtered["Revenue"]) * 100
fig2 = plt.figure(figsize=(8, 5))
sns.boxplot(data=filtered, x="Company", y="Profit_Margin")
plt.title("Profit Margin Distribution")
st.pyplot(fig2)


st.subheader("❌ Contract Losses by Reason")
fig3 = plt.figure()
sns.countplot(data=filtered, x="Loss_Reason", hue="Company")
plt.xticks(rotation=30)
st.pyplot(fig3)

st.subheader("❗ Loss Reason Share (Overall)")
loss_counts = filtered["Loss_Reason"].value_counts()
fig3 = plt.figure(figsize=(6, 6))
plt.pie(loss_counts, labels=loss_counts.index, autopct="%1.1f%%", startangle=140)
plt.axis("equal")
plt.title("Loss Reasons - Proportion by Count")
st.pyplot(fig3)


df = load_data()
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100
companies = df["Company"].unique().tolist()
st.subheader("📈 Forecasting")

selected_metric = st.selectbox("Select Metric to Forecast", ["Revenue", "Profit"])
selected_company = st.selectbox("Select Company", companies)

if st.button("Run Forecast"):
    historical, predicted = forecast(df, selected_company, selected_metric)

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=historical["ds"], y=historical["y"],
                             mode='lines+markers', name='Historical'))
    fig.add_trace(go.Scatter(x=predicted["ds"], y=predicted["yhat"],
                             mode='lines+markers', name='Forecast'))
    st.plotly_chart(fig, use_container_width=True)


st.subheader("📥 Export Report")

if st.button("Generate PDF Report"):
    with st.spinner("Generating PDF report..."):
        # Pass filtered dataframe to generate_pdf
        report_generator.generate_pdf(filtered)
    st.success("✅ PDF report generated! Check IntelliRev_Report.pdf in your folder.")

