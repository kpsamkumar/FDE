from fastapi import FastAPI

invoices = [
    {"id": 1, "amount": 100.0, "status": "paid"},
    {"id": 2, "amount": 200.0, "status": "unpaid"},
    {"id": 3, "amount": 150.0, "status": "paid"},
    {"id": 4, "amount": 300.0, "status": "unpaid"},
    {"id": 5, "amount": 250.0, "status": "paid"}
    ]

app = FastAPI() 

@app.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):   
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            invoices.remove(invoice)
            return {"message": "Invoice deleted successfully"}
    return {"error": "Invoice not found"}

