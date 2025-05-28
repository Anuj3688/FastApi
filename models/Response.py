from pydantic import BaseModel, model_validator
from typing import Optional, Union, Dict, List

class GenericResponse(BaseModel):
    success: bool
    data: Optional[Union[Dict, List]] = None
    error: Optional[str] = None

    @model_validator(mode='after')
    def validate_fields(self) -> 'GenericResponse':
        if self.success and self.error:
            raise ValueError("Cannot include 'error' if 'success' is True.")
        if not self.success and not self.error:
            raise ValueError("'error' must be provided if 'success' is False.")
        return self
