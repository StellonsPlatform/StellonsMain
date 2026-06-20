from pydantic import BaseModel


class DeploymentResult(BaseModel):

    deployment_id: str

    status: str

    environment: str

    resource_type: str

    ready_for_deployment: bool

    approved: bool