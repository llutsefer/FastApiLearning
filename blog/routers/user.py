from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['User']
)
get_db = database.get_db


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
