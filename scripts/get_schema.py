import pandas as pd
import sys

path = r"c:\Users\hp\Downloads\KAIM\KAIM WEEK 10\Forecasting-Digital-Finance-Ethiopia\data\raw\ethiopia_fi_unified_data.xlsx"
out_path = r"c:\Users\hp\Downloads\KAIM\KAIM WEEK 10\Forecasting-Digital-Finance-Ethiopia\schema_info.txt"

try:
    with open(out_path, "w") as f:
        xl = pd.ExcelFile(path)
        f.write(f"Sheet Names: {xl.sheet_names}\n\n")
        for sheet in xl.sheet_names:
            f.write(f"--- Sheet: {sheet} ---\n")
            df = pd.read_excel(path, sheet_name=sheet, nrows=5)
            f.write(f"Columns: {list(df.columns)}\n")
            f.write(f"Head:\n{df.head().to_string()}\n\n")
    print("Schema info written to schema_info.txt")
except Exception as e:
    print(f"Error: {e}")
