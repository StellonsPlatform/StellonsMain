from backend.services.infrastructure_intent_service import (
    InfrastructureIntentService,
)

service = InfrastructureIntentService()

result = service.extract(
    "Deploy production AKS cluster with monitoring in East US and 5 nodes"
)

print()
print("=" * 60)
print("INFRASTRUCTURE INTENT")
print("=" * 60)

print(result.model_dump())