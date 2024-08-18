from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema for common user fields
class ChatbotUserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[str] = None
    preferences: Optional[str] = None

# Schema used for creating a new user
class ChatbotUserCreate(ChatbotUserBase):
    username: str
    email: EmailStr
    password: str  # This is the plain text password which will be hashed

# Schema used for reading user data
class ChatbotUserRead(ChatbotUserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode: True

# Schema used for updating user data
class ChatbotUserUpdate(ChatbotUserBase):
    pass
