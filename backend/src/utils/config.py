from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "XiW5JX9LURpyjuIPP9fDS-_ncYhfNWuAGdcnebEa_nM"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB: str = os.getenv("MYSQL_DB", "ecom_db")
    MYSQL_PORT: int = 3306


settings = Settings()
