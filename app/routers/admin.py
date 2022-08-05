from os import sync
from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, util, oauth2
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(
    prefix="/admin",
    tags=['Admin']
)
@router.get('/',response_model=List[schemas.AdminOut])
def get_all_admins(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_admin)):
        admins = db.query(models.AdminId).all()
        return admins

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.AdminOut)
async def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    hashed_password = util.hash(admin.passwd)
    admin.passwd = hashed_password

    new_admin = models.AdminId(**admin.dict())
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

@router.get("/{id}", response_model=schemas.AdminSearchOut)
async def get_my_admin(id: int, db: Session = Depends(get_db),current_admin: int = Depends(oauth2.get_current_admin)):
    admin = db.query(models.AdminId).filter(models.AdminId.aid == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'User {id} does not exist'
                            )
    return admin

@router.get("/user_details/{id}", response_model=schemas.UserSearchOut)
async def get_user_details(id: int, db: Session = Depends(get_db),current_admin: int = Depends(oauth2.get_current_admin)):
    user = db.query(models.LoginId).filter(models.LoginId.oid == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'User {id} does not exist'
                            )
    return user

