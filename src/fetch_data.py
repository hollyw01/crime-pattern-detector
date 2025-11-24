"""
fetch_data.py

Download UK Police crime data for a given location and save it to data/raw/.
API docs: https://data.police.uk/docs/
"""

from pathlib import Path
import json
import requests


# Directory where raw data will be saved
ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_crime_data(lat: float, lng: float, date: str | None = None) -> list[dict]:
    """
    Fetch street-level crime data from the UK Police API.

    :param lat: Latitude of the location
    :param lng: Longitude of the location
    :param date: Optional date in YYYY-MM format (e.g. "2024-01")
    :return: List of crime records (dictionaries)
    """
    url = "https://data.police.uk/api/crimes-street/all-crime"
    params: dict[str, str | float] = {"lat": lat, "lng": lng}
    if date:
        params["date"] = date

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def save_json(data: list[dict], filename: str) -> Path:
    """
    Save data to a JSON file in data/raw/.
    """
    path = RAW_DATA_DIR / filename
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return path


def main() -> None:
    # Example: Leicester city centre coordinates (can change later)
    lat = 52.629729
    lng = -1.131592

    print("Fetching crime data...")
    records = fetch_crime_data(lat, lng)

    output_path = save_json(records, "leicester_all_crime.json")
    print(f"Saved {len(records)} records to {output_path}")


if __name__ == "__main__":
    main()
