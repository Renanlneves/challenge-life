from typing import Optional

from pydantic import BaseModel as SCBaseModel

class UserSchema(SCBaseModel):
    id: Optional[int]
    active: bool
    age: int
    name: str
    gender: str
    email: str 

    class Config:
        orm_mode = True