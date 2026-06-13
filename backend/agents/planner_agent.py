from backend.llm.nvidia_client import NvidiaClient


class PlannerAgent:

    def __init__(self):
        self.client = NvidiaClient()

    def plan(self, goal: str):

        prompt = f"""
You are a cloud solution architect.

Break the following goal into implementation tasks.

Goal:
{goal}

Return a numbered list.
"""

        return self.client.generate(prompt)
    
if __name__ == "__main__":

    planner = PlannerAgent()

    result = planner.plan(
        "Build AKS deployment platform"
    )

    print(result)