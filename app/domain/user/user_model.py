from app.commons.configs import settings

from sqlalchemy import Column, Integer, String, Boolean

class UserModel(settings.DBBaseModel):
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    active: bool = Column(Boolean)
    age: int = Column(Integer)
    name: str = Column(String(100))
    gender: str = Column(String(15))
    email: str = Column(String(100))