import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode
from DB.mysql.models.ohho.base.model_ohho_interest import OHHOInterest


class OHHOUserImpression(BaseModel):
    __tablename__ = "ohho_user_impression"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    apply_id = Column(Integer, ForeignKey("ohho_record_match_apply.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", onupdate="CASCADE", ondelete="CASCADE"))
    user = relationship("OHHOUser", primaryjoin="OHHOUser.id==OHHOUserImpression.user_id")
    another_user_id = Column(Integer, ForeignKey("ohho_user.id", onupdate="CASCADE", ondelete="CASCADE"))
    another_user = relationship("OHHOUser", primaryjoin="OHHOUser.id==OHHOUserImpression.another_user_id")
    content_id = Column(Integer, ForeignKey("ohho_interest.id", onupdate="CASCADE", ondelete="CASCADE"))
    content = relationship("OHHOInterest")
    type = Column(Integer, default=0)  # 类型，0 - 完成反馈， 1 - 取消反馈
