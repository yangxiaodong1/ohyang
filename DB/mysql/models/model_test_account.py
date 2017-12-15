import datetime
from sqlalchemy import Column, String, Integer, Float, BigInteger, DateTime
from DB.mysql.base_model import BaseModel


class Account(BaseModel):
    __tablename__ = "test_account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String(50))
    description = Column(String(200))
