from fastapi import APIRouter, status, Request
from fastapi_sqlalchemy import db

from models.users import Users
from schema.category import CategorySchema, UserRegisterSchema
from utils.auth import auth_required, role_required

router = APIRouter()


@router.get("/category/")
async def get_all_category_view():
    users = db.session.query(Users).all()

    return users


@router.post("/user/register/")
@role_required(roles=["Admin"])
async def user_register_view(user: UserRegisterSchema):
    users = db.session.query(Users).all()

    return users
