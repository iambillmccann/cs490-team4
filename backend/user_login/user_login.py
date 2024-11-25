from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel, EmailStr
from backend.models.enums import *
import jwt
from datetime import datetime, timedelta
from backend.user_signup.user_signup import accounts_storage, verify_password

# JWT
SECRET_KEY = "verystrongsecretkey"
ALGORITHM = "HS256"

login_router = APIRouter()


class LoginPayload(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str
    status: str


def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@login_router.post("/api/login", response_model=LoginResponse)
async def login_user(payload: LoginPayload):
    user = accounts_storage.get(payload.email)
    if not user or not verify_password(payload.password, user["password"]):
        return LoginResponse(message=UserLogin.InvalidCredentials, status=Status.Error)

    token = create_jwt_token(
        data={"sub": payload.email}, expires_delta=timedelta(hours=1)
    )

    return {"token": token}  # MIGHT ADD A RESPONSE MESSAGE