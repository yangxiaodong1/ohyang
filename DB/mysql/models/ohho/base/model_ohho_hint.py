import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from DB.mysql.base_model import BaseModel


class OHHOHint(BaseModel):
    __tablename__ = "ohho_hint"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    key = Column(String(64), primary_key=True, default=None)
    name = Column(String(64), default=None)
    description = Column(String(256), default=None)
    parent_id = Column(Integer, ForeignKey("ohho_hint.id", ondelete='CASCADE', onupdate='CASCADE'), default=None)
    children = relationship("OHHOHint")
    state = Column(Integer, default=1)
