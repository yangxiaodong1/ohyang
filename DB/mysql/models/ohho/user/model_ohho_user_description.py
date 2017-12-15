import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode


class OHHOUserDescription(BaseModel):
    __tablename__ = "ohho_user_description"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    user_id = Column(Integer, ForeignKey("ohho_user.id", onupdate="CASCADE", ondelete="CASCADE"))
    user = relationship("OHHOUser")
    type = Column(Integer, default=0)  # 1我是... 2我喜欢 3我不喜欢 4我希望Ta
    first = Column(String(50), default="")
    second = Column(String(50), default="")
    third = Column(String(50), default="")
