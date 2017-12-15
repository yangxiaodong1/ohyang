from sqlalchemy import Column, String, Integer, ForeignKey, SmallInteger
from DB.mysql.base_model import BaseModel


class School(BaseModel):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    # place = Column(String(32))
    # type = Column(String(32))
    # property = Column(String(32))
