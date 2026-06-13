from backend.models.task import Task
from backend.orchestrator.agent_runner import AgentRunner


def main():

    task = Task(
        id="1",
        title="Build AKS Deployment Service",
        description="Generate AKS deployment workflow",
        assigned_agent="planner"
    )

    runner = AgentRunner()

    result = runner.run(task)

    print(result)


if __name__ == "__main__":
    main()