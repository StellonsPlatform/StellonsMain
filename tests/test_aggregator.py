from backend.orchestrator.workflow_engine import WorkflowEngine
from backend.orchestrator.task_extractor import TaskExtractor
from backend.orchestrator.execution_engine import ExecutionEngine
from backend.orchestrator.result_aggregator import ResultAggregator


workflow = WorkflowEngine()
extractor = TaskExtractor()
executor = ExecutionEngine()
aggregator = ResultAggregator()


plan = workflow.execute(
    "Build AKS Deployment Platform"
)

tasks = extractor.extract(plan)

results = executor.execute_tasks(tasks)

report = aggregator.aggregate(results)

print("\nFINAL REPORT\n")

print(report[:5000])