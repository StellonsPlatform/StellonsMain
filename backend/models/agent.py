from pydantic import BaseModel


class Agent(BaseModel):
    name: str
    role: str
    system_prompt_path: str