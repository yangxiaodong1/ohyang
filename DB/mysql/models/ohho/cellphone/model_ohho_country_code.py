import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOCountryCode(BaseModel):
    __tablename__ = "ohho_country_code"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    country_code = Column(String(20), unique=True)
    country_name = Column(String(128))

