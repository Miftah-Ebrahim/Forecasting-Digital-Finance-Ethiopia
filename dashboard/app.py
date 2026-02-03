import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="EthioPulse Dashboard")

# Title and Context
st.title("EthioPulse: Digital Finance Forecasting")
st.markdown("### National Bank of Ethiopia: Inclusion Strategy 2025-2027")

# Sidebar
st.sidebar.header("Scenario Configuration")
intervention_level = st.sidebar.select_slider(
    "Policy Intervention Intensity",
    options=["Baseline", "Moderate", "Aggressive"],
    value="Moderate",
)


# Load Data (Simulated or Real)
# For dashboard, we might load the same CSV
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("../data/raw/ethiopia_fi_unified_data.csv")
    except:
        # Fallback if running from dashboard dir
        df = pd.read_csv("data/raw/ethiopia_fi_unified_data.csv")
    return df


try:
    df = load_data()
    st.write(f"Loaded {len(df)} records.")
except:
    st.warning("Data not found, using simulation.")
    df = pd.DataFrame()

# Key Metrics Row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Current 4G Coverage", value="51%", delta="+12% YoY")
with col2:
    st.metric(label="Est. Account Ownership (2024)", value="49%", delta="+3% vs 2021")
with col3:
    # P2P/ATM Metric
    p2p_ratio = 1.2  # Placeholder or calc
    st.metric(
        label="P2P / ATM Withdrawal Ratio",
        value=f"{p2p_ratio}x",
        delta="Cash-Lite Transition",
    )

# Main Forecast Plot
st.subheader("Account Ownership Forecast (2025-2027)")

years = [2021, 2022, 2023, 2024, 2025, 2026, 2027]
base_values = [46, 47, 48, 49, 50, 51, 52]  # Historical + Base Trend

# Shocks based on selection
boost = 0
if intervention_level == "Moderate":
    boost = 5  # Fayda
elif intervention_level == "Aggressive":
    boost = 12  # Fayda + Liberalization

forecast_values = base_values[:4] + [
    v + (boost * (i + 1) / 3) for i, v in enumerate(base_values[4:])
]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, base_values, "k--", alpha=0.5, label="Baseline Trend")
ax.plot(
    years, forecast_values, "g-o", linewidth=2, label=f"{intervention_level} Scenario"
)
ax.fill_between(
    years,
    [v - 2 for v in forecast_values],
    [v + 2 for v in forecast_values],
    color="green",
    alpha=0.1,
)
ax.set_ylabel("Account Ownership (%)")
ax.set_title("Impact of Strategic Interventions")
ax.legend()
st.pyplot(fig)

# Heatmap Section
st.subheader("Event Impact Analysis")
# Synthetic Matrix for Display if real one depends on complex processing not in app
matrix_data = pd.DataFrame(
    [[0.8, 0.2, 0.1], [0.3, 0.9, 0.4], [0.6, 0.5, 0.8]],
    columns=["Access", "Usage", "Affordability"],
    index=["Fayda ID", "Telebirr", "Liberalization"],
)
fig2, ax2 = plt.subplots()
sns.heatmap(matrix_data, annot=True, cmap="Blues", ax=ax2)
st.pyplot(fig2)

st.markdown("---")
st.caption("EthioPulse v1.0 | Selam Analytics Consortium")
