from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

service = GoalToTerraformService()

project = service.generate(
    """
    Create 2 AKS clusters
    Premium Tier
    India Central
    GZRS
    Sidecar Support
    """
)

print()
print("=" * 60)
print("V0.4.14 TERRAFORM UNIFICATION")
print("=" * 60)
print()

print(type(project).__name__)

print()

print(project.model_dump())