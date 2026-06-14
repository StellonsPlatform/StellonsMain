from backend.agents.base_agent import BaseAgent


class ArchitectAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "agents/architect/system_prompt.md"
        )


if __name__ == "__main__":

    agent = ArchitectAgent()

    result = agent.execute(
        "Design multi-cloud deployment platform"
    )

    print(result)