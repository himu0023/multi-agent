from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.chat_session import ChatSession
from app.repositories.chat_session_repository import ChatSessionRepository


class SessionService:

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

    @staticmethod
    def get_session(
        db: Session,
        session_id: int
    ):

        session = ChatSessionRepository.get_by_id(
            db,
            session_id
        )

        if not session:
            raise HTTPException(
                status_code=404,
                detail="Chat session not found"
            )

        return session
    
    @staticmethod
    def validate_session_owner(
        db: Session,
        session_id: int,
        user_id: int
    ):

        session = SessionService.get_session(
            db,
            session_id
        )

        if session.user_id != user_id:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return session
    
    @staticmethod
    def get_user_sessions(
        db: Session,
        user_id: int
    ):

        return ChatSessionRepository.get_all_by_user(
            db,
            user_id
        )