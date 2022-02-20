from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db

from models.category import CategoryModel
from utils.auth import get_current_user

router = APIRouter()


@router.get("/category/")
async def get_all_category_view(token=Depends(get_current_user)):
    users = db.session.query(CategoryModel).all()
    return users
