import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOPermissionGroupAndPageRelation(BaseModel):
    __tablename__ = "ohho_permission_group_and_page_relation"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    group_id = Column(Integer, ForeignKey("ohho_permission_group.id", ondelete='CASCADE', onupdate='CASCADE'))
    page_permission_id = Column(Integer,
                                ForeignKey("ohho_permission_page_permission.id", ondelete='CASCADE', onupdate='CASCADE'))
