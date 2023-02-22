from datetime import datetime

from fastapi import APIRouter, Depends
import models
from schemas import schemas

router = APIRouter(prefix="/User", tags=["user"])


@router.get("/<user_id>")
def get_user_by_id(user_id: int) -> schemas.User:
    return schemas.User(
        id=user_id,
        name="adasd",
        email="asfasfasfaa@fakemail.ru",
        age=21334,
        gender=models.GenderEnum.female,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
