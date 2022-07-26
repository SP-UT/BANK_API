from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.expression import true
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    address: str
    verified: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    online_id: str
    email: EmailStr
    created_at: datetime
