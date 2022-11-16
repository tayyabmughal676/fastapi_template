from pydantic import BaseSettings, AnyHttpUrl
from decouple import config
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
    ]
    PROJECT_NAME: str = "FastApi Scaffold Template"

    # Database
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    MAIL_USERNAME = config("MAIL_USERNAME", cast=str)
    MAIL_PASSWORD = config("MAIL_PASSWORD", cast=str)
    MAIL_FROM = config("MAIL_FROM", cast=str)
    MAIL_PORT = config("MAIL_PORT", cast=int)
    MAIL_SERVER = config("MAIL_SERVER", cast=str)
    MAIL_FROM_NAME = config("MAIL_FROM_NAME", cast=str)

    class Config:
        case_sensitive = True


settings = Settings()
