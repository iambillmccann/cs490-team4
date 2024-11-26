from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from backend.models.enums import *
import bcrypt

signup_router = APIRouter()

accounts_storage = {}


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


class UserSignupPayload(BaseModel):
    username: str
    email: EmailStr
    password: str


class SignupResponse(BaseModel):
    message: str
    status: str


@signup_router.post("/api/signup")
async def user_signup(user: UserSignupPayload) -> SignupResponse:
    if user.email in accounts_storage:
        return SignupResponse(message=UserSignUp.EmailExists, status=Status.Error.value)

    hashed_password = hash_password(user.password)
    accounts_storage[user.email] = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
    }

    return SignupResponse(
        message=UserSignUp.RegisteredSuccessfully, status=Status.Success.value
    )
