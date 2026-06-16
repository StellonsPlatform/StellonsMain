from backend.orchestrator.agent_router import AgentRouter

from backend.agents.devops_agent import DevOpsAgent

from backend.services.infrastructure_service import (
    InfrastructureService,
)


class ExecutionEngine:

    def __init__(self):

        self.router = AgentRouter()

        self.infrastructure_service = (
            InfrastructureService()
        )

    def execute_tasks(self, tasks):

        results = []

        for task in tasks:

            print(f"\nExecuting: {task}")

            agent = self.router.route(task)

            # =====================================
            # DEVOPS → TERRAFORM
            # =====================================

            if isinstance(
                agent,
                DevOpsAgent,
            ):

                artifact = (
                    self.infrastructure_service.generate(
                        task
                    )
                )

                results.append(
                    {
                        "task": task,
                        "agent": type(agent).__name__,
                        "artifact_type": artifact.tool,
                        "artifact": artifact.code,
                    }
                )

                continue

            # =====================================
            # NORMAL AGENTS
            # =====================================

            result = agent.execute(task)

            results.append(
                {
                    "task": task,
                    "agent": type(agent).__name__,
                    "result": result,
                }
            )

        return results