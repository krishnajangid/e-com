from fastapi import APIRouter

from api import category, users

router = APIRouter()
router.include_router(category.router)
router.include_router(users.router)
