from backend.agents.planner_agent import PlannerAgent


class AgentRunner:

    def run(self, task):

        if task.assigned_agent == "planner":

            planner = PlannerAgent()

            result = planner.execute(
                task.description
            )

            print(result)

            return result