# → tablo yapısı

from sqlalchemy import Column, String, Integer, Float, Date
from database import Base
import uuid
from datetime import date

class Invoice(Base): #Base class'ın özelliklerinin modelini oluşturduk.
    __tablename__ = "invoices"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    recipient = Column(String, nullable=False)
    seller = Column(String, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    vat_rate = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    date = Column(Date, default=date.today)