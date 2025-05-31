from pydantic import BaseModel, Field, field_validator


class Tea(BaseModel):
    id: int
    name: str = Field(...,min_length=4)
    origin: str
    price:int = Field(...,ge=100)

    @field_validator('name')
    def name_validation(cls,v):
        if len(v)<4:
            raise ValueError("name should be more then 4 char")
        return v