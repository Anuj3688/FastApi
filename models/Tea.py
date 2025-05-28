from pydantic import BaseModel, Field


class Tea(BaseModel):
    id: int = Field(...,min_length=6)
    name: str = Field(...,min_length=4)
    origin: str
    price:int = Field(...,ge=100)