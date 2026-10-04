
import json
from typing import Annotated

from fastapi import FastAPI, Path
from json import load
from pathlib import Path as FilePath

app = FastAPI()


@app.delete("/invoices/{invoice_id}")
def delete_invoices(invoice_id: Annotated[str, Path()]):
    json_file_path = FilePath(__file__).parent / "data" / "invoices.json"

    with open(json_file_path, "r") as file:
        invoices = load(file)

        for invoice in invoices:
            if invoice.get("invoice_id") == invoice_id:
                invoices.remove(invoice)
                break
    
    with open(json_file_path, "w") as file:
        json.dump(invoices, file)
    return {"message": "Invoice deleted successfully"}
