from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

from backend.services.terraform_packaging_service import (
    TerraformPackagingService,
)

from backend.services.terraform_export_service import (
    TerraformExportService,
)

terraform_service = (
    GoalToTerraformService()
)

packaging_service = (
    TerraformPackagingService()
)

export_service = (
    TerraformExportService()
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

package = (
    packaging_service.package(
        project
    )
)

result = export_service.export(
    package
)

print()
print("=" * 60)
print("TERRAFORM EXPORT")
print("=" * 60)

print()

print(
    result.model_dump()
)