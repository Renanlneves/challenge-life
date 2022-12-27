from app.commons.configs import settings

from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

class EventModel(settings.DBBaseModel):
    __tablename__ = "Events"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    description: str = Column(String(150))
    start: datetime = Column(DateTime) 
    end: datetime = Column(DateTime)
    online_event: bool = Column(Boolean)
    location_address: str = Column(String(100))
    organizer_email: str = Column(String(100))
    status: str = Column(String(15))
    capacity: int = Column(Integer)