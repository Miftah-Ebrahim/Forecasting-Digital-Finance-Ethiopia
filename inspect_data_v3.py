import pandas as pd
import os

path = r"c:\Users\hp\Downloads\KAIM\KAIM WEEK 10\Forecasting-Digital-Finance-Ethiopia\data\raw\ethiopia_fi_unified_data.xlsx"

try:
    xl = pd.ExcelFile(path)
    print("File:", path)
    print("Sheet names:", xl.sheet_names)
    for sheet in xl.sheet_names:
        print(f"--- Sheet: {sheet} ---")
        df = pd.read_excel(path, sheet_name=sheet, nrows=5)
        print("Columns:", df.columns.tolist())
        print(df.head())
        print("\n")
except Exception as e:
    print(f"Error: {e}")
