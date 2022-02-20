from functools import wraps
from typing import List, Union
from fastapi import requests, Request
from fastapi.security import OAuth2PasswordBearer


def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print("i am here")
        return await func(*args, **kwargs)

    return wrapper


def role_required(roles: Union[List[str], None, str] = None):
    def decorator_auth(func):
        @wraps(func)
        async def wrapper_auth(*args, **kwargs):
            # requests.Request["value"]= "kjskjs"
            return await func(*args, **kwargs)

        return wrapper_auth

    return decorator_auth
