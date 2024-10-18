from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import logging
from fastapi import HTTPException
from .config import DB_PORT, DB_NAME, DB_HOST, DB_USER, DB_PASS



SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=20, future=True, echo=True)

SessionLocal = sessionmaker( engine, expire_on_commit=False, class_= Session )

Base = declarative_base()
metadata = Base.metadata





def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as e:
        logging.debug(e)  # Теперь работает корректно
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
        logging.debug("Database connection closed.")







