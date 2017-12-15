import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOIMUser(BaseModel):
    __tablename__ = "ohho_im_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time() * 1000))
    account_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'), unique=True)
    token = Column(String(128), default=None)  # IM返回的密码
    name = Column(String(64), default=None)
    props = Column(String(1024), default=None)
    icon = Column(String(1024), default=None)
    type = Column(Integer, default=1)  # 登录类型1:移动端, 2:PC端, 3:两端同时
    state = Column(Integer, default=1)
