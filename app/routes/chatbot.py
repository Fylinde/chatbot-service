from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.customer_bot import customer_bot
from app.vendor_bot import vendor_bot
from app.database import get_db
from app.models.user import UserModel
from app.schemas.user import UserCreate, UserResponse, UserWithOrders


router = APIRouter()

@router.post("/customer-support/")
def customer_support(query: str, db: Session = Depends(get_db)):
    # Here you can use the db session if needed
    response = customer_bot.handle_query(query)
    return response

@router.post("/vendor-support/")
def vendor_support(query: str, db: Session = Depends(get_db)):
    # Here you can use the db session if needed
    response = vendor_bot.handle_query(query)
    return response

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=UserWithOrders)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user