from fastapi import FastAPI
from pydantic import BaseModel

from backend.orchestrator.workflow_engine import WorkflowEngine


app = FastAPI(
    title="Stellons API",
    version="0.2.2"
)


class GoalRequest(BaseModel):
    goal: str


@app.get("/")
def root():

    return {
        "platform": "Stellons",
        "version": "0.2.2"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/execute")
def execute(request: GoalRequest):

    workflow = WorkflowEngine()

    result = workflow.execute(
        request.goal
    )

    return result