import datetime
from sqlalchemy import Column, TIMESTAMP, Integer, String, BigInteger
from DB.mysql.base_model import BaseModel
import time


class TestTimestamp(BaseModel):
    __tablename__ = "test_timestamp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(BigInteger, default=(time.time() * 1000))
    name = Column(String(32), default=None)
