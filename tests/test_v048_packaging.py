from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

from backend.services.terraform_packaging_service import (
    TerraformPackagingService,
)

terraform_service = (
    GoalToTerraformService()
)

packaging_service = (
    TerraformPackagingService()
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

package = packaging_service.package(
    project
)

print()
print("=" * 60)
print("TERRAFORM PACKAGE")
print("=" * 60)

print()

for name, content in package.files.items():

    print(f"\nFILE: {name}")
    print("-" * 40)

    print(content[:200])