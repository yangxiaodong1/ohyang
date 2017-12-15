import datetime
from sqlalchemy import Column, String, Integer, Float, BigInteger, DateTime, Numeric
from DB.mysql.base_model import BaseModel


class TestPhonePosition(BaseModel):
    __tablename__ = "test_phone_position"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    name = Column(String(100))
    environment = Column(String(100))
    timestamp = Column(BigInteger)
    type = Column(Integer, default=None)
    input_distance = Column(Float, default=0)
    latitude = Column(Numeric(10, 6), default=None)
    longitude = Column(Numeric(10, 6), default=None)
    accuracy = Column(Float, default=None)
    supplier = Column(String(32), default=None)
    altitude = Column(Float, default=None)
    floor = Column(String(16), default=None)
    building_id = Column(Integer, default=None)
    speed = Column(String(16), default=None)
    angle = Column(Float, default=None)
    satellite_number = Column(Integer, default=None)
    country = Column(String(32), default=None)
    province = Column(String(32), default=None)
    city = Column(String(32), default=None)
    city_code = Column(String(32), default=None)
    area = Column(String(32), default=None)
    area_code = Column(String(32), default=None)
    address = Column(String(128), default=None)
    interest_point = Column(String(64), default=None)
    aoi = Column(String(64), default=None)  # area of interest
    position_time = Column(DateTime, default=datetime.datetime.now())
