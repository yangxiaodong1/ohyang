import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from DB.mysql.base_model import BaseModel


class OHHOProfession(BaseModel):
    __tablename__ = "ohho_profession"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    name = Column(String(64), unique=True)
    state = Column(Integer, default=1)
