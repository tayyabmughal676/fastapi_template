# from pydantic_settings import BaseSettings, AnyHttpUrl
from pydantic_settings import BaseSettings  # NEW
from pydantic import AnyUrl
from decouple import config
from typing import List
from pydantic import BaseModel, Field, PydanticUserError
from typing import List, ClassVar


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    # ALGORITHM = "HS256"
    ALGORITHM: ClassVar[str] = "HS256"  # Annotated as a ClassVar
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    BACKEND_CORS_ORIGINS: List[AnyUrl] = [
        "http://localhost:3000",
    ]
    PROJECT_NAME: str = "FastApi Scaffold Template"

    # Database
    # MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)
    # Database
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str) + "?tlsAllowInvalidCertificates=true"

    # MAIL_USERNAME: ClassVar[str] = config("MAIL_USERNAME", cast=str)
    # MAIL_PASSWORD: ClassVar[str] = config("MAIL_PASSWORD", cast=str)
    # MAIL_FROM: ClassVar[str] = config("MAIL_FROM", cast=str)
    # MAIL_PORT: ClassVar[str] = config("MAIL_PORT", cast=int)
    # MAIL_SERVER: ClassVar[str] = config("MAIL_SERVER", cast=str)
    # MAIL_FROM_NAME: ClassVar[str] = config("MAIL_FROM_NAME", cast=str)

    class Config:
        case_sensitive = True


settings = Settings()
