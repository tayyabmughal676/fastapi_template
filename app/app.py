from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.api.api_v1.router import api_v1_router
from .core.config import settings
from .system_logs.system_logs import checkSystemLogs

# Databases
from app.models.user_models.user_model import UserModel
from app.models.todo_models.todo_model import TodoModel

# FastAPI App
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# [...]
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """
        initialize application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).fastapitemplate
    await init_beanie(
        database=db_client,
        document_models=[
            UserModel,
            TodoModel,
        ]
    )

    print("initialize application services")
    checkSystemLogs.passLogs("Initialize application services", logLevel=2)


@app.get("/")
async def read_root():
    """
    :return:
    """
    return {
        "Welcome to": "Python FastAPI Framework with Mongodb Scaffold Template",
        "Software Engineer": "Tayyab Mughal",
        "Github": "https://github.com/tayyabmughal676"
    }


# Including the API V1 Routes
app.include_router(api_v1_router, prefix="/api/v1")
