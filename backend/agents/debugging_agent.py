from backend.agents.base_agent import BaseAgent


class DebuggingAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "agents/debugging/system_prompt.md"
        )


if __name__ == "__main__":

    agent = DebuggingAgent()

    result = agent.execute(
        "Analyze Kubernetes CrashLoopBackOff"
    )

    print(result)