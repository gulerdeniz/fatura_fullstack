# → API giriş/çıkış formatları (yeni kavram)
from datetime import date
from pydantic import BaseModel #FastAPI'ye gelen ve giden verileri otomatik doğrulayan kütüphane.
# Örneğin quantity: int yazdınız. Kullanıcı oraya "abc" gönderirse Pydantic otomatik hata döndürür, siz hiç kontrol kodu yazmak zorunda kalmazsınız.
# Kısacası: veri doğrulama + tip kontrolü işini hallediyor.


#                                                                       Kullanıcı → API → Veritabanı

class InvoiceCreate(BaseModel): #Kullanıcıdan,api ile, veritabanına gelen --bilgilerin sahip olması gereken özellikleri tanımlıyoruz.
    recipient: str
    seller: str
    product: str
    quantity: int
    unit_price: float
    vat_rate: float

#                                                                       Kullanıcı ← API ← Veritabanı

class InvoiceResponse(BaseModel):  #Veritabanından, api ile, kullanıcıya giden --bilgilerin sahip olması gereken özellikleri tanımlıyoruz.
    id: str
    recipient: str
    seller: str
    product: str
    quantity: int
    unit_price: float
    vat_rate: float
    total: float
    date: date

    class Config: #SQLAlchemy modelini (models.py) Pydantic'e çevirmeye yarıyor. BU Olmadan InvoiceResponse veritabanından gelen objeyi okuyamaz.
        from_attributes = True