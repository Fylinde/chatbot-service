from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseModel

class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile_picture = Column(String, nullable=True)
    preferences = Column(String, nullable=True)

    # Relationships
    chatbot_interactions = relationship("ChatbotUserModel", back_populates="user")
    orders = relationship("OrderModel", back_populates="owner")
