import datetime
from sqlalchemy import Column, Integer, DateTime, BigInteger, SmallInteger, Float, String
from DB.mysql.base_model import BaseModel


class TestRssiDistance(BaseModel):
    __tablename__ = "test_rssi_distance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.datetime.utcnow)

    timestamp = Column(BigInteger)
    app_distance = Column(Float)
    server_distance = Column(Float)
    phone = Column(String(128), default=None)
    real_distance = Column(Float, default=None)  # 真实的距离（量出来的）
    compute_distance = Column(Float, default=None)  # 计算的距离
    compute_type = Column(SmallInteger, default=None)  # 计算距离的公式类型
