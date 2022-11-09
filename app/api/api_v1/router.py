from fastapi import APIRouter
from .manage_routes.todo_routes.todo_route import todo_router
from .manage_routes.user_routes.user_route import user_router
from app.api.auth.jwt import auth_router

# Main Entry Point for the API V1 Routes
api_v1_router = APIRouter()


@api_v1_router.get("/")
async def read_root():
    """
    :return:
    """
    return {
        "Route": "API V1",
    }


# Including Auth Routes prefix with /auth tags Auth
api_v1_router.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Including User Routes prefix with /users tags users
api_v1_router.include_router(user_router, prefix="/users", tags=["Users"])

# Including Todos Routes prefix with /todos tags todos
api_v1_router.include_router(todo_router, prefix="/todos", tags=["Todos"])
