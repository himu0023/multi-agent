from app.database.database import SessionLocal
from app.services.chat.conversation_service import ConversationService

db = SessionLocal()

ConversationService.save_user_message(
    db = db, 
    session_id = 4,
    content = "Hello AI, how are you?"
)

history = ConversationService.get_history(
    db,
    4
)

for msg in history:
    print(f"{msg.role}: {msg.content}")