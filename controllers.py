from schemas import ProductoCreate
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config import SessionLocal, engine
from models import Base
import repository

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    return repository.delete_producto(db, producto_id)
