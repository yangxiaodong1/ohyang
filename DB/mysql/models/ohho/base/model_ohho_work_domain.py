import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOWorkDomain(BaseModel):
    __tablename__ = "ohho_work_domain"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    name = Column(String(64))
    parent_id = Column(Integer, ForeignKey("ohho_work_domain.id"), default=None)
    state = Column(Integer, default=1)
