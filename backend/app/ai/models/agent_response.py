from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResponse:

    content: str

    agent_name: str

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)