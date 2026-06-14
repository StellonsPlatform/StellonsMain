from backend.agents.base_agent import BaseAgent


class DevOpsAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "agents/devops/system_prompt.md"
        )


if __name__ == "__main__":

    agent = DevOpsAgent()

    result = agent.execute(
        "Create AKS Terraform"
    )

    print(result)