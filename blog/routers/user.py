from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas , database
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('/' , response_model=schemas.showuser)
def create_user(request: schemas.User , db : Session = Depends(get_db)):
    return user.create_user(request, db)

    # new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user



@router.get('/' , response_model=schemas.showuser)
def get(id:int , db: Session = Depends(get_db)):
    return user.get(id , db)
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} not found")
    # return user
