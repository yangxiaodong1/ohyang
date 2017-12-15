import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHODeviceSetting(BaseModel):
    __tablename__ = "ohho_device_setting"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    device_id = Column(Integer, ForeignKey("ohho_device.id", ondelete='CASCADE', onupdate='CASCADE'), unique=True)
    password = Column(String(128), default=None)  # 密码
    name = Column(String(64), default=None)  # 名称
    power = Column(Integer, default=None)  # 发射功率
    periods = Column(Integer, default=None)  # 发射周期，毫秒
