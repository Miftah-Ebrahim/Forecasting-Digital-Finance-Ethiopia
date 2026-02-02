import sys
import os

sys.path.append("notebooks")
from data_loader import load_raw_data, process_data
import pandas as pd

df_u, _ = load_raw_data()
obs, evts, imps = process_data(df_u)

print("ALL Impact Indicators (Normalized):")
print(imps["indicator_code"].unique())

print("Original Descriptions:")
temp_imps = df_u[df_u["record_type"].isin(["impact", "impact_link", "impact link"])]
if "indicator" in temp_imps.columns:
    print(temp_imps["indicator"].unique())
else:
    print(temp_imps["indicator_code"].unique())
