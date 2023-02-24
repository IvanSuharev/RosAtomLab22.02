from sqlalchemy.orm import Session
import schemas
import database
from exceptions import ItemNotFound


class CarService:
    @staticmethod
    def create_car(db: Session, new_car: schemas.CarCreate) -> database.Car:
        new_car = database.Car(**new_car.dict())
        db.add(new_car)
        db.commit()
        return new_car

    @staticmethod
    def update(db: Session, obj: schemas.CarUpdate, obj_id: int) -> database.Car:
        db_obj = db.query(database.Car).get(obj_id)
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj


class UserService:
    @staticmethod
    def create_user(db: Session, new_user: schemas.UserCreate):
        new_user = database.User(**new_user.dict())
        db.add(new_user)
        db.commit()
        return new_user

    @staticmethod
    def update(db: Session, obj: schemas.UserUpdate, obj_id: int) -> database.User:
        db_obj = db.query(database.User).get(obj_id)
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj


class ManufacturerService:
    @staticmethod
    def create(db: Session, new_man: schemas.ManufacturerCreate):
        new_man = database.Manufacturer(**new_man.dict())
        db.add(new_man)
        db.commit()
        return new_man

    @staticmethod
    def update(db: Session, obj: schemas.ManufacturerUpdate, obj_id: int) -> database.Manufacturer:
        db_obj = db.query(database.Manufacturer).get(obj_id)
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj