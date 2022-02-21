from typing import List, Optional

from pydantic import BaseModel, EmailStr


class CategoryOutSchema(BaseModel):
    id: int
    name: str
    description: str
    sort_order: Optional[int]
    child: List
