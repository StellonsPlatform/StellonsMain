import uuid

from backend.models.terraform_project import (
    TerraformProject,
)

from backend.models.deployment_result import (
    DeploymentResult,
)


class DeploymentEngine:

    def prepare(
        self,
        project: TerraformProject,
        environment: str,
        resource_type: str,
        approved: bool,
    ) -> DeploymentResult:

        deployment_id = str(
            uuid.uuid4()
        )

        status = "queued"

        ready = True

        if not project.main_tf.strip():

            ready = False

            status = "failed"

        if not approved:

            ready = False

            status = "blocked"

        return DeploymentResult(
            deployment_id=deployment_id,
            status=status,
            environment=environment,
            resource_type=resource_type,
            ready_for_deployment=ready,
            approved=approved,
        )