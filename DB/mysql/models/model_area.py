from sqlalchemy import Column, String, Integer
from DB.mysql.base_model import BaseModel


class Area(BaseModel):
    __tablename__ = "area"
    id = Column(Integer, primary_key=True, autoincrement=True)
    administration_id = Column(String(11), unique=True)
    name = Column(String(50))
    city_id = Column(Integer)
