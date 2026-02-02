import json
import os

nb_path = "notebooks/01_exploration_eda.ipynb"

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Define new cells
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 3. Advanced Visualizations\n",
            "### 3.1 Account Ownership Growth Rate (YoY)",
        ],
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Filter for Account Ownership\n",
            "acc_own = observations[observations['indicator_code'] == 'ACC_OWNERSHIP'].sort_values('observation_date').copy()\n",
            "acc_own['year'] = acc_own['observation_date'].dt.year\n",
            "\n",
            "# Calculate YoY Growth\n",
            "acc_own['growth_rate'] = acc_own['value_numeric'].pct_change() * 100\n",
            "\n",
            "plt.figure(figsize=(12, 6))\n",
            "sns.barplot(data=acc_own, x='year', y='growth_rate', palette='viridis')\n",
            "plt.title('YoY Growth Rate: Account Ownership')\n",
            "plt.ylabel('Growth Rate (%)')\n",
            "plt.xlabel('Year')\n",
            "plt.grid(axis='y', alpha=0.3)\n",
            "plt.savefig('../reports/figures/acc_ownership_growth_yoy.png')\n",
            "plt.show()",
        ],
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 3.2 Digital Payment Usage Trends w/ Event Markers"],
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "dig_pay = observations[observations['indicator_code'] == 'USG_DIGITAL_PAYMENT'].sort_values('observation_date')\n",
            "\n",
            "plt.figure(figsize=(14, 7))\n",
            "sns.lineplot(data=dig_pay, x='observation_date', y='value_numeric', marker='o', linewidth=2.5, color='orange')\n",
            "plt.title('Usage of Digital Payments Over Time')\n",
            "plt.ylabel('Percentage')\n",
            "plt.xlabel('Date')\n",
            "\n",
            "# Annotate key events if available\n",
            "for _, event in events_enriched.iterrows():\n",
            "    plt.axvline(x=event['observation_date_evt'], color='red', linestyle='--', alpha=0.3)\n",
            "    # plt.text(event['observation_date_evt'], 0, event['original_text_evt'][:10], rotation=90, fontsize=8)\n",
            "\n",
            "plt.grid(True)\n",
            "plt.savefig('../reports/figures/digital_payment_trend.png')\n",
            "plt.show()",
        ],
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 3.3 Indicator Correlation Heatmap"],
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Pivot data to have indicators as columns\n",
            "pivot_df = observations.pivot_table(index='observation_date', columns='indicator_code', values='value_numeric')\n",
            "\n",
            "plt.figure(figsize=(10, 8))\n",
            "sns.heatmap(pivot_df.corr(), annot=True, cmap='coolwarm', center=0)\n",
            "plt.title('Correlation Matrix of Financial Indicators')\n",
            "plt.tight_layout()\n",
            "plt.savefig('../reports/figures/indicator_correlation.png')\n",
            "plt.show()",
        ],
    },
]

nb["cells"].extend(new_cells)

with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Added visualization cells to notebook.")
