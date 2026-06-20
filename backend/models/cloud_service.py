from pydantic import BaseModel


class CloudService(BaseModel):

    cloud: str

    service_name: str

    resource_type: str

    supported_regions: list[str]