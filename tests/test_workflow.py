from backend.orchestrator.workflow_engine import WorkflowEngine


engine = WorkflowEngine()

engine.execute(
    "Build AKS Deployment Platform"
)