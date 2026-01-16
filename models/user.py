from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    """User model with validated fields."""
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: bool = True


class User_Response(BaseModel):
    """User response model returning only id and full_name."""
    id: int
    full_name: Optional[str] = None
