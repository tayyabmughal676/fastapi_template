from typing import Optional
from uuid import UUID
import pymongo
from app.core.security import get_password_hash, verify_password
from app.models.user_models.user_model import UserModel
from app.schemas.user_schema import UserAuth, UserUpdate


class UserService:
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[UserModel]:
        """
        :param email:
        :param password:
        :return:
        """
        user = await UserService.get_user_by_email(email)
        print(f"authenticate-user: {user}")
        if not user:  # if user not found
            return None
        if not verify_password(password, user.hashed_password):  # If user's password not match
            return None
        return user

    # Create User
    @staticmethod
    async def create_user(user: UserAuth):
        """
        :param user:
        :return:
        """
        user_in = UserModel(
            username=user.username,
            email=user.email,
            hashed_password=get_password_hash(user.password),
        )
        await user_in.save()
        return user_in

    # Get User By Email
    @staticmethod
    async def get_user_by_email(email: str) -> UserModel:
        """
        :param email:
        :return:
        """
        user = await UserModel.find_one(UserModel.email == email)
        print(f"get_user_by_email: {user}")
        return user

    # Get User By ID
    @staticmethod
    async def get_user_by_id(id: UUID) -> UserModel:
        """
        :param id:
        :return:
        """
        user = await UserModel.find_one(UserModel.user_id == id)
        return user

    # Update User By ID
    @staticmethod
    async def update_user(id: UUID, data: UserUpdate) -> UserModel:
        """
        :param id:
        :param data:
        :return:
        """
        user = await UserModel.find_one(UserModel.user_id == id)
        if not user:
            raise pymongo.errors.OperationFailure("User not found")
        await user.update({"$set": data.dict(exclude_unset=True)})
        return user
