from backend.orchestrator.workflow_engine import WorkflowEngine
from backend.orchestrator.task_extractor import TaskExtractor

engine = WorkflowEngine()

extractor = TaskExtractor()

plan = engine.execute(
    "Build AKS Deployment Platform"
)

tasks = extractor.extract(plan)

print("\nEXTRACTED TASKS\n")

for task in tasks:

    print(task)