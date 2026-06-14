from backend.agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "agents/planner/system_prompt.md"
        )


if __name__ == "__main__":

    planner = PlannerAgent()

    result = planner.execute(
        "Build AKS deployment platform"
    )

    print(result)