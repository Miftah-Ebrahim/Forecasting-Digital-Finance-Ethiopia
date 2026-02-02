import sys
import os

sys.path.append("notebooks")
from data_loader import load_raw_data, process_data
import pandas as pd

df_u, _ = load_raw_data()
obs, evts, imps = process_data(df_u)

print("Observation Indicators:", obs["indicator_code"].unique())
print("Impact Link Indicators:", imps["indicator_code"].unique())

if "observation_date" in obs.columns:
    print("Observation Dates:", obs["observation_date"].dt.year.unique())

if "observation_date_evt" in evts.columns:
    print("Event Dates:", evts["observation_date_evt"].dt.year.unique())

# Check ACC_OWNERSHIP specifically
acc = obs[obs["indicator_code"] == "ACC_OWNERSHIP"]
print("ACC_OWNERSHIP Observations:", len(acc))
if not acc.empty:
    print(acc[["observation_date", "value_numeric"]])
