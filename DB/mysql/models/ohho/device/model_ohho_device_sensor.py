import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey, Float
from DB.mysql.base_model import BaseModel


class OHHODeviceSensor(BaseModel):
    __tablename__ = "ohho_device_sensor"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    device_id = Column(Integer, ForeignKey("ohho_device.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    rssi = Column(Integer, default=None)
    distance = Column(Float, default=None)
