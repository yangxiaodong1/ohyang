import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from DB.mysql.base_model import BaseModel


class OHHOWatchword(BaseModel):
    __tablename__ = "ohho_watchword"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    first = Column(String(64), default=None)
    second = Column(String(64), default=None)
