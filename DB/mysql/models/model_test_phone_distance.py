import datetime
from sqlalchemy import Column, Integer, Float, ForeignKey, BigInteger, DateTime
from DB.mysql.base_model import BaseModel


class PhoneDistance(BaseModel):
    __tablename__ = "test_phone_distance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    phone_one = Column(Integer, ForeignKey("test_phone_position.id", ondelete='CASCADE', onupdate='CASCADE'))
    phone_another = Column(Integer, ForeignKey("test_phone_position.id", ondelete='CASCADE', onupdate='CASCADE'))
    timestamp = Column(BigInteger)
    distance = Column(Float)
    input_distance = Column(Float, default=0)
