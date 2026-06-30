from app.database.database import SessionLocal
from app.schemas.user import UserCreate
from app.services.user_service import UserService

db = SessionLocal()

user = UserCreate(
    name="Himanshu",
    email="himanshu@gmail.com",
    password="123456"
)

created_user = UserService.create_user(db, user)

print(created_user.id)
print(created_user.name)
print(created_user.email)