from pydantic import BaseModel


class InfrastructureRequest(BaseModel):

    cloud: str

    resource_type: str

    region: str

    node_count: int

    environment: str = "production"

    monitoring: bool = False

    cluster_count: int = 1

    sku_tier: str = "standard"

    redundancy: str = "none"

    sidecar_support: bool = False