from backend.services.infrastructure_intent_service import (
    InfrastructureIntentService,
)

service = InfrastructureIntentService()

intent = service.extract(
    """
    Production AKS cluster

    1 node

    Premium tier

    East US
    """
)

print()
print("=" * 60)
print("V0.4.15 INTENT NORMALIZATION")
print("=" * 60)
print()

print(
    intent.model_dump()
)