from app.core.security import create_access_token

token = create_access_token(
    {"sub": "himanshu2@gmail.com"}
)

print(token)