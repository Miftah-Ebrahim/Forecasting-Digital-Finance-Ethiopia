import sys
import os

sys.path.append("notebooks")
from data_loader import load_raw_data, process_data

try:
    df_u, _ = load_raw_data()
    print("Loaded Raw Data:", df_u.shape)
    print("Record Types:", df_u["record_type"].unique())

    obs, evts, imps = process_data(df_u)
    print("Observations:", obs.shape)
    print("Events:", evts.shape)
    print("Impacts:", imps.shape)

except Exception as e:
    print(e)
