from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, util, oauth2

router = APIRouter(
    tags=['Authentication']
    )

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    user = db.query(models.LoginId).filter(models.LoginId.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, 
            detail=f"Invalid Credentials"
            )
    if not util.verify(user_credentials.password, user.passwd):
        raise HTTPException(status.HTTP_403_FORBIDDEN, 
            detail=f"Invalid Credentials"
            )
    access_token = oauth2.create_acess_token(data = {"user_id": user.oid })

    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/admin_login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    admin = db.query(models.AdminId).filter(models.AdminId.email == user_credentials.username).first()
    if not admin:
        raise HTTPException(status.HTTP_403_FORBIDDEN, 
            detail=f"Invalid Credentials"
            )
    if not util.verify(user_credentials.password, admin.passwd):
        raise HTTPException(status.HTTP_403_FORBIDDEN, 
            detail=f"Invalid Credentials"
            )
    access_token = oauth2.create_acess_token(data = {"user_id": admin.aid })

    return {"access_token": access_token, "token_type": "bearer"}