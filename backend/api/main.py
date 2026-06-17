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

app = FastAPI(
    title="Stellons API",
    version="0.4.18",
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


@app.get("/")
def root():

    return {
        "service": "Stellons API",
        "version": "0.4.18",
        "status": "running",
    }


@app.post(
    "/terraform/export",
    response_model=TerraformResponse,
)
def export_terraform(
    request: TerraformRequest,
):

    intent = (
        intent_service.extract(
            request.goal
        )
    )

    cost_estimate = (
        cost_service.estimate(
            intent
        )
    )

    terraform_project = (
        terraform_service.generate(
            request.goal
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
        cost_estimation=(
            cost_estimate.model_dump()
        ),
        validation=(
            validation_result.model_dump()
        ),
        export_path=export_path,
        files=files,
        file_count=len(files),
        generated_at=datetime.utcnow().isoformat(),
        cloud=intent.cloud,
        resource_type=intent.resource_type,
        api_version="0.4.18",
    )