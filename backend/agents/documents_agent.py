from backend.agents.base_agent import BaseAgent


class DocumentationAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "agents/documentation/system_prompt.md"
        )


if __name__ == "__main__":

    agent = DocumentationAgent()

    result = agent.execute(
        "Create README"
    )

    print(result)