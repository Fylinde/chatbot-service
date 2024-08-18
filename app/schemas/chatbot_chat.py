from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatbotBase(BaseModel):
    interaction_type: str
    message: str
    response: str

class ChatbotCreate(BaseModel):
    user_id: Optional[int] = None
    vendor_id: Optional[int] = None
    interaction_type: str
    message: str
    response: str

class ChatbotResponse(ChatbotBase):
    id: int
    user_id: Optional[int] = None
    vendor_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True

class ChatbotRead(ChatbotCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True