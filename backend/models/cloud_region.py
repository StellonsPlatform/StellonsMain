from pydantic import BaseModel


class CloudRegion(BaseModel):

    cloud: str

    region: str

    status: str