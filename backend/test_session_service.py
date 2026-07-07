from app.database.database import SessionLocal
from app.services.chat.session_service import SessionService

db = SessionLocal()

sessions = SessionService.get_user_sessions(
    db,
    user_id=2
)

for session in sessions:
    print(
        session.id,
        session.title
    )