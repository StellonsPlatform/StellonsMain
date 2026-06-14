from pydantic import BaseModel


class TaskAssignment(BaseModel):
    task: str
    agent: str


class AgentResult(BaseModel):
    agent: str
    task: str
    result: str


class WorkflowResponse(BaseModel):
    goal: str
    tasks: list[TaskAssignment]
    results: list[AgentResult]