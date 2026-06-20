from pydantic import BaseModel


class CloudProvider(BaseModel):

    provider_name: str

    version: str

    cloud: str

    supported_services: list[str]