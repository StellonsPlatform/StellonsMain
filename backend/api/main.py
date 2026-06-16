from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.orchestrator.workflow_engine import WorkflowEngine


app = FastAPI(
    title="Stellons API",
    version="0.2.2"
)

# ==========================
# CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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