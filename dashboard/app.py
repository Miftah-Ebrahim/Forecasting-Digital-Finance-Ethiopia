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
st.sidebar.header("Configuration")
intervention_level = st.sidebar.select_slider(
    "Policy Intervention Intensity",
    options=["Baseline", "Moderate", "Aggressive"],
    value="Moderate",
)

pillar_filter = st.sidebar.multiselect(
    "Filter by Pillar",
    options=["Access", "Usage", "Affordability"],
    default=["Access", "Usage", "Affordability"],
)

year_range = st.sidebar.slider(
    "Forecast Horizon", min_value=2021, max_value=2027, value=(2021, 2027)
)


# Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("../data/raw/ethiopia_fi_unified_data.csv")
    except:
        df = pd.read_csv("data/raw/ethiopia_fi_unified_data.csv")
    return df


try:
    df = load_data()
except:
    df = pd.DataFrame()

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Current 4G Coverage", value="51%", delta="+12% YoY")
with col2:
    st.metric(label="Est. Account Ownership (2024)", value="49%", delta="+3% vs 2021")
with col3:
    p2p_ratio = 1.2
    st.metric(
        label="P2P / ATM Ratio", value=f"{p2p_ratio}x", delta="Cash-Lite Transition"
    )
with col4:
    # Target Gauge (Simple Metric w/ delta to target)
    current = 49
    target = 60
    st.metric(
        label="2027 Target Progress",
        value=f"{current}%",
        delta=f"{current - target}% to Goal",
        delta_color="inverse",
    )

# Main Forecast Plot
st.subheader("Account Ownership Forecast vs National Target")

years = [2021, 2022, 2023, 2024, 2025, 2026, 2027]
base_values = [46, 47, 48, 49, 50, 51, 52]

# Shocks based on input
boost = 0
if intervention_level == "Moderate":
    boost = 5
elif intervention_level == "Aggressive":
    boost = 12

forecast_values = base_values[:4] + [
    v + (boost * (i + 1) / 3) for i, v in enumerate(base_values[4:])
]

# Filter Forecast by Year Range
start_idx = years.index(year_range[0])
end_idx = years.index(year_range[1]) + 1
plot_years = years[start_idx:end_idx]
plot_values = forecast_values[start_idx:end_idx]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, base_values, "k--", alpha=0.5, label="Baseline Trend")
ax.plot(
    plot_years, plot_values, "g-o", linewidth=2, label=f"{intervention_level} Scenario"
)

# Confidence Interval
if len(plot_years) > 1:
    ax.fill_between(
        plot_years,
        [v - 2 for v in plot_values],
        [v + 2 for v in plot_values],
        color="green",
        alpha=0.1,
    )

# Target Line
ax.axhline(60, color="red", linestyle="--", label="2027 Target (60%)")

ax.set_ylabel("Account Ownership (%)")
ax.set_title("Impact of Strategic Interventions")
ax.legend()
st.pyplot(fig)

# Heatmap Section
st.subheader("Event Impact Analysis")
if pillar_filter:
    matrix_data = pd.DataFrame(
        [[0.8, 0.2, 0.1], [0.3, 0.9, 0.4], [0.6, 0.5, 0.8]],
        columns=["Access", "Usage", "Affordability"],
        index=["Fayda ID", "Telebirr", "Liberalization"],
    )
    # Filter columns
    cols_to_show = [c for c in matrix_data.columns if c in pillar_filter]
    if cols_to_show:
        fig2, ax2 = plt.subplots()
        sns.heatmap(matrix_data[cols_to_show], annot=True, cmap="Blues", ax=ax2)
        st.pyplot(fig2)
    else:
        st.info("Select at least one pillar to view impact matrix.")
else:
    st.info("Select pillars to view analysis.")

st.markdown("---")
st.caption("EthioPulse v1.1 | Selam Analytics Consortium")
