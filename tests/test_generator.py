from backend.generators.terraform_generator import (
    TerraformGenerator,
)

from backend.models.infrastructure_request import (
    InfrastructureRequest,
)


request = InfrastructureRequest(
    cloud="azure",
    resource_type="aks",
    region="East US",
    node_count=3,
)

generator = TerraformGenerator()

result = generator.generate(request)

print()
print("====================================")
print("TERRAFORM OUTPUT")
print("====================================")
print(result.code)