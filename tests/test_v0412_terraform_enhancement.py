from backend.models.infrastructure_request import (
    InfrastructureRequest,
)

from backend.generators.terraform_generator import (
    TerraformGenerator,
)

generator = TerraformGenerator()

request = InfrastructureRequest(
    cloud="azure",
    resource_type="aks",
    region="India Central",
    node_count=10,
    environment="production",
    monitoring=True,
    cluster_count=2,
    sku_tier="premium",
    redundancy="gzrs",
    sidecar_support=True,
)

result = generator.generate(
    request
)

print()
print("=" * 60)
print("V0.4.12 TERRAFORM ENHANCEMENT")
print("=" * 60)
print()

print(result.code)