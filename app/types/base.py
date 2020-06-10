from pydantic import BaseModel


class BaseObject(BaseModel):
    class Config:
        allow_mutation = False

