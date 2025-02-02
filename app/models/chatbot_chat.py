from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import BaseModel

class ChatbotChatModel(BaseModel):
    __tablename__ = 'chatbot_interactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('chatbot_users.id'), nullable=True)
    seller_id = Column(Integer, ForeignKey('sellers.id'), nullable=True)
    interaction_type = Column(String, index=True)
    message = Column(Text)
    response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("ChatbotUserModel", back_populates="chatbot_interactions", primaryjoin="ChatbotChatModel.user_id == ChatbotUserModel.id")
    seller = relationship("SellerModel", back_populates="chatbot_interactions")
