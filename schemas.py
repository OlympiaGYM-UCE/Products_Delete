from pydantic import BaseModel

class ProductoCreate(BaseModel):
    name: str
    stock: int
    cost: float
