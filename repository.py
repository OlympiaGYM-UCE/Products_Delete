from sqlalchemy.orm import Session
from models import Producto



def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()


def delete_producto(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
    return producto
