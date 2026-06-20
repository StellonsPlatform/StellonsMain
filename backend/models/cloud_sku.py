from pydantic import BaseModel


class CloudSKU(BaseModel):

    cloud: str

    service: str

    sku_name: str

    category: str

    available: bool