from sqlalchemy import Column, Integer, String, Float
from config import Base

class Producto(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    stock = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
