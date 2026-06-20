from pydantic import BaseModel


class ServiceAvailability(BaseModel):

    cloud: str

    service: str

    region: str

    available: bool

    sku: str