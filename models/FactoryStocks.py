from pydantic import BaseModel, computed_field, Field

from models.Tea import Tea


class FactoryStocks(BaseModel):
    factory_id:int
    factory_name:str = Field(...,min_length=5,max_length=12)
    tea_details:Tea
    quantity:int
    price: float
    @computed_field
    @property
    def total_value(self) -> float:
        return self.prize*self.quantity