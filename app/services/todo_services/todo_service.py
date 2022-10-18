from typing import List
from uuid import UUID
from app.models.todo_models.todo_model import TodoModel
from app.models.user_models.user_model import UserModel
from app.schemas.todo_schema import TodoCreate, TodoUpdate


class TodoService:
    @staticmethod
    async def list_todos(user: UserModel) -> List[TodoModel]:
        """
        :param user:
        :return:
        """
        todos = await TodoModel.find(TodoModel.owner.id == user.id).to_list()
        return todos

    @staticmethod
    async def create_todo(user: UserModel, data: TodoCreate) -> TodoModel:
        """
        :param user:
        :param data:
        :return:
        """
        todo = TodoModel(**data.dict(), owner=user)
        return await todo.insert()

    @staticmethod
    async def retrieve_todo(user: UserModel, todo_id: UUID) -> TodoModel:
        """
        :param user:
        :param todo_id:
        :return:
        """
        todo = await TodoModel.find_one(TodoModel.todo_id == todo_id, TodoModel.owner.id == user.id)
        return todo

    @staticmethod
    async def update_todo(user: UserModel, todo_id: UUID, data: TodoUpdate) -> TodoModel:
        """
        :param user:
        :param todo_id:
        :param data:
        :return:
        """
        todo = await TodoService.retrieve_todo(user, todo_id)
        await todo.update({"$set": data.dict(exclude_unset=True)})
        await todo.save()
        return todo

    @staticmethod
    async def delete_todo(user: UserModel, todo_id: UUID) -> None:
        """
        :param user:
        :param todo_id:
        :return:
        """
        todo = await TodoService.retrieve_todo(user, todo_id)
        if todo:
            await todo.delete()
        return None
