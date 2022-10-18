from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


# User Auth
class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=4, max_length=50, description="user username")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


# User Response Model
class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: bool = False
    email_confirmed_at: Optional[str] = None


# Update User
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
