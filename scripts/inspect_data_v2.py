import pandas as pd
import os

data_dir = r"c:\Users\hp\Downloads\KAIM\KAIM WEEK 10\Forecasting-Digital-Finance-Ethiopia\data\raw"
files = ["ethiopia_fi_unified_data.xlsx", "Additional Data Points Guide.xlsx"]

for f in files:
    path = os.path.join(data_dir, f)
    print(f"--- {f} ---")
    try:
        xl = pd.ExcelFile(path)
        print("Sheet names:", xl.sheet_names)
        for sheet in xl.sheet_names:
            print(f"  Sheet: {sheet}")
            df = pd.read_excel(path, sheet_name=sheet, nrows=5)
            print("  Columns:", df.columns.tolist())
            print("  Head:")
            print(df.head())
            print("-" * 20)
    except Exception as e:
        print(f"Error reading {f}: {e}")
    print("\n")
