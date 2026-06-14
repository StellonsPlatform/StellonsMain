from backend.agents.planner_agent import PlannerAgent
from backend.orchestrator.task_extractor import TaskExtractor
from backend.orchestrator.task_dispatcher import TaskDispatcher
from backend.orchestrator.execution_engine import ExecutionEngine


class WorkflowEngine:

    def __init__(self):

        self.planner = PlannerAgent()

        self.extractor = TaskExtractor()

        self.dispatcher = TaskDispatcher()

        self.execution_engine = ExecutionEngine()

    def execute(self, goal: str):

        print(f"\nGOAL:\n{goal}\n")

        print("Planning...\n")

        plan = self.planner.execute(goal)

        print(plan)

        print("\n" + "=" * 50)
        print("EXTRACTED TASKS")
        print("=" * 50)

        tasks = self.extractor.extract(plan)

        for task in tasks:
            print(task)

        print(f"\nTOTAL TASKS: {len(tasks)}")

        print("\n" + "=" * 50)
        print("TASK ASSIGNMENTS")
        print("=" * 50)

        assignments = self.dispatcher.dispatch(tasks)

        for assignment in assignments:
            print(
                f"{assignment['task']} -> "
                f"{assignment['agent']}"
            )

        print("\n" + "=" * 50)
        print("EXECUTION")
        print("=" * 50)

        results = self.execution_engine.execute_tasks(
            tasks
        )

        return {
            "goal": goal,
            "tasks": assignments,
            "results": results
        }