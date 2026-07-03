from app.database.database import SessionLocal
from app.services.user_service import UserService

db = SessionLocal()

user = UserService.authenticate_user(
    db,
    "rahul@gmail.com",
    "wrongpassword" # rahul123
)

if user:
    print("Login Successful")
    print(user.email)
else:
    print("Invalid Credentials")