import json
from pathlib import Path

from fastapi import Body

from fastapi import APIRouter


app = APIRouter()

@app.post("/invoices")
def save_invoices(invoices: list[dict] = Body(...)):
    json_file_path = Path(__file__).parent / "data" / "invoices.json"

    with json_file_path.open("r", encoding="utf-8") as f:
        existing_invoices = json.load(f)
        existing_invoices.extend(invoices)
    with json_file_path.open("w", encoding="utf-8") as f:
        json.dump(existing_invoices, f, indent=4)
    return existing_invoices

