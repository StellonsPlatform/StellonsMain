from pydantic import BaseModel


class TerraformValidation(BaseModel):

    valid: bool

    errors: list[str]

    warnings: list[str]