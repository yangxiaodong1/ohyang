import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from sqlalchemy import ForeignKey
from DB.mysql.base_model import BaseModel


class OHHORecordMatchLabel(BaseModel):
    __tablename__ = "ohho_match_label"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    name = Column(String(64), default=None)
    parent_id = Column(Integer, ForeignKey("ohho_match_label.id", ondelete='CASCADE', onupdate='CASCADE'), default=1)
    state = Column(Integer, default=1)
