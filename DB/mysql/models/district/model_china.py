from sqlalchemy import Column, String, Integer, ForeignKey, SmallInteger
from DB.mysql.base_model import BaseModel


class China(BaseModel):
    __tablename__ = "china"
    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey("china.id", ondelete="CASCADE", onupdate="CASCADE"), default=0)
    name = Column(String(50))
    level = Column(SmallInteger, default=0)
