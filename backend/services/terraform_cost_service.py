from backend.models.cost_estimate import (
    CostEstimate,
)

from backend.models.infrastructure_intent import (
    InfrastructureIntent,
)


class TerraformCostService:

    def estimate(
        self,
        intent: InfrastructureIntent,
    ) -> CostEstimate:

        node_cost = (
            intent.node_count * 100
        )

        premium_cost = 0

        if (
            intent.sku_tier.lower()
            == "premium"
        ):
            premium_cost = 200

        cluster_cost = (
            intent.cluster_count * 50
        )

        monitoring_cost = 0

        if intent.monitoring:

            monitoring_cost = 100

        total = (
            node_cost
            + premium_cost
            + cluster_cost
            + monitoring_cost
        )

        return CostEstimate(
            estimated_monthly_cost=total,
            currency="USD",
            breakdown={
                "nodes": node_cost,
                "premium": premium_cost,
                "clusters": cluster_cost,
                "monitoring": monitoring_cost,
            },
        )