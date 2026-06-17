from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

from backend.services.terraform_validation_service import (
    TerraformValidationService,
)

terraform_service = (
    GoalToTerraformService()
)

validation_service = (
    TerraformValidationService()
)

project = terraform_service.generate(
    goal="""
Deploy production AKS cluster
with monitoring
in East US
and 5 nodes
""",
    tasks=[],
)

result = validation_service.validate(
    project
)

print()
print("=" * 60)
print("TERRAFORM VALIDATION")
print("=" * 60)

print()

print(
    result.model_dump()
)