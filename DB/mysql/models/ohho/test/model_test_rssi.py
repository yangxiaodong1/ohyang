import datetime
from sqlalchemy import Column, Integer, DateTime, BigInteger, String, SmallInteger, Float
from DB.mysql.base_model import BaseModel


class TestRssi(BaseModel):
    __tablename__ = "test_rssi"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.datetime.utcnow)
    timestamp = Column(BigInteger)

    rssi = Column(Integer)  # 设备发送来的rssi数据
    type = Column(SmallInteger)  # 0， 自己的， 1， 别人的
    device = Column(String(64), default=None)  # 发送信息的设备ID
    phone = Column(String(64), default=None)  # 获取rssi的手机设备
    real_distance = Column(Float, default=None)  # 真实的距离（量出来的）