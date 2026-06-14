from backend.agents.planner_agent import PlannerAgent
from backend.orchestrator.agent_router import AgentRouter


class WorkflowEngine:

    def __init__(self):

        self.planner = PlannerAgent()

        self.router = AgentRouter()

    def execute(self, goal: str):

        print(f"\nGOAL:\n{goal}\n")

        print("Planning...\n")

        plan = self.planner.execute(goal)

        print(plan)

        return plan