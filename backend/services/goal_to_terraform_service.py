from backend.services.infrastructure_intent_service import (
    InfrastructureIntentService,
)

from backend.generators.terraform_generator import (
    TerraformGenerator,
)

from backend.models.infrastructure_request import (
    InfrastructureRequest,
)


class GoalToTerraformService:

    def __init__(self):

        self.intent_service = (
            InfrastructureIntentService()
        )

        self.generator = (
            TerraformGenerator()
        )

    def generate(
        self,
        goal: str,
    ):

        intent = (
            self.intent_service.extract(
                goal
            )
        )

        request = InfrastructureRequest(
            cloud=intent.cloud,
            resource_type=intent.resource_type,
            region=intent.region,
            node_count=intent.node_count,
            environment=intent.environment,
            monitoring=intent.monitoring,
            cluster_count=intent.cluster_count,
            sku_tier=intent.sku_tier,
            redundancy=intent.redundancy,
            sidecar_support=intent.sidecar_support,
        )

        return self.generator.generate(
            request
        )