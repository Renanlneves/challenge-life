from typing import Optional

from datetime import datetime

from pydantic import BaseModel as SCBaseModel

class EventSchema(SCBaseModel):
    id: Optional[int]
    name: str
    description: str
    start:  datetime
    end: datetime
    online_event: bool
    location_address: str
    organizer_email: str
    status: str
    capacity: int

    class Config:
        orm_mode = True