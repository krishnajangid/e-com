from fastapi import APIRouter, status, Request
from fastapi_sqlalchemy import db

from models.users import Users
from schema.schema import UsersSchema

router = APIRouter()


@router.post("/user/login/")
async def user_login_view(user: UsersSchema):
    users = db.session.query(Users).all()

    return users
