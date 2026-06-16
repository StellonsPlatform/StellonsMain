from backend.services.infrastructure_aggregator import (
    InfrastructureAggregator,
)

from backend.generators.terraform_generator import (
    TerraformGenerator,
)

from backend.models.infrastructure_request import (
    InfrastructureRequest,
)


class GoalToTerraformService:

    def __init__(self):

        self.aggregator = (
            InfrastructureAggregator()
        )

        self.generator = (
            TerraformGenerator()
        )

    def generate(
        self,
        goal: str,
        tasks: list[str],
    ):

        context = self.aggregator.aggregate(
            goal=goal,
            tasks=tasks,
        )

        request = InfrastructureRequest(
            cloud=context.cloud,
            resource_type=context.resource_type,
            region=context.region,
            node_count=context.node_count,
        )

        return self.generator.generate(
            request
        )