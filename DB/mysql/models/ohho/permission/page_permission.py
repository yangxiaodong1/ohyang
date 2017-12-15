import datetime
import time
from sqlalchemy import Column, ForeignKey, Integer, DateTime, BigInteger, SmallInteger
from DB.mysql.base_model import BaseModel


class OHHOPermissionPagePermission(BaseModel):
    __tablename__ = "ohho_permission_page_permission"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    page_id = Column(Integer, ForeignKey("ohho_permission_page.id", ondelete='CASCADE', onupdate='CASCADE'))
    insert = Column(SmallInteger, default=0)
    delete = Column(SmallInteger, default=0)
    update = Column(SmallInteger, default=0)
    select = Column(SmallInteger, default=0)
