from pydantic import BaseModel


class CostEstimate(BaseModel):

    estimated_monthly_cost: float

    currency: str

    breakdown: dict