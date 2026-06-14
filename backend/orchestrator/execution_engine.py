from backend.orchestrator.agent_router import AgentRouter


class ExecutionEngine:

    def __init__(self):

        self.router = AgentRouter()

    def execute_tasks(self, tasks):

        results = []

        for task in tasks:

            print(f"\nExecuting: {task}")

            agent = self.router.route(task)

            result = agent.execute(task)

            results.append(
                {
                    "task": task,
                    "agent": type(agent).__name__,
                    "result": result
                }
            )

        return results