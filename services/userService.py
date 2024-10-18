from fastapi import HTTPException

from models.user_model import User
from sqlalchemy.orm import Session
from schemas.user import UserBase



def create_user(data: UserBase  , db:Session):

    # Создаем объект User
    user = User (
        name= data.name,
        email = data.email,
        hashed_password = data.hashed_password,
    )
    try:
        db.add(user)       # Добавляем объект User  # Добавляем объект UserInfo
        db.commit()        # Коммитим изменения
        db.refresh(user)   # Обновляем данные user после коммита
    except Exception as e:
        db.rollback()      # Откатим изменения при ошибке
        print(f"Error creating user: {e}")
        return None  # Возвращаем None или выбрасываем исключение

    return user



def get_user(id:int, db: Session):
    return db.query(User).filter(User.id == id).first()

def get_all(db):
    return db.query(User).all()


def update_user(data: UserBase, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Обновляем только те поля, которые переданы в запросе
    if data.name:
        user.name = data.name
    if data.email:
        user.email = data.email
    if data.hashed_password:
        user.hashed_password = data.hashed_password



    return user


def delete_user(db: Session, id: int ):
    user = db.query(User).filter(User.id==id).first()
    db.delete(user)
    db.commit()
    return  f"{user} is deleted"

def delete_all_users(db:Session):
    users = db.query(User).all()
    for user in users:
        db.delete(user)
        db.commit()

    return "all users are deleted"


