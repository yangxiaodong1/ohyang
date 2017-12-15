import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from DB.mysql.models.ohho.record.model_ohho_record_match_condition import OHHORecordMatchCondition


# 记录申请匹配
class OHHORecordUserAndMatchCondition(BaseModel):
    __tablename__ = "ohho_record_user_and_match_condition"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    name = Column(String(64), default=None)
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))

    match_condition_id = Column(Integer,
                                ForeignKey("ohho_record_match_condition.id", ondelete='CASCADE', onupdate='CASCADE'),
                                unique=True)
