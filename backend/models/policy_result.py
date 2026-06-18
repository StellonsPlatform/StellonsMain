from pydantic import BaseModel


class PolicyResult(BaseModel):

    approved: bool

    violations: list[str]

    warnings: list[str]