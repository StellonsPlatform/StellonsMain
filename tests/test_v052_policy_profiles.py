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
    region="Europe West",
    node_count=60,
    environment="production",
    monitoring=False,
    cluster_count=6,
    sku_tier="standard",
    redundancy="none",
    sidecar_support=False,
)

result = engine.evaluate(
    intent,
    profile_name="regulated",
)

print()
print("=" * 60)
print("V0.5.2 POLICY PROFILES")
print("=" * 60)
print()

print(
    result.model_dump()
)