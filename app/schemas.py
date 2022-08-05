from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.expression import true
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    passwd: str
    first_name: str
    last_name: str
    address: str

class UserValidate(BaseModel):
    verified_account: bool

class UserOut(BaseModel):
    oid: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = true

class UserSearchOut(BaseModel):
    oid: int
    email: EmailStr
    created_at: datetime
    first_name: str
    last_name: str
    verified_account: bool

    class Config:
        orm_mode = true

class AdminCreate(BaseModel):
    email: EmailStr
    passwd: str
    first_name: str
    last_name: str
    department: str

class AdminSearchOut(BaseModel):
    aid: int
    email: EmailStr
    created_at: datetime
    first_name: str
    last_name: str

    class Config:
        orm_mode = true

class AdminOut(BaseModel):
    aid: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = true