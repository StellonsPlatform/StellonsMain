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
    region="Moon Region",
    node_count=25,
    environment="production",
    monitoring=False,
    cluster_count=10,
    sku_tier="premium",
    redundancy="none",
    sidecar_support=False,
)

result = engine.evaluate(
    intent
)

print()
print("=" * 60)
print("V0.5.1 POLICY RULE EXPANSION")
print("=" * 60)
print()

print(
    result.model_dump()
)