import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOPermissionGroupAndStaffRelation(BaseModel):
    __tablename__ = "ohho_permission_group_and_staff_relation"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    group_id = Column(Integer, ForeignKey("ohho_permission_group.id", ondelete='CASCADE', onupdate='CASCADE'))
    username = Column(String(32), ForeignKey("ohho_staff.username", ondelete='CASCADE', onupdate='CASCADE'))
