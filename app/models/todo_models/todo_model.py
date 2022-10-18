from beanie import Document, Link, Replace, Insert, before_event, Indexed
from uuid import UUID, uuid4
from pydantic import Field
from datetime import datetime
from app.models.user_models.user_model import UserModel


class TodoModel(Document):
    todo_id: UUID = Field(default_factory=uuid4,)
    status: bool = False
    title: Indexed(str)
    description: str = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[UserModel]

    def __repr__(self) -> str:
        return f"<Todo {self.title} >"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TodoModel):
            return self.todo_id == other.todo_id
        return False

    @before_event([Insert, Replace])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Collection:
        name = "todos"
