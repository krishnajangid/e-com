from typing import List, Optional, TypeVar, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class PaginationSchema(GenericModel, Generic[T]):
    total: int
    page_size: int
    page_number: int
    result: List[T]


class CategoryOutSchema(BaseModel):
    id: int
    name: str
    description: str
    sort_order: Optional[int]
    child: List = []
