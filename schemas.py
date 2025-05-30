from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str


class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime
    role: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class PasswordChange(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str


class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str
    confirm_password: str


class OTP(BaseModel):
    email: EmailStr
    otp: str


class NotesOut(BaseModel):
    title1: str
    content1: str
    title2: str
    content2: str