import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from DB.mysql.base_model import BaseModel


class OHHOTopic(BaseModel):
    __tablename__ = "ohho_topic"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    message = Column(String(256), default="")
    icon = Column(String(128), default="")
