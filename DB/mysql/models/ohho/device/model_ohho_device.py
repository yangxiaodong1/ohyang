import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from DB.mysql.base_model import BaseModel


class OHHODevice(BaseModel):
    __tablename__ = "ohho_device"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    application_id = Column(String(128))
    identity_id = Column(String(32), unique=True)
    mac_address = Column(String(32))
    tx_power = Column(Integer)
