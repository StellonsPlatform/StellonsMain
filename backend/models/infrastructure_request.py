from pydantic import BaseModel


class InfrastructureRequest(BaseModel):
    cloud: str
    resource_type: str
    region: str
    node_count: int = 1