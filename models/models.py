from sqlalchemy import Text, Column, Integer, Enum, DateTime, ForeignKey, Date
from database import Base
from enum import IntEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True, index=True)
    birth_date = Column(Date, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())

    cars = relationship("Car")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    issued = Column(Integer, nullable=False)
    model = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    manufacturer = relationship("Manufacturer")


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
