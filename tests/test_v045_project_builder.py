from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

service = GoalToTerraformService()

project = service.generate(
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
print("MAIN.TF")
print("=" * 60)
print(project.main_tf)

print()
print("=" * 60)
print("VARIABLES.TF")
print("=" * 60)
print(project.variables_tf)

print()
print("=" * 60)
print("OUTPUTS.TF")
print("=" * 60)
print(project.outputs_tf)

print()
print("=" * 60)
print("TERRAFORM.TFVARS")
print("=" * 60)
print(project.terraform_tfvars)