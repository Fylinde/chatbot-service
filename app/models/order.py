from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseModel

class OrderModel(BaseModel):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    order_description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    # Establishing relationship with UserModel
    owner = relationship("UserModel", back_populates="orders")
