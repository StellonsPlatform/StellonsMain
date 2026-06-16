from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

service = GoalToTerraformService()

result = service.generate(
    goal="Deploy AKS cluster in East US with 3 nodes",
    tasks=[
        "Create Resource Group",
        "Create Service Principal",
        "Create AKS Cluster",
        "Verify AKS Cluster",
    ],
)

print()
print("===================================")
print("GOAL TO TERRAFORM")
print("===================================")

print()
print(result.code)