from typing import Union

from pydantic import BaseModel, EmailStr


class UserLoginInSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "test@gmail.com",
                "password": "Te21@.cse"
            }
        }


class UserLoginOutSchema(BaseModel):
    access_token: str
    user_id: int


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    name: str
