from operator import index

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from conf.database import Base # Импортируйте ваш базовый класс из файла базы данных

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Идентификатор пользователя
    name = Column(String, index=True)  # Имя пользователя
    nickname = Column(String, index=True) #Позывной
    email = Column(String, unique=True, index=True) # Электронная почта
    hashed_password = Column(String)  # Хэшированный пароль
    registered_at = Column(DateTime(timezone=True), server_default=func.now())  # Дата регистрации

    # def __repr__(self):
    #     return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
