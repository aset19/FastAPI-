from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    registered_at: Optional[datetime] = None
    class Config:
        from_attributes = True