
from json import load
from pathlib import Path
from fastapi import APIRouter


app = APIRouter()

def load_invoices():
    json_file_path = Path(__file__).parent / "data" / "invoices.json"
    with open(json_file_path, "r") as f:
        invoices = load(f)
    return invoices


@app.get("/invoices")
def get_invoices():
    invoices = load_invoices()
    return invoices 