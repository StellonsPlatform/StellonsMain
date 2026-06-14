from pathlib import Path
from backend.llm.nvidia_client import NvidiaClient

class PlannerAgent:

    def __init__(self):

        self.client=NvidiaClient()
        self.system_prompt=Path("agents/planner/system_prompt.md").read_text()
        
    def plan(self,goal:str):
        prompt = f"""
            {self.system_prompt}

            Goal: {goal}
        """

        return self.client.generate(prompt)
    
if __name__ == "__main__":

    planner = PlannerAgent()

    result = planner.plan(
        "Build AKS deployment platform"
    )

    print(result)