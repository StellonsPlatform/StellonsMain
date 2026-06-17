from backend.services.infrastructure_service import (
    InfrastructureService,
)


service = InfrastructureService()

result = service.generate(
    "Deploy AKS cluster in East US with 3 nodes"
)

print()
print("====================================")
print("INFRASTRUCTURE SERVICE")
print("====================================")
print()

print("Tool:")
print(result.tool)

print()
print("Generated Artifact:")
print()

print(result.code)