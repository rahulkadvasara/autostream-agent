from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    intent: str | None
    name: str | None
    email: str | None
    platform: str | None
    lead_captured: bool
