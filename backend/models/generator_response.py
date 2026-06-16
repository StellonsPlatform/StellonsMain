from pydantic import BaseModel


class GeneratorResponse(BaseModel):
    tool: str
    code: str