from pydantic import BaseModel, Field, field_validator
from uuid import UUID
from typing import Optional,Union

class Tea(BaseModel):
    id: Optional[Union[UUID,str]] = None
    name: str = Field(...,min_length=4)
    origin: str
    price:int = Field(...,ge=100)

    @field_validator('name')
    def name_validation(cls, v):
        if len(v) < 4:
            raise ValueError("name should be more than 4 char")
        return v