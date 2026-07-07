from datetime import datetime

from pydantic import BaseModel


class ChatSessionCreate(BaseModel):
    title: str = "New Chat"


class ChatSessionResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True