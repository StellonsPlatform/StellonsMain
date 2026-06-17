from pydantic import BaseModel


class RouterResponse(BaseModel):
    agent: str
    confidence: float
    reasoning: str