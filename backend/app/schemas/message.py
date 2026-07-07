from datetime import datetime

from pydantic import BaseModel


class MessageRequest(BaseModel):
    session_id: int
    message: str


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    agent_name: str | None
    created_at: datetime

    class Config:
        from_attributes = True