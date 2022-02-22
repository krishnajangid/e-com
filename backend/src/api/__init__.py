from fastapi import APIRouter

from api.category import api as category
from api.users import api as users

router = APIRouter()
router.include_router(category.router)
router.include_router(users.router)
