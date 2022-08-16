from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, util, oauth2
from pydantic import EmailStr
from typing import Union
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = util.hash(user.passwd)
    user.passwd = hashed_password

    new_user = models.LoginId(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserSearchOut)
async def get_my_user(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    if id != current_user.oid:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail = f'User {current_user.first_name} {current_user.last_name} not authorized to request this information.'
                            )
    user = db.query(models.LoginId).filter(models.LoginId.oid == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'User {id} does not exist'
                            )
    return user

@router.put("/{id}", response_model=schemas.UserOut)
async def verify_account(id: int, verify: schemas.UserValidate, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_admin)):
    user_search = db.query(models.LoginId).filter(models.LoginId.oid == id)
    user = user_search.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'User {id} does not exist'
                            )
    user_search.update(verify.dict(), synchronize_session=False)
    db.commit()
    return user_search.first()

@router.get("/email/", response_model=schemas.UserSearchOut)
async def get_my_email(email: EmailStr, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.LoginId).filter(models.LoginId.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'Login account {email} - Not Found.'
                            )
    return user

@router.get("/pii/", response_model=schemas.UserSearchOut)
async def get_my_pii(email: EmailStr, first_name = str, last_name = str, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.LoginId).filter(models.LoginId.email == email, models.LoginId.first_name == first_name, models.LoginId.last_name == last_name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'User {first_name} {last_name} does not exist'
                            )
    return user
