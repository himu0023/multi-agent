from sqlalchemy import Column, Integer, String

from app.database.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, index=True)

    hashed_password = Column(String(255), nullable=False)

    chat_sessions = relationship(
    "ChatSession",
    back_populates="user",
    cascade="all, delete-orphan"
)