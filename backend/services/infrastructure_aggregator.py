from backend.models.infrastructure_context import (
    InfrastructureContext,
)


class InfrastructureAggregator:

    def aggregate(
        self,
        goal: str,
        tasks: list[str],
    ) -> InfrastructureContext:

        goal_lower = goal.lower()

        # =====================================
        # AKS
        # =====================================

        if "aks" in goal_lower:

            return InfrastructureContext(
                cloud="azure",
                resource_type="aks",
                region="East US",
                node_count=3,
            )

        # =====================================
        # KUBERNETES
        # =====================================

        if "kubernetes" in goal_lower:

            return InfrastructureContext(
                cloud="azure",
                resource_type="aks",
                region="East US",
                node_count=3,
            )

        # =====================================
        # DEFAULT
        # =====================================

        return InfrastructureContext(
            cloud="azure",
            resource_type="aks",
            region="East US",
            node_count=1,
        )