from app.ai.agents.base_agent import BaseAgent
from app.ai.agents.dummy_agent import DummyAgent
from app.ai.models.agent_response import AgentResponse


class AgentOrchestrator:

    def __init__(self):

        # Temporary
        # Later this becomes BillingAgent, FAQAgent, etc.
        self.default_agent: BaseAgent = DummyAgent()

    def process(
        self,
        message: str
    ) -> AgentResponse:

        return self.default_agent.generate_response(message)