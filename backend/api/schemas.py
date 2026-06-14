from pydantic import BaseModel


class ExecuteRequest(BaseModel):
    goal: str