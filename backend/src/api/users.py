from fastapi import APIRouter, status, Request
from fastapi_sqlalchemy import db

from models.users import UsersModel
from schema.users import UserLoginSchema, UserRegisterSchema
from utils.auth import auth_required, role_required

router = APIRouter()


@router.post("/user/login/", response_model=UserLoginSchema)
async def user_login_view(user: UserLoginSchema):
    users = db.session.query(UsersModel).all()

    return users


@router.post("/user/register/")
@role_required(roles=["Admin"])
async def user_register_view(user: UserRegisterSchema):
    users = db.session.query(UsersModel).all()

    return users
