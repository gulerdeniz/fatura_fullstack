from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Invoice
from schemas import InvoiceCreate, InvoiceResponse
from datetime import date
import models
import os

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Lokal gelistirme icin localhost her zaman acik.
# Production frontend adresi FRONTEND_URL environment variable'i ile eklenir (Render dashboard'dan ayarlanir).
allowed_origins = ["http://localhost:5173"]
frontend_url = os.environ.get("FRONTEND_URL")
if frontend_url:
    allowed_origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Invoice API is running"}

@app.post("/invoices", response_model= InvoiceResponse)
def create_invoice(data: InvoiceCreate, db: Session = Depends(get_db)): #data: InvoiceCreate -> data, bu class'tan oluşan bir nesne ve pydantic ile oto doğrula dedik. 
    total = data.quantity * data.unit_price * (1+ data.vat_rate / 100)
    invoice = Invoice(
        recipient = data.recipient,
        seller = data.seller,
        product = data.product,
        quantity = data.quantity,
        unit_price = data.unit_price,
        vat_rate = data.vat_rate,
        total = round(total, 2),
        date = date.today()
    )
    db.add(invoice) # Yeni fatura nesnesini database'e kaydettik.
    db.commit() # Commit diyerek değişiklikleri kalıcı hale aldık.
    db.refresh(invoice) # Refresh diyerek pull yaptık ve returnden önce son hali garantilemiş olduk.
    return invoice

@app.get("/invoices", response_model= list[InvoiceResponse]) # Birden fazla fatura döneceği için liste içinde bekliyoruz. 
def get_invoices(db: Session = Depends(get_db)): #db bir database nesnesi, ona bağlanmak için oluşturduk.
    results = db.query(Invoice).all() #db.query diyerek bu database'i taramak istiyoruz. Ancak burada hangi tabloyu taramak istediğimizi yazmalıyız. Şuan Invoice tablosu mevcut.
    return results