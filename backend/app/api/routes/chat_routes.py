from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.chat_session import (
    ChatSessionResponse,
)
from app.services.chat_service import ChatService
from app.services.chat.session_service import SessionService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/session",
    response_model=ChatSessionResponse
)
def create_chat_session(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return SessionService.create_session(
        db,
        current_user.id
    )