from backend.orchestrator.agent_router import AgentRouter


class TaskDispatcher:

    def __init__(self):

        self.router = AgentRouter()

    def dispatch(self, tasks):

        assignments = []

        for task in tasks:

            agent = self.router.route(task)

            assignments.append(
                {
                    "task": task,
                    "agent": type(agent).__name__
                }
            )

        return assignments