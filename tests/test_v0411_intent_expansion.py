from backend.services.infrastructure_intent_service import (
    InfrastructureIntentService,
)

service = (
    InfrastructureIntentService()
)

intent = service.extract(
    """
Create 2 AKS clusters

10 nodes

Premium tier

Sidecar container support

India Central

GZRS redundancy

Production environment
"""
)

print()
print("=" * 60)
print("V0.4.11 INTENT EXPANSION")
print("=" * 60)
print()

print(
    intent.model_dump()
)