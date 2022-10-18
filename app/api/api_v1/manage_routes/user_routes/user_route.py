from fastapi import APIRouter, HTTPException, status, Depends
from app.services.user_services.user_service import UserService
import pymongo
from app.schemas.user_schema import UserOut, UserAuth, UserUpdate
from app.models.user_models.user_model import UserModel
from app.api.deps.user_deps import get_current_user

# User Route Entry Point
user_router = APIRouter()


@user_router.post("/create", summary="Create new user", )
async def create_user(data: UserAuth):
    try:
        print(f"data: {data}")
        user = await UserService.create_user(data)
        return {
            "code": 1,
            "message": "Success",
            "data": user
        }
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists"
        )


@user_router.get("/get_all_users", summary="Get All Users", )
async def get_all_users():
    return {"get_all_users": "Get all users"}


@user_router.get("/me", summary="Get user by email", response_model=UserOut)
def get_me(user: UserModel = Depends(get_current_user)):
    return user


@user_router.get("/user/id", summary="Get user by id")
async def get_user_by_id(userId: int):
    return {"get_user_by_id": f"get user by {userId}"}


@user_router.patch("/update", summary="Update user by email", response_model=UserOut)
async def update_user(data: UserUpdate, user: UserModel = Depends(get_current_user)):
    try:
        return await UserService.update_user(user.user_id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email does not exist"
        )


@user_router.delete("/delete", summary="Delete User", )
async def delete_user():
    return {"delete_user": "Delete User"}
