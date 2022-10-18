from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


# Todo Create
class TodoCreate(BaseModel):
    title: str = Field(..., title="Title", max_length=55, min_length=5)
    description: str = Field(..., title="Description", max_length=200, min_length=5)
    status: Optional[bool] = Field(default=False, title="Status of todo")


# Todo Update
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(..., title="Title", max_length=55, min_length=5)
    description: Optional[str] = Field(..., title="Description", max_length=200, min_length=5)
    status: Optional[bool] = False


# Todo Response Model
class TodoOut(BaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str = None
    created_at: datetime
    updated_at: datetime
