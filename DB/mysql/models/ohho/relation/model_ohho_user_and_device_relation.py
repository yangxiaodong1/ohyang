import datetime
import time
from sqlalchemy import Column, Boolean, Integer, DateTime, BigInteger, ForeignKey
from sqlalchemy import String
from DB.mysql.base_model import BaseModel


class OHHOUserAndDeviceRelation(BaseModel):
    __tablename__ = "ohho_user_and_device_relation"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    name = Column(String(16), default=None)
    device_id = Column(Integer, ForeignKey("ohho_device.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    version = Column(Integer, default=None)  # 硬件版本号
    type = Column(Integer, default=1)  # 是否是主设备
    is_lost = Column(Integer, default=0)
    state = Column(Integer, default=1)
