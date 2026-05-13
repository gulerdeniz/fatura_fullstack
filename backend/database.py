# → veritabanı bağlantısı

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./invoices.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) #Motoru oluşturduk.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) #Motor'u session'a bağladık.
Base = declarative_base() #Bundan sonra bu Base'i miras alan her class bir veritabanı tablosudur" demeyi sağlıyor.
#Aynı zamanda Base.metadata.create_all(engine) yazınca, Base'i miras alan tüm class'ları tarayıp veritabanında tablolarını otomatik oluşturuyor.

def get_db(): #Db oluşturmak için çağırılacak fonksiyonu yazdık.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()