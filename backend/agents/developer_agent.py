from backend.agents.base_agent import BaseAgent


class DeveloperAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "agents/developer/system_prompt.md"
        )


if __name__ == "__main__":

    agent = DeveloperAgent()

    result = agent.execute(
        "Create FastAPI endpoint"
    )

    print(result)