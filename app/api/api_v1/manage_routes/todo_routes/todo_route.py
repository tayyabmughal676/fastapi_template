from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.models.user_models.user_model import UserModel
from app.services.todo_services.todo_service import TodoService
from app.api.deps.user_deps import get_current_user
from app.schemas.todo_schema import TodoOut, TodoUpdate, TodoCreate

# User Route Entry Point
todo_router = APIRouter()


@todo_router.post("/create", summary="Create new todo", )
async def create_todo(data: TodoCreate, current_user: UserModel = Depends(get_current_user)):
    """
    :param data:
    :param current_user:
    :return:
    """
    return await TodoService.create_todo(current_user, data)


@todo_router.get('/get_all_todos', summary='Get all todos', response_model=List[TodoOut])
async def get_all_todos(current_user: UserModel = Depends(get_current_user)):
    """
    :param current_user:
    :return:
    """
    return await TodoService.list_todos(current_user)


@todo_router.get('/{todo_id}', summary="Get Todo by id", response_model=TodoOut)
async def retrieve(todo_id: UUID, current_user: UserModel = Depends(get_current_user)):
    """
    :param todo_id:
    :param current_user:
    :return:
    """
    return await TodoService.retrieve_todo(current_user, todo_id)


@todo_router.put('/{todo_id}', summary='Update a todo', response_model=TodoOut)
async def update(todo_id: UUID, data: TodoUpdate, current_user: UserModel = Depends(get_current_user)):
    """
    :param todo_id:
    :param data:
    :param current_user:
    :return:
    """
    return await TodoService.update_todo(current_user, todo_id, data)


@todo_router.delete('/{todo_id}', summary='Delete a todo', status_code=204)
async def delete_todo(todo_id: UUID, current_user: UserModel = Depends(get_current_user)):
    """
    :param todo_id:
    :param current_user:
    :return:
    """
    await TodoService.delete_todo(current_user, todo_id)
    return None

# try:
# except
#     raise {"create": "Create User Error Occurs"}
