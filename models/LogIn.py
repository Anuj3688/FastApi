from pydantic import BaseModel, Field, field_validator

class Login(BaseModel):
    password: str
    username: str