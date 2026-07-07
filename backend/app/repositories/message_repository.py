from sqlalchemy.orm import Session

from app.models.message import Message


class MessageRepository:

    @staticmethod
    def create(
        db: Session,
        message: Message
    ):
        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    @staticmethod
    def get_by_session(
        db: Session,
        session_id: int
    ):
        return (
            db.query(Message)
            .filter(
                Message.session_id == session_id
            )
            .order_by(
                Message.created_at.asc()
            )
            .all()
        )

    @staticmethod
    def get_recent_messages(
        db: Session,
        session_id: int,
        limit: int = 10
    ):
        return (
            db.query(Message)
            .filter(
                Message.session_id == session_id
            )
            .order_by(
                Message.created_at.desc()
            )
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_last_message(
        db: Session,
        session_id: int
    ):
        return (
            db.query(Message)
            .filter(
                Message.session_id == session_id
            )
            .order_by(
                Message.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        message: Message
    ):
        db.delete(message)
        db.commit()