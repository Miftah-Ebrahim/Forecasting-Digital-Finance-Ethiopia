import sys
import os

sys.path.append("notebooks")
from data_loader import load_raw_data, process_data
import pandas as pd

try:
    df_u, _ = load_raw_data()
    print("Loaded Unified Data Shape:", df_u.shape)

    # Check record types in the combined dataframe
    if "record_type" in df_u.columns:
        print("Unique Record Types:", df_u["record_type"].unique())
    else:
        print("Column 'record_type' missing!")

    obs, evts, imps = process_data(df_u)
    print("Impacts Shape:", imps.shape)
    if not imps.empty:
        print(imps.head())
    else:
        print("Impacts DataFrame is EMPTY.")

except Exception as e:
    print(f"Error: {e}")
