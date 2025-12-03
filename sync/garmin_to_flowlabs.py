"""
Placeholder sync script for moving Garmin-derived check-ins
into the FlowLabs Hormone and Sensitivity API.

Currently does NOT connect to the Garmin Health API.
It simply reads local JSON files from an 'exports/' folder
and POSTs them to the FastAPI backend.
"""

import json
import pathlib
import requests


API_URL = "http://localhost:8000/ingest/hormone-checkin"
EXPORTS_DIR = pathlib.Path("exports")


def send_checkin(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    resp = requests.post(API_URL, json=payload)
    resp.raise_for_status()
    print(f"Sent {path.name}: {resp.json()}")


def main():
    if not EXPORTS_DIR.exists():
        print(f"Exports directory not found: {EXPORTS_DIR}")
        return

    for json_file in EXPORTS_DIR.glob("*.json"):
        send_checkin(json_file)


if __name__ == "__main__":
    main()
