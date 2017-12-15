import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Float, ForeignKey
from DB.mysql.base_model import BaseModel


# 记录申请匹配
class OHHORecordMatchRefuse(BaseModel):
    __tablename__ = "ohho_record_match_refuse"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    apply_id = Column(Integer, ForeignKey("ohho_record_match_apply.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    distance = Column(Float, default=0)
    information = Column(String(256), default="")
