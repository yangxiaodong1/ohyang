import datetime
from sqlalchemy import Column, Integer, DateTime, BigInteger, String, SmallInteger, Numeric, Float
from DB.mysql.base_model import BaseModel


class TestInterestPoint(BaseModel):
    __tablename__ = "test_interest_point"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    changed_at = Column(DateTime, default=datetime.datetime.utcnow)
    timestamp = Column(BigInteger)

    phone = Column(String(64), default=None)
    name = Column(String(64), default=None)
    longitude = Column(Numeric(10, 6), default=None)
    latitude = Column(Numeric(10, 6), default=None)
    adCode = Column(String(16), default=None)
    adName = Column(String(32), default=None)
    businessArea = Column(String(32), default=None)
    cityCode = Column(String(8), default=None)
    provinceCode = Column(String(16), default=None)
    provinceName = Column(String(16), default=None)
    distance = Column(Float, default=None)
    poiId = Column(String(32), default=None)
    snippet = Column(String(128), default=None)
    tel = Column(String(32), default=None)
    title = Column(String(64), default=None)
    typeCode = Column(String(16), default=None)
    typeDes = Column(String(128), default=None)
    img1 = Column(String(256), default=None)
    img2 = Column(String(256), default=None)
    img3 = Column(String(256), default=None)
