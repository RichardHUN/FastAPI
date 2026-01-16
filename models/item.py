from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """Full Item model with all fields."""
    id: int
    name: str
    description: Optional[str] = None
    price: float


class Item_Response(BaseModel):
    """Item response model returning only id and name."""
    id: int
    name: str
