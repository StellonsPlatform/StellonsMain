from backend.agents.planner_agent import PlannerAgent
from backend.agents.developer_agent import DeveloperAgent
from backend.agents.devops_agent import DevOpsAgent
from backend.agents.documents_agent import DocumentationAgent
from backend.agents.debugging_agent import DebuggingAgent
from backend.agents.architect_agent import ArchitectAgent


class AgentRouter:

    def route(self, task: str):

        task_lower = task.lower()

        # =====================================
        # Architect Agent
        # =====================================

        if "architecture" in task_lower:
            return ArchitectAgent()

        if "design" in task_lower:
            return ArchitectAgent()

        if "plan" in task_lower:
            return ArchitectAgent()

        if "solution" in task_lower:
            return ArchitectAgent()

        if "security" in task_lower:
            return ArchitectAgent()

        if "rbac" in task_lower:
            return ArchitectAgent()

        if "aad" in task_lower:
            return ArchitectAgent()

        if "key vault" in task_lower:
            return ArchitectAgent()

        if "azure environment" in task_lower:
            return ArchitectAgent()

        if "environment" in task_lower:
            return ArchitectAgent()

        if "compliance" in task_lower:
            return ArchitectAgent()

        # =====================================
        # Developer Agent
        # =====================================

        if "fastapi" in task_lower:
            return DeveloperAgent()

        if "python" in task_lower:
            return DeveloperAgent()

        if "application" in task_lower:
            return DeveloperAgent()

        if "applications" in task_lower:
            return DeveloperAgent()

        if "api" in task_lower:
            return DeveloperAgent()

        if "code" in task_lower:
            return DeveloperAgent()

        # =====================================
        # DevOps Agent
        # =====================================

        if "terraform" in task_lower:
            return DevOpsAgent()

        if "opentofu" in task_lower:
            return DevOpsAgent()

        if "aks" in task_lower:
            return DevOpsAgent()

        if "kubernetes" in task_lower:
            return DevOpsAgent()

        if "cluster" in task_lower:
            return DevOpsAgent()

        if "deployment" in task_lower:
            return DevOpsAgent()

        if "networking" in task_lower:
            return DevOpsAgent()

        if "network" in task_lower:
            return DevOpsAgent()

        if "load balancer" in task_lower:
            return DevOpsAgent()

        if "ingress" in task_lower:
            return DevOpsAgent()

        if "monitor" in task_lower:
            return DevOpsAgent()

        if "monitoring" in task_lower:
            return DevOpsAgent()

        if "logging" in task_lower:
            return DevOpsAgent()

        # =====================================
        # Documentation Agent
        # =====================================

        if "readme" in task_lower:
            return DocumentationAgent()

        if "documentation" in task_lower:
            return DocumentationAgent()

        if "guide" in task_lower:
            return DocumentationAgent()

        if "release note" in task_lower:
            return DocumentationAgent()

        # =====================================
        # Debugging Agent
        # =====================================

        if "debug" in task_lower:
            return DebuggingAgent()

        if "error" in task_lower:
            return DebuggingAgent()

        if "exception" in task_lower:
            return DebuggingAgent()

        if "crash" in task_lower:
            return DebuggingAgent()

        if "failure" in task_lower:
            return DebuggingAgent()

        if "test" in task_lower:
            return DebuggingAgent()

        if "validate" in task_lower:
            return DebuggingAgent()

        if "verification" in task_lower:
            return DebuggingAgent()

        # =====================================
        # Default Agent
        # =====================================

        return PlannerAgent()