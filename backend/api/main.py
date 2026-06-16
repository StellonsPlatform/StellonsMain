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

app = FastAPI(
    title="Stellons API",
    version="0.4.17",
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

@app.get("/")
def root():

    return {
        "service": "Stellons API",
        "version": "0.4.17",
        "status": "running"
    },

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
        validation=validation_result.model_dump(),
        export_path=export_path,
        files=files,
        file_count=len(files),
        generated_at=datetime.utcnow().isoformat(),
        cloud=intent.cloud,
        resource_type=intent.resource_type,
        api_version="0.4.17",
    )