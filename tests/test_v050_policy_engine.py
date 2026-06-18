from backend.services.policy_engine import (
    PolicyEngine,
)

from backend.models.infrastructure_intent import (
    InfrastructureIntent,
)

engine = PolicyEngine()

intent = InfrastructureIntent(
    cloud="azure",
    resource_type="aks",
    region="East US",
    node_count=1,
    environment="production",
    monitoring=False,
    cluster_count=1,
    sku_tier="standard",
    redundancy="none",
    sidecar_support=False,
)

result = engine.evaluate(
    intent
)

print()
print("=" * 60)
print("V0.5.0 POLICY ENGINE")
print("=" * 60)
print()

print(
    result.model_dump()
)