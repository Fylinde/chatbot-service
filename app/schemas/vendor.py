from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.schemas.order import OrderResponse

class VendorBase(BaseModel):
    name: str
    email: EmailStr

class VendorCreate(VendorBase):
    name: str
    email: EmailStr
    description: Optional[str] = None
    rating: Optional[float] = None
    password: str  # Add the password field here


class VendorUpdate(VendorBase):
    pass

class VendorResponse(VendorBase):
    id: int
    name: str
    description: Optional[str] = None
    rating: Optional[float] = None

    class Config:
        orm_mode = True

class VendorWithOrders(VendorResponse):
    orders: List["OrderResponse"] = []
