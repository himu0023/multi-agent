from sqlalchemy.orm import Session

from app.models.chat_session import ChatSession


class ChatSessionRepository:

    @staticmethod
    def create(
        db: Session,
        session: ChatSession
    ):
        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def get_by_id(
        db: Session,
        session_id: int
    ):
        return (
            db.query(ChatSession)
            .filter(ChatSession.id == session_id)
            .first()
        )

    @staticmethod
    def get_all_by_user(
        db: Session,
        user_id: int
    ):
        return (
            db.query(ChatSession)
            .filter(ChatSession.user_id == user_id)
            .order_by(ChatSession.created_at.desc())
            .all()
        )