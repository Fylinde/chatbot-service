from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import BaseModel

class VendorModel(BaseModel):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)  # Optional field
    rating = Column(Integer, nullable=True)  # Optional field
    profile_picture = Column(String, nullable=True)
    preferences = Column(String, nullable=True)
    hashed_password = Column(String)  # Store the hashed password

    # Relationships
    chatbot_interactions = relationship("ChatbotChatModel", back_populates="vendor")
