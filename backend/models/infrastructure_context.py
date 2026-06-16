from pydantic import BaseModel


class InfrastructureContext(BaseModel):

    cloud: str

    resource_type: str

    region: str

    node_count: int