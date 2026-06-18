from datetime import datetime

from fastapi import FastAPI

from backend.api.schemas import (
    TerraformRequest,
    TerraformResponse,
)

from backend.services.infrastructure_intent_service import (
    InfrastructureIntentService,
)

from backend.services.goal_to_terraform_service import (
    GoalToTerraformService,
)

from backend.services.terraform_validation_service import (
    TerraformValidationService,
)

from backend.services.terraform_packaging_service import (
    TerraformPackagingService,
)

from backend.services.terraform_cost_service import (
    TerraformCostService,
)

from backend.services.policy_engine import (
    PolicyEngine,
)

app = FastAPI(
    title="Stellons API",
    version="0.5.3",
)

intent_service = (
    InfrastructureIntentService()
)

terraform_service = (
    GoalToTerraformService()
)

validation_service = (
    TerraformValidationService()
)

packaging_service = (
    TerraformPackagingService()
)

cost_service = (
    TerraformCostService()
)

policy_engine = (
    PolicyEngine()
)


@app.get("/")
def root():

    return {
        "service": "Stellons API",
        "version": "0.5.3",
        "status": "running",
    }


@app.post(
    "/terraform/export",
    response_model=TerraformResponse,
)
def export_terraform(
    request: TerraformRequest,
):

    #
    # Default Governance Profile
    #

    policy_profile = "startup"

    intent = (
        intent_service.extract(
            request.goal
        )
    )

    policy_result = (
        policy_engine.evaluate(
            intent,
            profile_name=policy_profile,
        )
    )

    #
    # Policy Rejection Path
    #

    if not policy_result.approved:

        return TerraformResponse(
            success=False,
            intent=intent.model_dump(),
            policy_profile=policy_profile,
            policy=policy_result.model_dump(),
            cost_estimation={},
            validation={},
            export_path="",
            files=[],
            file_count=0,
            generated_at=datetime.utcnow().isoformat(),
            cloud=intent.cloud,
            resource_type=intent.resource_type,
            api_version="0.5.3",
        )

    terraform_project = (
        terraform_service.generate(
            request.goal
        )
    )

    cost_estimation = (
        cost_service.estimate(
            intent
        )
    )

    validation_result = (
        validation_service.validate(
            terraform_project
        )
    )

    export_path = (
        packaging_service.write(
            terraform_project
        )
    )

    files = [
        "main.tf",
        "variables.tf",
        "outputs.tf",
        "terraform.tfvars",
    ]

    return TerraformResponse(
        success=True,
        intent=intent.model_dump(),
        policy_profile=policy_profile,
        policy=policy_result.model_dump(),
        cost_estimation=cost_estimation.model_dump(),
        validation=validation_result.model_dump(),
        export_path=export_path,
        files=files,
        file_count=len(files),
        generated_at=datetime.utcnow().isoformat(),
        cloud=intent.cloud,
        resource_type=intent.resource_type,
        api_version="0.5.3",
    )