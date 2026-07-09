from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.ai.agents.dummy_agent import DummyAgent
from app.api.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.message import MessageRequest, ChatResponse
from app.services.chat.conversation_service import ConversationService
from app.services.chat.session_service import SessionService
from app.ai.orchestrator.agent_orchestrator import AgentOrchestrator

router = APIRouter(
    prefix="/chat",
    tags=["Messages"]
)

@router.post(
    "/message",
    response_model=ChatResponse
)
def send_message(
    request: MessageRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    print("========== STEP 1 ==========")

    SessionService.validate_session_owner(
        db=db,
        session_id=request.session_id,
        user_id=current_user.id
    )

    print("========== STEP 2 ==========")

    user_message = ConversationService.save_user_message(
        db=db,
        session_id=request.session_id,
        content=request.message
    )

    print("========== STEP 3 ==========")

    orchestrator = AgentOrchestrator()

    print("========== STEP 4 ==========")

    ai_response = orchestrator.process(request.message)

    print("========== STEP 5 ==========")

    assistant_message = ConversationService.save_assistant_message(
        db=db,
        session_id=request.session_id,
        content=ai_response.content,
        agent_name=ai_response.agent_name
    )

    print("========== STEP 6 ==========")

    return {
        "user_message": user_message,
        "assistant_message": assistant_message
    }