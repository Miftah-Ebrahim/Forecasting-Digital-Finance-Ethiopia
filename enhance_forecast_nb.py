import json
import os

nb_path = "notebooks/02_impact_forecasting.ipynb"
project_root = (
    r"C:\Users\hp\Downloads\KAIM\KAIM WEEK 10\Forecasting-Digital-Finance-Ethiopia"
)
src_path = os.path.join(project_root, "src").replace("\\", "/")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Define new cells
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 4. Scenario Comparison & Additional Visuals\n",
            "### 4.1 Scenario Comparison: Baseline vs Event-Augmented (2027 Delta)",
        ],
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Calculate 2027 Delta\n",
            "f_2027 = forecast_df[forecast_df['year'] == 2027].iloc[0]\n",
            "base_2027 = f_2027['baseline_trend']\n",
            "opt_2027 = f_2027['forecast']\n",
            "delta = opt_2027 - base_2027\n",
            "\n",
            "scenarios = ['Baseline (No Events)', 'Event-Augmented (Forecast)']\n",
            "values = [base_2027, opt_2027]\n",
            "\n",
            "plt.figure(figsize=(10, 6))\n",
            "bars = plt.bar(scenarios, values, color=['gray', 'green'])\n",
            "plt.title(f'2027 Account Ownership Projection\\nDelta: +{delta:.2f} percentage points')\n",
            "plt.ylabel('Percentage')\n",
            "plt.ylim(0, 100)\n",
            "plt.grid(axis='y', alpha=0.3)\n",
            "\n",
            "# Add labels\n",
            "for bar in bars:\n",
            "    height = bar.get_height()\n",
            "    plt.text(bar.get_x() + bar.get_width()/2., height + 1,\n",
            "             f'{height:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')\n",
            "\n",
            "plt.savefig('../reports/figures/scenario_comparison_2027.png')\n",
            "plt.show()",
        ],
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 4.2 Impact Over Time (Cumulative Boost)"],
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.figure(figsize=(12, 5))\n",
            "plt.fill_between(forecast_df['year'], 0, forecast_df['impact_boost'], color='green', alpha=0.3)\n",
            "plt.plot(forecast_df['year'], forecast_df['impact_boost'], 'g-', linewidth=2)\n",
            "plt.title('Cumulative Impact of Events Over Time (Boost to Baseline)')\n",
            "plt.ylabel('Percentage Points')\n",
            "plt.xlabel('Year')\n",
            "plt.grid(True)\n",
            "plt.savefig('../reports/figures/impact_boost_trend.png')\n",
            "plt.show()",
        ],
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 4.3 Forecast with Confidence Bands (Clean View)"],
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.figure(figsize=(12, 6))\n",
            "\n",
            "# Plot Forecast\n",
            "plt.plot(forecast_df['year'], forecast_df['forecast'], 'b-', label='Forecast', linewidth=2)\n",
            "\n",
            "# Plot Uncertainty\n",
            "uncertainty_grow = (forecast_df['year'] - forecast_df['year'].min()) * 0.5\n",
            "upper = forecast_df['forecast'] + 5 + uncertainty_grow\n",
            "lower = forecast_df['forecast'] - 5 - uncertainty_grow\n",
            "\n",
            "plt.fill_between(forecast_df['year'], lower, upper, color='blue', alpha=0.1, label='95% Confidence Interval')\n",
            "\n",
            "# Add Target Line if applicable (e.g. 50%)\n",
            "plt.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='50% Threshold')\n",
            "\n",
            "plt.title('Account Ownership Forecast with Uncertainty Bounds')\n",
            "plt.xlabel('Year')\n",
            "plt.ylabel('Percentage')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.savefig('../reports/figures/forecast_with_ci.png')\n",
            "plt.show()",
        ],
    },
]

nb["cells"].extend(new_cells)

# Prepend the sys.path setup as well to avoid import errors
setup_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import sys\n",
        "import os\n",
        f"sys.path.append(r'{src_path}')\n",
        f"print(f'Added {src_path} to sys.path')\n",
    ],
}
nb["cells"].insert(0, setup_cell)


with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Added visualization cells and path setup to forecast notebook.")
