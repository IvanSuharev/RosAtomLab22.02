from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1234@localhost/ros_atom_labs")

Base = declarative_base()

SessionLocal = sessionmaker(engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
