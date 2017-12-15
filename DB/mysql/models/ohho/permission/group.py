import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from DB.mysql.base_model import BaseModel


class OHHOPermissionGroup(BaseModel):
    __tablename__ = "ohho_permission_group"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    name = Column(String(64), default=None)
    description = Column(String(1024), default=None)
    # is_all = Column(Integer, default=0)
