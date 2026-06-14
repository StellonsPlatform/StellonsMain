from backend.orchestrator.workflow_engine import WorkflowEngine
from backend.orchestrator.task_extractor import TaskExtractor
from backend.orchestrator.execution_engine import ExecutionEngine


workflow = WorkflowEngine()

extractor = TaskExtractor()

executor = ExecutionEngine()


plan = workflow.execute(
    "Build AKS Deployment Platform"
)

tasks = extractor.extract(plan)

results = executor.execute_tasks(tasks)

print("\nEXECUTION RESULTS\n")

for result in results:

    print(
        f"\nAgent: {result['agent']}"
    )

    print(
        f"Task: {result['task']}"
    )

    print(
        f"Result:\n{result['result'][:300]}"
    )