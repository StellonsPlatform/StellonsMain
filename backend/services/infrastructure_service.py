from backend.generators.terraform_generator import (
    TerraformGenerator,
)

from backend.models.infrastructure_request import (
    InfrastructureRequest,
)

from backend.models.generator_response import (
    GeneratorResponse,
)


class InfrastructureService:

    def __init__(self):

        self.terraform_generator = (
            TerraformGenerator()
        )

    def generate(
        self,
        task: str,
    ) -> GeneratorResponse:

        task_lower = task.lower()

        # =====================================
        # AKS
        # =====================================

        if "aks" in task_lower:

            request = InfrastructureRequest(
                cloud="azure",
                resource_type="aks",
                region="East US",
                node_count=3,
            )

            return self.terraform_generator.generate(
                request
            )

        # =====================================
        # KUBERNETES
        # =====================================

        if "kubernetes" in task_lower:

            request = InfrastructureRequest(
                cloud="azure",
                resource_type="aks",
                region="East US",
                node_count=3,
            )

            return self.terraform_generator.generate(
                request
            )

        # =====================================
        # DEFAULT
        # =====================================

        return GeneratorResponse(
            tool="terraform",
            code="# No infrastructure generated",
        )