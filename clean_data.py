"""
clean_data.py

Load raw JSON crime data and convert it into a clean CSV file
in data/processed/ for analysis.
"""

from pathlib import Path
import json
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_raw_json(filename: str) -> list[dict]:
    path = RAW_DATA_DIR / filename
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return data


def to_dataframe(records: list[dict]) -> pd.DataFrame:
    """
    Convert the list of crime records into a Pandas DataFrame
    with the most useful columns.
    """
    if not records:
        raise ValueError("No records supplied")

    rows = []
    for r in records:
        loc = r.get("location") or {}
        row = {
            "category": r.get("category"),
            "month": r.get("month"),
            "latitude": loc.get("latitude"),
            "longitude": loc.get("longitude"),
            "street_name": (loc.get("street") or {}).get("name"),
            "crime_id": r.get("id"),
            "outcome_status": (r.get("outcome_status") or {}).get("category"),
        }
        rows.append(row)

    return pd.DataFrame(rows)


def save_csv(df: pd.DataFrame, filename: str) -> Path:
    path = PROCESSED_DATA_DIR / filename
    df.to_csv(path, index=False)
    return path


def main() -> None:
    raw_filename = "leicester_all_crime.json"
    print(f"Loading {raw_filename} from data/raw/ ...")
    records = load_raw_json(raw_filename)

    print("Converting to DataFrame...")
    df = to_dataframe(records)
    print(f"DataFrame shape: {df.shape}")

    output_path = save_csv(df, "leicester_all_crime.csv")
    print(f"Saved cleaned data to {output_path}")


if __name__ == "__main__":
    main()
