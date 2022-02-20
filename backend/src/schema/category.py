from pydantic import BaseModel, EmailStr


class CategorySchema(BaseModel):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "test@gmail.com",
                "password": "Te21@.cse"
            }
        }


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    name: str
