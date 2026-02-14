from pydantic import BaseModel

class UserInput(BaseModel):
    income: str
    income_stability: str
    savings_buffer: str
    stress_level: str
    goal_urgency: str
    decision_preference: str


class AgentResponse(BaseModel):
    decision: str
    opportunity_window: str
    explanation: str
