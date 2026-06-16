from pydantic import BaseModel


class TerraformPackage(BaseModel):

    files: dict[str, str]