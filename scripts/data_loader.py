import pandas as pd
import os
import re


def load_raw_data():
    paths = [
        "data/raw/ethiopia_fi_unified_data.xlsx",
        "../data/raw/ethiopia_fi_unified_data.xlsx",
        "../../data/raw/ethiopia_fi_unified_data.xlsx",
    ]

    path = None
    for p in paths:
        if os.path.exists(p):
            path = p
            break

    if not path:
        raise FileNotFoundError(f"Could not find data file in {paths}")

    print(f"Loading data from {path}...")

    df_main = pd.read_excel(path, sheet_name=0)

    try:
        df_impact = pd.read_excel(path, sheet_name="Impact_sheet")
        df = pd.concat([df_main, df_impact], ignore_index=True)
    except Exception as e:
        print(f"Warning: {e}")
        df = df_main

    if "indicator" in df.columns and "indicator_code" in df.columns:
        df["indicator_code"] = df["indicator_code"].fillna(df["indicator"])
    elif "indicator" in df.columns and "indicator_code" not in df.columns:
        df["indicator_code"] = df["indicator"]

    # Enhanced Mapping
    mapping = {
        "Account Ownership": "ACC_OWNERSHIP",
        "Data Affordability": "AFF_DATA_COST",
        "Gender Gap": "GEN_GAP_ACC",
        "Mobile Money Share": "GEN_MM_SHARE",
        "4G Coverage": "ACC_4G_COVERAGE",
        "P2P Count": "USG_P2P_COUNT",
        "Digital Payment": "USG_DIGITAL_PAYMENT",
        "Fayda": "ACC_OWNERSHIP",
        "Digital ID": "ACC_OWNERSHIP",
        "EthioPay": "USG_P2P_COUNT",
        "Safaricom": "AFF_DATA_COST",
    }

    def map_indicator(val):
        if pd.isna(val):
            return val
        val_str = str(val)
        for key, code in mapping.items():
            if key in val_str:
                return code
        return val

    df["indicator_code"] = df["indicator_code"].apply(map_indicator)

    if "observation_date" not in df.columns:
        if "collection_date" in df.columns:
            df["observation_date"] = df["collection_date"]
        elif "date" in df.columns:
            df["observation_date"] = df["date"]

    if "observation_date" in df.columns:
        df["observation_date"] = pd.to_datetime(df["observation_date"], errors="coerce")

    return df, None


def process_data(df_u, df_i=None):
    df = df_u.copy()
    if "record_type" in df.columns:
        df["record_type"] = df["record_type"].astype(str).str.lower().str.strip()

    observations = df[df["record_type"] == "observation"].copy()
    events = df[df["record_type"] == "event"].copy()
    impacts = df[
        df["record_type"].isin(["impact", "impact_link", "impact link"])
    ].copy()

    events_enriched = events.rename(
        columns={
            "observation_date": "observation_date_evt",
            "original_text": "original_text_evt",
        }
    )

    if "observation_date_evt" not in events_enriched.columns:
        events_enriched["observation_date_evt"] = (
            events_enriched["observation_date"]
            if "observation_date" in events_enriched.columns
            else pd.to_datetime("today")
        )
    if "original_text_evt" not in events_enriched.columns:
        events_enriched["original_text_evt"] = (
            events_enriched["original_text"]
            if "original_text" in events_enriched.columns
            else ""
        )

    if "value_numeric" in observations.columns:
        observations["value_numeric"] = pd.to_numeric(
            observations["value_numeric"], errors="coerce"
        )

    return observations, events_enriched, impacts


def enrich_data(df_u, df_i):
    return df_u, df_i
