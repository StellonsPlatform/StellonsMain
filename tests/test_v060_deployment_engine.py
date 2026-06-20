from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

from backend.services.deployment_engine import (
    DeploymentEngine,
)

service = GoalToTerraformService()

deployment_engine = (
    DeploymentEngine()
)

project = service.generate(
    """
    Production AKS Cluster

    East US

    Premium

    5 Nodes
    """
)

result = deployment_engine.prepare(
    project=project,
    environment="production",
    resource_type="aks",
    approved=True,
)

print()
print("=" * 60)
print("V0.6.0 DEPLOYMENT ENGINE")
print("=" * 60)
print()

print(
    result.model_dump()
)