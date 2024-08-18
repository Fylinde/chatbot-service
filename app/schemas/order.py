from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    order_description: str

class OrderCreate(OrderBase):
    owner_id: int

class OrderUpdate(OrderBase):
    owner_id: Optional[int] = None

class OrderResponse(OrderBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
