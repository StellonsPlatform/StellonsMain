from backend.orchestrator.workflow_engine import WorkflowEngine
from backend.orchestrator.task_extractor import TaskExtractor
from backend.orchestrator.execution_engine import ExecutionEngine
from backend.orchestrator.result_aggregator import ResultAggregator


workflow = WorkflowEngine()

extractor = TaskExtractor()

executor = ExecutionEngine()

aggregator = ResultAggregator()


# =====================================
# Generate Plan
# =====================================

plan = workflow.execute(
    "Build AKS Deployment Platform"
)

# =====================================
# Extract Tasks
# =====================================

tasks = extractor.extract(plan)

print("\n" + "=" * 50)
print("EXTRACTED TASKS")
print("=" * 50)

for task in tasks:
    print(task)

print(f"\nTOTAL TASKS: {len(tasks)}")

# =====================================
# Execute Tasks
# =====================================

results = executor.execute_tasks(tasks)

print("\n" + "=" * 50)
print("EXECUTION RESULTS")
print("=" * 50)

for result in results:

    print(f"\nAgent : {result['agent']}")
    print(f"Task  : {result['task']}")

# =====================================
# Aggregate Results
# =====================================

report = aggregator.aggregate(results)

print("\n" + "=" * 50)
print("FINAL REPORT")
print("=" * 50)

print(report[:5000])