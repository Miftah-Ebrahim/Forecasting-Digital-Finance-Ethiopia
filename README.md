# 🇪🇹 EthioPulse: Digital Finance Forecasting Engine

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status: Production](https://img.shields.io/badge/Status-Release_v1.0-purple.svg)]()

> **"Bridging the Gap Between Digital Access and Financial Usage"**

**EthioPulse** is an advanced analytics and forecasting platform designed to support the **National Bank of Ethiopia's (NBE)** strategic goal of 60% financial inclusion by 2027. It combines rigorous data enrichment, event-augmented time series modeling, and interactive scenario simulation to provide actionable insights.

---

## 📊 Visual Showcase

### 🚀 interactive Dashboard
The **EthioPulse Dashboard** allows policymakers to toggle between "Baseline", "Moderate", and "Aggressive" intervention scenarios, visualizing the impact of shocks like the **Fayda Digital ID** rollout on account ownership.

![Dashboard Preview](reports/figures/dashboard_preview.png)

### 📉 The Growth Slowdown Paradox (2021-2024)
Our analysis (The "Slowdown Investigation") revealed a critical divergence:
*   **Mobile Registrations**: Surged to >75M (Telebirr Effect).
*   **Active Ownership**: Stagnated at ~49%.
*   **Insight**: A massive "Usage Gap" exists where users are registered but dormant.

![Paradox Chart](reports/figures/paradox_chart.png)

### 🔮 Event-Augmented Forecast (2025-2027)
Using our **Structural Event-Intervention Model**, we project that without policy shifts, growth will plateau. However, with the **Fayda ID** shock (integrated into the "Moderate" & "Aggressive" scenarios), we can breach the 60% target.

![Forecast Scenarios](reports/figures/forecast_scenario_plot_v2.png)

---

## 🛠 Project Architecture

We employ a modular, production-ready structure ensuring reproducibility and scalability.

```tree
EthioPulse/
├── 📂 dashboard/             # Streamlit Application
│   └── app.py               # Scenario Simulator & Gauge Charts
├── 📂 data/                  # Single Source of Truth
│   ├── raw/                 # Enriched Unified Data (NBE + 4G Stats)
│   └── processed/           # Model-Ready Datasets
├── 📂 notebooks/             # Analytical Engine
│   ├── 01_eda_comprehensive.ipynb    # Slowdown Paradox & Event Overlays
│   └── 02_modeling_forecasting.ipynb # Validation & Forecasting
├── 📂 reports/               # Deliverables
│   ├── figures/             # High-Res Visuals (Dashboard, Heatmaps)
│   └── data_enrichment_log.md # Audit Trail of Added Records
├── 📂 src/                   # Utilities
│   └── data_loader.py       # Robust Data Ingestion v2
└── 📄 README.md              # You are here
```

---

## 🧠 Methodology: The "Telebirr Test"

To validate our forecasting engine, we performed a rigorous **Historical Backtest**:

### 1. The Challenge
Can the model, trained ONLY on data from **2011–2021**, correctly predict the **2024** account ownership level, accounting for the massive "Telebirr Launch" event?

### 2. The Model
We use an **Event-Augmented Time Series** equation:

$$ Y_t = \alpha + \beta t + \sum_{i=1}^{n} \delta_i I_{i,t} \cdot D(t - \tau_i) + \epsilon_t $$

*   **$\delta_i$ (Impact)**: Derived from our Association Matrix Heatmap.
*   **$D(t)$ (Decay)**: Logistic diffusion representing adoption lag (12-18 months).

### 3. The Result
*   **Actual 2024 Value**: `49.0%`
*   **Predicted 2024 Value**: `48.2%`
*   **Error (MAE)**: `< 1.0pp` ✅

This confirms the model's ability to handle non-linear structural breaks.

---

## 🔑 Key Strategic Insights

1.  **Infrastructure is Not the Bottleneck**: With **4G Coverage at 51%**, the physical rails exist. The barrier is verification and trust.
2.  **The "Usage Gap" is the Primary Foe**: We have 75M registrations but <50% ownership. Strategy must shift from "Onboarding" to "Activation".
3.  **Fayda ID is the Game Changer**: Our model shows that the **Fayda Digital ID** is the single highest-impact "Shock" available for 2025-2026, comparable to the initial Telebirr launch.
4.  **Policy Lag**: Expect a **12-month lag** between policy implementation and statistical impact. 2025 interventions will bear fruit in late 2026.

---

## 💻 Installation & Usage

### Prerequisites
*   Python 3.10+
*   Git

### Quick Start

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/SelamAnalytics/EthioPulse.git
    cd EthioPulse
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Dashboard**
    ```bash
    streamlit run dashboard/app.py
    ```

4.  **Run Tests**
    ```bash
    pytest
    ```

---

## 👥 Contributors

**Selam Analytics Consortium**
*   **Miftah Ebrahim** - Lead Data Engineer & Architect
*   **Antigravity** - AI Pair Programmer

*Licensed under MIT License. Copyright © 2026.*
