# EthioPulse: Advanced Financial Inclusion Forecasting Platform

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.32.0-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Executive Summary

**EthioPulse** is the flagship forecasting engine developed by the **Selam Analytics Consortium** to power the National Bank of Ethiopia's "Digital Ethiopia 2025" strategy. Our mission is to provide a rigorous, data-driven roadmap to achieve **60% financial inclusion** by predicting the impact of policy interventions and infrastructure scaling.

### The Growth Slowdown Paradox
Despite a surge in digital accounts to **65 Million** (driven by Telebirr registration), **Global Findex** ownership data has only grown by **+3 percentage points** in real terms (2021-2024). EthioPulse addresses this using an Event-Augmented model to bridge the "Access vs Usage" gap.

---

## Key Analytical Components

### 1. [Enrichment Log](reports/data_enrichment_log.md)
*   **Methodology**: Hard-coded addition of 2024 NBE policy records and 4G coverage statistics.
*   **Key Source**: Ethio Telecom 2024 Report (51% 4G Coverage).

### 2. [Comprehensive EDA](notebooks/01_eda_comprehensive.ipynb)
*   **The Slowdown Investigation**: Analysis of the divergence between Mobile Money Registrations (explosive growth) and Findex Ownership (stagnant).
*   **Event Overlay**: Timeline visualization showing the lag between policy launch and statistical impact.

### 3. [Modeling & Forecasting](notebooks/02_modeling_forecasting.ipynb)
*   **Impact Matrix**: Heatmap quantifying the effect of "Fayda ID" and "Liberalization" on Access logic.
*   **Event-Augmented Forecast**: 2025-2027 projection comparing Baseline trend vs. Strategic Intervention scenarios (Optimistic).

### 4. [Interactive Dashboard](dashboard/app.py)
*   **Scenario Simulator**: Toggles for "Moderate" vs "Aggressive" policy intervention.
*   **Forecast Visuals**: Real-time rendering of the 2027 inclusion targets.

---

## Project Architecture

```tree
.
├── dashboard/
│   └── app.py              # Interactive Streamlit Scenario Simulator
├── data/
│   ├── raw/                # Enriched Data (CSV + XLSX)
│   └── processed/          # Cleaned CSVs for modeling
├── notebooks/
│   ├── 01_eda_comprehensive.ipynb    # YoY, Slowdown, Event Overlay
│   └── 02_modeling_forecasting.ipynb # Impact Matrix & Forecasting
├── reports/
│   ├── data_enrichment_log.md        # Documentation of enforced records
│   └── figures/                      # High-res output visuals
├── src/
│   └── data_loader.py      # Schema v2 Ingestion Logic
└── README.md               # Technical Documentation
```
---

## Key Insights
1.  **Paradox of Plenty**: Infrastructure (4G ~51%) exceeds Adoption (Ownership ~49%), indicating an "Usage Gap" rather than coverage gap.
2.  **Policy Lag**: Major events like Telebirr Launch show a 12-18 month lag before impacting Findex metrics significantly.
3.  **Future Catalyst**: The new **Fayda Digital ID** is the un-captured shock projected to drive the next wave of *verified* ownership (+5-7% boost).

---

## Setup & Deployment
```bash
# Clone
git clone https://github.com/SelamAnalytics/EthioPulse.git

# Install
pip install -r requirements.txt

# Run Dashboard
streamlit run dashboard/app.py
```

*Selam Analytics Consortium*
