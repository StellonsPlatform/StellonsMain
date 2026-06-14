from backend.agents.planner_agent import PlannerAgent
from backend.agents.developer_agent import DeveloperAgent
from backend.agents.devops_agent import DevOpsAgent
from backend.agents.documents_agent import DocumentationAgent
from backend.agents.debugging_agent import DebuggingAgent
from backend.agents.architect_agent import ArchitectAgent


class AgentRouter:

    def route(self, task: str):

        task_lower = task.lower()

        if "fastapi" in task_lower:
            return DeveloperAgent()

        if "python" in task_lower:
            return DeveloperAgent()

        if "terraform" in task_lower:
            return DevOpsAgent()

        if "opentofu" in task_lower:
            return DevOpsAgent()

        if "aks" in task_lower:
            return DevOpsAgent()

        if "debug" in task_lower:
            return DebuggingAgent()

        if "error" in task_lower:
            return DebuggingAgent()

        if "architecture" in task_lower:
            return ArchitectAgent()

        if "design" in task_lower:
            return ArchitectAgent()

        if "readme" in task_lower:
            return DocumentationAgent()

        return PlannerAgent()