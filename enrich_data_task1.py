import pandas as pd
import os
import shutil
from datetime import datetime

# Paths
xlsx_path = "data/raw/ethiopia_fi_unified_data.xlsx"
backup_path = "data/raw/ethiopia_fi_unified_data_backup.xlsx"

# Backup
if os.path.exists(xlsx_path):
    shutil.copy(xlsx_path, backup_path)
    print(f"Backed up {xlsx_path} to {backup_path}")

# Load Data
try:
    df_main = pd.read_excel(xlsx_path, sheet_name=0)
    print(f"Loaded {len(df_main)} records from Main Sheet.")

    # Check if Impact Sheet exists and load/append if needed for unified View
    # Note: Task says add to unified_data.csv. We will create that.

    # 1. Observation: ACC_4G_COVERAGE, 2024, 51.0
    new_obs = {
        "record_id": f"REC_ENRICH_{datetime.now().strftime('%M%S')}1",
        "record_type": "observation",
        "category": "Infrastructure",
        "pillar": "Access",
        "indicator_code": "ACC_4G_COVERAGE",
        "indicator": "4G Network Coverage",
        "value_numeric": 51.0,
        "value_unit": "Percentage",
        "observation_date": pd.Timestamp("2024-12-31"),
        "collection_date": pd.Timestamp("2024-12-31"),
        "source": "Ethio Telecom 2024 Report",
        "original_text": "4G coverage reached 51% of population",
        "confidence": "High",
    }

    # 2. Event: EVT_FAYDA_PILOT
    new_evt = {
        "record_id": "EVT_FAYDA_PILOT",
        "record_type": "event",
        "category": "infrastructure",  # Lowercase as requested? keeping mixed safe
        "pillar": "Access",
        "indicator_code": None,
        "observation_date": pd.Timestamp("2023-06-01"),
        "original_text": "Fayda Digital ID Pilot Launch",
        "source": "NBE",
        "confidence": "High",
    }

    # 3. Impact Link: EVT_FAYDA_PILOT -> ACC_OWNERSHIP
    # Note: Impact links might be in a separate sheet or unified.
    # Structure for Impact Link usually: record_type='impact_link', parent_id='EVT_...', indicator_code='ACC_OWNERSHIP'
    new_link = {
        "record_id": f"IMP_{datetime.now().strftime('%M%S')}",
        "record_type": "impact_link",
        "parent_id": "EVT_FAYDA_PILOT",
        "indicator_code": "ACC_OWNERSHIP",
        "indicator": "Account Ownership",
        "impact_magnitude": "High",
        "lag_months": 6,
        "original_text": "Digital ID reduces KYC friction significantly",
        "confidence": "High",
    }

    # Append to Main DataFrame (assuming unified structure)
    # Align columns
    for r in [new_obs, new_evt, new_link]:
        # specific handling if we need to put impact in a different sheet?
        # The prompt implies a unified CSV. Let's create a unified DataFrame.
        # If the original file has multiple sheets, we'll try to append to the appropriate one or just the main one if it holds all types.
        # Based on previous exploration, record_type distinguishes them in the "unified" view.

        # Ensure all keys in r are columns in df_main, add missing if needed
        for k in r.keys():
            if k not in df_main.columns:
                df_main[k] = None

        df_main = pd.concat([df_main, pd.DataFrame([r])], ignore_index=True)

    print(f"Added {3} new records.")

    # Save as CSV (Requested)
    csv_path = "data/raw/ethiopia_fi_unified_data.csv"
    df_main.to_csv(csv_path, index=False)
    print(f"Saved unified data to {csv_path}")

    # Also update XLSX for system consistency?
    # Maybe safest to update XLSX too so existing loaders verify it.
    # But let's check if the Impact Link needs to go to 'Impact_sheet'.
    # Previous task showed 'Impact_sheet' exists.

    try:
        df_impact_sheet = pd.read_excel(xlsx_path, sheet_name="Impact_sheet")

        # Check if we should add the impact link here too
        # To be safe, let's skip modifying the Source Excel for now to avoid corruption unless necessary.
        # The User asked to add to "ethiopia_fi_unified_data.csv".
        pass
    except:
        pass

except Exception as e:
    print(f"Error enriching data: {e}")
