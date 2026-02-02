import sys
import os

sys.path.append("notebooks")
from data_loader import load_raw_data

df_u, _ = load_raw_data()
targets = df_u[df_u["record_type"] == "target"]
print("Target Records Head:")
print(targets.head())
print("Target Columns:")
print(targets.columns)
