import datetime
from sqlalchemy import Column, String, Integer, Float, BigInteger, DateTime
from DB.mysql.base_model import BaseModel


class DeviceInformation(BaseModel):
    __tablename__ = "test_device_information"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String(100))
    phone_name = Column(String(100))
    environment = Column(String(100))
    timestamp = Column(BigInteger)
    rssi = Column(Integer)
    tx_power = Column(Integer)
    compute_distance = Column(Float)
    input_distance = Column(Float, default=0)
