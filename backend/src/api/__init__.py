from fastapi import APIRouter

from api import users
from api.category import api as category

router = APIRouter()
router.include_router(category.router)
router.include_router(users.router)
