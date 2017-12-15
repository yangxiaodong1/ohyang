import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOUserAndMatchConditionRelation(BaseModel):
    __tablename__ = "ohho_user_and_match_condition_relation"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    match_condition_id = Column(Integer, ForeignKey("ohho_match_condition.id", ondelete='CASCADE', onupdate='CASCADE'))
    state = Column(Integer, default=1)
