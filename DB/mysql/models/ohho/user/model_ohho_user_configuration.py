import datetime
import time
from sqlalchemy import Column, Boolean, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOUserConfiguration(BaseModel):
    __tablename__ = "ohho_user_configuration"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'), unique=True)
    is_match = Column(Integer, default=1)
    is_online = Column(Integer, default=1)
