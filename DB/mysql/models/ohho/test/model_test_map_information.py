import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from sqlalchemy import Float, Numeric
from DB.mysql.base_model import BaseModel


class TestMapInformation(BaseModel):
    __tablename__ = "test_map_information"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    user_id = Column(Integer, default=0)
    another_user_id = Column(Integer, default=0)
    type = Column(Integer, default=None)
    # latitude = Column(Float(20), default=None)
    # longitude = Column(Float(20), default=None)
    latitude = Column(Numeric(10, 6), default=None)
    longitude = Column(Numeric(10, 6), default=None)
    accuracy = Column(Float, default=None)
    supplier = Column(String(32), default=None)
    altitude = Column(Float, default=None)
    floor = Column(String(16), default=None)
    building = Column(String(16), default="")
    # building_id = Column(Integer, default=0)
    speed = Column(Float, default=None)
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
    geohash_code = Column(String(20), default=None)
