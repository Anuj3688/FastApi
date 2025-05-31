from pydantic import BaseModel, model_validator

class SignUp(BaseModel):
    password: str
    new_password: str

    @model_validator(mode="after")
    def password_check(cls,values):
        if values.password != values.new_password:
            raise ValueError("Password do not match")
        return values