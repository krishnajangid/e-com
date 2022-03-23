from typing import List, TypeVar, Generic

from fastapi import Query
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class PaginationParamSchema(BaseModel):
    page: int = Query(default=1, gt=0)
    per_page: int = Query(default=20, gt=0, lt=30)


class PaginationOutSchema(GenericModel, Generic[T]):
    total: int
    page_size: int
    page_number: int
    result: List[T]
