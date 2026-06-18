from pydantic import BaseModel


class PolicyProfile(BaseModel):

    name: str

    max_nodes: int

    max_clusters: int

    approved_regions: list[str]

    monitoring_required: bool

    premium_required: bool