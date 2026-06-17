from backend.orchestrator.workflow_engine import (
    WorkflowEngine,
)

workflow = WorkflowEngine()

result = workflow.execute(
    "Deploy AKS cluster in East US with 3 nodes"
)

print()
print("=" * 60)
print("V0.4.1 PIPELINE")
print("=" * 60)

print(result["terraform"]["artifact"])