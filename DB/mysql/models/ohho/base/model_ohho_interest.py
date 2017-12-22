import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship


class OHHOInterest(BaseModel):
    __tablename__ = "ohho_interest"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    name = Column(String(64), default=None)
    parent_id = Column(Integer, ForeignKey("ohho_interest.id", ondelete='CASCADE', onupdate='CASCADE'), default=None)
    state = Column(Integer, default=1)
    key = Column(String(64), primary_key=True, default=None)
    children = relationship("OHHOInterest")
