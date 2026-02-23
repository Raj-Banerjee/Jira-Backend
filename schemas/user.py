# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime