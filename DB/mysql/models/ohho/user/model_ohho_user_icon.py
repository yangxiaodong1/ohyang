import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, SmallInteger, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode


class OHHOUserIcon(BaseModel):
    __tablename__ = "ohho_user_icon"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    user_id = Column(Integer, ForeignKey("ohho_user.id", onupdate="CASCADE", ondelete="CASCADE"))
    user = relationship("OHHOUser")
    icon = Column(String(128), default="")
    thumbnail = Column(String(128), default="")
    is_head_sculpture = Column(SmallInteger, default=0)
