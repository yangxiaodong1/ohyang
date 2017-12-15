import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from DB.mysql.models.ohho.user.model_ohho_user import OHHOUser
from DB.mysql.models.ohho.record.model_ohho_record_match_condition import OHHORecordMatchCondition


# 记录申请匹配
class OHHORecordMatchApply(BaseModel):
    __tablename__ = "ohho_record_match_apply"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    one_user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    another_user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    one_user_match_condition_id = Column(Integer,
                                         ForeignKey("ohho_record_match_condition.id", ondelete='CASCADE',
                                                    onupdate='CASCADE'))
    another_user_match_condition_id = Column(Integer,
                                             ForeignKey("ohho_record_match_condition.id", ondelete='CASCADE',
                                                        onupdate='CASCADE'))
    message = Column(String(256), default="")
