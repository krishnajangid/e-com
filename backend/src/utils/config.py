from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "XiW5JX9LURpyjuIPP9fDS-_ncYhfNWuAGdcnebEa_nM"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = ""
    MYSQL_DB: str = "ecom_db"
    MYSQL_PORT: int = 3306


settings = Settings()
