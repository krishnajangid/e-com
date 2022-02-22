from fastapi import APIRouter, Depends, Query

from api.category.mod import CategoryMod
from schema.category import CategoryOutSchema, PaginationSchema
from utils.auth import get_current_user

router = APIRouter()


@router.get("/category/", response_model=PaginationSchema[CategoryOutSchema])
async def get_all_category_view(
        page: int = Query(default=1, gt=0, lt=10),
        per_page: int = Query(default=20, gt=0, lt=21),
        _=Depends(get_current_user)
) -> PaginationSchema[CategoryOutSchema]:
    category_mod_obj = CategoryMod()
    return category_mod_obj.get_all_category(page, per_page)
