from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_response import AgentResponse


class DummyAgent(BaseAgent):

    def generate_response(
        self,
        message: str
    ) -> AgentResponse:

        return AgentResponse(
            content=(
                f"I received your message: '{message}'. "
                "The AI service is not connected yet."
            ),
            agent_name="DummyAgent",
            confidence=1.0,
        )