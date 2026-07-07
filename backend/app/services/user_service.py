from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password
from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate):

        # Check if email already exists
        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise ValueError("Email already registered")

        # Create new user
        new_user = User(
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password)
        )

        return UserRepository.create(
            db,
            new_user
        )

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):

        user = UserRepository.get_by_email(
            db,
            email
        )

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return user