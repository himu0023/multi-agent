from sqlalchemy.orm import Session

from app.models.chat_session import ChatSession
from app.repositories.chat_session_repository import ChatSessionRepository


class ChatService:

    @staticmethod
    def create_session(
        db: Session,
        user_id: int,
        title: str = "New Chat"
    ):

        session = ChatSession(
            title=title,
            user_id=user_id
        )

        return ChatSessionRepository.create(
            db,
            session
        )
    