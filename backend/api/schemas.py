from pydantic import BaseModel


class TerraformRequest(BaseModel):

    goal: str


class TerraformResponse(BaseModel):

    success: bool

    intent: dict

    validation: dict

    export_path: str

    files: list[str]

    file_count: int

    generated_at: str

    cloud: str

    resource_type: str

    api_version: str