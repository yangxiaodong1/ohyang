import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, SmallInteger
from DB.mysql.base_model import BaseModel


class OHHOPermissionPage(BaseModel):
    __tablename__ = "ohho_permission_page"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    name = Column(String(64), default=None, unique=True)
    description = Column(String(128), default=None)
