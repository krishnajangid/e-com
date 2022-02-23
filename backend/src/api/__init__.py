from fastapi import APIRouter

from api.category import api as category
from api.users import api as users
from api.banner import api as banner
from api.coupon import api as coupon

router = APIRouter()
router.include_router(category.router)
router.include_router(users.router)
router.include_router(banner.router)
router.include_router(coupon.router)
