# app/routes/routes.py

from fastapi import APIRouter, HTTPException
from schemas.user import UserRegister, UserResponse
from services.services import register_user

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    try:
        new_user = register_user(user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))