import pandas as pd
import os


def load_raw_data():
    """
    Loads the unified Excel data.
    """
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
    df = pd.read_excel(path)

    # Map dates
    if "observation_date" not in df.columns:
        if "collection_date" in df.columns:
            df["observation_date"] = df["collection_date"]
        elif "date" in df.columns:
            df["observation_date"] = df["date"]

    if "observation_date" in df.columns:
        df["observation_date"] = pd.to_datetime(df["observation_date"])

    return df, None


def process_data(df_u, df_i=None):
    df = df_u.copy()

    observations = df[df["record_type"] == "observation"].copy()
    events = df[df["record_type"] == "event"].copy()
    impacts = df[df["record_type"] == "impact"].copy()

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
