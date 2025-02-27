# src/schemas.py

from pydantic import BaseModel, Field


class SyntheticRequest(BaseModel):
    num_patients: int = Field(
        ...,
        gt=0,
        le=1000,
        description="Number of synthetic patients to generate (1-1000).",
    )
