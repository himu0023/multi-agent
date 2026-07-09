from abc import ABC, abstractmethod

from app.ai.models.agent_response import AgentResponse


class BaseAgent(ABC):

    @abstractmethod
    def generate_response(
        self,
        message: str
    ) -> AgentResponse:
        pass