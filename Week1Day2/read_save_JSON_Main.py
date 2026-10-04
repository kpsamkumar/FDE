import importlib
from fastapi import FastAPI

Save_JSON = importlib.import_module("05_save_return_json").app
Read_JSON = importlib.import_module("04_read_invoices_JSON").app

app = FastAPI()
app.include_router(Save_JSON, tags=["Invoices"])
app.include_router(Read_JSON, tags=["Invoices"])