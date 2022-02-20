from fastapi import APIRouter, status, HTTPException
from fastapi_sqlalchemy import db

from models.users import UsersModel
from schema.users import UserLoginSchema, UserRegisterSchema
from utils.auth import (get_password_hash, authenticate_user, create_access_token)

router = APIRouter()


@router.post("/user/login/")
async def user_login_view(user: UserLoginSchema):
    user = await authenticate_user(email=user.email, password=user.password)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Username or Password",
            headers={"Authenticate": "Bearer"}
        )

    return {
        "access_token": await create_access_token(user.id),
        "user_id": user.id
    }


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
