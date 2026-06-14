from backend.orchestrator.workflow_engine import WorkflowEngine
from backend.orchestrator.task_extractor import TaskExtractor
from backend.orchestrator.task_dispatcher import TaskDispatcher


engine = WorkflowEngine()

extractor = TaskExtractor()

dispatcher = TaskDispatcher()


plan = engine.execute(
    "Build AKS Deployment Platform"
)

tasks = extractor.extract(plan)

assignments = dispatcher.dispatch(tasks)

print("\nTASK ASSIGNMENTS\n")

for item in assignments:

    print(
        f"{item['task']} -> {item['agent']}"
    )