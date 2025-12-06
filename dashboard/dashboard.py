import pandas as pd
import plotly.express as px
import streamlit as st


# Load Data

df = pd.read_csv(r"C:\Users\dyuti\OneDrive\Desktop\readmission_project\data\FY_2025_Hospital_Readmissions_Reduction_Program_Hospital (1).csv")
df.columns = df.columns.str.strip()

# Convert numeric columns
num_cols = [
    "Number of Discharges",
    "Excess Readmission Ratio",
    "Predicted Readmission Rate",
    "Expected Readmission Rate",
    "Number of Readmissions"
]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Sidebar Filters

st.sidebar.title("Filters")

condition = st.sidebar.multiselect(
    "Select Condition",
    df["Measure Name"].dropna().unique(),
    default=df["Measure Name"].dropna().unique()
)

state = st.sidebar.multiselect(
    "Select State",
    sorted(df["State"].dropna().unique()),
    default=df["State"].dropna().unique()
)

filtered = df[
    (df["Measure Name"].isin(condition)) &
    (df["State"].isin(state))
]


# Page Title

st.title("Hospital Readmission Dashboard")


# KPIs

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Hospitals", filtered["Facility ID"].nunique())
col2.metric("Avg Readmission Ratio", round(filtered["Excess Readmission Ratio"].mean(), 3))
col3.metric("Total Discharges", int(filtered["Number of Discharges"].sum()))

# Chart 1: By Condition
st.subheader("Readmission Ratio by Condition")

fig1 = px.box(
    filtered,
    x="Measure Name",
    y="Excess Readmission Ratio",
    title="Readmission by Condition"
)

st.plotly_chart(fig1)


# Chart 2: Scatter Plot

st.subheader("Discharges vs Readmission Ratio")

fig2 = px.scatter(
    filtered,
    x="Number of Discharges",
    y="Excess Readmission Ratio",
    color="Measure Name",
    title="Case Volume vs Readmission Risk",
    hover_data=["Facility Name", "State"]
)

st.plotly_chart(fig2)


# Chart 3: State Map

st.subheader("Average Readmission by State")

state_summary = filtered.groupby("State", as_index=False)["Excess Readmission Ratio"].mean()

fig3 = px.choropleth(
    state_summary,
    locations="State",
    locationmode="USA-states",
    color="Excess Readmission Ratio",
    scope="usa",
    title="State Readmission Performance"
)

st.plotly_chart(fig3)

# Table

st.subheader("Top High-Risk Hospitals")

table = filtered.sort_values("Excess Readmission Ratio", ascending=False)[
    ["Facility Name", "State", "Measure Name", "Excess Readmission Ratio"]
].head(15)

st.dataframe(table)
