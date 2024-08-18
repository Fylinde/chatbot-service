from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseModel

class ChatbotUserModel(BaseModel):
    __tablename__ = 'chatbot_users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile_picture = Column(String, nullable=True)
    preferences = Column(String, nullable=True)

    # Foreign key to UserModel (if needed)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship("UserModel")

    # Foreign key to VendorModel (if needed)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=True)
    vendor = relationship("VendorModel")

    # Correct relationship to ChatbotChatModel
    chatbot_interactions = relationship("ChatbotChatModel", back_populates="user", primaryjoin="ChatbotUserModel.id == ChatbotChatModel.user_id")
