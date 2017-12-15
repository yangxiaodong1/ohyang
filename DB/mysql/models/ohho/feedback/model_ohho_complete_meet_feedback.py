import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Float, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOCompleteMeetFeedback(BaseModel):
    __tablename__ = "ohho_complete_meet_feedback"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    apply_id = Column(Integer, ForeignKey("ohho_record_match_apply.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    another_user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    score = Column(Float, default=0)
    impression = Column(String(128), default="")
    # impression_id = Column(Integer, ForeignKey("ohho_interest.id", onupdate="CASCADE", ondelete="CASCADE"))
    message = Column(String(128), default="")
