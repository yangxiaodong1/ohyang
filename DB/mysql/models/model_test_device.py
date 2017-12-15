import datetime
from sqlalchemy import Column, String, Integer, Float, BigInteger, DateTime, ForeignKey
from DB.mysql.base_model import BaseModel
import time


class TestDevice(BaseModel):
    __tablename__ = "test_device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    # timestamp = Column(BigInteger, default=1000)
    timestamp = Column(BigInteger, default=(time.time() * 1000))
    # timestamp = Column(BigInteger, default=time.time())

    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    identity_id = Column(String(64), default=None)
    name = Column(String(64), default=None)
    rssi = Column(Integer, default=None)
