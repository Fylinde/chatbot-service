from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.schemas.order import OrderResponse
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserWithOrders(UserResponse):
    orders: List["OrderResponse"] = []
