import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOUserAndDeviceIMEI(BaseModel):
    __tablename__ = "ohho_user_and_device_imei"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    device_id = Column(Integer, ForeignKey("ohho_device.id", ondelete='CASCADE', onupdate='CASCADE'), unique=True)
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    imei = Column(String(128), unique=True)
