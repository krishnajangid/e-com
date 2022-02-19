from pydantic import BaseModel


class UsersSchema(BaseModel):
    id: int
