from pydantic import BaseModel, EmailStr, Field
from typing import List


class MailSchema(BaseModel):
    email: List[EmailStr] = Field(..., description="user email")
