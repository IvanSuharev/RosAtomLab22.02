from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from database import Base
from enum import IntEnum


class GenderEnum(IntEnum):
    male = 0
    female = 1


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer)
    gender = Column(Enum(GenderEnum))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now)
