from sqlalchemy.orm import Session

from app.models.message import Message
from app.repositories.message_repository import MessageRepository


class ConversationService:

    @staticmethod
    def save_user_message(
        db: Session,
        session_id: int,
        content: str
    ):

        message = Message(
            session_id=session_id,
            role="user",
            content=content,
            agent_name=None
        )

        return MessageRepository.create(
            db,
            message
        )

    @staticmethod
    def save_assistant_message(
        db: Session,
        session_id: int,
        content: str,
        agent_name: str
    ):

        message = Message(
            session_id=session_id,
            role="assistant",
            content=content,
            agent_name=agent_name
        )

        return MessageRepository.create(
            db,
            message
        )

    @staticmethod
    def get_history(
        db: Session,
        session_id: int
    ):
        return MessageRepository.get_by_session(
            db,
            session_id
        )

    @staticmethod
    def get_recent_context(
        db: Session,
        session_id: int,
        limit: int = 10
    ):
        return MessageRepository.get_recent_messages(
            db,
            session_id,
            limit
        )