from datetime import datetime

from pydantic import BaseModel, EmailStr
from models import GenderEnum
from typing import Optional


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    gender: GenderEnum


class UserCreated(BaseModel):
    pass


class UserUpdated(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    gender: Optional[GenderEnum]
    age: Optional[int]


class User(BaseUser):
    id: int
    age: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
