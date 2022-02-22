from fastapi import APIRouter, status, HTTPException
from fastapi_sqlalchemy import db

from models.users import UsersModel
from schema.users import UserLoginInSchema, UserRegisterSchema, UserLoginOutSchema
from utils.auth import (get_password_hash, authenticate_user, create_access_token)

router = APIRouter()


@router.post("/user/login/", response_model=UserLoginOutSchema)
async def user_login_view(user: UserLoginInSchema) -> UserLoginOutSchema:
    user = await authenticate_user(email=user.email, password=user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Username or Password",
            headers={"Authenticate": "Bearer"}
        )

    data = {
        "access_token": await create_access_token(user.id),
        "user_id": user.id
    }
    return data


@router.post("/user/register/")
async def user_register_view(user: UserRegisterSchema):
    password = get_password_hash(user.password)
    user_obj = UsersModel(
        name=user.name,
        email=user.email,
        password=password,
        is_verified=True
    )
    db.session.add(user_obj)
    db.session.commit()

    print(user)
    users = db.session.query(UsersModel).all()

    return users
