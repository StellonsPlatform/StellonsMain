from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

service = GoalToTerraformService()

result = service.generate(
    goal="""
Deploy production AKS cluster
with monitoring
in East US
and 5 nodes
""",
    tasks=[],
)

print()
print("=" * 60)
print("V0.4.4 TERRAFORM ENHANCEMENT")
print("=" * 60)

print()
print(result.code)