import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from api.users import router
from utils.config import settings

app = FastAPI(openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    DBSessionMiddleware,
    db_url="mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DB,
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT
    )

)
app.include_router(router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=5050, reload=True)
